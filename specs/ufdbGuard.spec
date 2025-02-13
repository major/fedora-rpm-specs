Name:		ufdbGuard
Version:	1.35.8
Release:	5%{?dist}
Summary:	A URL filter for squid
URL:		https://www.urlfilterdb.com/
License:	GPL-2.0-only

Source0:	https://www.urlfilterdb.com/files/downloads/%{name}-%{version}.tar.gz
Source1:	ufdbGuard.logrotate

%if 0%{?fedora} || 0%{?rhel} >= 7
%bcond_without tmpfiles
%else
%bcond_with    tmpfiles
%endif

BuildRequires: make
BuildRequires: bzip2-devel
BuildRequires: zlib-devel
BuildRequires: perl-interpreter 
BuildRequires: gcc
%if %{?rhel:7}%{!?rhel:0}
%{?systemd_requires}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif
BuildRequires: openssl-devel
BuildRequires: openssl-devel-engine
BuildRequires: bind-utils
BuildRequires: wget
Requires: logrotate

%description
ufdbGuard is a free URL filter for Squid with additional features like
SafeSearch enforcement for a large number of search engines, safer HTTPS 
visits and dynamic detection of proxies (URL filter circumventors).

ufdbGuard supports free and commercial URL databases that can be
downloaded from various sites and vendors.
You can also make your own URL database for ufdbGuard.

%prep
%setup -q

iconv -c --from-code=ISO-8859-1 --to-code=UTF-8 -o CHANGELOG.new CHANGELOG
mv CHANGELOG.new CHANGELOG

# Create a sysusers.d config file
cat >ufdbguard.sysusers.conf <<EOF
u ufdb - 'ufdbGuard URL filter' /var/lib/ufdbguard -
EOF

%build
INSTALL_PROGRAM=./install-sh %configure \
	--with-ufdb-user=ufdb \
	--prefix=%{_prefix} \
	--with-ufdb-bindir=%{_sbindir} \
	--with-ufdb-piddir=%{_localstatedir}/run/ufdbguard \
	--with-ufdb-mandir=%{_mandir} \
	--with-ufdb-images_dir=%{_sharedstatedir}/ufdbguard/images \
	--with-ufdb-logdir=%{_localstatedir}/log/ufdbguard \
	--with-ufdb-samplesdir=%{_sharedstatedir}/ufdbguard/samples \
	--with-ufdb-config=%{_sysconfdir}/ufdbguard \
	--with-ufdb-dbhome=%{_sharedstatedir}/ufdbguard/blacklists \
	--with-ufdb-imagesdir=%{_sharedstatedir}/ufdbguard/images

%make_build

%install
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
mkdir -p %{buildroot}%{_sysconfdir}/init.d
mkdir -p %{buildroot}%{_sysconfdir}/ufdbguard
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
%make_install INSTALL="../install-sh -c"
for i in $(find doc/ -type f -name '*.1'); do
    install -p -D -m 0644 $i %{buildroot}%{_mandir}/man1/
done
for i in $(find doc/ -type f -name '*.8'); do
    install -p -D -m 0644 $i %{buildroot}%{_mandir}/man8/
done

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/ufdbGuard

rm -rf %{buildroot}%{_sysconfdir}/rc.d/init.d/ufdb

#remove sysinit file
rm -rf %{buildroot}%{_sysconfdir}/init.d

#remove ufdbsignal as it's setuid.
rm -f %{buildroot}%{_sbindir}/ufdbsignal

mkdir -p %{buildroot}%{_var}/run/ufdbguard
%if %{with tmpfiles}
# Setup tmpfiles.d config for the above
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
echo 'd /var/run/ufdbguard 0750 ufdb ufdb -' > \
    %{buildroot}/usr/lib/tmpfiles.d/ufdbGuard.conf
%endif

install -m0644 -D ufdbguard.sysusers.conf %{buildroot}%{_sysusersdir}/ufdbguard.conf



%post
%systemd_post ufdbguard.service

%preun
%systemd_preun ufdbguard.service

%postun
%systemd_postun_with_restart ufdbguard.service


%files
%license COPYING GPL
%doc README CHANGELOG CREDITS
%config(noreplace) %{_sysconfdir}/sysconfig/ufdbguard
%config(noreplace) %dir %{_sysconfdir}/ufdbguard/
%config(noreplace) %{_sysconfdir}/ufdbguard/*
%config(noreplace) %{_sysconfdir}/logrotate.d/ufdbGuard
%{_sbindir}/*
%{_mandir}/man1/ufdb*
%{_mandir}/man8/ufdb*
%dir %{_sharedstatedir}/ufdbguard/
%attr(-, ufdb, ufdb) %dir %{_localstatedir}/log/ufdbguard/
%{_sharedstatedir}/ufdbguard/*
%{_unitdir}/ufdbguard.service
%attr(-, ufdb, ufdb) %dir %{_var}/run/ufdbguard/
%if %{with tmpfiles}
%config(noreplace) %{_tmpfilesdir}/ufdbGuard.conf
%endif
%{_sysusersdir}/ufdbguard.conf

%changelog
* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.35.8-5
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.35.8-3
- Fix FTBFS

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 03 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.35.8-1
- 1.35.8

* Fri Mar 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.35.7-1
- 1.35.7
- use upstream unit file

* Fri Feb 02 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.35.6-1
- 1.35.6

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.35.5-2
- migrated to SPDX license

* Tue Feb 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.35.5-1
- 1.35.5

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.35.4-1
- 1.35.4

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.35.3-5
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.35.3-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.35.3-1
- 1.35.3

* Fri Oct 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.35.2-1
- 1.35.2

* Thu Oct 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.35.1-1
- 1.35.1

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.34.6-3
- Correct logrotate configure.

* Fri Aug 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.34.6-2
- Correct sysconfig file placement.
- Fix tmpfiles config.

* Mon Aug 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.34.6-1
- 1.34.6

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.34.5-2
- Review fixes.

* Fri Apr 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.34.5-1
- Initial package.
