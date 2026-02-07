# EPEL10 build of python3-pcapy is not yet available
%if 0%{?fedora} >= 29 || (0%{?rhel} > 7 && 0%{?rhel} < 10)
%bcond_without python3
%else
%bcond_with    python3
%endif

%global forgeurl0 https://codeberg.org/DNS-OARC/dnsperf

Summary: Benchmarking authorative and recursing DNS servers
Name: dnsperf
Version: 2.15.0
Release: %autorelease
# New page was found, but on github is also project, that seems to be official.
#
# Github project has different license and so far is the only one with any
# license mentioned. Unfortunately, project seems to be dead.
# It changed license text to Apache License 2.0
# Url: https://github.com/akamai/dnsperf
# License: ASL 2.0
#
# Another fork was maintained by ISC in contrib,
# now split into separate repository. This repository comes exactly from
# original nominum tarball, great source of patches.
# Url: https://gitlab.isc.org/isc-projects/dnsperf
#
# It seems DNS-OARC taken over the project, it has github page
# https://github.com/DNS-OARC/dnsperf

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
Url: https://www.dns-oarc.net/tools/dnsperf
Vcs: git:%{forgeurl0}

Source0: https://www.dns-oarc.net/files/dnsperf/%{name}-%{version}.tar.gz
Source2: dnsperf-data

BuildRequires: gcc, make
BuildRequires: autoconf automake libtool
BuildRequires: ldns-devel
BuildRequires: openssl-devel
BuildRequires: ck-devel
BuildRequires: libnghttp2-devel

%if %{with python3}
BuildRequires: python3-devel
BuildRequires: python3-dns
BuildRequires: python3-pcapy
%endif

%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
# resperf-report requires it, but not dnsperf itself
# do not force it always
Recommends: gnuplot
%else
Requires:   gnuplot
%endif
%if %{with python3}
BuildRequires: python3-devel
%endif

Provides: %{name}-data = %{version}-%{release}
Obsoletes: %{name}-data < 2.5.1-2

%description
This is dnsperf, a collection of DNS server performance testing tools.
For more information, see the dnsperf(1) and resperf(1) man pages.

%if %{with python3}
%package queryparse
Summary: Pcap dns query extraction utility
BuildArch: noarch
# Required for license file
Requires: %{name} = %{version}-%{release}
%if %{with python3}
Requires: python3-pcapy python3-dns
%endif

%description queryparse
This is dnsperf, a collection of DNS server performance testing tools.

Provides queryparse, python utility extracting queries from pcap files,
such as recorded by tcpdump or wireshark. Prints output in format
useable by dnsperf and resperf.

%endif

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%if %{with python3}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -p -n contrib/queryparse/queryparse
%endif

%install
%make_install dist_doc_DATA=''
%if %{with python3}
install -p contrib/queryparse/queryparse %{buildroot}/%{_bindir}
install -D -m 644 -p contrib/queryparse/queryparse.1 %{buildroot}/%{_mandir}/man1/queryparse.1
gzip %{buildroot}/%{_mandir}/man1/queryparse.1
%endif

mkdir -p %{buildroot}%{_datadir}/%{name}
touch %{buildroot}%{_datadir}/%{name}/queryfile-example-current
install -m 755 -p %{SOURCE2} %{buildroot}%{_bindir}/dnsperf-data

%check
%make_build check
%if %{with python3}
%{buildroot}/%{_bindir}/queryparse --version
%endif

%files 
%doc README.md CHANGES
%license LICENSE
%{_bindir}/*perf*
%{_mandir}/man*/*perf*
%dir %{_datadir}/dnsperf
%ghost %{_datadir}/dnsperf/queryfile-example-current

%if %{with python3}
%files queryparse
%{_bindir}/queryparse
%{_mandir}/man1/queryparse.1*
%endif

%changelog
%autochangelog
