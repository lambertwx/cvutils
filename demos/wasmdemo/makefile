default: main.html

main.html : main.c
	# This will create a main.wasm and a main.js that handles loading of the wasm.  
	# Our wasmdemo.html page will load the main.js and call the fib() function.
	#
        # It will also create a main.html containing boilerplate areas for text output and a canvas that will
        # be populated if your code draws graphics.
	# Instead of loading wasmdemo.html you can can load the main.html in your browser and see the result of
	# the main function.
	# But if you aren't going to do this, then remove the _main from the list of exported functions below.
	emcc -g  -s WASM=1 -s EXPORTED_FUNCTIONS="['_fib', '_main']" -o $@ $<

main-module.js : main.c
	# Make a modular version of main.  This is useful if you're going to load multiple WebAssembly modules
	# into a single web page.  See ../opencv-js/opencv_corners.html for an example that uses this.
	emcc -g  -s WASM=1 -s MODULARIZE=1 -s EXPORT_NAME="MyMain" -s EXPORTED_FUNCTIONS="['_fib']" -o $@ $<

clean:
	rm -f main.exe main.html main.js main.wasm main-module.js main-module.wasm
