# FIXME: most tests currently fail
%bcond_with tests

%global glib2_version	%(pkg-config --modversion glib-2.0 2>/dev/null || echo "2.44")
%global giturl		https://github.com/CanonicalLtd/lightdm

Name:		lightdm
Summary:	A cross-desktop Display Manager
Version:	1.32.0
Release:	13%{?dist}

# library/bindings are LGPLv2 or LGPLv3, the rest GPLv3+
# Automatically converted from old format: (LGPLv2 or LGPLv3) and GPLv3+ - review is highly recommended.
License:	(LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only) AND GPL-3.0-or-later
URL:		https://www.freedesktop.org/wiki/Software/LightDM/
Source0:	%{giturl}/archive/%{version}/lightdm-%{version}.tar.gz

Source10:	lightdm.pam
Source11:	lightdm-autologin.pam
Source12:	lightdm-tmpfiles.conf
Source13:	lightdm.service
Source14:	lightdm.logrotate
Source15:	lightdm.rules
Source16:	lightdm.sysusers


# .conf snippets
Source20:	50-backup-logs.conf
Source21:	50-minimum-vt.conf
Source22:	50-session-wrapper.conf
Source23:	50-user-authority-in-system-dir.conf
Source24:	50-xserver-command.conf
Source25:	50-disable-guest.conf
Source26:	50-run-directory.conf

Patch0:		gcc-10.patch
Patch1:     remove_bin_path.patch

# Upstreamed:
Patch2:		%{giturl}/pull/5.patch#/lightdm-1.25.1-disable_dmrc.patch

# Upstream commits

BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	gtk-doc itstool
BuildRequires:	intltool
BuildRequires:	libgcrypt-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(audit)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0) >= 2.26
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	pkgconfig(Qt5Core) pkgconfig(Qt5DBus) pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xdmcp)
BuildRequires:	systemd-rpm-macros
BuildRequires:	vala

Requires:	%{name}-gobject%{?_isa} = %{version}-%{release}
Requires:	accountsservice
Requires:	dbus
Requires:	polkit-js-engine
Requires:	/sbin/nologin
Requires:	systemd
Requires:	xorg-x11-server-Xorg
Requires:	xorg-x11-xinit
Requires:   lightdm-greeter = 1.2
Suggests:   slick-greeter
%{?systemd_requires}
%{?sysusers_requires_compat}

Obsoletes: lightdm-qt < %{version}-%{release}
Obsoletes: lightdm-qt-devel < %{version}-%{release}

Requires(post):	psmisc dbus-daemon

# needed for anaconda to boot into runlevel 5 after install
Provides:	service(graphical-login) = lightdm

%description
Lightdm is a display manager that:
* Is cross-desktop - supports different desktops
* Supports different display technologies
* Is lightweight - low memory usage and fast performance


%package gobject
Summary:	LightDM GObject client library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	glib2%{?_isa} >= %{glib2_version}
%description gobject
This package contains a GObject based library for LightDM clients to use to
interface with LightDM.


%package gobject-devel
Summary:	Development files for %{name}-gobject
Requires:	%{name}-gobject%{?_isa} = %{version}-%{release}
%description gobject-devel
%{summary}.


%package qt5
Summary:	LightDM Qt5 client library
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description qt5
This package contains a Qt5-based library for LightDM clients to use to interface
with LightDM.


