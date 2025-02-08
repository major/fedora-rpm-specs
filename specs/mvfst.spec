%bcond_without check
# compile --with all_tests to reenable disabled tests
%bcond_with all_tests

Name:           mvfst
Version:        2025.02.03.00
Release:        %autorelease
Summary:        An implementation of the QUIC transport protocol

License:        MIT
URL:            https://github.com/facebook/mvfst
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable building and installing tperf
# It gets enabled when building tests but gets installed with a
# missing shared library dependency
Patch:          %{name}-disable-tperf.diff

# same as the rest of the Folly stack
ExclusiveArch:  x86_64 aarch64 ppc64le riscv64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  folly-devel = %{version}
BuildRequires:  fizz-devel = %{version}
%if %{with check}
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
%endif

%global _description %{expand:
mvfst (Pronounced move fast) is a client and server implementation of IETF QUIC
protocol in C++ by Facebook. QUIC is a UDP based reliable, multiplexed transport
protocol that will become an internet standard. The goal of mvfst is to build a
performant implementation of the QUIC transport protocol that applications could
adapt for use cases on both the internet and the data-center. mvfst has been
tested at scale on android, iOS apps, as well as servers and has several
features to support large scale deployments.}

%description %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
Requires:       folly-devel = %{version}
Requires:       fizz-devel = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%cmake \
%if %{with check}
  -DBUILD_TESTS=ON \
%endif
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DCMAKE_INSTALL_MODDIR=%{_libdir}/%{name} \
  -DPACKAGE_VERSION=%{version}
%cmake_build


%install
%cmake_install


%if %{with check}
%check
%if %{with all_tests}
%ctest
%else
EXCLUDE_TESTS='--exclude-regex '
%ifarch x86_64 aarch64
# flaky; passed in mock locally but failed on Koji
EXCLUDE_TESTS+='QuicClientTransportAfterStartTest\.BadStatelessResetWontCloseTransport'
EXCLUDE_TESTS+='|\*\/QuicClientTransportIntegrationTest\.TestZeroRttSuccess\/'
EXCLUDE_TESTS+='|\*\/QuicClientTransportIntegrationTest\.TestZeroRttRejection\/\*'
# end x86_64 aarch64
%endif
%ifarch ppc64le
# these two failed on Koji
EXCLUDE_TESTS+='|\*\/QuicClientTransportIntegrationTest\.TestZeroRttRejection\/\*'
EXCLUDE_TESTS+='|ServerTransportParameters\.DatagramTestDisabled'
# end ppc64le
%endif
%ctest ${EXCLUDE_TESTS}
# end all_tests
%endif
# end check
%endif


%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.%{version}
%{_libdir}/cmake/%{name}

%files devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_includedir}/*
%{_libdir}/*.so


%changelog
%autochangelog
