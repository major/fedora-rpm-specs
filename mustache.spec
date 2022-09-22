%global appname Mustache

Name: mustache
Version: 4.1
Release: 6%{?dist}

License: Boost
Summary: Mustache text templates for modern C++

URL: https://github.com/kainjow/%{appname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/kainjow/Mustache/pull/42
Patch100: %{name}-4.1-catch-fixes.patch

BuildRequires: catch-devel
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

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
