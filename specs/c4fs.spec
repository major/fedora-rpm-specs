# The project contains a version number, but a release has never been tagged.
# The project is normally used as a git submodule and referred to by commit
# hash.
%global commit 1e00cc787787c2a0f30d293a9e45646da7c4b5c0
%global snapdate 20250124

# Upstream defaults to C++11, but recommends building c4core and rapidyaml with
# the same standard; and rapidyaml is built as C++14 because gtest 1.13.0 or
# later requires C++14 or later. Since c4fs supports the tests for c4core, it
# makes sense to apply the same advice here as well. See:
# https://github.com/biojppm/rapidyaml/issues/465#issuecomment-2307668270
%global cxx_std 14

Name:           c4fs
Summary:        C++ file system utilities
Version:        0.0.1^%{snapdate}git%{sub %{commit} 1 7}
# This is the same as the version number. To prevent undetected soversion
# bumps, we nevertheless express it separately.
%global so_version 0.0.1
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/biojppm/c4fs
Source:         %{url}/archive/%{commit}/c4fs-%{commit}.tar.gz

# Upstream always wants to build with c4core as a git submodule, but we want to
# unbundle it and build with an external library. We therefore maintain this
# patch without sending it upstream.
Patch:          c4fs-1abba00-external-c4core.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:    %{ix86}
%endif

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
Summary:        Development files for c4fs

Requires:       c4fs%{?_isa} = %{version}-%{release}
Requires:       c4core-devel%{?_isa}

%description devel
The c4fs-devel package contains libraries and header files for developing
applications that use c4fs.


%prep
%autosetup -n c4fs-%{commit} -p1

# Remove/unbundle additional dependencies

# c4project (CMake build scripts)
find ext
cp -rp '%{_datadir}/cmake/c4project' ext/c4core/cmake

# Do not try to link against a nonexistent doctest library (doctest is
# header-only, and we do not have the complete CMake project for doctest that
# would provide a target that knows this):
sed -r -i \
    -e 's/(LIBS.*)\bdoctest\b/\1/' \
    -e 's/(c4_setup_testing\()DOCTEST\)/\1\)/' \
    test/CMakeLists.txt


%conf
# We can stop the CMake scripts from downloading doctest by setting
# C4FS_CACHE_DOWNLOAD_DOCTEST to any directory that exists.
%cmake -GNinja \
  -DCMAKE_CXX_STANDARD=%{cxx_std} \
  -DC4FS_CACHE_DOWNLOAD_DOCTEST:PATH=/ \
  -DC4FS_BUILD_TESTS=ON


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
  mv -v %{buildroot}%{_prefix}/lib/libc4fs.so* '%{buildroot}%{_libdir}/'
  mkdir -p '%{buildroot}%{_libdir}/cmake'
  mv -v %{buildroot}%{_prefix}/lib/cmake/c4fs '%{buildroot}%{_libdir}/cmake/'
  find %{buildroot}%{_libdir}/cmake/c4fs -type f -name '*.cmake' -print0 |
    xargs -r -t -0 sed -r -i "s@/lib/@/$(basename '%{_libdir}')/@"
fi


%check
%cmake_build --target c4fs-test-run-verbose


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libc4fs.so.%{so_version}


%files devel
# %%{_includedir}/c4 is owned by c4core-devel
%{_includedir}/c4/fs
%{_libdir}/libc4fs.so
%{_libdir}/cmake/c4fs


%changelog
%autochangelog
