
%if 0%{?fedora} || 0%{?rhel} > 7
# Explicity require python3 on Fedora to help track which packages 
# no longer need python2.
%global use_python3 1
%else
%global use_python3 0
%endif

Name:		acme-tiny
Version:	5.0.1
Release:	11%{?dist}
Summary:	Tiny auditable script to issue, renew Let's Encrypt certificates

License:	MIT
URL:		https://github.com/diafygi/%{name}
Source0:	https://github.com/diafygi/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	acme-tiny-sign.sh
Source2:	cert-check.py
Source3:	acme.conf
Source6:	acme-tiny.timer
Source7:	acme-tiny.service
Source8:	README-fedora.md
# simple script hook to kick services when cert is updated
Source9:	notify.sh
Source10:	acme-tiny-notify.service
Source11:	acme-tiny.conf

Requires(pre): shadow-utils
BuildRequires: systemd-rpm-macros
%{?systemd_requires}
Requires: %{name}-core = %{version}-%{release}
BuildArch:	noarch
%if 0%{?fedora}
Suggests: httpd, mod_ssl, nginx
Enhances: httpd, mod_ssl, nginx
%endif

%description
This is a tiny, auditable script that you can throw on your server to issue and
renew Let's Encrypt certificates. Since it has to be run on your server and
have access to your private Let's Encrypt account key, I tried to make it as
tiny as possible (currently less than 200 lines). The only prerequisites are
python and openssl.  

Well, that and a web server - but then you only need this with a web server.
This package adds a simple directory layout and timer service that runs
acme_tiny on installed CSRs as the acme user for privilege separation.

%package core
Summary: Core python module of acme-tiny
Requires:	openssl
%if 0%{?rhel} >= 5 && 0%{?rhel} < 7
# EL6 uses python2.6, which does not include argparse
Requires:	python-argparse
%endif
BuildArch: noarch

%description core
Includes only the core acme_tiny.py script and its dependencies.
Alternate frameworks that use acme_tiny.py can install this to avoid pulling in
unneeded packages.

%prep
%setup -q -n %{name}-%{version}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE8} .
sed -i.orig -e '1,1 s,^.*python$,#!/usr/bin/python,' acme_tiny.py
%if %{use_python3}
sed -i.old -e '1,1 s/python$/python3/' *.py
%endif

echo 'u acme - "Tiny Auditable ACME Client" %{_sharedstatedir}/acme' >acme.sysusers.conf

%build

%install
mkdir -p %{buildroot}/var/www/challenges
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/acme/{private,csr,certs,.notify}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/notify.d
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
chmod 0700 %{buildroot}%{_sharedstatedir}/acme/private

install -m 0755 acme-tiny-sign.sh %{buildroot}%{_libexecdir}/%{name}/sign
install -m 0755 %{SOURCE9} %{buildroot}%{_libexecdir}/%{name}/notify
install -m 0755 acme_tiny.py %{buildroot}%{_sbindir}/acme_tiny
ln -sf acme_tiny %{buildroot}%{_sbindir}/%{name}
ln -sf %{_libexecdir}/%{name}/sign %{buildroot}%{_sbindir}/acme-tiny-sign
ln -sf %{_libexecdir}/%{name}/notify %{buildroot}%{_sysconfdir}/%{name}/notify.sh
install -m 0755 cert-check.py %{buildroot}%{_sbindir}/cert-check
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_unitdir}
install -pm 644	 %{SOURCE6} %{buildroot}%{_unitdir}
install -pm 644	 %{SOURCE7} %{buildroot}%{_unitdir}
install -pm 644	 %{SOURCE10} %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -m 0644 -D acme.sysusers.conf %{buildroot}%{_sysusersdir}/acme.conf

%pre
getent group acme > /dev/null || groupadd -r acme
getent passwd acme > /dev/null || /usr/sbin/useradd -g acme \
	-c "Tiny Auditable ACME Client" \
	-r -d %{_sharedstatedir}/acme -s /sbin/nologin acme
exit 0

%post
%systemd_post acme-tiny.service acme-tiny-notice.service acme-tiny.timer

%postun
%systemd_postun_with_restart acme-tiny.service acme-tiny-notice.service acme-tiny.timer