%package qt5-devel
Summary:	Development files for %{name}-qt5
Requires:	%{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.


%prep
%autosetup -p 1


%build
# Make libtoolize happy.
%{__cat} %{_datadir}/aclocal/intltool.m4 > aclocal.m4
# Bootstrap
NOCONFIGURE=1 ./autogen.sh

%configure                      \
	--disable-dmrc              \
	--disable-silent-rules      \
	--disable-static			\
	--enable-gtk-doc			\
	--enable-libaudit			\
	--enable-liblightdm-qt5     \
	--enable-introspection      \
%if %{with tests}
	--enable-tests				\
%else
	--disable-tests				\
%endif
	--enable-vala				\
	--with-greeter-user=lightdm \
	--with-greeter-session=lightdm-greeter

%make_build


%install
%make_install

# We need to own these
%{__mkdir_p} %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/		\
		%{buildroot}%{_datadir}/dbus-1/interfaces		\
		%{buildroot}%{_datadir}/dbus-1/system.d			\
		%{buildroot}%{_datadir}/lightdm/lightdm.conf.d/		\
		%{buildroot}%{_datadir}/lightdm/remote-sessions/	\
		%{buildroot}%{_datadir}/xgreeters/			\
		%{buildroot}%{_localstatedir}/cache/lightdm/		\
		%{buildroot}%{_rundir}/lightdm/		\
		%{buildroot}%{_localstatedir}/log/lightdm/		\
		%{buildroot}%{_localstatedir}/lib/lightdm/		\
		%{buildroot}%{_localstatedir}/lib/lightdm-data/

# libtool cruft
rm -fv %{buildroot}%{_libdir}/lib*.la

# We don't ship AppAmor
%{__rm} -rfv %{buildroot}%{_sysconfdir}/apparmor.d/

# omit upstart support
%{__rm} -rfv %{buildroot}%{_sysconfdir}/init

# install pam file
%{__install} -Dpm 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/lightdm
%{__install} -Dpm 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/pam.d/lightdm-autologin
%{__install} -Dpm 0644 %{SOURCE12} %{buildroot}%{_prefix}/lib/tmpfiles.d/lightdm.conf
%{__install} -Dpm 0644 %{SOURCE13} %{buildroot}%{_unitdir}/lightdm.service
%{__install} -Dpm 0644 %{SOURCE14} %{buildroot}%{_sysconfdir}/logrotate.d/lightdm
%{__install} -Dpm 0644 %{SOURCE15} %{buildroot}%{_datadir}/polkit-1/rules.d/lightdm.rules
%{__install} -Dpm 0644 %{SOURCE16} %{buildroot}%{_sysusersdir}/lightdm.conf
%{__install} -pm 0644 %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23}	\
	%{SOURCE24} %{SOURCE25} %{SOURCE26} %{buildroot}%{_datadir}/lightdm/lightdm.conf.d/


%find_lang lightdm --with-gnome


%if %{with tests}
%check
%make_build check ||:
%endif


%pre
%sysusers_create_compat %{SOURCE16}

%post
# todo: document need/purpose for this snippet
if [ $1 = 1 ] ; then
	%{_bindir}/killall -HUP dbus-daemon 2>&1 > /dev/null
fi
%{?systemd_post:%systemd_post lightdm.service}

%preun
%{?systemd_preun:%systemd_preun lightdm.service}

%postun
%{?systemd_postun}

%files -f lightdm.lang
%license COPYING.GPL3
%doc NEWS
%dir %{_sysconfdir}/lightdm/
%dir %{_sysconfdir}/lightdm/lightdm.conf.d
%config(noreplace) %{_sysconfdir}/pam.d/lightdm*
%config(noreplace) %{_sysconfdir}/lightdm/keys.conf
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf
%config(noreplace) %{_sysconfdir}/lightdm/users.conf
%dir %{_sysconfdir}/logrotate.d/
%{_sysconfdir}/logrotate.d/lightdm
%dir %attr(-,lightdm,lightdm) %{_localstatedir}/cache/lightdm/
%dir %attr(-,lightdm,lightdm) %{_localstatedir}/lib/lightdm/
%dir %attr(-,lightdm,lightdm) %{_localstatedir}/lib/lightdm-data/
%dir %attr(-,lightdm,lightdm) %{_localstatedir}/log/lightdm/
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%dir %{_datadir}/xgreeters/
%ghost %dir %{_rundir}/lightdm
%{_bindir}/dm-tool
%{_sbindir}/lightdm
%{_libexecdir}/lightdm-guest-session
%{_datadir}/lightdm/
%{_libdir}/girepository-1.0/LightDM-1.typelib
%{_mandir}/man1/dm-tool.1*
%{_mandir}/man1/lightdm*
%{_sysusersdir}/lightdm.conf
%{_unitdir}/lightdm.service
%{_datadir}/accountsservice
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/polkit-1/rules.d/lightdm.rules
%{_datadir}/polkit-1/actions/org.freedesktop.DisplayManager.AccountsService.policy
%{_datadir}/bash-completion/completions/dm-tool
%{_datadir}/bash-completion/completions/lightdm
%{_prefix}/lib/tmpfiles.d/lightdm.conf

