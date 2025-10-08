%ifarch s390x
%bcond libcerf 0
%else
%bcond libcerf 1
%endif

Name:           libecpint
Version:        1.0.7
Release:        16%{?dist}
Summary:        Efficient evaluation of integrals over ab initio effective core potentials
License:        MIT
Url:            https://github.com/robashaw/libecpint
Source0:        https://github.com/robashaw/libecpint/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix build with libcerf 3 - https://github.com/robashaw/libecpint/pull/66
Patch:          libecpint-cerf3.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.12
BuildRequires:  pugixml-devel
BuildRequires:  gtest-devel
%if %{with libcerf}
BuildRequires:  libcerf-devel >= 1.17
%else
Provides:       bundled(Faddeeva}
%endif
BuildRequires:  python3
BuildRequires:  doxygen
BuildRequires:  sphinx
Requires:       %{name}-common = %{version}-%{release}

%description
Libecpint is a C++ library for the efficient evaluation of integrals over ab
initio effective core potentials, using a mixture of generated, recursive
code and Gauss-Chebyshev quadrature. It is designed to be standalone and
generic.

%package common
Summary:        Architecture independent data files for libecpint
BuildArch:      noarch

%description common
This package contains architecture independent data files for libecpint

%package devel
Summary:        Devel package for libecpint
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libcerf-devel >= 1.17

%description devel
This package contains development headers and libraries for libecpint.

%prep
%autosetup -p1
# gtest 1.17.0 requires C++17 or later
# https://github.com/robashaw/libecpint/issues/58
sed -r -i 's/\b(CMAKE_CXX_STANDARD[[:blank:]]+)11\b/\117/' CMakeLists.txt

%build
%cmake %{?with_libcerf:-DLIBECPINT_USE_CERF=ON}
%cmake_build

%install
%cmake_install

%check
%ctest %{?testargs}

%files
%doc README.md CITATION
%{_libdir}/lib*.so.*

%files common
%{_datadir}/%{name}
%license LICENSE

%files devel
%{_includedir}/libecpint/
%{_includedir}/libecpint.hpp
%{_libdir}/cmake/ecpint
%{_libdir}/lib*.so

%changelog
* Mon Oct 06 2025 Terje Rosten <terjeros@gmail.com> - 1.0.7-16
- Switch to C++17 for gtest 1.17.0

* Tue Aug 12 2025 Orion Poplawski <orion@nwra.com> - 1.0.7-15
- No libcerf-3 on s390x

* Tue Aug 12 2025 Christoph Junghans <junghans@votca.org> - 1.0.7-14
- Rebuild for libcerf-3

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0.7-7
- Compile as C++14 for gtest 1.13.0 compatibility

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 10 2022 Christoph Junghans <junghans@votca.org> - 1.0.7-4
- Rebuild for libcerf-2.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Christoph Junghans <junghans@votca.org> - 1.0.7-2
- fix devel deps

* Mon Dec 06 2021 Christoph Junghans <junghans@votca.org> - 1.0.7-1
- Version bump to v1.0.7 (bug #2029226)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr 17 2021 Christoph Junghans <junghans@votca.org> - 1.0.6-1
- Version bump to v1.0.6 (bug #1950217)

* Fri Feb 05 2021 Christoph Junghans <junghans@votca.org> - 1.0.5-1
- Version bump to v1.0.5 (bug #1925367)

* Wed Jan 27 2021 Christoph Junghans <junghans@votca.org> - 1.0.4-3
- Add patch to fix memory leak

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 11:21:34 MST 2021 Christoph Junghans <junghans@lanl.gov> - 1.0.4-1
- Version bump to v1.0.4 (bug #19154510)

* Tue Oct 06 2020 Christoph Junghans <junghans@votca.org> - 1.0.2-1
- Initial add for packaging
