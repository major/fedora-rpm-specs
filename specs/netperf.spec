%global forgeurl https://github.com/HewlettPackard/netperf
%global commit 3bc455b23f901dae377ca0a558e1e32aa56b31c4
%forgemeta

Name:           netperf
Version:        2.7.0
Release:        %autorelease
Summary:        Benchmark to measure the performance of many different types of networking

# Most of the codebase is MIT, the stuff under src/missing/ is a mix of
# BSD-3-Clause and BSD-4-Clause
License:        MIT AND BSD-3-Clause AND BSD-4-Clause
URL:            https://hewlettpackard.github.io/netperf
Source0:        %{forgesource}
Source1:        netserver.service

# PR#63: netserver: do not chmod("/dev/null", 0644) when suppress_debug==1
Patch1:         %{forgeurl}/pull/63.patch

Patch2:         netperf-c99.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lksctp-tools-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  texinfo-tex

%description
Netperf is a benchmark that can be used to measure the performance of many
different types of networking. It provides tests for both unidirectional
throughput, and end-to-end latency.

%prep
%forgeautosetup -p1
# remove prebuilt documentation
rm doc/netperf.{html,pdf}

%build
./autogen.sh
# -fcommon is to workaround a build issue with GCC 10 and later
# -std=c99 is to workaround a build issue with GCC 15 and later
export CFLAGS="%{optflags} -fcommon -std=c99"
%configure \
  --enable-burst \
  --enable-dccp \
  --enable-demo \
  --enable-dirty \
  --enable-histogram \
  --enable-intervals \
  --enable-omni \
  --enable-sctp \
  --enable-unixdomain

%make_build
%make_build -C doc netperf.html netperf.pdf

%install
%make_install
install -Dpm0644 -t %{buildroot}%{_unitdir} %SOURCE1
rm %{buildroot}%{_infodir}/dir
rm doc/examples/Makefile*
chmod -x doc/examples/*

%post
%systemd_post netserver.service

%preun
%systemd_preun netserver.service

%postun
%systemd_postun_with_restart netserver.service

%files
%license COPYING
%doc AUTHORS README Release_Notes
%doc doc/netperf.pdf doc/netperf.html
%doc doc/examples
%{_bindir}/netperf
%{_bindir}/netserver
%{_unitdir}/netserver.service
%{_infodir}/netperf.*
%{_mandir}/man1/netperf.1*
%{_mandir}/man1/netserver.1*

%changelog
%autochangelog
