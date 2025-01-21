%define __cmake_in_source_build 1

%define main_version 24.02
%define async_version 1.7.0
%define echolib_version 1.3.4
%define qtel_version 1.2.5
%define server_version 1.8.0
%define reflector_version 1.2.0

Name:		svxlink
Epoch:		2
Version:	%{main_version}
Release:	4%{?dist}
Summary:	Repeater controller and EchoLink (simplex or repeater)

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.svxlink.org
Source0:	https://github.com/sm0svx/svxlink/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/sm0svx/svxlink-sounds-en_US-heather/releases/download/%{version}/svxlink-sounds-en_US-heather-16k-%{version}.tar.bz2

Source4:	%{name}-tmpfs.conf

BuildRequires:	make
BuildRequires:	cmake libsigc++-devel libsigc++20-devel qt-devel
BuildRequires:	speex-devel opus-devel popt-devel libgcrypt-devel tcl-devel
BuildRequires:	gsm-devel doxygen tk-devel desktop-file-utils alsa-lib-devel
BuildRequires:	systemd-units rtl-sdr-devel chrpath
BuildRequires:	jsoncpp-devel libcurl-devel

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
The SvxLink project is a multi purpose voice services system for
ham radio use. For example, EchoLink connections are supported.
Also, the SvxLink server can act as a repeater controller.

%package -n libasync
Summary: Svxlink async libs
Epoch: 2
Version: %{async_version}

%description -n libasync
The Async library is a programming framework that is used to write event driven
applications. It provides abstractions for file descriptor watches, timers,
network communications, serial port communications and config file reading.

Async is written in such a way that it can support other frameworks. Right now
there are two basic frameworks, a simple "select" based implementation and a Qt
implementation. The idea is that advanced libraries can be implemented in such
a way that they only depend on Async. That means that these libraries can be
used in both Qt and pure console applications and in any future frameworks
supported by Async (e.g. Gtk, wxWidgets etc).

Another big part of Async is the audio pipe framework. It is an audio handling
framework that is geared towards single channel (mono) audio applications. The
framework consists of a large number of audio handling classes such as
audio i/o, filtering, mixing, audio codecs etc.

%package -n libasync-devel
Summary: Svxlink async development files
Epoch: 2
Version: %{async_version}
Requires: libasync = %{epoch}:%{async_version}
Obsoletes:	svxlink-server-devel < 0.11.1-2

%description -n libasync-devel
The async library development files

%package -n libasync-doc
Summary: Svxlink async documentation files
Epoch: 2
Version: %{async_version}
Requires: libasync = %{epoch}:%{async_version}

%description -n libasync-doc
The async library documentation files in HTML format

%package -n echolib
Summary: EchoLink communications library
Epoch: 2
Version: %{echolib_version}

%description -n echolib
EchoLib is a library that is used as a base for writing EchoLink applications.
It implements the directory server protocol as well as the station to station
protocol. EchoLink is used to link ham radio stations together over the
Internet.

%package -n echolib-devel
Summary: Development files for the EchoLink communications library
Epoch: 2
Version: %{echolib_version}
Requires: echolib = %{epoch}:%{echolib_version}
Obsoletes:	svxlink-server-devel < 0.11.1-2

%description -n echolib-devel
Development files for the EchoLink communications library

%package -n echolib-doc
Summary: Documentation files for the EchoLink communications library
Epoch: 2
Version: %{echolib_version}
Requires: echolib = %{epoch}:%{echolib_version}

%description -n echolib-doc
Documentation files for the EchoLink communications library in HTML format

%package -n qtel
Summary: The Qt EchoLink Client
Epoch: 1
Version: %{qtel_version}
Requires: hicolor-icon-theme

%description -n qtel
This package contains Qtel, the Qt EchoLink client. It is an implementation of
the EchoLink software in Qt. This is only an EchoLink client, that is it can
not be connected to a transceiver to create a link. If it is a pure link node
you want, install the svxlink-server package.

%package -n svxlink-server
Summary: SvxLink - A general purpose voice services system
Epoch: 1
Version: %{server_version}
Requires: udev
Requires (pre): shadow-utils

%description -n svxlink-server
The SvxLink server is a general purpose voice services system for ham radio
use. Each voice service is implemented as a plugin called a module.
Some examples of voice services are: Help system, Simplex repeater,
EchoLink communications and voice mail.

