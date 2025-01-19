# Checks may only be ran from a host with internet connection
%global runcheck	0

%global hitch_user	hitch
%global hitch_group	hitch
%global hitch_homedir	%{_sharedstatedir}/hitch
%global hitch_confdir	%{_sysconfdir}/hitch
%global hitch_datadir	%{_datadir}/hitch
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# A bug in the rhel7 builders? Looks like they set _pkgdocdir fedora style
# without version...?
%if 0%{?rhel} == 7
%global _pkgdocdir %{_docdir}/%{name}-%{version}
%endif

%global _hardened_build 1

Name:		hitch
Version:	1.8.0
Release:	7%{?dist}
Summary:	Network proxy that terminates TLS/SSL connections

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://hitch-tls.org/
Source0:	https://hitch-tls.org/source/%{name}-%{version}%{?v_rc}.tar.gz

BuildRequires:	make
BuildRequires:	libev-devel
BuildRequires:	openssl
BuildRequires:	pkgconfig
BuildRequires:	libtool
#BuildRequires:	python-docutils >= 0.6
%if 0%{fedora} >= 41
BuildRequires:  openssl-devel-engine
%else
BuildRequires:	openssl-devel
%endif

Requires:	openssl

Patch0:		hitch.systemd.service.patch
Patch1:		hitch.initrc.redhat.patch

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd

%description
hitch is a network proxy that terminates TLS/SSL connections and forwards the
unencrypted traffic to some backend. It is designed to handle 10s of thousands
of connections efficiently on multicore machines.

%prep
%setup -q -n %{name}-%{version}%{?v_rc}
%patch -P0
%patch -P1

%build
#./bootstrap

#export CFLAGS

# manpages are prebuilt, no need to build again
export RST2MAN=/bin/true

%configure --docdir=%_pkgdocdir

make %{?_smp_mflags}


%install
%make_install
sed   '
	s/user = .*/user = "%{hitch_user}"/g;
	s/group = .*/group = "%{hitch_group}"/g;
	s/backend = "\[127.0.0.1\]:8000"/backend = "[127.0.0.1]:6081"/g;
	s/workers = ..../workers = auto/;
	$a\syslog = on
	$a\log-level = 1
	$a\# Add pem files to this directory
	$a\pem-dir = "/etc/pki/tls/private"
	' hitch.conf.example > hitch.conf

%if 0%{?fedora} 
	sed -i 's/^ciphers =.*/ciphers = "PROFILE=SYSTEM"/g' hitch.conf
%endif

rm -f %{buildroot}%{_datarootdir}/doc/%{name}/hitch.conf.example

install -p -D -m 0644 hitch.conf %{buildroot}%{_sysconfdir}/hitch/hitch.conf
install -d -m 0755 %{buildroot}%{hitch_homedir}
install -d -m 0755 %{buildroot}%{hitch_datadir}
install -p -D -m 0644 hitch.service %{buildroot}%{_unitdir}/hitch.service
install -p -D -m 0644 limit.conf    %{buildroot}%{_sysconfdir}/systemd/system/%{name}.service.d/limit.conf

# check is not enabled by default, as it won't work on the koji builders, 
# nor on machines that can't reach the Internet. 
%check
%if 0%{?runcheck} == 1
make check
%endif

%pre
groupadd -r %{hitch_group} &>/dev/null ||:
useradd -r -g %{hitch_group} -s /sbin/nologin -d %{hitch_homedir} %{hitch_user} &>/dev/null ||:


%post
%systemd_post hitch.service
%preun
%systemd_preun hitch.service
%postun
%systemd_postun_with_restart hitch.service


