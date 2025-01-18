Summary: Client for signing certificates with an ACME server
Name: dehydrated
Version: 0.7.1
Release: 7%{?dist}
License: MIT
URL: https://github.com/dehydrated-io/dehydrated
Source0: https://github.com/dehydrated-io/dehydrated/releases/download/v%{version}/dehydrated-%{version}.tar.gz
Source1: https://github.com/dehydrated-io/dehydrated/releases/download/v%{version}/dehydrated-%{version}.tar.gz.asc
Source2: https://keys.openpgp.org/vks/v1/by-fingerprint/3C2F2605E078A1E18F4793909C4DBE6CF438F333
Source3: dehydrated.tmpfiles
Source4: dehydrated.timer
Source5: dehydrated.service
Source6: 50-dehydrated.preset
Source7: dehydrated-cron

Patch0: dehydrated-autowash.patch
Patch1: dehydrated-improve-trap-handling.patch
Patch2: dehydrated-hook.sh-defaults.patch

BuildArch: noarch
BuildRequires: gnupg2
BuildRequires: systemd-rpm-macros
%{?systemd_requires}
Requires: coreutils
Requires: curl
Requires: diffutils
Requires: gawk
Requires: grep
%if 0%{?fedora} || 0%{?rhel} >= 9
# Usually provided by s-nail, historically by mailx
Requires: /usr/bin/mailx
%else
# s-nail (EPEL 8) provides /usr/bin/mailx, mailx (RHEL 8) provides /bin/mailx
Requires: (/usr/bin/mailx or /bin/mailx)
%endif
Requires: openssl
Requires: sed
Requires: util-linux

%description
This is a client for signing certificates with an ACME-server (currently
only provided by Let's Encrypt) implemented as a relatively simple bash-
script. Dehydrated supports both ACME v1 and the new ACME v2 including
support for wildcard certificates!

Current features:
- Signing of a list of domains (including wildcard domains!)
- Signing of a custom CSR (either standalone or completely automated using
  hooks!)
- Renewal if a certificate is about to expire or defined set of domains changed
- Certificate revocation

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1 -b .autowash
%patch -P1 -p1 -b .improve-trap-handling
%patch -P2 -p1

%build
: nothing to do

%install
mkdir -p %{buildroot}%{_rundir}/dehydrated
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/accounts
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/archive
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/certs
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/domains.txt.d
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/hook.d
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/dehydrated.conf
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/dehydrated.timer
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/dehydrated.service
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_presetdir}/50-dehydrated.preset
install -D -p -m 0755 %{SOURCE7} %{buildroot}%{_libexecdir}/dehydrated-cron
sed \
    -e 's|^#LOCKFILE="\${BASEDIR}/lock"|LOCKFILE="%{_rundir}/dehydrated/lock"|' \
    -e 's|^#CONFIG_D=|CONFIG_D="\${BASEDIR}/conf.d"|' \
    -e 's|^#HOOK=|HOOK="\${BASEDIR}/hook.sh"|' \
    -e 's|^#PRIVATE_KEY_RENEW="yes"|PRIVATE_KEY_RENEW="no"|' \
    -e 's|^#AUTO_CLEANUP="no"|AUTO_CLEANUP="yes"|' \
    -e 's|^#KEY_ALGO=secp384r1|KEY_ALGO=rsa|' \
    docs/examples/config >%{buildroot}%{_sysconfdir}/dehydrated/config
touch --reference=docs/examples/config \
    %{buildroot}%{_sysconfdir}/dehydrated/config
sed -i.orig -e 's|^\#!/usr/bin/env bash|#!/bin/bash|' \
    docs/examples/hook.sh
touch --reference=docs/examples/hook.sh.orig \
    docs/examples/hook.sh && rm docs/examples/hook.sh.orig
install -p docs/examples/hook.sh %{buildroot}%{_sysconfdir}/dehydrated/hook.sh
sed -i.orig -e 's|^\#!/usr/bin/env bash|#!/bin/bash|' \
    dehydrated
touch --reference=dehydrated.orig dehydrated && \
    rm dehydrated.orig

install -D -p -m 0755 dehydrated %{buildroot}%{_bindir}/dehydrated
install -D -p -m 0644 docs/man/dehydrated.1 \
    %{buildroot}%{_mandir}/man1/dehydrated.1
rm -rf docs/man/
# remove execute bits from documentation
chmod a-x docs/examples/hook.sh

