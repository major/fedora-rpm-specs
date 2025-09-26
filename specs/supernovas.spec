%global upstream_version     1.4.2

Name:            supernovas
Version:         1.4.2
Release:         %autorelease
Summary:         The Naval Observatory's NOVAS C astronomy library, made better 
License:         Unlicense
URL:             https://smithsonian.github.io/SuperNOVAS
Source0:         https://github.com/Smithsonian/SuperNOVAS/archive/refs/tags/v%{upstream_version}.tar.gz

# No i686 calceph package to build against
ExcludeArch:     %{ix86}

BuildRequires:   calceph-devel%{_isa} >= 4.0.0
BuildRequires:   gcc
BuildRequires:   sed
BuildRequires:   doxygen >= 1.13.0
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

%package solsys1
Summary: Legacy solar-system plugin for JPL DE200 through DE421
Requires:        %{name}%{?_isa} >= %{version}-%{release}
# This legacy module for ephemeris support is outdated, providing limited
# support to obsoleted planetary ephemerides DE421 or earlier only. The 
# source code of is available in the documentation of the devel sub-package,
# so anyone can still build and link against these even in the absence of
# the shared library that is provided by this sub-package.
Provides:        deprecated()

%description solsys1
Optional SuperNOVAS plugin library that provides legacy solar-system routines 
for accessing older JPL planetary data (DE200 through DE421).
 
%package solsys2
Summary: Legacy solar-system plugin for the JPL PLEPH routines
Requires:        %{name}%{?_isa} >= %{version}-%{release}
# This legacy module for ephemeris support is half-baked, and requires 
# additional code by the user to become functional. It is also outdated and 
# unsupported. The source code is available in the documentation of the devel 
# sub-package, so anyone can still build and link against these even in the 
# absence of the shared library that is provided by this sub-package.
Provides:        deprecated()

%description solsys2
Optional SuperNOVAS plugin library that provides legacy solar-system routines 
for accessing older JPL planetary data through the JPL PLEPH routines. It 
requires a user-provided FORTRAN adapter module, and PLEPH library. This 
package is provided only to support legacy applications that were written for 
that particular interfacing.

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


%package cio-data
Summary:         CIO location data for the SuperNOVAS C/C++ astronomy library
BuildArch:       noarch
# Future versions of SuperNOVAS will no longer need or use such 
# data in any way. The data themselves are quite specific to this library
# anb are not expected to be useful for other packages.
Provides:        deprecated()

%description cio-data
Optional CIO location vs GCRS lookup table. This file is not normally required
for the operation of the library. It is needed only if the user explicitly needs
to know the location of the CIO vs GCRS, rather than w.r.t. the equinox of date.
Applications that require CIO location w.r.t. the GCRS should depend on this
sub-package. Future versions of SuperNOVAS will no longer need or use such 
data in any way. Therefore this sub-package is now deprecated.

%package devel
Summary:         C development files for the SuperNOVAS C/C++ astronomy library
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires:        %{name}-solsys1%{?_isa} = %{version}-%{release}
Requires:        %{name}-solsys2%{?_isa} = %{version}-%{release}
Requires:        %{name}-solsys-calceph%{?_isa} = %{version}-%{release}

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

export CALCEPH_SUPPORT=1
make %{?_smp_mflags} distro CIO_LOCATOR_FILE=%{_datadir}/%{name}/CIO_RA.TXT

%check

export CALCEPH_SUPPORT=1
make test

%install

export CALCEPH_SUPPORT=1
make DESTDIR=%{buildroot} libdir=%{_libdir} install

%files
%license LICENSE
%doc CHANGELOG.md
%{_libdir}/lib%{name}.so.1{,.*}

%files solsys1
%{_libdir}/libsolsys1.so.1{,.*}

%files solsys2
%{_libdir}/libsolsys2.so.1{,.*}

%files solsys-calceph
%{_libdir}/libsolsys-calceph.so.1{,.*}

%files cio-data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/CIO_RA.TXT

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%doc examples
%doc legacy
%doc CONTRIBUTING.md

%files doc
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/supernovas.tag
%doc %{_docdir}/%{name}/html

%changelog
%autochangelog
