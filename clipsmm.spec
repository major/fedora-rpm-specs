%global clipsver 6.31

Summary:          C++ interface to the CLIPS expert system C library
Name:             clipsmm
Version:          0.3.5
Release:          %autorelease
License:          GPL-3.0-only
URL:              http://clipsmm.sourceforge.net
Source0:          http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# https://github.com/timn/clipsmm/pull/1
Patch0:           clipsmm.fix-multifield-retval-with-multi-env.patch
# https://github.com/timn/clipsmm/pull/2
Patch1:           clipsmm.fix-add-symbol-with-multiple-environments.patch
# https://github.com/timn/clipsmm/pull/3
Patch2:           clipsmm.clips-631.patch
BuildRequires:    clips-devel >= %{clipsver} 
BuildRequires:    gcc-c++
BuildRequires:    glibmm24-devel >= 2.6.0 
BuildRequires:    cppunit-devel >= 1.11 
BuildRequires:    doxygen, libxslt
BuildRequires:    pkgconfig, m4, libtool
BuildRequires: make

%description
The clipsmm library provides a C++ interface to the CLIPS C library.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the
construction of rule and/or object based expert systems.

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now
widely used throughout the government, industry, and academia.

%package          devel
Summary:          Headers for developing C++ applications with CLIPS
Requires:         %{name} = %{version}-%{release}
Requires:         clips-devel >= %{clipsver} 
Requires:         glibmm24-devel >= 2.6.0 
Requires:         pkgconfig

%description    devel
This package contains the libraries and header files needed for
developing clipsmm applications.

clipsmm provides a C++ interface to the CLIPS C library.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the
construction of rule and/or object based expert systems.

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now
widely used throughout the government, industry, and academia.

%package          doc
Summary:          Documentation for the C++ clipsmm library
Requires:         devhelp
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildArch:        noarch
%endif

%description      doc
This package contains developer's documentation for the clipsmm
library. clipsmm provides C++ based bindings for the C based
CLIPS library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser. 

If using a web browser the documentation is installed in the gtk-doc
hierarchy and can be found at /usr/share/gtk-doc/html/clipsmm-0.3

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the
construction of rule and/or object based expert systems.

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now
widely used throughout the government, industry, and academia.

%prep
%autosetup -p1

%build
./autogen.sh
%configure --enable-static=no --enable-unit-tests --enable-doc
%{__make} %{?_smp_mflags}
make docs

%install
%{__make} DESTDIR=%{buildroot} INSTALL="%{__install} -p" install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%{__mkdir} -p %{buildroot}%{_datadir}/gtk-doc/html/clipsmm-0.3/reference/html/
%{__install} -p --mode=0664 -t %{buildroot}%{_datadir}/gtk-doc/html/clipsmm-0.3/reference/html/ doc/reference/html/*
%{__install} -p --mode=0664 -t %{buildroot}%{_datadir}/gtk-doc/html/clipsmm-0.3/ doc/clipsmm-0.3.devhelp

%check
cd unit_tests
./clipsmm_unit_tests

%files
%{_libdir}/libclipsmm.so.*
%doc AUTHORS COPYING

%files devel
%{_libdir}/libclipsmm.so
%{_libdir}/pkgconfig/clipsmm-1.0.pc
%{_includedir}/clipsmm-0.3/
%doc ChangeLog

%files doc
%doc %{_datadir}/gtk-doc/html/clipsmm-0.3/
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/

%changelog
%autochangelog
