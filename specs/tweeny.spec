# This is a header-only library, but it install also cmake
# scripts to %%{_libdir}, so it cannot be noarch.
%global debug_package %{nil}

Name: tweeny
Version: 3.2.0
Release: 9%{?dist}

License: MIT
Summary: Modern C++ tweening library
URL: https://github.com/mobius3/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DTWEENY_BUILD_EXAMPLES:BOOL=OFF \
    -DTWEENY_BUILD_DOCUMENTATION:BOOL=OFF \
    -DTWEENY_BUILD_SANDBOX:BOOL=OFF
%cmake_build

%install
%cmake_install

%files devel
%doc README.md CHANGELOG.md
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/cmake/Tweeny

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 18 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-1
- Updated to version 3.2.0.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.1-1
- Updated to version 3.1.1.

* Sun Mar 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.0-1
- Updated to version 3.1.0.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3-1
- Updated to version 3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2-2.20180504git43f4130
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2-1.20180504git43f4130
- Initial SPEC release.
