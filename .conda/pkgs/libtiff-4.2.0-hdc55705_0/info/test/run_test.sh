

set -ex



test -f ${PREFIX}/lib/libtiff.a
test -f ${PREFIX}/lib/libtiffxx.a
test -f ${PREFIX}/lib/libtiff.so
test -f ${PREFIX}/lib/libtiffxx.so
python -m trace --trace --ignore-dir $CONDA_PREFIX downstream_tests.py
exit 0
