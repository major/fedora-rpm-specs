%global _hardened_build 1

Name:             3proxy
Version:          0.8.13
Release:          10%{?dist}

Summary:          Tiny but very powerful proxy
Summary(ru):      Маленький, но крайне мощный прокси-сервер

License:          BSD or ASL 2.0 or GPLv2+ or LGPLv2+
Url:              http://3proxy.ru/?l=EN

Source0:          https://github.com/z3APA3A/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:          3proxy.cfg
Source3:          3proxy.service
BuildRequires:    gcc
BuildRequires:    openssl-devel

# I correct config path in man only. It is fully Fedora related.
Patch0:           3proxy-0.6.1-config-path.patch

BuildRequires:    systemd
BuildRequires: make
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
# This is actually needed for the %triggerun script but Requires(triggerun)
# is not valid.  We can use %post because this particular %triggerun script
# should fire just after this package is installed.
Requires(post):   systemd
Obsoletes:        3proxy-sysvinit < 0.8.12


%description
%{name} -- light proxy server.
Universal proxy server with HTTP, HTTPS, SOCKS v4, SOCKS v4a, SOCKS v5, FTP,
POP3, UDP and TCP portmapping, access control, bandwith control, traffic
limitation and accounting based on username, client IP, target IP, day time,
day of week, etc.

%description -l ru
%{name} -- маленький прокси сервер.
Это универсальное решение поддерживающее HTTP, HTTPS, SOCKS v4, SOCKS v4a,
SOCKS v5, FTP, POP3, UDP и TCP проброс портов (portmapping), списки доступа
управление скоростью доступа, ограничением трафика и статистикоу, базирующейся
на имени пользователя, слиентском IP адресе, IP цели, времени дня, дня недели
и т.д.


%prep
%autosetup -p0

# To use "fedora" CFLAGS (exported)
sed -i -e "s/CFLAGS =/CFLAGS +=/" Makefile.Linux

%build
make -f Makefile.Linux

%install
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/
mkdir -p %{buildroot}%{_mandir}/man{3,8}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
install -m755 -D src/%{name} %{buildroot}%{_bindir}/%{name}
install -m755 -D src/dighosts %{buildroot}%{_bindir}/dighosts
install -m755 -D src/ftppr %{buildroot}%{_bindir}/ftppr
install -m755 -D src/mycrypt %{buildroot}%{_bindir}/mycrypt
install -m755 -D src/pop3p %{buildroot}%{_bindir}/pop3p
install -m755 -D src/%{name} %{buildroot}%{_bindir}/%{name}
install -m755 -D src/proxy %{buildroot}%{_bindir}/htproxy
install -m755 -D src/socks %{buildroot}%{_bindir}/socks
install -m755 -D src/tcppm %{buildroot}%{_bindir}/tcppm
install -m755 -D src/udppm %{buildroot}%{_bindir}/udppm

install -pD -m644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}.cfg
install -pD -m755 %{SOURCE3} %{buildroot}/%{_unitdir}/%{name}.service

