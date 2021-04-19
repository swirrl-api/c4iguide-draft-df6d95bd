

set -ex



test -f $PREFIX/lib/libwebp.a
test -f $PREFIX/lib/libwebp.so
test -f $PREFIX/lib/libwebpmux.so
test -f $PREFIX/include/webp/decode.h
test -f $PREFIX/include/webp/encode.h
test -f $PREFIX/include/webp/types.h
exit 0
