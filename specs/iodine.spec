Name:		iodine
Version:	0.8.0
Release:	7%{?dist}
Summary:	Solution to tunnel IPv4 data through a DNS server
Summary(ru):	Решение для туннелирования IPv4 трафика через DNS сервер
License:	ISC
URL:		http://code.kryo.se/iodine/
Source0:	https://github.com/yarrick/%{name}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# Initscripts and separate configs made by Nikolay Ulyanitsky
Source1:	%{name}-client.conf
Source2:	%{name}-server.conf

Source5:	%{name}.logrotate.client
Source6:	%{name}.logrotate.server

Source7:	%{name}-client.service
Source8:	%{name}-server.service

# Split man pages into client and server:
Patch1:		iodine-0.8.0-split-man.patch

# Install to bin rather than sbin:
# (see https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin)
Patch2:		iodine-0.8.0-bin-path.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	zlib-devel
BuildRequires:	systemd

Requires:	%{name}-client
Requires:	%{name}-server

%description
iodine lets you tunnel IPv4 data through a DNS server. This can be usable in
different situations where internet access is firewalled, but DNS queries are
allowed.

It runs on Linux, Mac OS X, FreeBSD, NetBSD, OpenBSD and Windows and needs a
TUN/TAP device. The bandwidth is asymmetrical with limited upstream and up to
1 Mbit/s downstream.

This is meta-package to install both client and server.
It also contain three documantation files: CHANGELOG, README, TODO.

%description -l ru
iodine предоставляет возможность пробросить IPv4 туннель сквозь DNS сервер.
Это может быть очень полезно в разных ситуациях, когда доступ в интернет
запрещён фаерволом, но DNS запросы пропускаются нормально.

Iodine работает на Linux, Mac OS X, FreeBSD, NetBSD, OpenBSD и Windows и
использует TUN/TAP устройство. Пропускная способность асимметрична - аплоад не
быстр, скачивание до 1 Mbit/s.

Это мета-пакет для инсталляции обоих пакетов, клиента и сервера.
Он также содержит 3 файла документации: CHANGELOG, README, TODO.

%package client
Summary:	Client part of solution to tunnel IPv4 data through a DNS server
Summary(ru):	Клиент для туннелирования IPv4 трафика через DNS сервер
%{?systemd_requires}
Provides:	bundled(md5-deutsch)

%description client
This is the client part of iodine.

%description client -l ru
Это пакет клиентской части.

%package server
Summary:	Server part of solution to tunnel IPv4 data through a DNS server
Summary(ru):	Сервер для туннелирования IPv4 трафика через DNS сервер
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
# This is actually needed for the %%triggerun script but Requires(triggerun)
# is not valid. We can use %%post because this particular %%triggerun script
# should fire just after this package is installed.
Requires(post):	systemd-sysv
# /sbin/ifconfig and /sbin/route (bz#922225)
Requires:	net-tools
Provides:	bundled(md5-deutsch)

%description server
This is the server part of iodine.

%description server -l ru
Это пакет серверной части

%prep
%autosetup -p1 -n %{name}-%{version}%{?prerel}

%build
# Fails to build without -c gcc flag (comes from upstream Makefile).
make %{?_smp_mflags} prefix=%{_prefix} CFLAGS="-c %{optflags} -DLINUX -D_GNU_SOURCE"

%install
make install prefix=%{buildroot}%{_prefix}

install -Dp -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}-client
install -Dp -m 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}-server

install -Dp -m 0644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}-client
install -Dp -m 0644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}-server

install -Dp -m 0644 %{SOURCE7} %{buildroot}/%{_unitdir}/%{name}-client.service
install -Dp -m 0644 %{SOURCE8} %{buildroot}/%{_unitdir}/%{name}-server.service

%post client
%systemd_post %{name}-client.service

%preun client
%systemd_preun %{name}-client.service

%postun client
%systemd_postun_with_restart %{name}-client.service

%post server
%systemd_post %{name}-server.service

%preun server
%systemd_preun %{name}-server.service

%postun server
%systemd_postun_with_restart %{name}-server.service

%files
%doc CHANGELOG LICENSE README.md

%files client
%{_bindir}/%{name}
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}-client
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-client
%{_mandir}/man8/%{name}.8.gz
%{_unitdir}/%{name}-client.service

%files server
%{_bindir}/%{name}d
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}-server
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%{_mandir}/man8/%{name}d.8.gz
%{_unitdir}/%{name}-server.service

%changelog
* Tue Jan 28 2025 Gabriel L. Somlo <gsomlo@gmail.com> - 0.8.0-7
- switch to 'bin' (from deprecated 'sbin') for binary install path (BZ #2340654)
- use autosetup to simplify patch management

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 23 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.8.0-1
- Update to 0.8.0
- Switch source to github
- Spec file cleanup

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-17
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 28 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-6
- Drop sysvinit script and lots of old stuff

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Adam Jackson <ajax@redhat.com> 0.7.0-3
- Drop sysvinit subpackage from F23+

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.7.0-1
- Update to 0.7.0 to fix CVE-2014-4168 iodine: authentication bypass vulnerability (bz#1110339, bz#1110338 [bz#1110340, bz#1110341, bz#1110342]).
- Drop old Patch0: iodine-0.5.2-prefix.patch
- Rebase iodine-0.6.0-rc1.split-man.patch -> iodine-0.7.0.split-man.patch
- Some spec cleanup.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.rc1.12.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 7 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.0-0.rc1.12
- Step to systemd macroses (#850160)

* Tue Jan 7 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.0-0.rc1.11
- Add Provides: bundled(md5-deutsch) to client and server sub-packages (#1046028)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.rc1.10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.0-0.rc1.10
- Add Requires: net-tools (bz#922225) for server package.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.rc1.9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.rc1.9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 23 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.0-0.rc1.9
- Introduce systemd support. Move legacy sysvinit part into subpackages (bz#789697).

* Sun Jan 8 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.0-0.rc1.8
- Split man pages also.

* Mon Jan 2 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.0-0.rc1.7
- By request bz#758930 split to subpackages.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.rc1.6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.0-0.rc1.6
- Add -DLINUX to build options (BZ#644310, thanks to Andy Shevchenko)
- Fix service scripts to find binaries in /usr/sbin instead of /usr/bin (BZ#644299 thanks to Andy Shevchenko)
- Add 0600 file attributes to prevent password access from regular users (BZ#644305).
- In comments configs add IODINE(D)_PASS variables description (BZ#644317).

* Wed Sep 29 2010 jkeating - 0.6.0-0.rc1.4.2
- Rebuilt for gcc bug 634757

* Wed Sep 29 2010 jkeating - 0.6.0-0.rc1.4.1
- Rebuilt for gcc bug 634757

* Sun Sep 12 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.0-0.rc1.4
- Build new version 0.6.0rc1
- Define prerel.

* Sat Mar 6 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.5.2-3
- Honor CFLAGS

* Mon Feb 22 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.5.2-2
- Import some items from Nikolay Ulyanitsky package ( https://bugzilla.redhat.com/show_bug.cgi?id=530747#c1 ):
	o Add initscripts support (modified)
	o Add logrotate support
	o Exclude README-win32.txt and respective delete dos2unix BR.
	o Add BR zlib-devel

* Sat Oct 24 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.5.2-1
- Initial spec.
