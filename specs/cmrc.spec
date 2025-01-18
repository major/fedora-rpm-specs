%global appname cmakerc
%global _description %{expand:
CMakeRC is a resource compiler provided in a single CMake script that can
easily be included in another project.

For the purpose of this project, a resource compiler is a tool that will
compile arbitrary data into a program. The program can then read this data
from without needing to store that data on disk external to the program.}

Name: cmrc
Version: 2.0.1
Release: 7%{?dist}

License: MIT
Summary: Standalone CMake-Based C++ Resource Compiler
URL: https://github.com/vector-of-bool/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

# https://github.com/vector-of-bool/cmrc/pull/40
Patch100: %{name}-installation.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description %{_description}

%package devel
Summary: Standalone CMake-Based C++ Resource Compiler
Provides: %{appname} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{appname}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel %{_description}

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE.txt
%{_datadir}/cmake/%{appname}/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 11 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.1-1
- Initial SPEC release.
