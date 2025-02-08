%bcond_with toolchain_clang

# use this to re-test running all tests
%bcond_with all_tests

%if %{with toolchain_clang}
%global toolchain clang
%endif

%bcond_without check

Name:           wangle
Version:        2025.02.03.00
Release:        %autorelease
Summary:        Framework for building services in a consistent/modular/composable way

License:        Apache-2.0
URL:            https://github.com/facebook/wangle
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:   x86_64 aarch64 ppc64le riscv64

BuildRequires:  cmake
%if %{with toolchain_clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif
# Library dependencies
BuildRequires:  fizz-devel = %{version}
BuildRequires:  folly-devel = %{version}
%if %{with check}
BuildRequires:  boost-devel
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
%endif


%global _description %{expand:
Wangle is a library that makes it easy to build protocols, application clients,
and application servers.

It's like Netty + Finagle smooshed together, but in C++.}

%description %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-static < 2022.02.28.00-1

%description    devel %{_description}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
cd wangle
%cmake \
%if %{with check}
  -DBUILD_TESTS=ON \
%else
  -DBUILD_TESTS=OFF \
%endif
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name} \
  -DPACKAGE_VERSION=%{version}
%cmake_build
cd -


%install
cd wangle
%cmake_install
cd -


%if %{with check}
%check
cd wangle
%if %{with all_tests}
%ctest
%else
EXCLUDED_TESTS='--exclude-regex '
# somehow we can't just disable these two
# [  FAILED  ] SSLContextManagerTest.TestSingleClientCAFileSet
# [  FAILED  ] SSLContextManagerTest.TestMultipleClientCAsSet
EXCLUDED_TESTS+='SSLContextManagerTest'

%ifarch ppc64le
# The following tests FAILED:
# 	    6 - BroadcastPoolTest (SEGFAULT)
EXCLUDED_TESTS+='|BroadcastPoolTest'
%endif

%ctest ${EXCLUDED_TESTS}
%endif
cd -
%endif


%files
%license LICENSE
%{_libdir}/*.so.%{version}

%files devel
%doc CONTRIBUTING.md README.md tutorial.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}


%changelog
%autochangelog
