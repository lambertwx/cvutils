# Getting started with WebAssembly

There is lots of aging documentation and repos out there, which is understandable given the speed with which WebAssembly is evolving.
This is what worked for me in April 2020.

1. Get `emcc` by downloading from [https://github.com/emscripten-core/emsdk](emscripten-core/emsdk) and following the instructions at https://emscripten.org/docs/getting_started/downloads.html

2. Invoke `make` with no arguments.  This will use `emcc` to build main.wasm, main.js, and main.html from main.c.  

3. Launch an http server in this directory.  E.g., you can run node's `http-server -p 8081`.

4. Point your browser to http://localhost:8081/wasmdemo.html.  This is a simple web page that shows how to load the main.js (which in turn loads the main.wasm), call its `fib()` function, and display its printfs both on the browser console and in an HTML textarea element.

5. Point your browser to http://localhost:8081/main.html.  This is a boilerplate file output by emcc that has a canvas to display OpenGL output and a text area to display printf output.  A good example of how use this boilerplate for graphics is the [https://github.com/emscripten-core/emscripten/blob/master/tests/hello_world_sdl.cpp](hello_world_sdl.cpp) file example described in https://emscripten.org/docs/getting_started/Tutorial.html#generating-html

## Good resources
- https://emscripten.org/docs/getting_started/Tutorial.html#generating-html

- https://emscripten.org/docs/getting_started/FAQ.html - this covers many common errors and questions

- the [https://github.com/emscripten-core/emscripten](emscripten-core/emscripten) repo - this focuses specifically on compiling C/C++ to WebAssembly, and supporting common library APIs.

 - https://emscripten.org/docs/compiling/index.html - Details about how incorporate emscripten and WebAssembly into build systems

## Resources which were OK but are a bit old
https://itnext.io/the-anatomy-of-webassembly-writing-your-first-webassembly-module-using-c-c-d9ee18f7ac9b

https://github.com/mdn/webassembly-examples/ - this focuses specifically on low-level WASM and WAT examples.  It's much easier to work with the higher-level examples at [https://github.com/emscripten-core/emscripten](emscripten-core/emscripten) in its `test` directory.