for man in man/*.{3,8} ; do
  install "$man" "%{buildroot}%{_mandir}/man${man:(-1)}/"
done


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license copying
%doc README authors Release.notes
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_localstatedir}/log/%{name}
%{_mandir}/man8/*.8.gz
%{_mandir}/man3/*.3.gz
%{_unitdir}/%{name}.service

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.13-5
- Rebuilt for updated fedora-rpm-macros.
  See https://pagure.io/fesco/issue/2583.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Pavel Alexeev <Pahan@Hubbitus.info> - 0.8.13-1
- Update to 0.8.13 version (bz#1742435).
- Try build on epel8 (bz#1757824).
- Completely remove SOURCE1 sysvinit legacy.
- Reformat with spaces.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.12-1
- Update 0.8.12
- Retire sysvinit

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 0.8.2-1
- Major upstream update - 0.8.2. Bz#1300097.
- Tarballs now on github.

* Fri Jan 01 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 0.7.1.3-1
- New upstream release 0.7.1.3 - bz#1263482.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 05 2015 Adam Jackson <ajax@redhat.com> 0.7.1.2-2
- Drop sysvinit subpackage on F23+

* Mon Feb 23 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 0.7.7.2-1
- New upstream version 0.7.7.2

* Mon Aug 18 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.7.7.1-1
- Update to 0.7.7.1 - bz#1114274.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 8 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.7-1
- Update to 0.7 version bz#1085256.
- Add BR openssl-devel.

* Tue Jan 7 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.1-18
- Step to systemd macroses (#850383)

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.1-16
- Harden build - bz#955141

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.1-12
- Make service systemd compliant (BZ#657412).

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 4 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.1-10
- Add man3/3proxy.cfg.3 man (BZ#648204).
- Gone explicit man gzip - leave it for rpm.

* Sun May 30 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.1-9
- Correct path to config file in man (BUG#596087) add Patch0: 3proxy-0.6.1-config-path.patch

* Mon Mar 15 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6.1-8
- Update to version 0.6.1
- In NM event processing replace service restart to condrestart - BZ#572662

* Wed Nov 25 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6-7
- Again new init-script for Fix BZ#533144 :).

* Wed Nov 25 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6-6
- Forgot commit new init-script for Fix BZ#533144.

* Sun Nov 8 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6-5
- Fix BZ#533144:
- Add reload section to service file, fix stop.
- Add %%{_sysconfdir}/NetworkManager/dispatcher.d/40-%%{name} (Thanks to Pankaj Pandey)
- Include man-files.
- Add Requires: initscripts as owner directory %%{_sysconfdir}/NetworkManager/dispatcher.d/

* Thu Aug 20 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6-3
- Fedora Review started - thank you Peter Lemenkov.
- Change rights (0755->0644) of config.
- Disable service by default.
- Add BR dos2unix.

* Mon Aug 17 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6-2
- /usr/bin/proxy renamed to htproxy to avoid name bump with libproxy-bin.
- Add Source2: 3proxy.cfg from Alt Linux (slightly modified) - http://sisyphus.ru/ru/srpm/Sisyphus/3proxy/sources/1 (thanks to Afanasov Dmitry).
- Add log-dir %%{_localstatedir}/log/%%{name}

* Mon Aug 17 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.6-1
- Ressurect old spec. New version 0.6.
- Rename spec to classic %%{name}.spec.
- Remove Hu part from release and add %%{?dist}.
- Change summary, description, URL. Add Russian localisation of sumamry and description.
- Strip some old comments.
- Add to %%doc Readme Changelog authors copying news.
- Turn macros usage from %%name to %%{name} for consistence.
- Change group from System/Servers to standard System Environment/Daemons.
- Add %%defattr(-,root,root,-) in %%files section.
- Add cleanup in %%install section.
- Add %%clean section with cleanup buildroot.
- License changed from just GPL to "BSD or ASL 2.0 or GPLv2+ or LGPLv2+" (according to Makefile.Linux)
- Add %%config(noreplace) mark to all configs.
- Add file %%{_initdir}/%%{name}
- Old %%{_initdir} macros replaced by %%{_initrddir}
- Hack makefile to use system CFLAGS.
- Add %%post/%%postun sections.

* Fri Jan 25 2008 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] info> - 0.5.3k
- Import from ftp://ftp.nluug.nl/pub/os/Linux/distr/altlinux/4.0/Server/4.0.1/files/SRPMS/3proxy-0.5.3h-alt1.src.rpm
	Combine with ftp://ftp.pbone.net/mirror/ftp.sourceforge.net/pub/sourceforge/t/th/three-proxy/3proxy-0.5.3g-1.src.rpm
- Steep to version 0.5.3k
- Comment out packager
- Reformat header of spec with tabs
- Add desc from second src.rpm of import
- Correct source0
- Add -c key fo %%setup macro
- Add BuildRoot definition (this is not ALT)
- Change
	Release:	alt1
	to
	Release:	0.Hu.0

* Fri Apr 13 2007 Lunar Child <luch@altlinux.ru> 0.5.3h-alt1
- new version

* Wed Mar 21 2007 Lunar Child <luch@altlinux.ru> 0.5.3g-alt2
- Added init script.
- Added new trivial config file.

* Tue Mar 20 2007 Lunar Child <luch@altlinux.ru> 0.5.3g-alt1
- First build for ALT Linux Sisyphus
