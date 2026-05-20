%bcond ctest 1

Name:           optional-lite
Version:        3.6.0
Release:        %autorelease
Summary:        Represent optional (nullable) objects and pass them by value

License:        BSL-1.0
URL:            https://github.com/martinmoene/optional-lite
Source:         %{url}/archive/v%{version}/optional-lite-%{version}.tar.gz

BuildSystem:    cmake
BuildOption(conf): %{shrink:
    -DOPTIONAL_LITE_OPT_BUILD_TESTS:BOOL=%{?with_ctest:ON}%{?!with_ctest:OFF}
    }

BuildRequires:  gcc-c++

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


%prep -a
# Unbundle lest
rm --recursive --verbose test/lest
ln --symbolic /usr/include/lest test/lest


%files devel
%license LICENSE.txt
# We don’t package CHANGES.txt because it is hasn’t been updated since release
# 1.0.2, so it isn’t very useful. If we did, we would need to fix its encoding,
# https://github.com/martinmoene/optional-lite/pull/80.
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

# This directory is co-owned with packages for similar libraries, e.g.
# variant-lite, by the same author.
%dir %{_includedir}/nonstd/
%{_includedir}/nonstd/optional.hpp

%{_libdir}/cmake/optional-lite/


%changelog
%autochangelog
