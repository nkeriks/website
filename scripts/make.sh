#!/bin/bash

set -e
python build.py
python build_cv.py
cd ../cv
pdflatex cv.tex
pdflatex cv.tex
cp cv.pdf ../web/pdf/eriksson-cv.pdf
