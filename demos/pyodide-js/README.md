# Getting started with Pyodide

It's relatively easy to get started.  The HTML demo here shows you how to use Python from
 JavaScript. The `pydemo.html` file shows how you can run Python code inline, load it from a file, and
  load and invoke standard packages such as matplotlib, numpy, and sympy.  

1. Launch an http server in this directory.  E.g., you can run node's `http-server -p 8081`.

1. Point your browser to http://localhost:8081/pydemo.html.  You'll see some text appear in
 the text display box pretty quickly once the pyodide.js WebAssembly is downloaded.  
 Then wait 15-20 seconds and you'll see a matplotlib 
 drawing appear and a message about polygon intersection appear in the text area.  (The reason
 for the long delay is that it's downloading matplotlib, numpy, and sympy from the pyodide CDN.)

1. Open the F12 debugger in your browser and reload pydemo.html.  You'll see the output on the
 JavaScript console.  Text outputted by calling `print()` in Python will *only* appear 
 on the JavaScript console and not in the HTML text display box.

## Good resources
- https://pyodide.readthedocs.io/en/latest/using_pyodide_from_javascript.html

- The list of currently distributed Python packages for pyodide is at 
https://github.com/iodide-project/pyodide/tree/master/packages

