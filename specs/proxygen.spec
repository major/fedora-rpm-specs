%bcond_with toolchain_clang

%if %{with toolchain_clang}
%global toolchain clang
%endif

%bcond_without check

# use this to re-test running all tests
%bcond_with all_tests

# https://bugzilla.redhat.com/show_bug.cgi?id=1927961
%bcond_with docs

%global _static_builddir static_build

Name:           proxygen
Version:        2025.02.03.00
Release:        %autorelease
Summary:        A collection of C++ HTTP libraries including an easy to use HTTP server.

License:        BSD-3-Clause
URL:            https://github.com/facebook/proxygen
Source:         %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# include <cstdint> for GCC 15 header changes. Will be in next release
Patch:          %{name}-fix-headers-for-gcc15.diff

ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  cmake
%if %{with toolchain_clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  folly-devel = %{version}
BuildRequires:  fizz-devel = %{version}
BuildRequires:  mvfst-devel = %{version}
BuildRequires:  wangle-devel = %{version}
BuildRequires:  gperf
%if 0%{?fedora} >= 41
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  perl
BuildRequires:  libzstd-devel
%if %{with docs}
BuildRequires:  doxygen
%endif
%if %{with check}
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
%endif

%global _description %{expand:
Proxygen comprises the core C++ HTTP abstractions used at Facebook.
Internally, it is used as the basis for building many HTTP servers, proxies,
and clients. This release focuses on the common HTTP abstractions and our
simple HTTPServer framework. Future releases will provide simple client APIs
as well. The framework supports HTTP/1.1, SPDY/3, SPDY/3.1, HTTP/2, and
HTTP/3. The goal is to provide a simple, performant, and modern C++ HTTP
library.}

%description %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-static < 2022.02.21.00-1

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%if %{with docs}
%package        docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    docs %{_description}

The %{name}-docs package contains additional documentation for proxygen.
%endif


%package        libs
Summary:        Shared libraries for %{name}

%description    libs %{_description}
The %{name}-libs package contains shared libraries provided by proxygen.


%prep
%autosetup -c -p1


%build
%cmake \
%if %{with check}
  -DBUILD_TESTS=ON \
%else
  -DBUILD_TESTS=OFF \
%endif
  -DBUILD_SHARED_LIBS=ON \
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name} \
  -DPACKAGE_VERSION=%{version}
%cmake_build

%if %{with docs}
doxygen
%endif


%install
%cmake_install


%if %{with check}
%check
%if %{with all_tests}
%ctest
%else
cd "%{__cmake_builddir}"

# these on all architectures
EXCLUDED_TESTS='HTTPMessage\.TestParseQueryParamsSimple'
EXCLUDED_TESTS+='|SSL\.SSLTest'
EXCLUDED_TESTS+='|SSL\.SSLTestWithMultiCA'
EXCLUDED_TESTS+='|SSL\.TestAllowInsecureOnSecureServer'
EXCLUDED_TESTS+='|SSL\.DisallowInsecureOnSecureServer'
EXCLUDED_TESTS+='|SSL\.TestResumptionWithTickets'
EXCLUDED_TESTS+='|SSL\.TestResumptionAfterUpdateFails'
EXCLUDED_TESTS+='|SSL\.TestUpdateTLSCredentials'
EXCLUDED_TESTS+='|GetListenSocket\.TestBootstrapWithNoBinding'
EXCLUDED_TESTS+='|GetListenSocket\.TestBootstrapWithBinding'
EXCLUDED_TESTS+='|ScopedServerTest\.StartSSLWithInsecure'
EXCLUDED_TESTS+='|ConnectionFilterTest\.Test'

%ifarch %{ix86} armv7hl
EXCLUDED_TESTS+='|DownstreamTransactionTest\.DeferredEgress'
EXCLUDED_TESTS+='|HTTP2DownstreamSessionTest\.H2TimeoutWin'
EXCLUDED_TESTS+='|HTTP2DownstreamSessionTest\.TestTransactionStallByFlowControl'
EXCLUDED_TESTS+='|HTTP2UpstreamSessionTest\.TestUnderLimitOnWriteError'
EXCLUDED_TESTS+='|HTTP2UpstreamSessionTest\.DetachFlowControlTimeout'
EXCLUDED_TESTS+='|MockCodecDownstreamTest.FlowControlWindow'
%endif

%ifarch ppc64le
EXCLUDED_TESTS+='|SessionPoolFixture\.MoveIdleSessionBetweenThreadsTest'
%endif

%{__ctest} --output-on-failure --force-new-ctest-process %{?_smp_mflags} \
  -E ${EXCLUDED_TESTS}

cd -
%endif
%endif


%files
%license LICENSE
%{_bindir}/*

%files libs
%{_libdir}/*.so.*

%files devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md CoreProxygenArchitecture.png
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}

%if %{with docs}
%files docs
%doc html
%endif


%changelog
%autochangelog
