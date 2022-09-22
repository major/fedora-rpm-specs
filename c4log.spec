# The project contains a version number, but a release has never been tagged.
# The project is normally used as a git submodule and referred to by commit
# hash.
%global commit c9477dc2576031357d61c8ed0a77e43928cbfe99
%global snapdate 20220818

Name:           c4log
Summary:        C++ type-safe logging, mean and lean
Version:        0.0.1^%{snapdate}git%(echo '%{commit}' | cut -b -7)
# This is the same as the version number. To prevent undetected soversion
# bumps, we nevertheless express it separately.
%global so_version 0.0.1
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/biojppm/c4log
Source0:        %{url}/archive/%{commit}/c4log-%{commit}.tar.gz

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
Requires:       cmake-filesystem

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


%build
# We can stop the CMake scripts from downloading doctest by setting
# C4LOG_CACHE_DOWNLOAD_DOCTEST to any directory that exists.
%cmake -GNinja \
  -DC4LOG_CACHE_DOWNLOAD_DOCTEST:PATH=/ \
  -DC4LOG_BUILD_TESTS=ON
%cmake_build


%install
%cmake_install
# Fix wrong installation paths for multilib; it would be nontrivial to patch
# the source to get this right in the first place.
if [ '%{_libdir}' != '%{_prefix}/lib' ]
then
  mkdir -p '%{buildroot}%{_libdir}'
  mv -v %{buildroot}%{_prefix}/lib/libc4log.so* '%{buildroot}%{_libdir}/'
  mkdir -p '%{buildroot}%{_libdir}/cmake'
  mv -v %{buildroot}%{_prefix}/lib/cmake/c4log '%{buildroot}%{_libdir}/cmake/'
fi


%check
%cmake_build --target c4log-test-run-verbose


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libc4log.so.%{so_version}


%files devel
# %%{_includedir}/c4 is owned by c4core-devel
%{_includedir}/c4/log
%{_libdir}/libc4log.so
%{_libdir}/cmake/c4log


%changelog
%autochangelog