%post
%systemd_post dehydrated.timer dehydrated.service
if [ $1 -eq 1 ]; then
    systemctl start dehydrated.timer >/dev/null 2>&1 || :
fi
umask=$(umask)
umask 027
if [ -z "$(ls -1 %{_sysconfdir}/dehydrated/conf.d/*.sh 2>/dev/null)" ]; then
    touch %{_sysconfdir}/dehydrated/conf.d/local.sh
fi
if [ ! -e %{_sysconfdir}/dehydrated/domains.txt ]; then
    touch %{_sysconfdir}/dehydrated/domains.txt
fi
umask ${umask} || :

%preun
%systemd_preun dehydrated.timer dehydrated.service

%postun
%systemd_postun_with_restart dehydrated.timer
%systemd_postun dehydrated.service

%triggerun -- dehydrated <= 0.7.0-2
systemctl preset dehydrated.timer dehydrated.service >/dev/null 2>&1 || :
systemctl start dehydrated.timer >/dev/null 2>&1 || :

%files
%doc README.md CHANGELOG docs/*
%license LICENSE
%{_presetdir}/50-dehydrated.preset
%{_unitdir}/dehydrated.service
%{_unitdir}/dehydrated.timer
%{_tmpfilesdir}/dehydrated.conf
%{_libexecdir}/dehydrated-cron
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/dehydrated/config
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/dehydrated/hook.sh
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated/accounts
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated/archive
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated/certs
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated/conf.d
%attr(0640,root,root) %ghost %{_sysconfdir}/dehydrated/conf.d/local.sh
%attr(0640,root,root) %ghost %{_sysconfdir}/dehydrated/domains.txt
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated/domains.txt.d
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated/hook.d
%attr(0750,root,root) %dir %{_rundir}/dehydrated
%{_bindir}/dehydrated
%{_mandir}/man1/dehydrated.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 26 2024 Robert Scheck <robert@fedoraproject.org> - 0.7.1-6
- Added missing dehydrated run-time requirements
- Resolved: rhbz#2279854 dehydrated dependency issue on EL8

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 31 2023 Robert Scheck <robert@fedoraproject.org> - 0.7.1-1
- Resolved: rhbz#2139056 dehydrated-0.7.1 is available
- Resolved: rhbz#2035549 genkey ecparam - ECDSA key, P-384 (secp384r1)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 Carl George <carl@george.computer> - 0.7.0-5
- Require path instead of package name for mailx rhbz#2050852

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 01 2021 Paul Wouters <paul.wouters@aiven.io> - 0.7.0-2
- Update trigger to proper version

* Tue Jun 01 2021 Paul Wouters <paul.wouters@aiven.io> - 0.7.0-1
- Resolved: rhbz#1872621 [RFE] Ship systemd units for auto-renewal
- Resolved: rhbz#1906674 dehydrated-0.7.0 is available

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Paul Wouters <pwouters@redhat.com> - 0.6.5-1
- Resolves: rhbz#1723766 Updated to 0.6.5

* Tue Jun 25 2019 Robert Scheck <robert@fedoraproject.org> - 0.6.4-1
- Upgrade to 0.6.4 (#1723766)
- Update source link

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Robert Scheck <robert@fedoraproject.org> - 0.6.2-1
- Resolves: rhbz#1572609 Updated to 0.6.2

* Sat Mar 31 2018 Robert Scheck <robert@fedoraproject.org> - 0.6.1-1
- Resolves: rhbz#1554153 Updated to 0.6.1 with ACME v2 support

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Paul Wouters <pwouters@redhat.com> - 0.5.0-1
- Resolves: rhbz#1534189 dehydrated-0.5.0 is available

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Paul Wouters <pwouters@redhat.com> - 0.4.0-5
- Include license with proper macros

* Mon Mar 20 2017 Paul Wouters <pwouters@redhat.com> - 0.4.0-4
- Set PRIVATE_KEY_RENEW=no so pubkeys are re-used, allowing TLSA DNS records

* Sat Mar 18 2017 Tuomo Soini <tis@foobar.fi> - 0.4.0-3
- Fix file mode of crontab entry

* Sat Mar 18 2017 Kim B. Heino <b@bbbs.net> - 0.4.0-2
- Add archive directory, cleanup

* Sat Mar 18 2017 Tuomo Soini <tis@foobar.fi> - 0.4.0-1
- Initial build
