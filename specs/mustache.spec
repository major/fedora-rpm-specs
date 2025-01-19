%global appname Mustache

Name: mustache
Version: 4.1
Release: 14%{?dist}

License: BSL-1.0
Summary: Mustache text templates for modern C++

URL: https://github.com/kainjow/%{appname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/kainjow/Mustache/pull/42
Patch100: %{name}-4.1-catch-fixes.patch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

# mustache currently support only catch v2
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10
BuildRequires: catch2-devel
%else
BuildRequires: catch-devel
%endif

BuildArch: noarch

%description
Text templates implementation for modern C++ (requires C++11).

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The %{name}-devel package contains C++ headers for developing
applications that use %{name}.

%prep
%autosetup -n %{appname}-%{version}
sed -e '/-Werror/d' -i CMakeLists.txt
ln -svf %{_includedir}/catch2/catch.hpp ./catch.hpp

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%check
%ctest

%install
mkdir -p %{buildroot}%{_includedir}
install -m 0644 -p %{name}.hpp %{buildroot}%{_includedir}

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 4.1-9
- Fixed FTBFS in EPEL/ELN due to catch v3 update.

* Tue Feb 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 4.1-8
- Fixed FTBFS due to catch v3 update.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 4.1-1
- Updated to version 4.1.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0-1
- Updated to version 4.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.1-1
- Initial SPEC release.
