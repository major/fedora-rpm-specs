Name:           mstore
Version:        0.3.0
Release:        3%{?dist}
Summary:        Molecular structure store for testing
License:        Apache-2.0
URL:            https://github.com/grimme-lab/mstore
Source0:        https://github.com/grimme-lab/mstore/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-gfortran
BuildRequires:  mctc-lib-devel

%description
Molecular structure store for testing

%package devel
Summary:       Development headers for mstore
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers for mstore.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
# Move Fortran modules to the right place
mkdir -p %{buildroot}%{_libdir}/gfortran/modules
mv %{buildroot}%{_includedir}/mstore/gcc-*/*.mod %{buildroot}%{_libdir}/gfortran/modules
# Remove static library
\rm %{buildroot}%{_libdir}/libmstore.a

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libmstore.so.*
%{_bindir}/mstore-info

%files devel
%{_libdir}/libmstore.so
%{_libdir}/gfortran/modules/mstore*.mod
%{_libdir}/pkgconfig/mstore.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 07 2024 Susi Lehtola <susi.lehtola@iki.fi> - 0.3.0-2
- Add missing require in devel package.

* Fri Sep 06 2024 Susi Lehtola <susi.lehtola@iki.fi> - 0.3.0-1
- First release