%files
%doc README.md
%doc CHANGES.rst
%doc hitch.conf.example
%doc docs/*
%license LICENSE
%{_sbindir}/%{name}
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*
%dir %{_sysconfdir}/%{name}
%attr(0700,%hitch_user,%hitch_user) %dir %hitch_homedir
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/systemd/system/%{name}.service.d/limit.conf
%ghost %verify(not md5 size mtime)  /run/%{name}/%{name}.pid

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.0-6
- convert license to SPDX

* Fri Aug 02 2024 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.8.0-5
- Fedora >= 41 needs specific openssl-devel-engine

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 09 2023 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.8.0-1
- New upstream release
- Number of workers are now default set to 'auto', ie. one per cpu

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.7.3-1
- New upstream release
- Removed support for el6

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.7.2-1
- New upstream release

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.7.0-5
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.7.0-1
- New upstream release

* Fri Oct 16 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6.1-2
- Built from recently released official upstream tarball
- Removed extra buildreqs and stuff

* Tue Oct 13 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6.1-1
- New upstream release.
- Built from git tag, as no upstream tarball exists since August. Pinged
  upstream about it.
- Extra buildreqs and stuff

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6.0-1
- New upstream release
- Removed patches merged upstream

* Mon Feb 10 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5.2-3
- Added upstream patch for gcc-10.0.1, upstream issue 326

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5.2-1
- New upstream release
- Removed patches merged upstream

* Tue Nov 26 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5.1-1
- New upstream release
- Added a patch working around upstream bug #322
- Example config now sets debug-level=1 and logs to syslog

* Tue Nov 12 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5.0-4
- Added support for epel8
- Added a systemd limit.conf with defaults LimitCORE=infinity, LimitNOFILE=10240
- Added pem-dir = "/etc/pki/tls/private" to the example config
- Changed systemd Type=forking matching the example config, fixes bz #1731420
- Simplified handling of the _docdir macro

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.5.0-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Ingvar Hagelund <ingvar@redpill-linpro.com>  - 1.4.8-1
- New upstream release 1.4.8, closes bz 1569501

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 04 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.4.6-4
- Rebuilt against openssl-1.0.2k for epel7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.4.6-1
- New upstream release
- Removed unnecessary fix for upstream bug #181

* Wed May 31 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.4.5-1
- New upstream release
- Had to add -Wno-error=strict-aliasing because of upstream bug #181

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4.4-2
- More macros
- Use systemd's RuntimeDirectory instead of tmpfilesd
- hitch now owns its homedir, closing bz #1405948

* Thu Dec 22 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4.4-1
- New upstream release
- Removed merged patch for openssl-1.1

* Thu Nov 17 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4.3-1
- New upstream release
- Added upstream patch for openssl-1.1

* Thu Nov 17 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4.2-1
- New upstream release
- Added new manpage for hitch.conf
- Updated sed edit of the example config to match values in the test suite
- Added a hack for un-fedora-styling _pkgdocdir on rhel7 builders

* Sat Sep 24 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4.1-1
- New upstream release

* Tue Sep 13 2016 Ingvar Hagelund <ingvar@repdill-linpro.com> 1.4.0-1
- New upstream release

* Thu Aug 25 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.3.1-1
- New upstream release
- Fixes for beta3 ironed out upstream, so removed

* Mon Aug 08 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.3.0-0.1.beta3
- New upstream beta release
- Manually build man page, BuildRequires python-docutils => 0.6
- Check suit now runs on el6 without patching

* Fri May 20 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.2.0-2
- Added missing check on upgrade/uninstall in postun script on epel6

* Mon Apr 25 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.2.0-1
- New upstream release
- Clean up test tree before build
- Removed no longer needed test patch 
- Rebased missing_curl_resolve_on_el6 test patch
- Added reload option to systemd service file and sysv initrc script
- Changed the default cipher to "PROFILE=SYSTEM" on fedora

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.1.1-1
- New upstream release
- Removed patches included upstream
- No need to rebuild the manpage, as the upstream distribution includes it

* Mon Nov 23 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.1.0-1
- New upstream release
- Use the _pkgdocdir macro to avoid docdir hacks for el6
- Added a patch from upstream that sets stronger ciphers as default

* Thu Oct 15 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.1-1
- New upstream release
- New Home and Source0 URLs
- Rebased patches
- Changed initrc and systemd start up scripts to match new binary name

* Tue Aug 04 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.5.1.beta5
- New upstream beta
- Dropped patch3 and patch5, they are fixed in upstream
- Rebased patch for curl on el6
- hitch no longer autocreates the default config, so use the provided example

* Tue Aug 04 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.4.3.beta4
- Much simpler patch for github issue #37

* Mon Aug 03 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.4.2.beta4
- Patching around upstream github issue #37

* Mon Aug 03 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.4.1.beta4
- New upstream beta
- Dropped setgroups patch as it has been accepted upstream
- Simple sed replace nobody for nogroup in test08

* Sun Jul 19 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.3.4.beta3
- Some more fixes for the fedora package review, ref Cicku

* Thu Jul 16 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.3.3.beta3
- Some more fixes for the fedora package review, ref Jeff Backus

* Fri Jun 26 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.3.2.beta3
- Added _hardened_build macro and PIE on el6

* Thu Jun 25 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.3.1.beta3
- Some fixes for the fedora package review, ref Sören Möller
- Now runs the test suite in check, adding BuildRequire openssl
- Added a patch that fixed missing cleaning running daemons from test suite
- Added a patch that made test07 run on older curl (epel6)
- Package owns /etc/hitch
- Added pidfile to systemd and tmpfiles.d configuration
- Added pidfile to redhat sysv init script

* Wed Jun 10 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.3.beta3
- Initial wrap for fedora

