
CC=cc
prefix=/usr
exec_prefix=/usr
bindir=/usr/bin
libdir=/usr/lib
includedir=/usr/include
sysconfdir=/etc
CPPFLAGS+= -DSUPER_SECURE
LD_SET_SONAME = -Wl,--soname,
