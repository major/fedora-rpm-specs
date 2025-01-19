Name:           inadyn-mt
Version:        2.28.10
Release:        22%{?dist}
Summary:        Dynamic DNS Client
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://inadyn-mt.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/inadyn-mt/inadyn-mt.v.0%{version}.tar.gz
Source1:        inadyn-mt.conf
Source2:        inadyn.service
Source3:        inadyn-nm-dispatcher
Patch1:         inadyn-mt-libao.patch
# https://gitlab.com/bhoover/inadyn-mt/commit/84c18b121886e22375e2163d495f75a207b96d11
Patch2:         inadyn-mt-gcc10.patch
Patch3: inadyn-mt-c99.patch

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libao-devel
BuildRequires:  systemd-units
BuildRequires: make

Obsoletes:      inadyn < %{version}
Provides:       inadyn = %{version}-%{release}

Requires(pre):    shadow-utils
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units

Obsoletes:      inadyn-mt-units < %{version}-%{release}
Provides:       inadyn-mi-units = %{version}-%{release}

Obsoletes:      inadyn-mt-sysvinit < %{version}-%{release}
Provides:       inadyn-mt-sysvinit = %{version}-%{release}


%description
INADYN-MT is a dynamic DNS client. It maintains the IP address of 
a host name. It periodically checks whether the IP address stored
by the DSN server is the real current address of the machine that
is running INADYN-MT.

Before using inadyn-mt for the first time you must use the DynDNS
provider's web interface to create the entry for the hostname. You
should then fill in /etc/inadyn.conf with the appropriate detail

%prep
%setup -q -n %name.v.0%{version}
%patch -P1 -p1 -b .libao
%patch -P2 -p1 -b .gcc10
%patch -P3 -p1

%build
rm -rf bin/
autoreconf
%configure --prefix=/usr/share
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
install -m 0755 src/inadyn-mt $RPM_BUILD_ROOT%{_sbindir}/inadyn

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man5
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 0644 man/inadyn.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 0644 man/inadyn.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/inadyn-mt/lang
cp lang/* $RPM_BUILD_ROOT%{_datadir}/inadyn-mt/lang

mkdir -p $RPM_BUILD_ROOT%{_datadir}/inadyn-mt/extra
cp -R extra/* $RPM_BUILD_ROOT%{_datadir}/inadyn-mt/extra

mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -p -m 0644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_unitdir}

mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/NetworkManager/dispatcher.d
install -p %{SOURCE3} ${RPM_BUILD_ROOT}%{_prefix}/lib/NetworkManager/dispatcher.d/30-inadyn

mkdir -p $RPM_BUILD_ROOT/var/cache/inadyn-mt

%pre
getent group inadyn >/dev/null || groupadd -r inadyn
getent passwd inadyn >/dev/null || \
    useradd -r -g inadyn -d /var/cache/inadyn-mt -s /sbin/nologin \
    -c "Dynamic DNS client" inadyn
exit 0

%post
%systemd_post inadyn.service
[ $1 -gt 1 ] && chown -R inadyn: /var/cache/inadyn-mt || :

%preun
%systemd_preun inadyn.service

%postun
%systemd_postun_with_restart inadyn.service

%files 
%license COPYING
%doc readme.html
%{_sbindir}/inadyn
%{_unitdir}/inadyn.service
%{_mandir}/man*/*
%attr(640,inadyn,inadyn) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{_prefix}/lib/NetworkManager/
%{_datadir}/%{name}/
%attr(755,inadyn,inadyn) %dir /var/cache/inadyn-mt/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.28.10-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Florian Weimer <fweimer@redhat.com> - 2.28.10-15
- C99 compatibility fixes

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.28.10-11
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 Michael Cronenworth <mike@cchtml.com> - 2.28.10-8
- Patch for gcc 10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Michael Cronenworth <mike@cchtml.com> - 2.28.10-6
- Drop NetworkManager Requires