%preun
%systemd_preun acme-tiny.service acme-tiny-notice.service acme-tiny.timer

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README-fedora.md
%attr(0755,acme,acme) /var/www/challenges
%attr(-,acme,acme) %{_sharedstatedir}/acme
%{_libexecdir}/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/acme.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/*
%{_sbindir}/acme-tiny-sign
%{_sbindir}/cert-check
%{_sbindir}/%{name}
%{_sysconfdir}/%{name}
%{_sysusersdir}/acme.conf

%files core
%license LICENSE
%doc README.md
%{_sbindir}/acme_tiny

%changelog
* Thu Jan 16 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.0.1-11
- Add sysusers.d config file

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Stuart D. Gathman <stuart@gathman.org> - 5.0.1-5
- Verified SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Stuart D. Gathman <stuart@gathman.org> 5.0.1-1
- New upstream release

* Wed Sep  8 2021 Stuart D. Gathman <stuart@gathman.org> 4.1.1-2
- Remove CLI override in acme-tiny.service (uses /etc/sysconfig/acme-tiny now)

* Tue Sep  7 2021 Stuart D. Gathman <stuart@gathman.org> 4.1.1-1
- New upstream release
- Set days before expiration in /etc/sysconfig

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 27 2021 Stuart D. Gathman <stuart@gathman.org> 4.1.0-7
- Fix BZ#1839904
- enhance notify after cert update, incrond no longer needed

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.1.0-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr  9 2020 Stuart D. Gathman <stuart@gathman.org> 4.1.0-3
- Update README-fedora.md to describe notify.sh
- Apply selected changes from Marcel Metz <mmetz@adrian-broher.net>:
- Use openssl x509 -checkend parameter to determine certificate expiration
- Remove Let's Encrypt intermediate certificate
- Remove cron job used on non systemd systems

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Tim Jackson <rpm@timj.co.uk> - 4.1.0-1
- Update to 4.1.0

* Fri Oct 11 2019 Stuart D. Gathman <stuart@gathman.org> 4.0.4-5
- Add generic notify script for incron

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Stuart D. Gathman <stuart@gathman.org> 4.0.4-1
- Official upstream release! BZ#1560531
- Move acme_tiny.py to acme-tiny-core subpackage BZ#1438181

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4.20170516gitaf025f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Stuart D. Gathman <stuart@gathman.org> 0.2-3.20170616gitaf025f5
- BZ#1507333 EL6 missing python-argparse dependency
- BZ#1515781 Agreement updated.
- BZ#1409345 Unwritable certs silently skipped

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2.20170516gitaf025f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul  6 2017 Stuart D. Gathman <stuart@gathman.org> 0.2-1.20170616gitaf025f5
- BZ#1468045 Update to new upstream version
- BZ#1409686 Message.getallmatchingheaders() is broken in python3.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12.20160810git5a7b4e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-11.20160810git5a7b4e7
- Rebuild for Python 3.6

* Mon Aug 22 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-10.20160810git5a7b4e7
- Fix cert writable check in sign script
- More tips in README-fedora.md

* Mon Aug 22 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-9.20160810git5a7b4e7
- Use %%{systemd_requires}
- Remove unneeded cronie, python dependencies
- Add acme-tiny.timer to systemd scriptlets
- Add README-fedora.md
- acme_tiny: Fix --chain patch for python2.6 (el6)
- acme_tiny: Suppress traceback on error

* Sun Aug 21 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-8
- Add use_systemd flag to use systemd timer and enable on Fedora and epel7
- Enable use_python3 flag for Fedora (but not epel7).

* Sat Aug 20 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-7
- sign: Actually use the new --chain flag
- cron: Make days to expiration explicit
- spec: Set file modes with install
- acme.conf: mark as config

* Fri Aug 19 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-6
- Python3 fixes for cert-check
- acme-tiny: Update patch to leave default behavior unchanged
- make /var/lib/acme readable by all except private

* Thu Aug 11 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-5
- sign: Use tmp output to avoid wiping existing cert on error
- acme_tiny: get intermediate cert from acme protocol

* Thu Aug 11 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-4
- Fix path of acme_tiny and make days explicit in sign script
- Add crontab

* Wed Aug 10 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-3
- Add global acme httpd conf
- Append intermediate certs, add current lets-encrypt intermediate cert

* Tue Aug  9 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-2
- add private, csr, certs directories
- add sign script suitable for cron

* Mon Aug  8 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-1
- Initial RPM
