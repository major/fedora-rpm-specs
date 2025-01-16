Name:           optional-lite
Version:        3.6.0
Release:        %autorelease
Summary:        Represent optional (nullable) objects and pass them by value

License:        BSL-1.0
URL:            https://github.com/martinmoene/optional-lite
Source:         %{url}/archive/v%{version}/optional-lite-%{version}.tar.gz

# Convert CHANGES.txt to UTF-8 (from, apparently, Windows-1252)
# https://github.com/martinmoene/optional-lite/pull/80
Patch:          %{url}/pull/80.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

# Required for testing; bundled upstream, unbundled in %%prep.
# Header-only library (-static required by policy)
BuildRequires:  lest-devel lest-static

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
A single-file header-only version of a C++17-like optional, a nullable object
for C++98, C++11 and later.}

%description %{common_description}


%package devel
Summary:        Development files for %{name}

# Header-only library
Provides:       %{name}-static = %{version}-%{release}

%description devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n optional-lite-%{version}

# Unbundle lest
rm -rvf test/lest
ln -s /usr/include/lest test/lest


%conf
%cmake


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%license LICENSE.txt
%doc CHANGES.txt
%doc README.md
%doc example/

# Contains gdb/nonstd_optional_printer.py. We would like to be able to install
# this system-wide so it could be automatically initialized, and there is some
# relevant documentation at
#
# https://sourceware.org/gdb/current/onlinedocs/gdb.html/Writing-a-Pretty_002dPrinter.html
#
# but it’s not quite clear how to correctly tie everything together. Help is
# welcome; until then, we just install the pretty-printer as documentation.
%doc extra/

# This directory may end up being co-owned with packages for similar libraries,
# e.g. bit-lite, by the same author.
%dir %{_includedir}/nonstd/
%{_includedir}/nonstd/optional.hpp

%{_libdir}/cmake/optional-lite/


%changelog
%autochangelog
