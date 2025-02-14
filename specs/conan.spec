Name: conan
Version: 2.12.2
Release: %autorelease

License: MIT
Summary: Open-source C/C++ package manager
URL: https://github.com/%{name}-io/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
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

%files -f %{pyproject_files}
%license LICENSE.md
%doc README.md contributors.txt
%{_bindir}/%{name}

%changelog
%autochangelog
