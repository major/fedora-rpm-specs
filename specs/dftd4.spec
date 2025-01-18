Name:           dftd4
Version:        3.7.0
Release:        5%{?dist}
Summary:        Generally Applicable Atomic-Charge Dependent London Dispersion Correction
License:        LGPL-3.0-or-later
URL:            https://dftd4.readthedocs.io/
Source0:        https://github.com/dftd4/dftd4/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-gfortran
BuildRequires:  mctc-lib-devel
BuildRequires:  mstore-devel
BuildRequires:  multicharge-devel
BuildRequires:  flexiblas-devel
BuildRequires:  python3-devel
BuildRequires:  python3-cffi
BuildRequires:  rubygem-asciidoctor

%description
Generally Applicable Atomic-Charge Dependent London Dispersion Correction.

%package devel
Summary:        Development headers for dftd4
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers for dftd4

%package -n python3-dftd4
Summary:        Python 3 interface for dftd4
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-dftd4
This package contains the Python 3 interface for dftd4.

%prep
%setup -q

%build
%ifarch %{ix86}
# flexiblas64 not available on ix86 architecture
%meson -Dlapack=custom -Dcustom_libraries=flexiblas -Dilp64=false -Dpython=true
%else
%meson -Dlapack=custom -Dcustom_libraries=flexiblas64 -Dilp64=true -Dpython=true
%endif
%meson_build

%install
%meson_install
# Move Fortran modules to the right place
mkdir -p %{buildroot}%{_libdir}/gfortran/modules
mv %{buildroot}%{_includedir}/dftd4/gcc-*/*.mod %{buildroot}%{_libdir}/gfortran/modules
# Remove static library
\rm %{buildroot}%{_libdir}/libdftd4.a

%check
# Reduce parallellism and increase the timeout multiplier since the default is not enough on some architectures
MESON_TESTTHREADS=2 %meson_test --timeout-multiplier 4

%files
%license COPYING COPYING.LESSER
%doc README.md
%{_libdir}/libdftd4.so.*
%{_bindir}/dftd4
%{_mandir}/man1/dftd4.1*
%{_datadir}/dftd4/

%files devel
%{_libdir}/libdftd4.so
%{_libdir}/gfortran/modules/dftd4*.mod
%{_libdir}/pkgconfig/dftd4.pc
%{_includedir}/dftd4.h

%files -n python3-dftd4
%{python3_sitearch}/dftd4/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 12 2024 Susi Lehtola <susi.lehtola@iki.fi> - 3.7.0-4
- Add missing BR: mstore-devel and python3-cffi.

* Sat Sep 07 2024 Susi Lehtola <susi.lehtola@iki.fi> - 3.7.0-3
- Add missing requires in the subpackages.

* Fri Sep 06 2024 Susi Lehtola <susi.lehtola@iki.fi> - 3.7.0-2
- Add BR: rubygem-asciidoctor and fixed link to flexiblas on ix86.

* Fri Sep 06 2024 Susi Lehtola <susi.lehtola@iki.fi> - 3.7.0-1
- First release.
