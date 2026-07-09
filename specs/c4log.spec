# The project contains a version number, but a release has never been tagged.
# The project is normally used as a git submodule and referred to by commit
# hash.
%global commit 23e9bdba1edca287042b45d6ae6c8ea0fb1ad211
%global snapdate 20260624

# Upstream defaults to C++11, but recommends building c4core and rapidyaml with
# the same standard; and rapidyaml is built as C++17 because gtest 1.17.0 or
# later requires C++17 or later. Since c4log supports the tests for c4core, it
# makes sense to apply the same advice here as well. See:
# https://github.com/biojppm/rapidyaml/issues/465#issuecomment-2307668270
%global cxx_std 17

Name:           c4log
Summary:        C++ type-safe logging, mean and lean
Version:        0.0.1^%{snapdate}.%{sub %{commit} 1 7}
# This is the same as the version number. To prevent undetected soversion
# bumps, we nevertheless express it separately.
%global so_version 0.0.1
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/biojppm/c4log
Source:         %{url}/archive/%{commit}/c4log-%{commit}.tar.gz

# Upstream always wants to build with c4core as a git submodule, but we want to
# unbundle it and build with an external library. We therefore maintain this
# patch without sending it upstream.
Patch:          c4log-b8b86f3-external-c4core.patch

BuildSystem:    cmake
# We can stop the CMake scripts from downloading doctest by setting
# C4LOG_CACHE_DOWNLOAD_DOCTEST to any directory that exists.
BuildOption(conf): %{shrink:
    -DCMAKE_CXX_STANDARD=%{cxx_std}
    -DC4LOG_CACHE_DOWNLOAD_DOCTEST:PATH=/
    -DC4LOG_BUILD_TESTS=ON
    }

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
# Minimum version with proper multilib (GNUInstallDirs) support
BuildRequires:  c4project >= 0^20260428.fa85cab-1

BuildRequires:  cmake(c4core)

# For each header-only library, the guidelines require us to BR the -static
# package for tracking.
BuildRequires:  doctest-devel
BuildRequires:  doctest-static

%description
%{summary}.


%package devel
Summary:        Development files for c4log

Requires:       c4log%{?_isa} = %{version}-%{release}
Requires:       c4core-devel%{?_isa}

%description devel
The c4log-devel package contains libraries and header files for developing
applications that use c4log.


%prep -a
# Remove/unbundle additional dependencies

# c4project (CMake build scripts)
cp --recursive --preserve '%{_datadir}/cmake/c4project' ext/c4core/cmake

# Do not try to link against a nonexistent doctest library (doctest is
# header-only, and we do not have the complete CMake project for doctest that
# would provide a target that knows this):
sed --regexp-extended --in-place \
    --expression 's/(LIBS.*)\bdoctest\b/\1/' \
    --expression 's/(c4_setup_testing\()DOCTEST\)/\1\)/' \
    test/CMakeLists.txt


%check
%cmake_build --target c4log-test-run-verbose


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libc4log.so.%{so_version}


%files devel
# %%{_includedir}/c4 is owned by c4core-devel
%{_includedir}/c4/log/
%{_libdir}/libc4log.so
%{_libdir}/cmake/c4log/


%changelog
%autochangelog
