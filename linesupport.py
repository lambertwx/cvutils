# -*- coding: utf-8 -*-
"""
Functions for taking a bunch of points that lie very close to a line and building a line segment or cleaing them up.

MIT License

Copyright (c) 2018 Lambert Wixson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

$Id$
"""
import heapq
import numpy as np

#%%
def build_line_attributes(line, points):
    """
    Compute some useful attributes and add them to the line object.
    
    @param line: An object representing a 2D line.  E.g., skimage's LineModel.  It must have predict_x() and predict_y() methods.
    
    @param points: The points that were used to fit the line.  E.g., these might be the inliers returned by skimage's ransac().
    A 2D array with one row for each point.  
    The first two columns of each row represent the coords of the point.
    """
    xmin = np.amin(points[:,0])
    xmax = np.amax(points[:,0])
    ymin = np.amin(points[:,1])
    ymax = np.amax(points[:,1])
    
    line.support_xmin = xmin
    line.support_xmax = xmax
    line.support_ymin = ymin
    line.support_ymax = ymax
    
    # Add attributes to line
    if (xmax-xmin) > (ymax-ymin):
        line.x0 = xmin
        line.y0 = line.predict_y(xmin)
        line.x1 = xmax
        line.y1 = line.predict_y(xmax)
        
        # When you have very short lines, i.e. lines with just one or two pixels of support, the prediction can give 
        # wacky results.  Specifically it can give you endpoints that are far beyond the extent of your line.
        # E.g. if xmin = xmax and ymax = ymin + 1.    The logic below deals with that.
        if line.y0 <= line.y1:
            line.y0 = max(line.y0, ymin)
            line.y1 = min(line.y1, ymax)
        else:
            line.y0 = min(line.y0, ymax)
            line.y1 = max(line.y1, ymin)
            
    else:
        line.x0 = line.predict_x(ymin)
        line.y0 = ymin 
        line.x1 = line.predict_x(ymax)
        line.y1 = ymax
    
        if line.x0 <= line.x1:
            line.x0 = max(line.x0, xmin)
            line.x1 = min(line.x1, xmax)
        else:
            line.x0 = min(line.x0, xmax)
            line.x1 = max(line.x1, xmin)
            
      
    
    return line

#%%
def project_points_onto_line(line, points):
    """
    Returns a sorted version of points where the points have been sorted in increasing order of their distance from line.x0, line.y0.
    """
    deltax = line.x1 - line.x0
    deltay = line.y1 - line.y0
    
    # Projects the points onto the line.  
    projs = np.array([[p[0], p[1], ((p[0] - line.x0)*deltax) + ((p[1] - line.y0)*deltay), i] for (i, p) in enumerate(points)])
    # Sort them by their distance along the line
    sortindexes = np.argsort(projs[:,2])
    return projs[sortindexes]

#%%
def remove_gaps(line, points, max_allowed_gap):
    """
    Removes points that lie along the specified line if there is too much of a gap between them and their neighbors.
    For each gap larger than max_allowed, in order of decreasing gap size, find the side of the gap with the most points.  
    Keep those, discard the others.  Return the list of points left.
    
    @param points: List of points along line, sorted from project_points_onto_line.
    """
    # Compute the neg of the squared dist to the next point in the list, for all but the last point in the list.
    # We use the negative because we're going to put them into a min-heap
    sqdist_to_next = [[-((p[0] - points[i+1,0])**2 + (p[1] - points[i+1,1])**2), i] for (i, p) in enumerate(points[0:-1])]
    maxsq = max_allowed_gap**2
    
    keepstart = 0
    keepend = len(points) -1
    
    # Transform sqdist_to_next to be a min-heap, with the smallest val at the top, i.e. in position 0.
    heapq.heapify(sqdist_to_next)
    while True:
        (gapsq, dex) = heapq.heappop(sqdist_to_next)
        # The gap is between points[dex] and points[dex+1]
        if -gapsq < maxsq:
            break
        if dex < keepstart:
            continue
        if dex > keepend:
            continue
        numL = dex - keepstart + 1      # The number of points to the left of the gap
        numR = keepend - dex            # The number of points to the right of the gap
        if numL >= numR:
            keepend = dex
        else:
            keepstart = dex + 1
    
    # Get the indices we're keeping
    return points[keepstart:keepend+1]
        
#%%
def cleanup_line(line, points, max_allowed_gap):
    """
    Cleans up the line model by removing points that are separated by too large a gap.
    
    @param points: points on the line.  E.g., the samples[inliers] returned from ransacAS
    """
    filtered_pts = remove_gaps(line, project_points_onto_line(line, points), max_allowed_gap)
    
    # TODO: Really we should refit the line using only the filtered points.  If we don't do so, then the line model
    # can be seriously out of sync with the filtered_pts, which can cause problems in build_line_attributes.
    build_line_attributes(line, filtered_pts)
    return line, filtered_pts

    