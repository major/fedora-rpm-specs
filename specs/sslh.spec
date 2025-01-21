%global gh_commit    368f286ce53a13e887daa973fb87333af94dad93
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     yrutschle
%global gh_project   sslh
#%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
# disable tests until perl-conf-libconfig is in Fedora
%global with_tests   0
%define _default_patch_fuzz 3

Name:    sslh
Version: 1.21c
Release: 11%{?dist}
Summary: Applicative protocol(SSL/SSH) multiplexer
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://github.com/%{gh_owner}/%{gh_project}
Source0: https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

# Make the systemd unit a little nicer for Fedora
Patch0:  00-systemd-tuning.patch

# Don't do lcov coverage testing
Patch1:  01-remove-lcov-testing.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: pkgconfig(libconfig)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libpcre)
BuildRequires: systemd
BuildRequires: perl(Pod::Man)


%if %{with_tests}
# Required for %check
BuildRequires: perl(IO::Socket::INET6)
BuildRequires: perl(Test::More)
BuildRequires: perl(Conf::Libconfig)
BuildRequires: valgrind
BuildRequires: psmisc
%endif

%if 0%{?fedora} >= 28 || 0%{?rhel} > 7
%global use_libwrap 0
%else
%global use_libwrap 1
BuildRequires: tcp_wrappers-devel
%endif

Requires(pre):    shadow-utils
%{?systemd_requires}

%description
sslh accepts connections on specified ports, and forwards them further
based on tests performed on the first data packet sent by the remote
client.

Probes for HTTP, SSL, SSH, OpenVPN, tinc, XMPP are implemented, and
any other protocol that can be tested using a regular expression, can
be recognized. A typical use case is to allow serving several services
on port 443 (e.g. to connect to ssh from inside a corporate firewall,
which almost never block port 443) while still serving HTTPS on that port.

Hence sslh acts as a protocol multiplexer, or a switchboard. Its name
comes from its original function to serve SSH and HTTPS on the same port.


%prep
%autosetup -n %{name}-%{gh_commit} -p1

%build
./genver.sh >version.h
%if 0%{?rhel}
export CFLAGS="${CFLAGS} -std=gnu99"
%endif
%if %{use_libwrap}
  make %{?_smp_mflags} USELIBWRAP=1 USELIBCAP=1 USESYSTEMD=1 sslh echosrv
%else
  make %{?_smp_mflags} USELIBCAP=1 USESYSTEMD=1 sslh echosrv
%endif
pod2man --section=8 --release=%{version} --center=" " %{name}.pod > %{name}.8
iconv --from=ISO-8859-1 --to=UTF-8 ChangeLog > ChangeLog.conv && \
touch -r ChangeLog ChangeLog.conv && \
mv ChangeLog.conv ChangeLog

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_pkgdocdir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_unitdir}
cp -p %{name}-fork %{buildroot}%{_sbindir}/%{name}
cp -p %{name}-select %{buildroot}%{_sbindir}/%{name}-select
cp -p basic.cfg %{buildroot}/etc/%{name}.cfg
cp -p %{name}.8 %{buildroot}%{_mandir}/man8/
cp -p scripts/systemd.sslh.service %{buildroot}%{_unitdir}/%{name}.service
cat > %{buildroot}%{_sysconfdir}/sysconfig/%{name} << EOF
#
# The options passed to the sslh binary can be provided here
# Defaults to passing the configuration file to the daemon
#
DAEMON_OPTS="-F/etc/sslh.cfg"
EOF
cat > %{buildroot}%{_unitdir}/%{name}.socket << EOF
[Unit]
Description=Socket support for sslh
Before=sslh.service

[Socket]
FreeBind=true

[Install]
WantedBy=sockets.target
EOF

%check
%if %{with_tests}
# Use right ip6 localhost for Fedora
sed -i 's/ip6-localhost/localhost6/g' t
# Build the binaries with gcc coverage enabled
make test
%endif

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d /dev/null -s /sbin/nologin \
    -c "SSLH daemon" %{name}
exit 0

%post
%systemd_post sslh.service

%preun
%systemd_preun sslh.service

%postun
%systemd_postun_with_restart sslh.service

%files
%doc README.md ChangeLog example.cfg
%license COPYING
%doc %{_mandir}/man8/%{name}.8*
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0755,root,root) %{_sbindir}/%{name}-select
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/%{name}.cfg
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/sysconfig/%{name}




%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.21c-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.21c-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21c-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21c-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21c-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21c-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.21c-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 08 2021 Alex Perez <aperez@alexperez.com> - 1.21c-1
- Update to 1.21c

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 James Hogarth <james.hogarth@gmail.com> - 1.20-1
- Update to 1.20 upstream

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19c-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Petr Pisar <ppisar@redhat.com> - 1.19c-4
- Rebuild against patched libpcreposix library (bug #1667614)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 James Hogarth <james.hogarth@gmail.com> - 1.19c-2
- Fix wrong path bz#1574831

* Wed Apr 18 2018 James Hogarth <james.hogarth@gmail.com> - 1.19c-1
- Update to 1.19c upstream

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.18-6
- Escape macros in %%changelog

* Thu Nov 30 2017 James Hogarth <james.hogarth@gmail.com> - 1.18-5
- Remove dependency on libwrap for F28+ as per accepted change

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 30 2016 James Hogarth <james.hogarth@gmail.com> - 1.18-1
- Update to 1.18 upstream
- Add systemd socket template
- Add %%check to rpm spec
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Sep 17 2015 James Hogarth <james.hogarth@gmail.com> - 1.17-4
- Bug in systemd unit with incorrect variable usage BZ#1264140
* Mon Jul 20 2015 James Hogarth <james.hogarth@gmail.com> - 1.17-3
- Make sslh.cfg argument overrideable from sysconfig BZ#1221320
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Wed Mar 18 2015 James Hogarth <james.hogarth@gmail.com> - 1.17-1
- Initial packaging of sslh 1.17