* Thu Aug 22 2019 Lubomir Rintel <lkundrak@v3.sk> - 2.28.10-5
- Move the NetworkManager dispatcher script out of /etc

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Michael Cronenworth <mike@cchtml.com> - 2.28.10-1
- New upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 28 2016 Michael Cronenworth <mike@cchtml.com> - 2.28.07-1
- New upstream release

* Fri Aug 05 2016 Michael Cronenworth <mike@cchtml.com> - 2.28.06-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Michael Cronenworth <mike@cchtml.com> - 2.24.49-1
- New upstream release

* Sat Jan 23 2016 Michael Cronenworth <mike@cchtml.com> - 2.24.48-1
- New upstream release

* Mon Nov 09 2015 Michael Cronenworth <mike@cchtml.com> - 2.24.47-2
- Fix service order (rhbz#1279174)

* Mon Aug 31 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.24.47-1
- Update to 2.24.47
- Run as dedicated inadyn user/group
- Use /var/cache/inadyn-mt for caching
- Restrict read access to config file (contains auth data)
- Avoid duplicate syslog messages
- Fix systemd service type

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Michael Cronenworth <mike@cchtml.com> - 2.24.46-1
- New upstream release

* Sat Jan 31 2015 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.44-1
- New upstream release

* Mon Jan 19 2015 Michael Cronenworth <mike@cchtml.com> - 2.24.43-1
- New upstream release
- Multiple packaging fixes (rhbz# 1090317)

* Sun Dec  7 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.40-3
- Make systemd unit file none-executable (#1171375)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul  2 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.40-1
- New upstream release
- Set explicit account information in the systemd unit file (#1100889)
- Rebuilt to fix dep. issue agains libao (#1100889)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.38-2
- Fix wrong NetworkManger dispatcher directory

* Sun Apr 27 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.38-1
- New upstream release
- Remove'type=forking' from service file (#1036471)
- Set default cache dir to /var/cache/inadyn-mt (#1090533)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.36-11
- Fix issue to build aarch64 release (#925507)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.36-9
- Add Type=forking to the systemd unit file (#90344)

* Sat Oct 13 2012 Jochen Schmitt <sJochen herr-schmitt de> - 2.24.36-8
- Fix Sigfault (#863026)

* Fri Oct  5 2012 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.36-7
- Fix wrong changelog entry

* Fri Oct  5 2012 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.36-6
- Fix wrong systemd macro usage

* Fri Oct  5 2012 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.36-5
- Use of systemd macros instread scritlets (#850157)
- Fix start up issues with systemd (#830064)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May  8 2012 Jochen Schmitt <Jochen herr-schmitt de> - 2.24.36-3
- Remove PIDFile statement from unit file (#819586)

* Wed Apr 25 2012 Jochen Schmitt <Jochen herr-schmitt de>  2.24.36-1
- New upstream release

* Wed Apr 25 2012 Jochen Schmitt <Jochen herr-schmitt de> 2.24.34-3
- Change type to oneshot in inadyn.service (#803844)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr 23 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.24.36-1
- New upstream release

* Thu Mar 31 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.24.34-2
- Change PID file to /run/inadyn.pid

* Wed Mar 30 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.24.34-1
- New upstream release

* Mon Mar 21 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.24.30-1
- New upstream release
- Rewriting systemd scriptlets

* Wed Mar  2 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.24.24-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.24.06-2
- New upstream release

* Tue Jan  4 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.20.44-1
- New upstream release

* Mon Dec  6 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.40-1
- New upstream release

* Thu Dec  2 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.38-4
- Some changes to the unit file to adopt to trad. daemon behaviour

* Tue Nov 30 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.38-3
- Fix some systemd releated issues

* Sat Nov 27 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.38-2
- Obsoleting units and sysvinit subpakages

* Fri Nov 26 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.38-1
- New upstream release

* Wed Nov 24 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.34-1
- New upstream release
- try to provide a systemd-only release

* Mon Nov 22 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.32-1
- New upstream release

* Wed Nov 17 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.28-1
- New upstream release

* Wed Nov 17 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.22-1
- New upstream release

* Tue Nov  9 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.20-1
- New upstream release
- Add nm dispatcher
- Rework systemd scriptlets

* Tue Nov  2 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.20.08-1
- New upstream release

* Mon Nov  1 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.18.50-1
- New upstream release

* Sun Oct 24 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.18.42-1
- New upstream release

* Sat Jul 24 2010 Jochen Schmitt <Nochen herr-schmitt de> 2.18.36-2
- Fix broken inistscript
- Renaming service file in units subpackage

* Mon Jul 19 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.18.36-1
- New upstream release

* Sun Jul 18 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.18.34-3
- Fix typo

* Sun Jul 18 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.18.34-2
- Create seperate subpackages for sysv and systemd init
- Move inadyn-mt.conf to %%{_sysconfdir}
- Remove symlink from inadyn.conf to inadyn-mt.conf

* Tue May 18 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.18.24-1
- New upstream release

* Thu May 13 2010 Jochen Schmitt <JOchen herr-schmitt de> 2.18.18-1
- New upstream release

* Wed May 12 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.18.14-3
- Add patch for better handling of http_client_shutdown

* Tue May 11 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.18.14-2
- Suppress warnings of skipping /usr/lib libraries on x86_64 systems

* Sun Apr 25 2010 Jochen Schmitt <Jochen herr-schmitt de> 2.18.14-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 2.12.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 2.12.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 30 2008 Jochen Schmitt <Jochen herr-schmitt de> 2.12.24-1
- New upstream release

* Mon Jul 28 2008 Jochen Schmitt <Jochen herr-schmitt de> 2.12.22-2
- Add lang file
- Versioned Obsolete/Provide

* Sun Jul 27 2008 Jochen Schmitt <Jochen herr-schmitt de> 2.12.22-1
- New upstream release
- Add verbatin text of the license
- Change license to GPLv3

* Wed Jun 18 2008 Jochen Schmitt <Jochen herr-schmitt de> 2.12.18-1
- New upstream release

* Mon May 19 2008 Jochen Schmitt <Jochen herr-schmitt de> 2.12.01-1
- New upstream release

* Thu Apr 10 2008 Jochen Schmitt <Jochen herr-schmitt de> 2.11.96-1
- Inadyn-mt released as a succesor of inadyn

* Sun Feb 10 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.96.2-3
- Rebuild for gcc-4.3

* Wed Jan 23 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.96.2-2
- Rebuild
- Make initscript LSB-Compilant

* Sun Sep  2 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.96.2-1
- New upstream release (#270801)

* Wed Aug  8 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.96-4
- Changing license tag

* Sun Sep  3 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.96-3
- Rebuilt for FC-6

* Sun Feb 12 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.96-2
- Rebuilt for FC5

* Mon Oct 24 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.96-1
- New upstream relase

* Mon Aug 01 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.95-2
- Add suggested changes from Michael Schwendt

* Wed Jul 20 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.95-1
- New upstream release

* Tue May  3 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.90-11
- Move note from README.Fedora to %%description

* Tue May  3 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.90-9
- And special usage notes
- Use of /sbin/service to manage initscript in scriptlet
- Modify initscript, becouse bash don't return PID

* Thu Apr 28 2005 Jochen Schmitt <Jochen herr-schmitt.de> 1.90-8
- Replace ez_pid to ina_pid in initscript

* Wed Apr 27 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.90-7
- Enable status in initscript

* Wed Apr 27 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.90-6
- Add initscript

* Tue Apr 26 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.90-5
- Add URL to Source0

* Tue Apr 12 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.90-4
- Corrected use of percentage sign in changelog

* Mon Apr 11 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.90-3
- Some inprovements from Michael Schwendt

* Sun Apr 10 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.90-2
- Clearance in the %%Setup macro

* Thu Apr  7 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.90-1
- Initial RPM release
