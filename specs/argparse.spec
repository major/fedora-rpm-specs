# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

Name:           argparse
Version:        3.2
Release:        %autorelease
Summary:        Argument parser for modern C++

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

License:        MIT
URL:            https://github.com/p-ranav/argparse
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Argparse is an argument parser for C++17 in a single header file.

%package devel
Summary:        Argument parser for modern C++
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description devel
Argparse is an argument parser for C++17 in a single header file.

%prep
%autosetup

%conf
# Install into the noarch directory
# https://github.com/p-ranav/argparse/pull/323
sed -i 's/CMAKE_INSTALL_LIBDIR/CMAKE_INSTALL_DATADIR/' CMakeLists.txt

# Fix end of line encoding
sed -i.orig 's/\r//' README.md
touch -r README.md.orig README.md
rm README.md.orig

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%{_vpath_builddir}/test/tests

%files devel
%doc README.md
%license LICENSE
%{_includedir}/argparse/
%{_datadir}/cmake/argparse/
%{_datadir}/pkgconfig/argparse.pc

%changelog
%autochangelog
