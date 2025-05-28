%global debug_package %{nil}

%global         forgeurl0 https://github.com/tcbrindle/span
%global         version0  0
%global         date      20250521
%global         commit    836dc6a0efd9849cb194e88e4aa2387436bb079b
%forgemeta

Name:           span
Version:        %forgeversion -p
Release:        %autorelease
Summary:        Implementation of C++20's std::span for older compilers

License:        BSL-1.0

URL:            %forgeurl0
Source:         %forgesource0

# Fix build without exceptions
Patch0:         https://github.com/tcbrindle/span/pull/53.patch
# Make the project installable
Patch1:         span-Fedora_patches.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Catch2)

%global _description %{expand:
Single-header implementation of C++20's std::span, conforming to the C++20
committee draft. It is compatible with C++11, but will use newer language
features if they are available.

It differs from the implementation in the Microsoft GSL in that it is
single-header and does not depend on any other GSL facilities. It also works
with C++11, while the GSL version requires C++14.}

%description %{_description}

%package devel
Summary:        Development files for span
# Header-only package
Provides:       span-static = %{version}-%{release}

%description devel %{_description}

This package contains the development files.


%prep
%forgeautosetup -p1


%conf
%cmake


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%dir %{_includedir}/tcb
%{_includedir}/tcb/span.hpp
%license LICENSE_1_0.txt
%doc README.md


%changelog
%autochangelog
