%global upstream_version     1.5.1

Name:            supernovas
Version:         1.5.1
Release:         %autorelease
Summary:         The Naval Observatory's NOVAS C astronomy library, made better 
License:         Unlicense
URL:             https://smithsonian.github.io/SuperNOVAS
Source0:         https://github.com/Smithsonian/SuperNOVAS/archive/refs/tags/v%{upstream_version}.tar.gz

# No i686 calceph package to build against
ExcludeArch:     %{ix86}

BuildRequires:   calceph-devel%{_isa} >= 4.0.0
BuildRequires:   gcc
BuildRequires:   cmake
BuildRequires:   doxygen >= 1.13.0

# Starting with v1.5.0, we no longer need or package cio-data
Obsoletes:       %{name}-cio-data < %{version}-%{release} 


Suggests:        %{name}-solsys-calceph = %{version}-%{release}

%description

SuperNOVAS is a C/C++ astronomy library, providing high-precision astronomical 
calculations such as one might need for running an observatory or a precise 
planetarium program. It is a fork of the Naval Observatory Vector Astrometry 
Software (NOVAS) C version 3.1, providing bug fixes and making it easier to 
use overall.

The main goals of SuperNOVAS are to improve usability, add new features, 
promote best practices, and provide accessible documentation -- all while 
retaining 100 percent API compatibility with NOVAS C 3.1. Thus, if you have 
written code for NOVAS C 3.1, you can build it with SuperNOVAS also.

SuperNOVAS is entirely free to use without licensing restrictions. Its source 
code is compatible with the C90 standard, and hence should be suitable for old 
and new platforms alike. It is light-weight and easy to use, with full support 
for the IAU 2000/2006 standards for sub-micro-arc-second position 
calculations.
 
%package solsys-calceph
Summary: Solar-system plugin based on the CALCEPH C library
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires:        calceph-libs%{?_isa} >= 4.0.0

%description solsys-calceph
Optional SuperNOVAS plugin library that provides Solar-system support via the 
CALCEPH C library. It allows using both JPL (SPK) and INPOP 2.0/3.0 data files 
with SuperNOVAS to obtain precise locations for Solar-system bodies. This 
plugin is currently the preferred option to use for Fedora / RPM Linux 
development, which requires use of precise Solar-system data.

%package devel
Summary:         C development files for the SuperNOVAS C/C++ astronomy library
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires:        %{name}-solsys-calceph%{?_isa} = %{version}-%{release}
# We no longer package legacy plugins, since upstream no longer builds these. 
# Their source codes are however available in devel, if needed.
Obsoletes:       %{name}-solsys1 < %{version}-%{release} 
Obsoletes:       %{name}-solsys2 < %{version}-%{release} 

%description devel
This sub-package provides C headers and non-versioned shared library symbolic 
links for the SuperNOVAS C/C++ library. It also provides a default FORTRAN
adapter module (as documentation) that may be used as is, or modified as 
needed, for the the JPL PLEPH module.

%package doc
Summary:         Documentation for the SuperNOVAS C/C++ astronomy library
BuildArch:       noarch


%description doc
This package provides HTML documentation, examples, and legacy adapter 
templates for the SuperNOVAS C/C++ astronomy library.

%prep
%setup -q -n SuperNOVAS-%{upstream_version}

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_DOC=ON \
    -DENABLE_CALCEPH=ON 

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc CHANGELOG.md
%{_libdir}/lib%{name}.so.1{,.*}

%files solsys-calceph
%{_libdir}/libsolsys-calceph.so.1{,.*}

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/cmake
%{_libdir}/pkgconfig
%doc %{_docdir}/%{name}/*.md
%doc %{_docdir}/%{name}/examples
%doc %{_docdir}/%{name}/legacy

%files doc
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/supernovas.tag
%doc %{_docdir}/%{name}/html

%changelog
%autochangelog
