Name:           calceph
Version:        4.0.4
Release:        %autorelease
Summary:        Astronomical library to access planetary ephemeris files

License:        CECILL-2.0 OR CECILL-B OR CECILL-C
URL:            https://www.imcce.fr/inpop/calceph
Source0:        https://www.imcce.fr/content/medias/recherche/equipes/asd/%{name}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Documentation build doesn't work anymore because it relies on several
# sphinx extensions not packaged / not packageable in Fedora
Obsoletes:      calceph-docs < 4.0.0

BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  cmake

%description
This library is designed to access the binary planetary ephemeris files,
such INPOPxx, JPL DExxx and SPICE ephemeris files.


%package        libs
Summary:        %{name} shared libraries
License:        CECILL-2.0 OR CECILL-B OR CECILL-C

%description    libs
Calceph shared libraries.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        fortran-devel
Summary:        Development files for using %{name} Fortran bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%if 0%{?fedora}
Requires:       gcc-gfortran%{?_isa}
%else
Requires:       gcc-gfortran
%endif

%description    fortran-devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake \
    -DBUILD_SHARED_LIBS=ON

%cmake_build


%install
%cmake_install


%check
%ctest


%files
%{_bindir}/calceph_*
%{_mandir}/man1/calceph_*.1.gz


%files      libs
%license COPYING_CECILL_V2.1.LIB COPYING_CECILL_B.LIB COPYING_CECILL_C.LIB
%{_libdir}/libcalceph.so.2
%{_libdir}/libcalceph.so.2.*


%files      devel
%{_libdir}/libcalceph.so
%{_libdir}/cmake/calceph
%{_includedir}/calceph.h


%files      fortran-devel
%{_includedir}/calceph.mod
%{_includedir}/f90calceph.h


%changelog
%autochangelog
