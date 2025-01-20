%global quassel_data_dir    %{_var}/lib/quassel

Name:    quassel
Summary: A modern distributed IRC system
Version: 0.14.0
Release: 9%{?dist}

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License: GPL-2.0-only OR GPL-3.0-only
URL:     https://quassel-irc.org/
Source0: https://quassel-irc.org/pub/quassel-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: dbusmenu-qt5-devel
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-rpm-macros
BuildRequires: openssl-devel
BuildRequires: perl-generators
BuildRequires: phonon-qt5-devel
BuildRequires: qca-qt5-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtwebkit-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: openldap-devel
BuildRequires: boost-devel

BuildRequires: systemd
BuildRequires: systemd-rpm-macros

BuildRequires: libappstream-glib

Requires: oxygen-icon-theme

Provides: %{name}-gui = %{version}-%{release}

Requires: %{name}-common = %{version}-%{release}

# Systemd service file and configuration script.
Source1: quasselcore.service
Source2: quassel.conf
Source3: quassel.sysusers

%description
Quassel IRC is a modern, distributed IRC client,
meaning that one (or multiple) client(s) can attach
to and detach from a central core --
much like the popular combination of screen and a
text-based IRC client such as WeeChat, but graphical

%package common
Summary: Quassel common/shared files
# not strictly required, but helps this get pulled out when
# someone removes %%name or %%name-client
Requires: %{name}-gui = %{version}-%{release}
# put here for convenience, instead of all subpkgs which
# provide %%{name}-gui
BuildArch: noarch
%description common
%{summary}.

%package core
Summary: Quassel core component

# Weak dependency on qt5 postgresql bindings.
# We use a weak dependency here so they can be uninstalled if necessary.
Recommends: qt5-qtbase-postgresql

%description core
The Quassel IRC Core maintains a connection with the
server, and allows for multiple clients to connect

%package client
Summary: Quassel client
Provides: %{name}-gui = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
%description client
Quassel client


%prep
%autosetup -p0 -n %{name}-%{version}

%build
%cmake_kf5 \
  -DWANT_MONO=1 -DUSE_QT5=1 -DWITH_KDE=1 -DHAVE_SSL=1 -DENABLE_SHARED=OFF

%cmake_build

%install
%cmake_install

# unpackaged files
rm -f %{buildroot}/%{_datadir}/pixmaps/quassel.png

# Install quassel.conf for systemd file
install -Dp -m 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}.conf

# Install systemd service file
install -Dp -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/quasselcore.service

# Install the systemd-sysusers config
install -Dp -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf

# Home directory for quassel user
install -d -m 0750 %{buildroot}/%{quassel_data_dir}

