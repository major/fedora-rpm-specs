%bcond_with toolchain_clang

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
Version:        2025.02.03.00
Release:        %autorelease
Summary:        A C++14 implementation of the TLS-1.3 standard

License:        BSD-3-Clause
URL:            https://github.com/facebookincubator/fizz
Source:         %{url}/archive/v%{version}/fizz-%{version}.tar.gz
# the fallback expansion of FOLLY_SDT seems to not work with GCC
# since folly commit b85c08e5e5f2729f2f50dc89b5d464b9f5e58c69 (20240521)
Patch:          fizz-gate-use-of-folly_sdt.diff

ExclusiveArch:  x86_64 aarch64 ppc64le riscv64

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
%{_libdir}/*.so.%{version}

%files devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/fizz-bogoshim
%{_bindir}/fizz-encryptedrecordbench
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}


%changelog
%autochangelog
