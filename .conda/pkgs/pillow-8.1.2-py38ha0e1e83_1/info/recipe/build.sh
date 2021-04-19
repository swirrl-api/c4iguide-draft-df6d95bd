#!/bin/bash

export JPEG_ROOT=$PREFIX
export JPEG2K_ROOT=$PREFIX
export ZLIB_ROOT=$PREFIX
# export IMAGEQUANT_ROOT=None
export TIFF_ROOT=$PREFIX
export FREETYPE_ROOT=$PREFIX
export LCMS_ROOT=$PREFIX

$PYTHON -m pip install . --no-deps --ignore-installed --no-cache-dir -vvv