The core of the system handle the radio interface and is quite flexible
as well. It can act both as a simplex node and as a repeater controller. It is
also possible to link multiple receivers in via TCP/IP. The best receiver is
chosen using a software voter.

%package -n svxlink-reflector
Summary: An audio reflector for connecting SvxLink Servers
Epoch: 1
Version: %{reflector_version}

%description -n svxlink-reflector
The SvxReflector application is meant to be used as a center point
to link SvxLink nodes together. The new SvxLink ReflectorLogic logic core is
used to connect a SvxLink node to the reflector server. One or more logics can
then be connected to the reflector using normal logic linking.

%prep
%setup -q -n %{name}-%{main_version}
%setup -q -D -T -a 1 -n %{name}-%{main_version}

%build
%cmake -DLOCAL_STATE_DIR=%{_localstatedir} -DWITH_SYSTEMD=1 \
	-DSYSTEMD_CONFIGURATIONS_FILES_DIR=%{_unitdir} \
	-DSYSTEMD_DEFAULTS_FILES_DIR=%{_sysconfdir}/sysconfig src
make %{?_smp_mflags} all doc
doxygen doc/doxygen.async
doxygen doc/doxygen.echolib


%install
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_datadir}/svxlink
cp -a en_US-heather-16k %{buildroot}%{_datadir}/svxlink/sounds/en_US
mkdir -p %{buildroot}%{_localstatedir}/log
mkdir -p %{buildroot}%{_localstatedir}/spool/svxlink/{propagation_monitor,qso_recorder,voice_mail}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_sysconfdir}/security/console.perms.d
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}
install -p -m 755 bin/devcal %{buildroot}%{_bindir}
chrpath --delete %{buildroot}%{_bindir}/devcal
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -p -m 0644 %{SOURCE4} %{buildroot}/%{_tmpfilesdir}/%{name}.conf
touch %{buildroot}%{_localstatedir}/log/svxlink
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications src/qtel/qtel.desktop
cp distributions/fedora/%{_sysconfdir}/logrotate.d/svxlink %{buildroot}%{_sysconfdir}/logrotate.d/svxlink-server
cp distributions/fedora/%{_sysconfdir}/logrotate.d/remotetrx %{buildroot}%{_sysconfdir}/logrotate.d
#don't pack htmlized man files
#seems to confuse cmake rules and doesn't make much
#sense to pack man files in html format
rm %{buildroot}%{_docdir}/svxlink/man1/*html*
rm %{buildroot}%{_docdir}/svxlink/man5/*html*

# Remove static linked files
find %{buildroot} -name '*.a' -exec rm -f {} ';'

sed -i -e "s@EnvironmentFile=/etc/default@EnvironmentFile=/etc/sysconfig@g" %{buildroot}%{_unitdir}/*.service

%ldconfig_scriptlets -n libasync

%ldconfig_scriptlets -n echolib


%pre -n svxlink-server
getent group daemon >/dev/null || groupadd -r daemon
getent passwd svxlink >/dev/null || \
useradd -r -g daemon -d / -s /sbin/nologin \
-c "SvxLink Daemon " svxlink
/usr/sbin/usermod -a -G audio,dialout svxlink >/dev/null 2>&1 || :
exit 0

%pre -n svxlink-reflector
getent group daemon >/dev/null || groupadd -r daemon
getent passwd svxlink >/dev/null || \
useradd -r -g daemon -d / -s /sbin/nologin \
-c "SvxLink Daemon " svxlink
/usr/sbin/usermod -a -G audio,dialout svxlink >/dev/null 2>&1 || :
exit 0

%post -n svxlink-server
%systemd_post svxlink.service
%systemd_post remotetrx.service

%preun -n svxlink-server
%systemd_preun svxlink.service
%systemd_preun remotetrx.service

%postun -n svxlink-server
%systemd_postun_with_restart svxlink.service
%systemd_postun_with_restart remotetrx.service

%triggerun -- svxlink < 2:14.08.1-1
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply svxlink
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save svxlink >/dev/null 2>&1 ||:
/usr/bin/systemd-sysv-convert --save remotetrx >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del svxlink >/dev/null 2>&1 || :
/sbin/chkconfig --del remotetrx >/dev/null 2>&1 || :
/bin/systemctl try-restart svxlink.service >/dev/null 2>&1 || :
/bin/systemctl try-restart remotetrx.service >/dev/null 2>&1 || :

%files -n libasync
%doc COPYRIGHT src/async/ChangeLog
%defattr(755,root,root)
%{_libdir}/libasync*.so.*

%files -n libasync-devel
%{_libdir}/libasyncaudio.so
%{_libdir}/libasynccore.so
%{_libdir}/libasynccpp.so
%{_libdir}/libasyncqt.so
%dir %{_includedir}/svxlink
%{_includedir}/svxlink/common.h
%{_includedir}/svxlink/Async*
%{_includedir}/svxlink/CppStdCompat.h

%files -n libasync-doc
%doc %{_pkgdocdir}/async/*

%files -n echolib
%doc COPYRIGHT src/echolib/ChangeLog
%defattr(755,root,root)
%{_libdir}/libecholib*.so.*

%files -n echolib-devel
%{_libdir}/libecholib.so
%dir %{_includedir}/svxlink
%{_includedir}/svxlink/EchoLink*

%files -n echolib-doc
%doc %{_pkgdocdir}/echolib/*

%files -n qtel
%doc COPYRIGHT src/qtel/ChangeLog
%{_bindir}/qtel
%{_datadir}/qtel
%{_datadir}/icons/hicolor/128x128/apps/qtel.png
%{_datadir}/applications/qtel.desktop
%{_metainfodir}/org.svxlink.Qtel.metainfo.xml
%{_mandir}/man*/qtel*

