Name:		blueman
Summary:	GTK+ Bluetooth Manager
License:	GPL-2.0-or-later

Epoch:		1
Version:	2.4.3
Release:	2%{?dist}

URL:		https://github.com/blueman-project/blueman
Source0:	%{URL}/archive/refs/tags/%{version}/blueman-%{version}.tar.gz

# The configure script checks if some python packages
# are present during build, but they aren't really required,
# and in Fedora, some of them are not available on all architectures.
Patch0:		0000-less-buildrequires.patch

# The value for each of these should be either "yes" or "no"
%global enable_caja_sendto	yes
%global enable_nautilus_sendto	yes
%global enable_nemo_sendto	yes
# blueman-sendto for Thunar is shipped by the Thunar package.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2103326
%global enable_thunar_sendto	no

BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python3)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iproute
BuildRequires:	make
BuildRequires:	marshalparser
BuildRequires:	python3-Cython >= 0.21
BuildRequires:	python3-cairo-devel
BuildRequires:	python3-dbus
BuildRequires:	systemd

%{?systemd_requires}

# Based on upstream's Dependencies.md file
Requires:	bluez >= 5.48
Requires:	bluez-obexd
Requires:	dbus >= 1.9.18
Requires:	dconf
Requires:	desktop-notification-daemon
Requires:	gdk-pixbuf2
Requires:	glib2 >= 2.32
Requires:	gtk3 >= 3.24
Requires:	iproute
Requires:	NetworkManager-libnm

Requires:	python3dist(dbus-python)
Requires:	python3dist(pycairo)
Requires:	python3dist(pygobject) >= 3.27.2

Requires:	pulseaudio-libs-glib2
Requires:	(pulseaudio-module-bluetooth if pulseaudio)

Provides:	dbus-bluez-pin-helper

%description
Blueman is a tool to use Bluetooth devices. It is designed to provide simple,
yet effective means for controlling BlueZ API and simplifying bluetooth tasks
such as:
- Connecting to 3G/EDGE/GPRS via dial-up
- Connecting to/Creating bluetooth networks
- Connecting to input devices
- Connecting to audio devices
- Sending/Receiving files via OBEX
- Pairing


# -- Subpackages start
# -- Caja

%if "yes" == "%{enable_caja_sendto}"
%package caja
Summary:	Blueman integration for Caja
Supplements:	(caja and %{name})

Requires:	python3-caja
BuildArch:	noarch

%description caja
%{summary}.
%endif

# -- Nautilus

%if "yes" == "%{enable_nautilus_sendto}"
%package nautilus
Summary:	Blueman integration for Nautilus
Supplements:	(nautilus and %{name})

Requires:	nautilus-python
BuildArch:	noarch

%description nautilus
%{summary}.
%endif

# -- Nemo

%if "yes" == "%{enable_nemo_sendto}"
%package nemo
Summary:	Blueman integration for Nemo
Supplements:	(nemo and %{name})

Requires:	nemo-python
BuildArch:	noarch

%description nemo
%{summary}.
%endif

# -- Thunar

%if "yes" == "%{enable_thunar_sendto}"
%package thunar
Summary:	Blueman integration for Thunar
Supplements:	(Thunar and %{name})

BuildArch:	noarch

%description thunar
%{summary}.
%endif

# -- Subpackages end


%prep
%autosetup -p1


%build
export PYTHON=%{_bindir}/python3

NOCONFIGURE="yes" ./autogen.sh
%configure \
	--enable-maintainer-mode \
	--disable-runtime-deps-check \
	--enable-caja-sendto=%{enable_caja_sendto} \
	--enable-nautilus-sendto=%{enable_nautilus_sendto} \
	--enable-nemo-sendto=%{enable_nemo_sendto} \
	--enable-thunar-sendto=%{enable_thunar_sendto} \
	--disable-static \
	--disable-schemas-compile
%make_build


%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/doc/blueman/

# Run the python interpreter in "don't load code from user-controlled directories" mode
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2207684
%global py3_shbang_opts %{py3_shbang_opts}E
%py3_shebang_fix %{buildroot}%{_bindir}/blueman-* %{buildroot}%{_libexecdir}/blueman-*

%find_lang blueman

# we need to own this, not only because of SELinux
mkdir -p %{buildroot}%{_sharedstatedir}/blueman
touch %{buildroot}%{_sharedstatedir}/blueman/network.state


%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/blueman.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/blueman-*.desktop

