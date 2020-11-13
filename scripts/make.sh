#!/bin/bash

set -e
python2 build.py
python2 build_cv.py
cd ../cv
pdflatex cv.tex
pdflatex cv.tex
cp cv.pdf ../web/pdf/eriksson-cv.pdf
