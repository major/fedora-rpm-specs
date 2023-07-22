%global debug_package %{nil}

Name: guidelines-support-library
Version: 4.0.0
Release: 5%{?dist}

License: MIT
URL: https://github.com/Microsoft/GSL
Summary: Guidelines Support Library
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/microsoft/GSL/pull/1027
Patch100: %{name}-wrong-version-fix.patch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: ninja-build

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description devel
The Guidelines Support Library (GSL) contains functions and types that are
suggested for use by the C++ Core Guidelines maintained by the Standard C++
Foundation. This repo contains Microsoft's implementation of GSL.

The entire implementation is provided inline in the headers under the gsl
directory. The implementation generally assumes a platform that implements
C++14 support.

While some types have been broken out into their own headers (e.g. gsl/span),
it is simplest to just include gsl/gsl and gain access to the entire library.

%prep
%autosetup -n GSL-%{version} -p1
sed -e '/-Werror/d' -i tests/CMakeLists.txt

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGSL_INSTALL:BOOL=ON \
    -DGSL_TEST:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc README.md CONTRIBUTING.md
%license LICENSE ThirdPartyNotices.txt
%{_datadir}/cmake/Microsoft.GSL/
%{_includedir}/gsl/

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.0-2
- Fixed wrong version number in exported CMake configs.

* Fri Jan 28 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.0-1
- Updated to version 4.0.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.0-2
- Added patch with architecture independent fixes.

* Fri Jun 05 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.0-1
- Updated to version 3.1.0.

* Sat Apr 25 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.1-1
- Updated to version 3.0.1.

* Fri Apr 17 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.0-1
- Updated to version 3.0.0.

* Mon Feb 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.0-1
- Updated to version 2.1.0.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Updated to version 1.0.0.

* Thu Mar 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20180305gitc9e423d
- Updated to latest snapshot.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20171014git1c95f94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20171014git1c95f94
- Initial SPEC release.