%files -n svxlink-server
%doc COPYRIGHT src/svxlink/ChangeLog
%{_bindir}/devcal
%{_bindir}/svxlink
%{_sbindir}/svxlink_gpio_up
%{_sbindir}/svxlink_gpio_down
%{_bindir}/remotetrx
%{_bindir}/siglevdetcal
%{_unitdir}/svxlink.service
%{_unitdir}/svxlink_gpio_setup.service
%{_unitdir}/remotetrx.service

%dir %{_libdir}/svxlink
%dir /run/%{name}
%{_tmpfilesdir}/svxlink.conf
%{_libdir}/svxlink/Module*.so
%{_libdir}/svxlink/*Logic.so
%dir %{_sysconfdir}/%{name}/svxlink.d
%{_datadir}/svxlink
%defattr(644,root,root)
%config(noreplace) %{_sysconfdir}/sysconfig/svxlink
%config(noreplace) %{_sysconfdir}/sysconfig/remotetrx
%config(noreplace) %{_sysconfdir}/%{name}/svxlink.conf
%config(noreplace) %{_sysconfdir}/%{name}/gpio.conf
%config(noreplace) %{_sysconfdir}/%{name}/node_info.json
%config(noreplace) %{_sysconfdir}/%{name}/.procmailrc
%config(noreplace) %{_sysconfdir}/%{name}/svxlink.d/*
%config(noreplace) %{_sysconfdir}/%{name}/TclVoiceMail.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/svxlink-server
%config(noreplace) %{_sysconfdir}/logrotate.d/remotetrx
%config(noreplace) %{_sysconfdir}/%{name}/remotetrx.conf
%{_mandir}/man1/devcal.*.*
%{_mandir}/man1/svxlink.*.*
%{_mandir}/man1/remotetrx.*.*
%{_mandir}/man1/siglevdetcal.*.*
%{_mandir}/man5/*
%attr(755,svxlink,daemon) %dir %{_localstatedir}/spool/svxlink
%attr(755,svxlink,daemon) %dir %{_localstatedir}/spool/svxlink/propagation_monitor
%attr(755,svxlink,daemon) %dir %{_localstatedir}/spool/svxlink/qso_recorder
%attr(755,svxlink,daemon) %dir %{_localstatedir}/spool/svxlink/voice_mail
%ghost %{_localstatedir}/log/svxlink

%files -n svxlink-reflector
%{_bindir}/svxreflector
%{_bindir}/svxreflector-status
%config(noreplace) %{_sysconfdir}/sysconfig/svxreflector
%config(noreplace) %{_sysconfdir}/%{name}/svxreflector.conf
%{_mandir}/man1/svxreflector.*
%{_mandir}/man5/svxreflector.*
%{_unitdir}/svxreflector.service

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:24.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1:1.2.0-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:24.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 06 2024 Scott K Logan <logans@cottsay.net> - 2:24.02-1
- Update to 24.02 (rhbz#2265946) (rhbz#2218712)

* Tue Apr 09 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2:17.12.2-17
- Rebuilt for new rtl-sdr

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2:17.12.2-10
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 22 2020 Jeff Law <law@redhat.com> - 2:17.12.2-8
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Lucian Langa <lucilanga@gnome.eu.org> - 2:17.12.2-1
- new app svnreflector
- drop systemd units in favor of vendor supplied ones
- update main url
- new upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:15.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:15.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:15.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:15.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Lucian Langa <lucilanga@gnome.eu.org> - 2:15.11-1
- install new binaries
- fix /run directory issues (#1270879)
- bring back smp builds
- update to latest upstream

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:14.08.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 27 2015 Lucian Langa <lucilanga@gnome.eu.org> - 2:14.08.1-3
- fix installed tmpfsfile (#1266511)

* Thu Aug 20 2015 Lucian Langa <lucilanga@gnome.eu.org> - 2:14.08.1-2
- fix permmissions under spool dir
- update license

* Wed Aug 05 2015 Lucian Langa <lucilanga@gnome.eu.org> - 2:14.08.1-1
- disable parallel builds
- add tmpdir configs
- fix audio clips loading location
- drop security/udev files - prefer group approach
- migrate to systemd
- cleanup specfile
- update BR
- sync with latest upstream

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:11.11.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2:11.11.1-15
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:11.11.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:11.11.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2:11.11.1-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Thu Apr 24 2014 Tomáš Mráz <tmraz@redhat.com> - 2:11.11.1-11
- Rebuild for new libgcrypt

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:11.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jan 26 2013 Lucian Langa <cooly@gnome.eu.org> - 2:11.11.1-9
- upload missing patch

* Sat Jan 26 2013 Lucian Langa <cooly@gnome.eu.org> - 2:11.11.1-8
- fix FTBFS (#904327)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:11.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:11.11.1-6
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:11.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Lucian Langa <cooly@gnome.eu.org> - 2:11.11.1-4
- try to fix epoch in subpackages

* Tue Dec 20 2011 Lucian Langa <cooly@gnome.eu.org> - 2:11.11.1-3
- fix nvr for subpackages too

* Thu Dec 08 2011 Lucian Langa <cooly@gnome.eu.org> - 1:11.11.1-2
- bump nvr to allow full build

* Wed Dec 07 2011 Lucian Langa <cooly@gnome.eu.org> - 11.11.1-1
- new upstream release

* Mon Nov 21 2011 Lucian Langa <cooly@gnome.eu.org> - 11.11-1
- update versions
- update BR
- drop all patches - fixed upstream
- new upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 090426-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Lucian Langa <cooly@gnome.eu.org> - 090426-5
- add COPYRIGHT license file

* Sun Feb 14 2010 Lucian Langa <cooly@gnome.eu.org> - 090426-4
- -fix implicit dso linking (#564753)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 090426-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Lucian Langa <cooly@gnome.eu.org> - 090426-2
- obsolete package svxlink-server-devel

* Tue Apr 28 2009 Lucian Langa <cooly@gnome.eu.org> - 090426-1
- update BR
- drop svxlink-devel package
- updated descriptions
- remove dtmf_plot
- drop patch0,1,2,3 as were fixed upstream
- new upstream release

* Thu Feb 26 2009 Lucian Langa <cooly@gnome.eu.org> - 080730-8
- patch to fix gcc44 issues

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 080730-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 07 2008 Lucian Langa <cooly@gnome.eu.org> - 080730-6
- added udev dependency
- fixed libs permissions
- update scriptlets

* Sat Dec 06 2008 Lucian Langa <cooly@gnome.eu.org> - 080730-5
- license update

* Wed Dec 03 2008 Lucian Langa <cooly@gnome.eu.org> - 080730-4
- fix duplicated files
- remove static libraries

* Fri Nov 21 2008 Lucian Langa <cooly@gnome.eu.org> - 080730-3
- added fedora optflags
- fix unowned dirs
- spandsp 0.5 patch
- update BR

* Thu Aug 21 2008 Lucian Langa <cooly@gnome.eu.org> - 080730-2
- mangle svxlink conf to include correct libdir
- misc -devel clean

* Sun Aug 10 2008 Lucian Langa <cooly@gnome.eu.org> - 080730-1
- Initial spec (parts of it imported from upstream spec)


