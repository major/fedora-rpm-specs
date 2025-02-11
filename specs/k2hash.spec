%if %{undefined package_revision}
%global package_revision 1
%endif

%if %{undefined make_build}
%global make_build %{__make} %{?_smp_mflags}
%endif

%if %{undefined autosetup}
%global autosetup %setup -q
%endif

%global release_version 1.0.98
%global gittag v%{release_version}

%if %{undefined make_check}
%global make_check 1
%endif

#
# main package
#
Summary: NoSQL Key Value Store(KVS) tools and library
Name: k2hash
Version: %{release_version}
Release: %autorelease
License: MIT

URL: https://github.com/yahoojapan/k2hash
Source0: https://github.com/yahoojapan/k2hash/archive/%{gittag}/%{name}-%{version}.tar.gz
Requires: libfullock%{?_isa} >= 1.0.36
BuildRequires: git-core gcc-c++ make libtool libfullock-devel >= 1.0.36 nss-devel
# k2hash does not support 32bit arch
ExcludeArch: i686 armv7hl

%description
K2HASH provides a NoSQL(key value store) tools and a library under
MIT license. K2HASH tools create/write/read files or memory which
is allocated by K2HASH library. K2HASH library stores its data in 
three ways: on-memory, fully mapping file and partially mapping
file and directly accessing a file.

Please visit the website and get more details at:

https://github.com/yahoojapan/k2hash

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh
%configure --disable-static --with-nss
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%if %{make_check}
%check
%{__make} check
find %{_builddir} -name '*.log' -exec echo {} ';'
find %{_builddir} -name '*.log' -exec cat {} ';'
%endif

%if %{defined ldconfig_scriptlets}
%ldconfig_scriptlets
%else
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%license COPYING
%doc README AUTHORS ChangeLog
%{_libdir}/libk2hash.so.1*
%{_mandir}/man1/k2hash.1*
%{_mandir}/man1/k2hbench.1*
%{_mandir}/man1/k2hcompress.1*
%{_mandir}/man1/k2hedit.1*
%{_mandir}/man1/k2himport.1*
%{_mandir}/man1/k2hlinetool.1*
%{_mandir}/man1/k2hreplace.1*
%{_mandir}/man1/k2htouch.1*
%{_bindir}/k2hbench
%{_bindir}/k2hcompress
%{_bindir}/k2hedit
%{_bindir}/k2himport
%{_bindir}/k2hlinetool
%{_bindir}/k2hreplace
%{_bindir}/k2htouch

#
# devel package
#
%package devel
Summary: NoSQL Key Value Store(KVS) tools and library (development)
Requires: %{name}%{?_isa} = %{version}-%{release}, libfullock-devel%{?_isa} >= 1.0.36

%description devel
Development package for building with k2hash shared library.
This package has header files and symbols for it.

%files devel
%doc README AUTHORS ChangeLog
%{_includedir}/k2hash/*
%{_libdir}/libk2hash.so
%{_libdir}/pkgconfig/libk2hash.pc

%changelog
%autochangelog

