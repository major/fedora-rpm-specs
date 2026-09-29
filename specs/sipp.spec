Summary:	SIP test tool / traffic generator
Name:		sipp
Version:	3.7.8
Release:	%autorelease
License:	GPL-2.0-or-later
URL:		https://github.com/SIPp/sipp
VCS:		git:%{url}.git
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(gtest)
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	pkgconfig(libsctp)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(pugixml)
BuildSystem:	cmake
BuildOption(conf): -DUSE_PCAP=1 -DUSE_GSL=1 -DUSE_SCTP=1 -DUSE_SYSTEM_PUGIXML=ON -DUSE_SYSTEM_GTEST=ON -DUSE_OPENSSL_KL=ON

%description
SIPp is a free Open Source test tool / traffic generator for the SIP protocol.
It includes a few basic SipStone user agent scenarios (UAC and UAS) and
establishes and releases multiple calls with the INVITE and BYE methods. It
can also reads custom XML scenario files describing from very simple to
complex call flows. It features the dynamic display of statistics about
running tests (call rate, round trip delay, and message statistics), periodic
CSV statistics dumps, TCP and UDP over multiple sockets or multiplexed with
retransmission management and dynamically adjustable call rates.

%prep -a
echo "#define SIPP_VERSION VERSION
#define VERSION \"v%{version}\"" > include/version.h

%install -a
mkdir -p %{buildroot}%{_datadir}/%{name}/pcap
install -p -m 644 pcap/*.pcap %{buildroot}%{_datadir}/%{name}/pcap

%files
%license LICENSE.txt
%doc CHANGES.md README.md THANKS
%caps(cap_net_raw=ep) %{_bindir}/%{name}
%{_bindir}/%{name}-multi.py
%{_datadir}/%{name}

%changelog
%autochangelog
