%bcond_with toolchain_clang

# use this to re-test running all tests
%bcond_with all_tests

%if %{with toolchain_clang}
%global toolchain clang
%endif

%bcond_without check

Name:           wangle
Version:        2023.07.03.00
Release:        %autorelease
Summary:        Framework for building services in a consistent/modular/composable way

License:        Apache-2.0
URL:            https://github.com/facebook/wangle
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# disable failing tests, see patch for context
%if %{without all_tests}
Patch0:         %{name}-disable_failed_tests.patch
%endif

ExclusiveArch:   x86_64 aarch64 ppc64le

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
%ctest
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