%if "yes" == "%{enable_thunar_sendto}"
desktop-file-validate %{buildroot}%{_datadir}/Thunar/sendto/*blueman*.desktop
%endif


%post
%systemd_post blueman-mechanism.service
%systemd_user_post blueman-applet.service

%postun
%systemd_postun_with_restart blueman-mechanism.service

%preun
%systemd_preun blueman-mechanism.service
%systemd_user_preun blueman-applet.service


%files -f blueman.lang
%doc CHANGELOG.md FAQ README.md
%license COPYING
%{_bindir}/blueman-*
%{python3_sitelib}/blueman/
%{python3_sitearch}/*.so
%{_libexecdir}/blueman-*
%{_sysconfdir}/xdg/autostart/blueman.desktop
%{_datadir}/applications/blueman-*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/blueman/
%{_datadir}/dbus-1/services/org.blueman.*.service
%{_datadir}/dbus-1/system.d/org.blueman.*.conf
%{_datadir}/dbus-1/system-services/org.blueman.*.service
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/polkit-1/actions/org.blueman.policy
%{_datadir}/polkit-1/rules.d/blueman.rules
%{_mandir}/man1/*
%{_unitdir}/blueman-*.service
%{_userunitdir}/blueman-*.service
%dir %{_sharedstatedir}/blueman
%ghost %attr(0644,root,root) %{_sharedstatedir}/blueman/network.state

%if "yes" == "%{enable_caja_sendto}"
%files caja
%{_datadir}/caja-python/extensions/*blueman*
%endif

%if "yes" == "%{enable_nautilus_sendto}"
%files nautilus
%{_datadir}/nautilus-python/extensions/*blueman*
%endif

%if "yes" == "%{enable_nemo_sendto}"
%files nemo
%{_datadir}/nemo-python/extensions/*blueman*
%endif

%if "yes" == "%{enable_thunar_sendto}"
%files thunar
%{_datadir}/Thunar/sendto/*blueman*
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.4.3-1
- Update to v2.4.3

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:2.4.2-3
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:2.4.2-2
- Rebuilt for Python 3.13

* Fri May 31 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.4.2-1
- Update to v2.4.2

* Tue Apr 09 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.4.1-1
- Update to v2.4.1

* Thu Apr 04 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.4-2
- Add missing Requires

* Sat Mar 30 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.4-1
- Update to v2.4
- Drop backported patches

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3.5-8
- Backport upstream fix for sending out too many notifications (rhbz#2193294)
- Fix broken patch for possible crash at startup (rhbz#2246819)
- Migrate license tag to SPDX

* Mon Sep 11 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3.5-7
- Backport upstream fix for possible crash at startup (rhbz#2173854)
- Backport upstream fix for crash on missing icon (rhbz#2217189)

* Sun Sep 10 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3.5-6
- Backport upstream fix for nautilus integration spamming system log (rhbz#2238225)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1:2.3.5-4
- Rebuilt for Python 3.12

* Thu Jun 08 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3.5-3
- Use py3_shebang_fix macro to add "-sPE" to Python shebangs

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3.5-1
- Update to v2.3.5

* Fri Oct 14 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3.4-1
- Update to v2.3.4

* Wed Oct 12 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3.3-1
- Update to v2.3.3

* Mon Aug 01 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3.2-1
- Update to v2.3.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 17 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3.1-1
- Update to v2.3.1
- Drop Patch1 (fix blueman breaking XFCE - backported from this release)

* Sat Jul 16 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3-4
- Add a patch to fix blueman breaking XFCE

* Tue Jul 05 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3-3
- Update to v2.3

* Sun Jul 03 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3-2.beta1
- Disable building the blueman-thunar subpackage

* Wed Jun 29 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.3-1.beta1
- Update to v2.3.beta1
- Call configure manually, instead of letting autogen.sh do that
- Add subpackages providing caja/nautilus/nemo/thunar integration

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:2.2.5-2
- Rebuilt for Python 3.11

* Fri Jun 10 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.2.5-1
- Update to v2.2.5

* Tue Feb 08 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.2.4-1
- Update to v2.2.4
- Drop "Obsoletes: blueman-nautilus" (originally added for 1.x.y -> 2.0.0 upgrade, not needed for a long time now)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.2.3-1
- Update to v2.2.3

* Fri Aug 06 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.2.2-1
- Update to v2.2.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:2.2.1-2
- Rebuilt for Python 3.10

* Thu Jun 03 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.2.1-1
- Update to v2.2.1
- Do not pull in pulseaudio-specific dependencies on pipewire systems

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.1.4-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.1.4-2
- Enable appindicator support

* Wed Oct 28 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:2.1.4-1
- Update to v2.1.4
- Update list of dependencies

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:2.1.3-2
- Rebuilt for Python 3.9

* Fri May 08 2020 Artur Iwicki <fedora@svgames.pl> - 1:2.1.3-1
- Update to latest upstream release (2.1.3)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Artur Iwicki <fedora@svgames.pl> - 1:2.1.2-1
- Update to latest upstream release (2.1.2)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.1.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Artur Iwicki <fedora@svgames.pl> - 1:2.1.1-1
- Update to latest upstream release (2.1.1)

* Mon Jun 10 2019 Artur Iwicki <fedora@svgames.pl> - 1:2.1-1
- Update to latest upstream release (2.1)
- Drop Patch0 and Patch1 (they were backports from today's release)

* Sat Jun 08 2019 Artur Iwicki <fedora@svgames.pl> - 1:2.1-0.17.beta1
- Add two upstream patches for crashes and IO issues

* Mon May 06 2019 Artur Iwicki <fedora@svgames.pl> - 1:2.1-0.16.beta1
- Upgrade to new upstream pre-release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-0.15.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Artur Iwicki <fedora@svgames.pl> - 1:2.1-0.14.alpha3
- Upgrade to new upstream pre-release
- Remove the Group: tag (no longer used in Fedora)

* Tue Sep 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:2.1-0.13.alpha2
- pygobject3 → python3-gobject-base

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-0.12.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1:2.1-0.11.alpha2
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-0.10.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:2.1-0.9.alpha2
- Remove obsolete scriptlets

* Mon Dec 11 2017 Pete Walter <pwalter@fedoraproject.org> - 1:2.1-0.8.alpha2
- Update to 2.1 alpha2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-0.7.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-0.6.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-0.5.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1:2.1-0.4.alpha1
- Rebuild for Python 3.6

* Wed Sep 21 2016 Peter Walter <pwalter@fedoraproject.org> - 1:2.1-0.3.alpha1
- Fix obexd dependencies (#1377640)

* Tue Sep 20 2016 Peter Walter <pwalter@fedoraproject.org> - 1:2.1-0.2.alpha1
- Enable polkit support
- Validate desktop files

* Mon Sep 19 2016 Peter Walter <pwalter@fedoraproject.org> - 1:2.1-0.1.alpha1
- Update to 2.1 alpha1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 18 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:2.0.4-2
- patch to try and fix some of the dbus exceptions

* Sun Apr 03 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:2.0.4-1
- update to 2.0.4 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.8.gita0408c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.7.gita0408c1
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Nov 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1-0.6.gita0408c1
- update to latest git

* Fri Oct 30 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1-0.5.git608efb8
- update to latest git

* Fri Sep 18 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1-0.4.git2a812a8
- update to latest git

* Wed Sep 16 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1-0.3.git7a2e20e
- build against python3

* Mon Aug 24 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1-0.2.git7a2e20e
- update to latest git

* Wed Aug 12 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1-0.1.git0a5defd
- update to git

* Mon Jul 27 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.0-11
- add requires dconf (bz 1246995)

* Mon Jul 13 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.0-10
- remove requires desktop-notification-daemon and PolicyKit-authentication-agent
- patch for gi and pyobject changes

* Mon Jun 22 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.0-9
- add upstream fix for bz 1233237

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.0-7
- remove appindicator support

* Fri Jun 05 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.0-6
- add requires bluez (bz 1228488)

* Thu May 28 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.0-5
- add requires pulseaudio-libs-glib2

* Thu May 28 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.0-4
- remove browse feature (upstream patch)
- ammend description
- rename service file (upstream patch)
- clean up requires and buildrequires
- update scriptlets
- clean up spec file

* Wed May 27 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.0-3
- add requires dbus-python
- add requires pulseaudio-module-bluetooth for audio

* Wed May 27 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.0-2
- fix bluetoothd path for report tool

* Tue May 26 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.0-1
- update to 2.0 release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.23-5
- Require pulseaudio-libs-glib2 (#856270)

* Sat Oct 06 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.23-4
- No longer require gnome-session
- Require gvfs-obexftp, needed when launching file managers from blueman

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 06 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.23-2
- Own /var/lib/blueman and /var/lib/blueman/network.state (#818528)

* Thu Apr 26 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.23-1
- Update to 1.23
- Drop upstreamed PulseAudio patch
- Fix statusicon
- Autostart blueman not only in GNOME but also in Xfce and LXDE
- Enhance description

