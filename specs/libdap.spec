Name: libdap
Summary: The C++ DAP2 and DAP4 library from OPeNDAP
Version: 3.21.1
Release: %autorelease

%global libdap_tag 3.21.0-120

License: LGPL-2.1-or-later
URL: http://www.opendap.org/
Source0: https://github.com/OPENDAP/libdap4/archive/%{libdap_tag}/%{name}-%{version}.tar.gz
# Don't run HTTP tests - builders don't have network connections
Patch0: libdap-offline.patch
# Add missing includes
# https://github.com/OPENDAP/libdap4/pull/258
Patch1: libdap-include.patch

BuildRequires: make
BuildRequires: gcc-c++
# For autoreconf
BuildRequires: libtool
BuildRequires: bison >= 3.0
BuildRequires: cppunit-devel
BuildRequires: curl-devel
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: graphviz
BuildRequires: libtirpc-devel
BuildRequires: libuuid-devel
BuildRequires: libxml2-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig
%ifarch %{valgrind_arches}
BuildRequires: valgrind
%endif

Provides: bundled(gnulib)


%description
The libdap++ library contains an implementation of DAP2 and DAP4. This
package contains the library, dap-config, and getdap. The script
dap-config simplifies using the library in other projects. The getdap
utility is a simple command-line tool to read from DAP2 servers. It is
built using the library and demonstrates simple uses of it.


%package devel
Summary: Development and header files from libdap
Requires: %{name} = %{version}-%{release}
Requires: curl-devel
Requires: libxml2-devel
Requires: pkgconfig
# for the /usr/share/aclocal directory ownership
Requires: automake

%description devel
This package contains all the files needed to develop applications that
will use libdap.


%package doc
Summary: Documentation of the libdap library

%description doc
Documentation of the libdap library.


%prep
%autosetup -n libdap4-%{libdap_tag} -p1
iconv -f latin1 -t utf8 < COPYRIGHT_W3C > COPYRIGHT_W3C.utf8
touch -r COPYRIGHT_W3C COPYRIGHT_W3C.utf8
mv COPYRIGHT_W3C.utf8 COPYRIGHT_W3C


%build
# To fix rpath
autoreconf -f -i
%configure --disable-static --disable-dependency-tracking
# --enable-valgrind - missing valgrind exclusions file
%make_build

make docs


%install
%make_install INSTALL="%{__install} -p"
mkdir -p $RPM_BUILD_ROOT%{_libdir}/libdap
mv $RPM_BUILD_ROOT%{_libdir}/libtest-types.a $RPM_BUILD_ROOT%{_libdir}/libdap/
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mv $RPM_BUILD_ROOT%{_bindir}/dap-config-pkgconfig $RPM_BUILD_ROOT%{_bindir}/dap-config

rm -rf __dist_docs
cp -pr html __dist_docs
# those .map and .md5 are of dubious use, remove them
rm -f __dist_docs/*.map __dist_docs/*.md5
# use the ChangeLog timestamp to have the same timestamps for the doc files 
# for all arches
touch -r ChangeLog __dist_docs/*


%check
# tarball is missing some needed files
make check || :


%ldconfig_scriptlets


%files
%license COPYRIGHT_W3C COPYING COPYRIGHT_URI
%doc README.md NEWS README.dodsrc
%{_bindir}/getdap
%{_bindir}/getdap4
%{_libdir}/libdap.so.27*
%{_libdir}/libdapclient.so.6*
%{_libdir}/libdapserver.so.7*
%{_mandir}/man1/getdap.1*
%{_mandir}/man1/getdap4.1*

%files devel
%{_libdir}/libdap.so
%{_libdir}/libdapclient.so
%{_libdir}/libdapserver.so
%{_libdir}/libdap/
%{_libdir}/pkgconfig/libdap*.pc
%{_bindir}/dap-config
%{_includedir}/libdap/
%{_datadir}/aclocal/*
%{_mandir}/man1/dap-config.1*

%files doc
%license COPYING COPYRIGHT_URI COPYRIGHT_W3C
%doc __dist_docs/


%changelog
%autochangelog
