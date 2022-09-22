%bcond_with toolchain_clang

# use this to re-test running all tests
%bcond_with all_tests

%if %{with toolchain_clang}
%global toolchain clang
%endif

%if 0%{?el8}
%ifarch ppc64le
# tests often stall after this
# 64/66 Test #60: SlidingBloomReplayCacheTest 
%bcond_with check
%else
# tests don't currently compile with el8's gmock
# error: use of deleted function
%bcond_with check
%endif
%else
%bcond_without check
%endif

Name:           fizz
Version:        2022.07.11.00
Release:        %autorelease
Summary:        A C++14 implementation of the TLS-1.3 standard

License:        BSD
URL:            https://github.com/facebookincubator/fizz
Source0:        %{url}/archive/v%{version}/fizz-%{version}.tar.gz
# Disable failing tests
Patch0:         %{name}-no_failed_tests.patch

ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  cmake
%if %{with toolchain_clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  folly-devel = %{version}
%if %{with check}
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
%endif

%global _description %{expand:
Fizz is a TLS 1.3 implementation.

Fizz currently supports TLS 1.3 drafts 28, 26 (both wire-compatible with the
final specification), and 23. All major handshake modes are supported, including
PSK resumption, early data, client authentication, and HelloRetryRequest.}

%description %{_description}
Fizz is a TLS 1.3 implementation.

Fizz currently supports TLS 1.3 drafts 28, 26 (both wire-compatible with the
final specification), and 23. All major handshake modes are supported, including
PSK resumption, early data, client authentication, and HelloRetryRequest.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-static < 2022.02.28.00-1

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%if %{without all_tests}
%patch0 -p1 -b .no_failed_tests
%endif


%build
cd fizz
%cmake \
%if %{without tests}
  -DBUILD_TESTS=OFF \
%endif
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name} \
  -DFOLLY_ROOT=%{_libdir}/cmake/folly \
  -DPACKAGE_VERSION=%{version} \
  -DSO_VERSION=%{version}
%cmake_build
cd -


%install
cd fizz
%cmake_install
cd -


%if %{with check}
%check
cd fizz
%ctest
cd -
%endif


%files
%license LICENSE
%{_bindir}/fizz
%{_bindir}/fizz-bogoshim
%{_libdir}/*.so.%{version}

%files devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}


%changelog
%autochangelog