# Install AppStream metadata
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
install -p -m 0644 data/*.appdata.xml %{buildroot}%{_datadir}/metainfo/

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

# Core pre/post macros.
%pre core
%sysusers_create_compat %{SOURCE3}

%post core
# Install quassel service.
%systemd_post quasselcore.service

%preun core
%systemd_preun quasselcore.service

%postun core
%systemd_postun_with_restart quasselcore.service

%files
%{_kf5_bindir}/quassel
%{_kf5_datadir}/applications/quassel.desktop
%{_datadir}/metainfo/quassel.appdata.xml

%files common
%doc README.md
%license COPYING gpl-2.0.txt gpl-3.0.txt
%{_kf5_datadir}/knotifications5/quassel.notifyrc
%{_kf5_datadir}/quassel/
%{_kf5_datadir}/icons/hicolor/*/*/*

%files core
%doc README.md
%license COPYING gpl-2.0.txt gpl-3.0.txt
%{_kf5_bindir}/quasselcore
%dir %attr(-,quassel,quassel) %{quassel_data_dir}
%{_unitdir}/quasselcore.service
%config(noreplace) %{_sysconfdir}/quassel.conf
%{_sysusersdir}/%{name}.conf

%files client
%{_kf5_bindir}/quasselclient
%{_kf5_datadir}/applications/quasselclient.desktop
%{_datadir}/metainfo/quasselclient.appdata.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.14.0-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 25 2022 Chris Egeland <phuzion@fedoraproject.org> - 0.14.0-1
- New upstream release (rhbz#1917071)

* Thu Feb 10 2022 Timothée Ravier <tim@siosm.fr> - 0.13.1-11
- Use systemd sysusers config to create user and group
- Use upstream AppStream metadata

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Chris Egeland <chris@chrisegeland.com> - 0.13.1-8
- Added security fix for CVE-2021-34825

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.13.1-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Jeff Law <law@redhat.com> - 0.13.1-6
- Fix missing #include for gcc-11

* Mon Jul 13 2020 Marie Loise Nolden <loise@kde.org> - 0.13.1-5
- Fix for Qt 5.14.2 from FreeBSD ports tree

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Ben Rosser <rosser.bjr@gmail.com> - 0.13.1-2
- Add a weak dep (Recommends) on qt5-qtbase-postgresql.

* Fri Feb 15 2019 Ben Rosser <rosser.bjr@gmail.com> - 0.13.1-1
- Updated to latest upstream release, 0.13.1 (rhbz#1677722).

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.13.0-1
- Updated to latest upstream release, 0.13.0.
- Add support for reloading quasselcore daemon via SIGHUP (#1380176).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.12.5-1
- Updated to latest upstream release (#1571443, #1573318, #1573319).

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Ben Rosser <rosser.bjr@gmail.com> - 0.12.4-4
- Remove quassel firewalld service file now that firewalld ships it.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep  9 2016 Ben Rosser <rosser.bjr@gmail.com> 0.12.4-2
- Include appstream metadata for client and monolithic client.

* Mon Apr 25 2016 Ben Rosser <rosser.bjr@gmail.com> 0.12.4-1
- Update to latest upstream quassel release

* Sat Apr 23 2016 Christian Dersch <lupinix@mailbox.org> - 0.12.3-6
- Enabled SSL support

* Sat Apr 23 2016 Christian Dersch <lupinix@mailbox.org> - 0.12.3-5
- migrated to Qt5
- modernized spec

* Mon Mar 21 2016 Ben Rosser <rosser.bjr@gmail.com> 0.12.3-4
- Use attr macro instead of chown to install quassel user homedir, that's much safer
- BuildRequires firewalld-filesystem, so the post script actually works, whoops

* Wed Mar 16 2016 Ben Rosser <rosser.bjr@gmail.com> 0.12.3-3
- Modify quassel configuration to listen on all IPv4 and IPv6 interfaces
- Added firewalld service for tcp/4242 to core

* Wed Feb 24 2016 Ben Rosser <rosser.bjr@gmail.com> 0.12.3-2
- Merged patch from John Villalovos to add a service file
- Added quassel user/group to -core subpackage
- Added configuration file and startup script to -core subpackage

* Tue Feb 09 2016 Ben Rosser <rosser.bjr@gmail.com> 0.12.3-1
- Update to latest upstream quassel release
- The CVE patch is not necessary for 0.12.3 or greater

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Christian Dersch <lupinix@mailbox.org> - 0.12.2-6
- Added security fix for CVE-2015-8547

* Thu Sep 24 2015 Adam Miller <maxamillion@fedoraproject.org> - 0.12.2-5
- Bump spec release because I typo'd and now it's in koji forever

* Thu Sep 24 2015 Adam Miller <maxamillion@fedoraproject.org> - 0.12.2-3
- Add oxygen-icon-theme requirement for BZ#1198788

* Wed Sep 16 2015 Richard Hughes <rhughes@redhat.com> - 0.12.2-2
- Remove the AppData file as the desktop file is no longer valid.

* Mon Aug 03 2015 Adam Miller <maxamillion@fedoraproject.org> - 0.12.2-1
- Update to latest upstream release.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.11.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.11.0-3
- Add an AppData file for the software center

* Tue Mar 24 2015 Adam Miller <maxamillion@fedoraproject.org> - 0.11.0-2
- BZ1205130 - patch for CTCP Denial of Service

* Wed Sep 24 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.11.0-1
- Update to latest upstream

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 09 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.10.0-1
- Update to latest upstream release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.9.2-1
- Update to latest upstream release

* Tue Oct 15 2013 Adam Miller <maxamillion@fedoraproject.org> - 0.9.1-1
- Update to latest upstream release
- Fix for CVE-2013-4422 (BZ#1017437)

* Tue Aug 27 2013 Adam Miller <maxamillion@fedoraproject.org> - 0.9.0-1
- Update to latest upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.8.0-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Steven M. Parrish <smparrish@gmail.com> - 0.8.0
- New release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Jaroslav Reznik <jreznik@redhat.com> - 0.7.3-1
- 0.7.3  (fixes - CVE-2011-3354 invalid CTCP handling causes DoS, rhbz#736868)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 7 2010 Steven M. Parrish <smparrish@gmail.com> - 0.7.1-1
- New ustream release

* Sat May 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.1-1
- quassel-0.6.1
- -common subpkg
- add minimal qt4/kdelibs4 deps

* Mon Feb 15 2010 Steven Parrish <smparrish@gmail.com> - 0.5.2-1
- New bugfix release

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.5.0-2
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Fri Oct 23 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.0-1
- Official 0.5.0 release

* Thu Sep 03 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5-0.1.rc1
- New release candidate

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.4.1-2
- cleanup dir ownership
- optimize scriptlets

* Fri Apr 24 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 0.4.1-1
- New upstream release

* Tue Apr 14 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 0.4.0-2
- Enabled KDE integration

* Fri Feb 20 2009 Steven M. Parirsh <tuxbrewr@fedoraproject.org> 0.4.0-1
- New upstream release

* Mon Dec 29 2008 Steven M. Parrish <tuxbrewr@fedoraproject.org> 0.3.1-2
- Fix bug #477850

* Fri Nov 28 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.3.1-1
- New upstream release

* Wed Nov 12 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.3.0.3-1
- New upstream release fixes a security issue with CTCP handling in 
- Quassel Core, that could potentially be exploited to send 
- arbitrary IRC commands on your behalf.

* Tue Sep 16 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.3.0.1-1
- New upstream release

* Fri Jul 04 2008 Steven Parrish <smparrish@shallowcreek.net> 0.1.rc1
- New upstream release.  Now uses cmake instead of qmake

* Wed Jul 02 2008 Steven Parrish <smparrish@shallowcreek.net> - 0.3.beta1
- Final spec for initial release to F9 and rawhide

* Tue Jun 24 2008 Steven Parrish <smparrish[at]shallowcreek.net>
- Revised spec file based on comments from package reviewer. 

* Mon Jun 23 2008 Steven Parrish <smparrish[at]shallowcreek.net>
- initial RPM
