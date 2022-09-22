Name:           libmaxminddb
Summary:        C library for the MaxMind DB file format
Version:        1.6.0
Release:        %autorelease
URL:            https://maxmind.github.io/libmaxminddb
Source:         https://github.com/maxmind/libmaxminddb/releases/download/%{version}/%{name}-%{version}.tar.gz

# original libmaxminddb code is Apache Licence 2.0
# src/maxminddb-compat-util.h is BSD
License:        ASL 2.0 and BSD

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  perl-interpreter
BuildRequires:  perl(FindBin)
BuildRequires:  make

%description
The package contains libmaxminddb library.

%package devel
Summary:        Development header files for libmaxminddb
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The package contains development header files for the libmaxminddb library
and the mmdblookup utility which allows IP address lookup in a MaxMind DB file.

%prep
%autosetup
sed -i -e '/AM_CFLAGS=/d' common.mk
sed -i -e '/CFLAGS=/d' configure.ac

%build
autoreconf -vfi
%configure --disable-static
%make_build

%check
# tests are linked dynamically, preload the library as we have removed RPATH
LD_PRELOAD=%{buildroot}%{_libdir}/libmaxminddb.so make check

%install
%make_install
rm -v %{buildroot}%{_libdir}/*.la

#downstream fix for multilib install of devel pkg
mv %{buildroot}%{_includedir}/maxminddb_config.h \
   %{buildroot}%{_includedir}/maxminddb_config-%{__isa_bits}.h
cat > %{buildroot}%{_includedir}/maxminddb_config.h << EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include <maxminddb_config-32.h>
#elif __WORDSIZE == 64
#include <maxminddb_config-64.h>
#else
#error "Unknown word size"
#endif
EOF

%files
%license LICENSE
%{_libdir}/libmaxminddb.so.0*
%{_bindir}/mmdblookup
%{_mandir}/man1/*.1*

%files devel
%license NOTICE
%doc Changes.md
%{_includedir}/maxminddb.h
%{_includedir}/maxminddb_config*.h
%{_libdir}/libmaxminddb.so
%{_libdir}/pkgconfig/libmaxminddb.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
