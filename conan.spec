Name: conan
Version: 2.0.1
Release: 1%{?dist}

License: MIT
Summary: Open-source C/C++ package manager
URL: https://github.com/%{name}-io/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

# https://github.com/conan-io/conan/pull/13007
Patch100: %{name}-2.0.0-gcc13.patch

BuildRequires: python3-devel

Requires: cmake
Requires: gcc
Requires: gcc-c++
Requires: git-core
Requires: ninja-build

%description
Conan is a package manager for C and C++ developers.

It is fully decentralized. Users can host their packages on their servers,
privately. Integrates with Artifactory and Bintray.

Works across all platforms, including Linux, OSX, Windows (with native and
first-class support, WSL, MinGW), Solaris, FreeBSD, embedded and
cross-compiling, docker, WSL.

It can create, upload and download binaries for any configuration and
platform, even cross-compiling, saving lots of time in development and
continuous integration. The binary compatibility can be configured and
customized. Manage all your artifacts in the same way on all platforms.

Integrates with any build system. Provides tested support for major build
systems (CMake, MSBuild, Makefiles, Meson, etc).

Its python based recipes, together with extensions points allows for great
power and flexibility.

Large and active community, especially in Github and Slack. This community
also creates and maintains packages in ConanCenter and Bincrafters
repositories in Bintray.

%prep
%autosetup -p1
sed -e 's/, .*//g' -i %{name}s/requirements.txt
find -name '*.py' \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; -exec sed -i '1d' {} \; \)

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name} %{name}s

%files -f %{pyproject_files}
%license LICENSE.md
%doc README.rst contributors.txt
%{_bindir}/%{name}

%changelog
* Fri Mar 03 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.1-1
- Updated to version 2.0.1.

* Wed Feb 22 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-1
- Updated to version 2.0.0.

* Sat Feb 18 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.10.beta10
- Updated to version 2.0.0-beta10.

* Tue Jan 31 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.9.beta9
- Updated to version 2.0.0-beta9.

* Fri Jan 20 2023 Tom Callaway <spot@fedoraproject.org> - 2.0.0-0.8.beta8
- teach conan to make fire ... i mean, teach conan that gcc 13 exists

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.7.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.6.beta8
- Updated to version 2.0.0-beta8.

* Thu Dec 22 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.5.beta7
- Updated to version 2.0.0-beta7.

* Fri Dec 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.4.beta6
- Updated to version 2.0.0-beta6.

* Sat Nov 12 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.3.beta5
- Updated to version 2.0.0-beta5.

* Tue Oct 11 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.2.beta4
- Updated to version 2.0.0-beta4.

* Mon Sep 12 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.1.beta3
- Initial SPEC release.
