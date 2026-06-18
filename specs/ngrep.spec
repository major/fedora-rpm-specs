%global debug_package %{nil}

Name:           ngrep
Version:        1.49.0
Release:        %autorelease
Summary:        Network layer grep tool
License:        ngrep
URL:            https://github.com/jpr5/ngrep
Source:         %{url}/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel
BuildRequires:  make
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
%autosetup -p1 -n %{name}-%{version}
# Make sure not to be using bundled libs
rm -r regex-0.12

%build
autoreconf -fiv
# Note: building with PCRE instead of GNU regex because of license
# incompatibilities (this one's basically a BSD with advertising clause).
%configure \
  --enable-pcre2 \
  --enable-ipv6 \
  --with-pcap-includes=%{_includedir} \
  --enable-tcpkill
%make_build STRIPFLAG=

%install
install -Ddpm0755 %{buildroot}%{_sbindir} %{buildroot}%{_mandir}/man8
%make_install BINDIR_INSTALL="%{_sbindir}"

%check
./ngrep -V

%files
%license LICENSE
%doc CREDITS EXAMPLES.md README.md
%{_sbindir}/ngrep
%{_mandir}/man8/ngrep.8*

%changelog
%autochangelog
