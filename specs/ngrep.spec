%global date 20241209
%global commit b2e3ba3c5a593abf203e65a407c3a9de0f998d4a
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

Name:           ngrep
Version:        1.47^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Network layer grep tool
# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-BSD-with-advertising
URL:            https://github.com/jpr5/ngrep
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
# PR#27: Port to PCRE2 API and enable JIT compilation
Patch:          %{url}/pull/27.patch
# PR#28: Include <err.h> and "tcpkill.h" to avoid implicit function declarations
Patch:          %{url}/pull/28.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel
BuildRequires:  pcre2-devel

%description
ngrep strives to provide most of GNU grep's common features, applying them
to the network layer. ngrep is a pcap-aware tool that will allow you to
specify extended regular or hexadecimal expressions to match against data
payloads of packets. It currently recognizes TCP, UDP, ICMP, IGMP and Raw
protocols across Ethernet, PPP, SLIP, FDDI, Token Ring, 802.11 and null
interfaces, and understands bpf filter logic in the same fashion as more
common packet sniffing tools, such as tcpdump and snoop.

%prep
%autosetup -p1 -n %{name}-%{commit}
# Make sure not to be using bundled libs
rm -r regex-0.12

%build
autoreconf -fiv
# Note: building with PCRE instead of GNU regex because of license
# incompatibilities (this one's basically a BSD with advertising clause).
%configure \
  --enable-pcre2 \
  --enable-ipv6 \
  --with-pcap-includes=%{_includedir}/pcap \
  --enable-tcpkill
%make_build STRIPFLAG=

%install
install -Ddpm0755 %{buildroot}%{_sbindir} %{buildroot}%{_mandir}/man8
%make_install BINDIR_INSTALL="%{_sbindir}"

%files
%license LICENSE
%doc CHANGES CREDITS EXAMPLES.md README.md
%{_sbindir}/ngrep
%{_mandir}/man8/ngrep.8*

%changelog
%autochangelog
