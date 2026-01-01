Summary:	SIP test tool / traffic generator
Name:		sipp
Version:	3.7.6
Release:	%autorelease
License:	GPL-2.0-or-later
URL:		https://github.com/SIPp/sipp
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:		sipp-0001-Removal-of-bundled-gmock-gtest.patch
Patch:		sipp-0002-Temporary-disable-this-gmock-flag.patch
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
BuildRequires:	libpcap-devel
BuildRequires:	lksctp-tools-devel
BuildRequires:	make
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig(openssl)

%description
SIPp is a free Open Source test tool / traffic generator for the SIP protocol.
It includes a few basic SipStone user agent scenarios (UAC and UAS) and
establishes and releases multiple calls with the INVITE and BYE methods. It
can also reads custom XML scenario files describing from very simple to
complex call flows. It features the dynamic display of statistics about
running tests (call rate, round trip delay, and message statistics), periodic
CSV statistics dumps, TCP and UDP over multiple sockets or multiplexed with
retransmission management and dynamically adjustable call rates.

%prep
%autosetup -p1
echo "#define SIPP_VERSION VERSION
#define VERSION \"v%{version}\"" > include/version.h

%build
# FIXME consider adding -DUSE_GSL=1
%{cmake} -DUSE_PCAP=1 -DUSE_SSL=1 -DUSE_SCTP=1
%cmake_build

%install
%cmake_install
# Extra data setup
mkdir -p %{buildroot}%{_datadir}/%{name}/pcap
install -p -m 644 pcap/*.pcap %{buildroot}%{_datadir}/%{name}/pcap

%check
%cmake_build -- sipp_unittest
./redhat-linux-build/sipp_unittest

%files
%license LICENSE.txt
%doc CHANGES.md README.md THANKS
%caps(cap_net_raw=ep) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
%autochangelog
