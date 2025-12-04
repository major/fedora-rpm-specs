Summary: An XML parser library
Name: expat
Version: 2.7.3
Release: %autorelease
Source0: https://github.com/libexpat/libexpat/releases/download/R_2_7_3/expat-%{version}.tar.gz
Source1: https://github.com/libexpat/libexpat/releases/download/R_2_7_3/expat-%{version}.tar.gz.asc
# Sebastian Pipping's PGP public key
Source2: https://keys.openpgp.org/vks/v1/by-fingerprint/3176EF7DB2367F1FCA4F306B1F9B0E909AF37285

URL: https://libexpat.github.io/
VCS: git:https://github.com/libexpat/libexpat.git
License: MIT
BuildRequires: autoconf, libtool, xmlto, gcc-c++
BuildRequires: make
BuildRequires: gnupg2

%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%package devel
Summary: Libraries and header files to develop applications using expat
Requires: expat%{?_isa} = %{version}-%{release}

%description devel
The expat-devel package contains the libraries, include files and documentation
to develop XML applications with expat.

%package static
Summary: expat XML parser static library
Requires: expat-devel%{?_isa} = %{version}-%{release}

%description static
The expat-static package contains the static version of the expat library.
Install it if you need to link statically with expat.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
sed -i 's/install-data-hook/do-nothing-please/' lib/Makefile.am
./buildconf.sh

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export DOCBOOK_TO_MAN="xmlto man"
%configure
%make_build

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS Changes
%license COPYING
%{_bindir}/*
%{_libdir}/libexpat.so.1
%{_libdir}/libexpat.so.1.*
%{_mandir}/*/*

%files devel
%doc doc/reference.html doc/*.css examples/*.c
%{_libdir}/libexpat.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%{_libdir}/cmake/expat-%{version}

%files static
%{_libdir}/libexpat.a

%changelog
%autochangelog
