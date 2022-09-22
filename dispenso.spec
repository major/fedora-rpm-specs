%ifarch %{arm} %{ix86}
# need to sort out tests, only 90% pass
%bcond_with check
%else
# 64-bit architectures
%if 0%{?fedora} && 0%{?fedora} < 36
%bcond_without check
%else
# EPEL 8 has gtest 1.8.0, too old
# EPEL 9 and Fedora 36 has gtest 1.11.0, API is different
%bcond_with check
%endif
%endif

%if 0%{?el8}
%undefine __cmake_in_source_build
%endif

Name:           dispenso
Version:        1.0.0
Release:        %{autorelease}
Summary:        A library for working with sets of tasks in parallel

License:        MIT
URL:            https://github.com/facebookincubator/dispenso
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# allow Dispenso to be installed and fix its version
Patch0:         %{url}/commit/d00e7402ffcc780df11024f8d2285c153b7635b1.patch#/%{name}-1.0.0-add-install.patch
# TODO: make toggleable and upstream
Patch1:         %{name}-1.0.0-use-system-gtest.patch
# being reviewed upstream
Patch2:         %{name}-1.0.0-fix-32bit-build.patch
# TODO: make toggleable and upstream
Patch3:         %{name}-1.0.0-use-system-moodycamel.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  moodycamel-concurrentqueue-devel
%if %{with check}
BuildRequires:  gmock-devel
BuildRequires:  (gtest-devel >= 1.10.0 with gtest-devel < 1.11.0)
%endif

%global _description %{expand:
Dispenso is a library for working with sets of tasks in parallel. It provides
mechanisms for thread pools, task sets, parallel for loops, futures, pipelines,
and more. Dispenso is a well-tested C++14 library designed to have minimal
dependencies (some dependencies are required for the tests and benchmarks), and
designed to be clean with compiler sanitizers (ASAN, TSAN). Dispenso is
currently being used in dozens of projects and hundreds of C++ files at Meta
(formerly Facebook). Dispenso also aims to avoid major disruption at every
release. Releases will be made such that major versions are created when a
backward incompatibility is introduced, and minor versions are created when
substantial features have been added or bugs have been fixed, and the aim would
be to only very rarely bump major versions. That should make the project
suitable for use from main branch, or if you need a harder requirement, you can
base code on a specific version.}

%description %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       moodycamel-concurrentqueue-devel

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1
# make sure we use the system library
rm -rf dispenso/third-party


%build
%cmake \
%if %{with check}
  -DDISPENSO_BUILD_TESTS=ON \
%else
  %{nil}
%endif

%cmake_build


%install
%cmake_install


%if %{with check}
%check
%ctest
%endif


%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/Dispenso-%{version}


%changelog
%autochangelog
