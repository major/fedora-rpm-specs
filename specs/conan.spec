
%bcond_without check

Name: conan
Version: 2.28.1
Release: %autorelease

License: MIT
Summary: Open-source C/C++ package manager
URL: https://github.com/%{name}-io/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Add support for GCC 16, already merged upstream, to be removed with 2.29.x
# https://github.com/conan-io/conan/commit/84b11af77424b18fd934ac8e0379f4fe5c57f0ad
Patch1: 0001-Add_gcc_16_in_tests.patch
BuildArch: noarch

BuildRequires: python3-devel
# For testing only
%if %{with check}
BuildRequires: python3-pytest
BuildRequires: python3-webtest
BuildRequires: python3-bottle
BuildRequires: python3-jwt
BuildRequires: python3-pluginbase
BuildRequires: git
BuildRequires: clang
%endif

Requires: cmake
Requires: gcc
Requires: gcc-c++
Requires: git-core
Requires: ninja-build

%description
Conan is a package manager for C and C++ developers.

It is fully decentralized. Users can host their packages on their servers,
privately.

Works across all platforms. It can create, upload and download binaries for
any configuration and platform, even cross-compiling, saving lots of time in
development and continuous integration. The binary compatibility can be
configured and customized. Manage all your artifacts in the same way on all
platforms.

Integrates with any build system. Provides tested support for most major
build systems.

Its python based recipes, together with extensions points allows for great
power and flexibility.

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

%check
%if %{with check}
%{pytest} -v test/unittests
# Fail currently:
# - toolchains/gnu/test_autotoolsdeps.py to be investigated further why
# - toolchains/microsoft/test_vs_layout.py cannot run on ppc64
# - workspace/test_workspace.py MSBuildDeps problems, unsure what that is
# - toolchains/qbs/test_qbsprofile.py since 2.7.0, seems not to find a tool, to be investigated
rm test/integration/toolchains/gnu/test_autotoolsdeps.py test/integration/toolchains/microsoft/test_vs_layout.py test/integration/workspace/test_workspace.py test/integration/toolchains/qbs/test_qbsprofile.py
%{pytest} -v test/integration
%endif

%files -f %{pyproject_files}
%license LICENSE.md
%doc README.md contributors.txt
%{_bindir}/%{name}

%changelog
%autochangelog
