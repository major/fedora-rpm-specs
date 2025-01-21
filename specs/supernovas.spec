%global upstream_version     1.2.0

Name:            supernovas
Version:         1.2.0
Release:         10%{?dist}
Summary:         The Naval Observatory's NOVAS C astronomy library, made better 
License:         Unlicense
URL:             https://smithsonian.github.io/SuperNOVAS
Source0:         https://github.com/Smithsonian/SuperNOVAS/archive/refs/tags/v%{upstream_version}.tar.gz

# No i686 calceph package to build against
ExcludeArch:     %{ix86}

BuildRequires:   calceph-devel%{_isa}
BuildRequires:   gcc
BuildRequires:   sed
BuildRequires:   doxygen >= 1.9.0
Suggests:        %{name}-cio-data = %{version}-%{release}
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
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description solsys1
Optional SuperNOVAS plugin library that provides legacy solar-system routines 
for accessing older JPL planetary data (DE200 through DE421).
 
%package solsys2
Summary: Legacy solar-system plugin for the JPL PLEPH routines
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description solsys2
Optional SuperNOVAS plugin library that provides legacy solar-system routines 
for accessing older JPL planetary data through the JPL PLEPH routines. It 
requires a user-provided FORTRAN adapter module, and PLEPH library. This 
package is provided only to support legacy applications that were written for 
that particular interfacing.

%package solsys-calceph
Summary: Solar-system plugin based on the CALCEPH C library
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires:        calceph-libs%{?_isa}

%description solsys-calceph
Optional SuperNOVAS plugin library that provides Solar-system support via the 
CALCEPH C library. It allows using both JPL (SPK) and INPOP 2.0/3.0 data files 
with SuperNOVAS to obtain precise locations for Solar-system bodies. This 
plugin is currently the preferred option to use for Fedora / RPM Linux 
development, which requires use of precise Solar-system data.


%package cio-data
Summary:         CIO location data for the SuperNOVAS C/C++ astronomy library
BuildArch:       noarch

%description cio-data
Optional CIO location vs GCRS lookup table. This file is not normally required
for the operation of the library. It is needed only if the user explicitly needs
to know the location of the CIO vs GCRS, rather than w.r.t. the equinox of date.
Applications that require CIO location w.r.t. the GCRS should depend on this
sub-package

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
Requires:        %{name} = %{version}-%{release}

%description doc
This package provides man pages and HTML documentation for the SuperNOVAS 
C/C++ astronomy library.

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
%doc CONTRIBUTING.md
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*.c
%doc %{_docdir}/%{name}/*.f
%{_prefix}/include/*
%{_libdir}/*.so

%files doc
%doc %{_docdir}/%{name}/%{name}.tag
%doc %{_docdir}/%{name}/html

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild


* Thu Jan 16 2025 Attila Kovacs <attipaci@gmail.com> - 1.2.0-9
- Bad dates in changelog

* Thu Jan 16 2025 Attila Kovacs <attipaci@gmail.com> - 1.2.0-8
- Fix solsys-calceph subpackage dependence

* Thu Jan 16 2025 Attila Kovacs <attipaci@gmail.com> - 1.2.0-7
- Switch to manual changelog
- Remove unwanted files committed earlier

* Thu Jan 16 2025 Attila Kovacs <attipaci@gmail.com> - 1.2.0-6
- Upstream rerelease v1.2.0 (fixes .so links)

* Wed Jan 15 2025 Attila Kovacs <attipaci@gmail.com> - 1.2.0-5
- Various small fixes to spec file

* Wed Jan 15 2025 Attila Kovacs <attipaci@gmail.com> - 1.2.0-4
- Exclude only solsys-calceph subpackage from i686 build

* Wed Jan 15 2025 Attila Kovacs <attipaci@gmail.com> - 1.2.0-3
- Exclude i686 from build

* Wed Jan 15 2025 Attila Kovacs <attipaci@gmail.com> - 1.2.0-2
- BuildRequires w/o {_isa}

* Wed Jan 15 2025 Attila Kovacs <attipaci@gmail.com> - 1.2.0-1
- Upstream v1.2.0

* Wed Nov 06 2024 Attila Kovacs <attipaci@gmail.com> - 1.1.1-1
- Upstream v1.1.1-2

* Sat Aug 03 2024 Attila Kovacs <attipaci@gmail.com> - 1.1.0-2
- v1.1.0-2: re-release with fixes to regression testing

* Sat Aug 03 2024 Attila Kovacs <attipaci@gmail.com> - 1.1.0-1
- Update to upstream SuperNOVAS v1.1.0

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Attila Kovacs <attipaci@gmail.com> - 1.0.1-1
- Initial import (fedora#2283055)

