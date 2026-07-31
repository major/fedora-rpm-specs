Name:           dftd4
Version:        4.2.0
Release:        1%{?dist}
Summary:        Generally Applicable Atomic-Charge Dependent London Dispersion Correction
License:        LGPL-3.0-or-later
URL:            https://dftd4.readthedocs.io/
Source0:        https://github.com/dftd4/dftd4/archive/v%{version}/%{name}-%{version}.tar.gz
# get_numerical_hessian_api is missing from the public list of the dftd4_api
# module, so gcc >= 16.1.1-4 drops the dftd4_get_numerical_hessian symbol
Patch0:         dftd4-4.2.0-export-numerical-hessian.patch

BuildRequires:  meson
BuildRequires:  gcc-gfortran
BuildRequires:  mctc-lib-devel
BuildRequires:  mstore-devel
BuildRequires:  multicharge-devel
BuildRequires:  flexiblas-devel
BuildRequires:  python3-devel
BuildRequires:  python3-cffi
BuildRequires:  python3-setuptools
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
%patch -P 0 -p 1 -b .numhess

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
# The tests are parallel code, so only run one at a time
export RPM_BUILD_NCPUS=1
%meson_test --timeout-multiplier 4

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
* Thu Jul 23 2026 Susi Lehtola <susi.lehtola@iki.fi> - 4.2.0-1
- Update to 4.2.0.

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Wed Jun 03 2026 Python Maint <python-maint@redhat.com> - 3.7.0-12
- Rebuilt for Python 3.15

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 3.7.0-9
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 3.7.0-8
- Rebuilt for Python 3.14.0rc2 bytecode

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 3.7.0-6
- Rebuilt for Python 3.14

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
