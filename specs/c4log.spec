# The project contains a version number, but a release has never been tagged.
# The project is normally used as a git submodule and referred to by commit
# hash.
%global commit f4cf64caedd622a739aaa3ecb67a5aac105c2919
%global snapdate 20240501

# Upstream defaults to C++11, but recommends building c4core and rapidyaml with
# the same standard; and rapidyaml is built as C++14 because gtest 1.13.0 or
# later requires C++14 or later. Since c4fs supports the tests for c4core, it
# makes sense to apply the same advice here as well. See:
# https://github.com/biojppm/rapidyaml/issues/465#issuecomment-2307668270
%global cxx_std 14

Name:           c4log
Summary:        C++ type-safe logging, mean and lean
Version:        0.0.1^%{snapdate}git%{sub %{commit} 1 7}
# This is the same as the version number. To prevent undetected soversion
# bumps, we nevertheless express it separately.
%global so_version 0.0.1
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/biojppm/c4log
Source:         %{url}/archive/%{commit}/c4log-%{commit}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:    %{ix86}
%endif

# Upstream always wants to build with c4core as a git submodule, but we want to
# unbundle it and build with an external library. We therefore maintain this
# patch without sending it upstream.
Patch:          c4log-b8b86f3-external-c4core.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  c4project
# Our choice; the default make backend should work just as well
BuildRequires:  ninja-build

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


%prep
%autosetup -n c4log-%{commit} -p1

# Remove/unbundle additional dependencies

# c4project (CMake build scripts)
ln -s '%{_datadir}/cmake/c4project' ext/c4core/cmake

# Do not try to link against a nonexistent doctest library (doctest is
# header-only, and we do not have the complete CMake project for doctest that
# would provide a target that knows this):
sed -r -i 's/\bdoctest\b//' test/CMakeLists.txt


%conf
# We can stop the CMake scripts from downloading doctest by setting
# C4LOG_CACHE_DOWNLOAD_DOCTEST to any directory that exists.
%cmake -GNinja \
  -DCMAKE_CXX_STANDARD=%{cxx_std} \
  -DC4LOG_CACHE_DOWNLOAD_DOCTEST:PATH=/ \
  -DC4LOG_BUILD_TESTS=ON


%build
%cmake_build


%install
%cmake_install
# Fix wrong installation paths for multilib; it would be nontrivial to patch
# the source to get this right in the first place. The installation path is
# determined by the scripts in https://github.com/biojppm/cmake, packaged as
# c4project.
#
# Installation directory on Linux 64bit OS
# https://github.com/biojppm/rapidyaml/issues/256
if [ '%{_libdir}' != '%{_prefix}/lib' ]
then
  mkdir -p '%{buildroot}%{_libdir}'
  mv -v %{buildroot}%{_prefix}/lib/libc4log.so* '%{buildroot}%{_libdir}/'
  mkdir -p '%{buildroot}%{_libdir}/cmake'
  mv -v %{buildroot}%{_prefix}/lib/cmake/c4log '%{buildroot}%{_libdir}/cmake/'
  find %{buildroot}%{_libdir}/cmake/c4log -type f -name '*.cmake' -print0 |
    xargs -r -t -0 sed -r -i "s@/lib/@/$(basename '%{_libdir}')/@"
fi


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