%ldconfig_scriptlets gobject

%files gobject
%license COPYING.LGPL2 COPYING.LGPL3
%{_libdir}/liblightdm-gobject-1.so.0*

%files gobject-devel
%doc %{_datadir}/gtk-doc/html/lightdm-gobject-1/
%{_includedir}/lightdm-gobject-1/
%{_libdir}/liblightdm-gobject-1.so
%{_libdir}/pkgconfig/liblightdm-gobject-1.pc
%{_datadir}/gir-1.0/LightDM-1.gir
%{_datadir}/vala/vapi/liblightdm-gobject-1.*

%ldconfig_scriptlets qt5

%files qt5
%license COPYING.LGPL2 COPYING.LGPL3
%{_libdir}/liblightdm-qt5-3.so.0*

%files qt5-devel
%{_includedir}/lightdm-qt5-3/
%{_libdir}/liblightdm-qt5-3.so
%{_libdir}/pkgconfig/liblightdm-qt5-3.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.32.0-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 18 2024 Leigh Scott <leigh123linux@gmail.com> - 1.32.0-10
- Add requires xorg-x11-server-Xorg rhbz#2281416

* Fri Jan 26 2024 Christoph Junghans <junghans@votca.org> - 1.32.0-9
- Fix start order with systemd-hostnamed.service in lightdm.service (bug #2167386)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Leigh Scott <leigh123linux@gmail.com> - 1.32.0-6
- Add suggests slick-greeter (rhbz#2208097)
- Remove /bin path from env (rhbz#2257618)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 25 2023 Leigh Scott <leigh123linux@gmail.com> - 1.32.0-4
- Use systemd sysusers config to create user and group

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Leigh Scott <leigh123linux@gmail.com> - 1.32.0-1
- lightdm-1.32.0

* Fri Jun 10 2022 Dan Horák <dan[at]danny.cz> - 1.30.0-18
- Enable all arches in EPEL

* Sun Jun 05 2022 Leigh Scott <leigh123linux@gmail.com> - 1.30.0-17
- Fix xauthority corruption (rhbz#2093668)
- Add missing requires for post scriptlet (rhbz#2093698)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.30.0-13
- disable qt4 support on f34+

* Tue Dec 22 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.30.0-12
- adjust dbus runtime dep:  -dbus-x11 +dbus (since fedora switched to dbus-broker)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Leigh Scott <leigh123linux@gmail.com> - 1.30.0-10
- Remove pam_console dependency (rhbz#1822212)

* Wed Apr 08 2020 Leigh Scott <leigh123linux@gmail.com> - 1.30.0-9
- Revert 'Add conf to remove useless wayland sessions'

* Thu Jan 30 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.30.0-8
- Suppress s390x gcc-10 build issue

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.30.0-6
- Tweak the boolean requires

* Sat Jan 18 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.30.0-5
- Revert last commit and use boolean requires instead

* Sat Jan 18 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.30.0-4
- Remove requires lightdm-greeter as it adds unacceptable deps to devel package

* Mon Oct 21 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.30.0-3
- Switch from /var/run to /run directory

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.30.0-1
- lightdm-1.30.0

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 1.28.0-7
- Update BRs for vala packaging changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 12 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-5
- limit memlock in systemd unit
- fix https://bugzilla.redhat.com/show_bug.cgi?id=1662857

* Mon Dec 31 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.28.0-4
- rebuilt

* Thu Nov 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.28.0-3
- Add conf to remove useless wayland sessions

* Wed Sep 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.28.0-2
- revert over-aggressive use of %%name macro
- lightdm.pam: move 'session...system-auth' before gnome_keyring/kwallet (#1581495,#1631220)

* Sat Sep 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.28.0-1
- lightdm-1.28.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.26.0-1
- lightdm-1.26.0
- Add upstream commits, maybe fix rhbz#1581495

* Fri Feb 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.25.2-1
- lightdm-1.25.2
- Fix scriptlets
- Drop upstream patches

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Björn Esser <besser82@fedoraproject.org> - 1.25.1-5
- Fix ownership of %%{_datadir}/accountsservice

* Fri Jan 19 2018 Björn Esser <besser82@fedoraproject.org> - 1.25.1-4
- Move DBus interfaces to proper location and create symlinks

* Fri Jan 19 2018 Björn Esser <besser82@fedoraproject.org> - 1.25.1-3
- Move DBus config to proper location

* Fri Jan 19 2018 Björn Esser <besser82@fedoraproject.org> - 1.25.1-2
- Fix claiming DBus service name (rhbz#1428379)

* Thu Jan 18 2018 Björn Esser <besser82@fedoraproject.org> - 1.25.1-1
- lightdm-1.25.1 (rhbz#1535730)

* Mon Nov 27 2017 Björn Esser <besser82@fedoraproject.org> - 1.25.0-1
- lightdm-1.25.0
- Enable smooth transition from plymouth to the greeter
- Enable coredumps from Xserver
- Change source url to github
- Explicitly require a greeter
- Enable explicit internal Requires

* Tue Sep 05 2017 Björn Esser <besser82@fedoraproject.org> - 1.18.3-5
- Disable guest login as system default preset (CVE-2017-8900)

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.18.3-4
- Start lightdm after dbus.service

* Sat Apr 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.18.3-3
- own %%{_datadir}/xgreeters

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.18.3-1
- lightdm-1.18.3

* Thu Jul 07 2016 Rex Dieter <rdieter@fedoraproject.org> 1.18.2-1
- lightdm-1.18.2

* Mon Apr 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.18.1-1
- lightdm-1.18.1

* Sat Apr 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.18.0-1
- lightdm-1.18.0 (#1321032)
- use lightdm.conf.d/ snippets for default configuration (instead of patching) (#1096216)

* Sat Apr 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.10.6-4
- Error connecting to XServer via ipv6 (1322775)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.10.6-2
- enable libaudit support
- (re)enable hardening for f23+, at least (#956868)
- disable tests
- drop now-unused lightdm.pam.f19

* Fri Nov 20 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.6-1
- 1.10.6

* Mon Oct 12 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.5-7
- use upstream listen.patch instead

* Tue Oct 06 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.5-6
- drop listen.patch for < f22 (#1269247)

* Thu Sep 24 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.5-5
- update Summary/%%description

* Thu Sep 10 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.5-4
- lightdm.pam: add pam_kwallet5 support

* Tue Sep 08 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.5-3
- rework -qtchooser.patch to avoid autoreconf'ing (fixes epel7 build)

* Fri Aug 28 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.5-2
- Lightdm runs without -nolisten but X not listening (#12255743)

* Mon Aug 17 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.5-1
- 1.10.5, add liblightdm-qt5 support

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.10.4-7
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 15 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.4-6
- -gobject: add versioned Requires: glib2 dep

* Tue Feb 24 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.4-5
- try harder to disable hardening

* Sun Feb 22 2015 Rex Dieter <rdieter@fedoraproject.org> 1.10.4-3
- explicitly disable hardening (#956868)

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.10.4-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Thu Nov 13 2014 Rex Dieter <rdieter@fedoraproject.org> 1.10.4-1
- lightdm-1.10.4, update URL to 1.10-specific branch

* Thu Oct 09 2014 Rex Dieter <rdieter@fedoraproject.org> 1.10.3-1
- lightdm-1.10.3

* Mon Oct 06 2014 Rex Dieter <rdieter@fedoraproject.org> 1.10.2-2
- respin/fix fedora_config.patch (properly use [SeatDefaults] section)

* Wed Sep 17 2014 Rex Dieter <rdieter@fedoraproject.org> 1.10.2-1
- lightdm-1.10.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.10.1-4
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 Rex Dieter <rdieter@fedoraproject.org> 1.10.1-2
- update pam config (+pam-kwallet,-mate-keying-pam)

* Sun Apr 27 2014 Rex Dieter <rdieter@fedoraproject.org> 1.10.1-1
- lightdm-1.10.1

* Thu Apr 17 2014 Rex Dieter <rdieter@fedoraproject.org> 1.10.0-1
- lightdm-1.10.0 (#1077562)

* Thu Mar 27 2014 Rex Dieter <rdieter@fedoraproject.org> 1.9.13-2
- Could not create user data directory /var/lib/lightdm-data/lightdm (#1081426)

* Tue Mar 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.9.13-1
- lightdm-1.9.13

* Thu Mar 13 2014 Rex Dieter <rdieter@fedoraproject.org> 1.9.11-1
- lightdm-1.9.11

* Tue Mar 11 2014 Rex Dieter <rdieter@fedoraproject.org> 1.9.9-1
- lightdm-1.9.9

* Thu Feb 20 2014 Rex Dieter <rdieter@fedoraproject.org> 1.9.8-1
- lightdm-1.9.8 (#1021834)
- lightdm adds /usr/libexec/lightdm: to user $PATH (#888337)

* Thu Feb 06 2014 Rex Dieter <rdieter@fedoraproject.org> 1.8.7-1
- lightdm-1.8.7

* Wed Jan 22 2014 Rex Dieter <rdieter@fedoraproject.org> 1.8.6-1
- lightdm-1.8.6

* Fri Nov 15 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.5-2
- create/own lightdm.conf.d dirs

* Fri Nov 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.5-1
- lightdm-1.8.5

* Fri Nov 01 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.4-1
- lightdm-1.8.4

* Wed Oct 30 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.3-1
- lightdm-1.8.3

* Wed Oct 16 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.2-1
- lightdm-1.8.2

* Thu Oct 10 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.1-1
- lightdm-1.8.1

* Wed Oct 09 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.0-2
- lightdm has no service file (#1017390)

* Wed Oct 09 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.0-1
- lightdm-1.8.0 (#1017081)

* Tue Oct 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.7.18-2
- systemd support no longer conditional/optional
- lightdm user home /var/lib/lightdm (instead of /var/log/lightdm)

* Mon Oct 07 2013 Rex Dieter <rdieter@fedoraproject.org> 1.7.18-1
- lightdm-1.7.18 (#1016230)

* Sat Oct 05 2013 Rex Dieter <rdieter@fedoraproject.org> 1.7.17-2
- lightdm does not maintain login history using /var/log/wtmp (#1014285)
- Lightdm leaks 6 FDs (#973584)

* Tue Sep 24 2013 Rex Dieter <rdieter@fedoraproject.org> 1.7.17-1
- lightdm-1.7.17

* Sat Sep 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.7.16-1
- lightdm-1.7.16 (#1010183)
- add %%check (mostly useless now, but wip)
- cleanup scriptlets

* Thu Sep 12 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.7.15-1
- 1.7.15 (#1006773)
- Word-readable .Xauthority (#1007187, CVE-2013-4331)

* Mon Sep 09 2013 Rex Dieter <rdieter@fedoraproject.org> 1.7.13-1
- 1.7.13

* Fri Sep 06 2013 Rex Dieter <rdieter@fedoraproject.org> 1.7.12-1
- 1.7.12 (#1001101)

* Tue Aug 27 2013 Rex Dieter <rdieter@fedoraproject.org> 1.7.11-2
- rebase nodaemon_option.patch

* Mon Aug 26 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.11-1
- Update to 1.7.11

* Tue Aug 20 2013 Rex Dieter <rdieter@fedoraproject.org> 1.7.9-3
- remove systemd preset (#963899)

* Thu Aug 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.7.9-2
- rebase patches (thanks poma)

* Sat Aug 03 2013 Rex Dieter <rdieter@fedoraproject.org> 1.7.9-1
- lightdm-1.7.9 (#975998)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-10
- fix systemd-logind support in -gobject bindings (#973618)

* Thu May 23 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-9
- really apply no_dmrc_save.patch (#963238)

* Tue May 21 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-8
- revert "lightdm is misusing the preset file logic of systemd" (#963899)

* Tue May 21 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-7
- cleanup/fix use of systemd macros

* Mon May 20 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-6
- disable lightdm writing to ~/.dmrc (#963238), 
  workaround selinux policy issue, use accountsservice exclusively.
- lightdm is misusing the preset file logic of systemd (#963899)

* Thu May 16 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-5
- %%post: setsebool -P xdm_write_home on (#963238)

* Thu Apr 25 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-4
- revert building PIE to avoid crashes (#956868)

* Thu Apr 25 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-3
- lightdm package should be built with PIE flags (#955147)
- apply systemd patch unconditionally

* Sun Apr 14 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-2
- lightdm does not honor UID_MIN from /etc/login.defs (#907312)

* Sun Apr 14 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-1
- lightdm-1.6.0
- No login key is writen in Mate-Desktop (#896130)

* Tue Apr 02 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5.3-1
- lightdm-1.5.3

* Wed Mar 27 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5.2-2
- lightdm.conf: +xserver-command=X -background none

* Wed Mar 27 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5.2-1
- lightdm-1.5.2 (#928255)

* Sat Mar 09 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5.1-1
- lightdm-1.5.1 (#919543)

* Fri Feb 22 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-3
- drop Requires: ConsoleKit (f18+)

* Wed Feb 06 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-2
- own %%_datadir/lightdm{,/remote-sessions}
- fix/cleanup macro usage

* Thu Jan 31 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-1
- lightdm-1.5.0
- License: (LGPLv2 or LGPLv3) and GPLv3+

* Thu Jan 31 2013 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-6
- Requires: polkit-js-engine (f19+)

* Thu Jan 10 2013 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-5
- polish systemd-login1 power support patch

* Tue Jan 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-4
- omit upstart/init support from packaging (#892157)

* Mon Nov 05 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-3
- native org.freedesktop.login1.(PowerOff|Reboot) support (#872797)

* Mon Nov 05 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-2
- lightdm: provide polkit .rules for actions (#872797)

* Fri Oct 05 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 1.4.0-1
- lightdm-1.4.0

* Tue Sep 04 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.3-2
- lightdm.service: After=+livesys-late.service (#853985)

* Thu Aug 30 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.3.3-1
- lightdm-1.3.3
- ship systemd preset for lightdm (#852845)

* Fri Aug 10 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-7
- conditionalize systemd unit support
- lightdm.pam: +-session optional pam_ck_connector.so

* Tue Aug  7 2012 Lennart Poettering <lpoetter@redhat.com> - 1.3.2-6
- Add bus name to service file

* Tue Aug  7 2012 Lennart Poettering <lpoetter@redhat.com> - 1.3.2-5
- Display Manager Rework
- https://fedoraproject.org/wiki/Features/DisplayManagerRework
- https://bugzilla.redhat.com/show_bug.cgi?id=846153

* Tue Jul 24 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 1.3.2-4
- import working lightdm-autologin pam config

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 1.3.2-2
- comply with guidelines concerning user and group handling

* Fri Jul 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-1
- lightdm-1.3.2

* Sun Jul 01 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-2
- lightdm.conf: minimum-vt=1 (allows for better plymouth no vt-switch)

* Wed Jun 27 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-1
- lightdm-1.3.1

* Fri Jun 15 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-15
- default to alternatives-provided greeter

* Thu Jun 14 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 1.2.2-14
- check if lightdm user exists, before creating him
- reset patch numbering
- use standard dir perm

* Tue Jun 12 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-13
- Requires: lightdm-greeter = 1.2

* Tue Jun 12 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-12
- move headers into -qt-devel pkg

* Mon Jun 11 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-11
- License: LGPLv3+ and GPLv3+
- make dbus files %%config
- gobject-devel, qt-devel subpkgs

* Mon May 14 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-10
- move /etc/tmpfiles.d/* => /usr/lib/tempfiles.d/

* Wed May 09 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-9
- fix typo, Requires: accountsservice

* Thu Apr 26 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-8
- Requires: accountservice ConsoleKit systemd

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-7
- respin nodaemon_option patch

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-6
- Requires: xorg-x11-xinit
- Requires: lightdm-greeter
- -gobject,-qt: drop dep on base pkg (easier for bootstrapping)

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-5
- make sane default lightdm.conf for fedora
- nodaemon_option.patch
- Requires: xorg-x11-xinit

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-4
- update lightdm.pam
- make /var/log/lightdm /var/lib/lightdm group-writable too

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-3
- omit useless %%post(un) scriptlets
- %%pre: add lightdm user/group
- BR: gnome-common
- %%build: --with-greeter-session=lightdm-gtk-greeter (for now)

* Tue Apr 24 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-2
- pkgconfig-style deps

* Tue Apr 24 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-1
- 1.2.2

* Fri Feb 17 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Fri Feb 17 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6
- Make build verbose

* Sun Oct 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Wed Aug 17 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3

* Fri Jul 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Sat Jul 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Sat Jun 25 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Fri Apr 22 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Sun Jan 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Sat Oct 23 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Initial package
