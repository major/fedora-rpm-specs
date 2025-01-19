Name:           multicharge
Version:        0.3.0
Release:        4%{?dist}
Summary:        Electronegativity equilibration model for atomic partial charges
License:        Apache-2.0
URL:            https://github.com/grimme-lab/multicharge
Source0:        https://github.com/grimme-lab/multicharge/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-gfortran
BuildRequires:  mctc-lib-devel
BuildRequires:  flexiblas-devel
BuildRequires:  mstore-devel
BuildRequires:  rubygem-asciidoctor

%description
Electronegativity equilibration model for atomic partial charges.

%package devel
Summary:        Development headers for multicharge
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers for multicharge

%prep
%autosetup

%build
%ifarch %{ix86}
# flexiblas64 not available on ix86 architecture
%meson -Dlapack=custom -Dcustom_libraries=flexiblas -Dilp64=false
%else
%meson -Dlapack=custom -Dcustom_libraries=flexiblas64 -Dilp64=true
%endif
%meson_build

%install
%meson_install
# Move Fortran modules to the right place
mkdir -p %{buildroot}%{_libdir}/gfortran/modules
mv %{buildroot}%{_includedir}/multicharge/gcc-*/*.mod %{buildroot}%{_libdir}/gfortran/modules
# Remove static library
\rm %{buildroot}%{_libdir}/libmulticharge.a

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libmulticharge.so.*
%{_bindir}/multicharge
%{_mandir}/man1/multicharge.1*

%files devel
%{_libdir}/libmulticharge.so
%{_libdir}/gfortran/modules/multicharge*.mod
%{_libdir}/pkgconfig/multicharge.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 07 2024 Susi Lehtola <susi.lehtola@iki.fi> - 0.3.0-3
- Add missing require in devel package.

* Sat Sep 07 2024 Susi Lehtola <susi.lehtola@iki.fi> - 0.3.0-2
- Add BR: rubygem-asciidoctor and fix flexiblas link on ix86.

* Fri Sep 06 2024 Susi Lehtola <susi.lehtola@iki.fi> - 0.3.0-1
- First release.
