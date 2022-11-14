%global beta beta5

Name: conan
Version: 2.0.0
Release: 0.3.%{beta}%{?dist}

License: MIT
Summary: Open-source C/C++ package manager
URL: https://github.com/%{name}-io/%{name}
Source0: %{url}/archive/%{version}-%{beta}/%{name}-%{version}-%{beta}.tar.gz
BuildArch: noarch

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
%autosetup -n %{name}-%{version}-%{beta}
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
* Sat Nov 12 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.3.beta5
- Updated to version 2.0.0-beta5.

* Tue Oct 11 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.2.beta4
- Updated to version 2.0.0-beta4.

* Mon Sep 12 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.1.beta3
- Initial SPEC release.
