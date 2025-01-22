%global debug_package %{nil}

Name: cxxopts
Version: 3.2.1
Release: 3%{?dist}

Summary: Lightweight C++ command line option parser
License: MIT
URL: https://github.com/jarro2783/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/jarro2783/cxxopts/commit/63d1b65a694cfceafc20863afa75df49dfbe6b2a
Patch100: %{name}-3.2.1-add-missing-include.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
CXXOpts is a lightweight C++ option parser library, supporting the standard
GNU style syntax for options.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCXXOPTS_ENABLE_INSTALL:BOOL=ON \
    -DCXXOPTS_ENABLE_WARNINGS:BOOL=OFF \
    -DCXXOPTS_BUILD_EXAMPLES:BOOL=ON \
    -DCXXOPTS_BUILD_TESTS:BOOL=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 21 2024 Orion Poplawski <orion@nwra.com> - 3.2.1-1
- Update to 3.2.1

* Fri Feb 16 2024 Orion Poplawski <orion@nwra.com> - 3.2.0-1
- Update to 3.2.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 15 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.1-1
- Updated to version 3.1.1.

* Wed Feb 15 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.0-1
- Updated to version 3.1.0.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.0-2
- Explicitly disabled -Werror flag.

* Sat Oct 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.0-1
- Updated to version 3.0.0.

* Wed Jul 28 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.2.1-4
- Provide un-arched versions of virtual Provides

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.1-1
- Updated to version 2.2.1.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.0-1
- Initial SPEC release.
