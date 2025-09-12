# Header-only library
%global debug_package %{nil}

%global commit 36459f42a84207330eae706c47e6fab712e6a149
%global shortcommit %%(c=%{commit}; echo ${c:0:7})

Summary:  A toolkit for programming parallel shared memory algorithms 
Name:     parlaylib
License:  MIT
#Version obtained from cmake config, but no tags upstream
Version:  2.3.1^20230215git%{shortcommit}
Release:  %autorelease

URL:      https://github.com/cmuparlay/parlaylib
Source0:  %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Do not download gtest, put cmake files in lib directory
Patch0:   nodownload.patch
# Tests fail on architectures other than x86_64
# https://github.com/cmuparlay/parlaylib/issues/46
ExcludeArch:  aarch64 s390x arm-hfp ppc64le i686

BuildRequires:  cmake
BuildRequires:  clang-tools-extra-devel
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  llvm
BuildRequires:  libstdc++-devel
BuildRequires:  re2-devel

%global _description %{expand:
ParlayLib is a header only C++ library for developing efficient parallel
algorithms and software on shared-memory multicore machines. It provides
additional tools and primitives that go beyond what is available in the
C++ standard library, and simplifies the task of programming provably
efficient and scalable parallel algorithms. It consists of a sequence
data type (analogous to std::vector), many parallel routines and
algorithms, a work-stealing scheduler to support nested parallelism,
and a scalable memory allocator.}

%description
%_description

%package devel
Summary:        A toolkit for programming parallel shared memory algorithms
Provides:       %{name}-static = %{version}-%{release}
%description devel
%_description

%package examples
Summary:    Examples for programming parallel shared memory algorithms
BuildArch:  noarch

%description examples
%_description

%prep
%autosetup -n %{name}-%{commit}

%build

%cmake -DBUILD_TESTING=ON \
       -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
       -DFETCH_CONTENT_FULLY_DISCONNECTED=ON \
       -DENABLE_CLANG_TIDY=ON \
       -DENABLE_CPP_CHECK=ON \
       -DPARLAY_TEST=ON \
       -DPARLAY_OPENMP=ON \
       -DPARLAY_EXAMPLES=ON \
       -DCMAKE_INSTALL_DATAROOTDIR=%{_libdir}/cmake
%cmake_build

%install
%cmake_install
%check

%ctest --timeout 7200


%files devel
%doc README.md
%license LICENSE
%dir %{_libdir}/cmake/parlay
%{_libdir}/cmake/parlay/*.cmake
%dir %{_includedir}/parlay
%{_includedir}/parlay/*.h
%dir %{_includedir}/parlay/internal
%{_includedir}/parlay/internal/*.h
%dir %{_includedir}/parlay/internal/concurrency
%{_includedir}/parlay/internal/concurrency/*.h
%dir %{_includedir}/parlay/internal/delayed
%{_includedir}/parlay/internal/delayed/*.h
%dir %{_includedir}/parlay/internal/posix
%{_includedir}/parlay/internal/posix/*.h
%dir %{_includedir}/parlay/internal/scheduler_plugins
%{_includedir}/parlay/internal/scheduler_plugins/*.h
%dir %{_includedir}/parlay/internal/windows
%{_includedir}/parlay/internal/windows/*.h

%files examples
%license LICENSE
%doc examples/


%changelog
%autochangelog

