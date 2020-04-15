# Example of how to use OpenCV.js

1. git clone the opencv repo into ~/party3

2. `cd ~/party3/opencv`

3. Add a declaration of `cornerSubPix()` to `platforms/js/opencv_js.config.py`

4. Build OpenCV.js with `docker run --rm --workdir /code -v "$PWD":/code "trzeci/emscripten:latest" python ./platforms/js/build_js.py build --build_test --build_perf --build_wasm`

4. `cd build/bin`

5. Add symlink to the html in this repo.
`ln -s ~/party3/cvutils/demos/opencv-js/opencv_corners.html .`
This is necessary because right now all the loading code seems to assume that the compiled WASM/JS is in the same folder as the HTML.

6. Because we also are demonstrating how to include more than one WebAssembly module, add symlinks to another module.
```
pushd ~/party3/cvutils/demos/wasmdemo
make main-module.js
popd
ln -s ~/party3/cvutils/demos/wasmdemo/main-module.wasm .
ln -s ~/party3/cvutils/demos/wasmdemo/main-module.js .
```

6. `http-server -p 8080`

7.  Aim your browser to http://localhost:8080/opencv_corners.html
