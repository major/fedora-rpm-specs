%global commit0 1fe1f5256d94e7ece0397e6237473ff8068dd4d6
%global date 20220712
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

%global __requires_exclude ^lib%{name}.so|^lib%{name}-js.so

%global cjs_version 5.6.0
%global cinnamon_desktop_version 5.6.0
%global cinnamon_translations_version 5.6.0
%global gobject_introspection_version 1.38.0
%global muffin_version 5.6.1
%global json_glib_version 0.13.2

%global __python %{__python3}

Name:           cinnamon
Version:        5.6.8
Release:        1%{!?tag:.%{date}git%{shortcommit0}}%{?dist}
Summary:        Window management and application launching for GNOME
License:        GPLv2+ and LGPLv2+
URL:            https://github.com/linuxmint/%{name}
%if 0%{?tag:1}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %url/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif
Source1:        polkit-%{name}-authentication-agent-1.desktop
Source2:        10_cinnamon-common.gschema.override
Source3:        10_cinnamon-apps.gschema.override.in

Patch0:         autostart.patch
Patch1:         set_wheel.patch
#Patch2:         revert_25aef37.patch
Patch3:         default_panal_launcher.patch
Patch4:         remove_crap_from_menu.patch

ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  python3-rpm-macros
BuildRequires:  pkgconfig(cjs-1.0) >= %{cjs_version}
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(lib%{name}-menu-3.0)
BuildRequires:  pkgconfig(%{name}-desktop) >= %{cinnamon_desktop_version}
BuildRequires:  gobject-introspection >= %{gobject_introspection_version}
BuildRequires:  pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(xapp)

# for screencast recorder functionality
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  intltool
BuildRequires:  pkgconfig(libcanberra)

# used in unused BigThemeImage
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libmuffin-0) >= %{muffin_version}
BuildRequires:  pkgconfig(libpulse)

# Bootstrap requirements
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  gnome-common

# media keys
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(colord)
%ifnarch s390 s390x
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(xorg-wacom)
%endif
BuildRequires:  pkgconfig(xtst)

#  Add a soup version requirement to cinnamon's environment.
Requires:       libsoup

Requires:       %{name}-desktop%{?_isa} >= %{cinnamon_desktop_version}
Requires:       muffin%{?_isa} >= %{muffin_version}
Requires:       cjs%{?_isa} >= %{cjs_version}
Requires:       gnome-menus%{?_isa} >= 3.0.0-2

# wrapper script used to restart old GNOME session if run --replace
# from the command line
Requires:       gobject-introspection%{?_isa} >= %{gobject_introspection_version}

# needed for loading SVG's via gdk-pixbuf
Requires:       librsvg2%{?_isa}

# needed as it is now split from Clutter
Requires:       json-glib%{?_isa} >= %{json_glib_version}
Requires:       upower%{?_isa}
Requires:       polkit%{?_isa} >= 0.100

# needed for session files
Requires:       %{name}-session%{?_isa}

# needed for schemas
Requires:       at-spi2-atk%{?_isa}

# needed for on-screen keyboard
Requires:       caribou%{?_isa}

# needed for the user menu
Requires:       accountsservice-libs%{?_isa}

# needed for settings
Requires:       gsound
Requires:       libtimezonemap%{?_isa}
Requires:       python3-distro
Requires:       python3-pytz
Requires:       python3-pexpect
Requires:       python3-gobject%{?_isa}
Requires:       python3-dbus%{?_isa}
Requires:       python3-lxml%{?_isa}
Requires:       python3-pillow%{?_isa}
Requires:       python3-pam
Requires:       python3-tinycss2
Requires:       python3-requests
Requires:       python3-setproctitle%{?_isa}
Requires:       python3-xapp
Requires:       mintlocale
Requires:       %{name}-control-center%{?_isa}
Requires:       %{name}-translations >= %{cinnamon_translations_version}

# needed for theme overrides
Requires:       desktop-backgrounds-basic
Requires:       desktop-backgrounds-gnome
Requires:       gnome-backgrounds
Requires:       system-logos

# Theming
Requires:       google-noto-sans-fonts
Requires:       %{name}-themes >= 1:1.7.4-0.2.20181112gitb94b890

# RequiredComponents in the session files
Requires:       nemo%{?_isa}
Requires:       %{name}-screensaver%{?_isa}

# metacity and tint2 are needed for fallback
Requires:       metacity%{?_isa}
Requires:       tint2%{?_isa}

# required for keyboard applet
Requires:       gucharmap%{?_isa}
Requires:       xapps%{?_isa}
Requires:       python3-xapps-overrides%{?_isa}

# required for calendar applet events
Recommends:     %{name}-calendar-server%{?_isa} = %{version}-%{release}

# required for network applet
Requires:       nm-connection-editor%{?_isa}
Requires:       network-manager-applet%{?_isa}

Requires:       python3-inotify


# required for cinnamon-killer-daemon
Requires:       keybinder3%{?_isa}

# required for sound applet
Requires:       wget%{?_isa}

# required for printer applet
Requires:       cups-client%{?_isa}

# required for spice
Requires:       gettext

Provides:       desktop-notification-daemon
Provides:       bundled(libcroco) = 0.6.12

%description
Cinnamon is a Linux desktop which provides advanced
innovative features and a traditional user experience.

The desktop layout is similar to Gnome 2.
The underlying technology is forked from Gnome Shell.
The emphasis is put on making users feel at home and providing
them with an easy to use and comfortable desktop experience.

%package calendar-server
Summary:        Calendar server for Cinnamon
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       evolution-data-server%{?_isa}
Requires:       gnome-calendar%{?_isa}

%description calendar-server
Calendar server for Cinnamon.

%if 0%{?fedora}
%package devel-doc
Summary:        Development Documentation files for Cinnamon
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description devel-doc
This package contains the code documentation for various Cinnamon components.
%endif

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

%{__sed} -i -e 's@gksu@pkexec@g' files%{_bindir}/%{name}-settings-users
%{__sed} -i -e 's@gnome-orca@orca@g' files%{_datadir}/%{name}/%{name}-settings/modules/cs_accessibility.py
# remove mintlocale im from settings
%{__sed} -i -e 's@mintlocale im@mintlocale_im_removed@g' files%{_datadir}/%{name}/%{name}-settings/%{name}-settings.py

# Fix rpmlint errors
for file in files%{_datadir}/%{name}/%{name}-settings/bin/*.py files%{_datadir}/%{name}/%{name}-looking-glass/*.py \
   files%{_datadir}/%{name}/%{name}-settings/modules/cs_{applets,desklets}.py; do
   chmod a+x $file
done
chmod a-x files%{_datadir}/%{name}/%{name}-settings/bin/__init__.py

%build
%meson \
 --libexecdir=%{_libexecdir}/cinnamon/ \
 -Ddeprecated_warnings=false \
 -Dpy3modules_dir=%{python3_sitelib} \
%if 0%{?fedora}
 -Ddocs=true
%else
 -Ddocs=false
%endif

%meson_build


%install
%meson_install
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/

# install polkit autostart desktop file
%{__install} --target-directory=%{buildroot}%{_datadir}/applications \
    -Dpm 0644 %{SOURCE1}

# install common gschema override
%{__install} --target-directory=%{buildroot}%{_datadir}/glib-2.0/schemas \
    -Dpm 0644 %{SOURCE2}

# install gschema-override for apps
%{__sed} -e 's!@pkg_manager@!org.mageia.dnfdragora.desktop!g' \
    < %{SOURCE3} > %{buildroot}%{_datadir}/glib-2.0/schemas/10_%{name}-apps.gschema.override

# install gschema-override for wallpaper
%{__cat} >> %{buildroot}%{_datadir}/glib-2.0/schemas/10_%{name}-wallpaper.gschema.override << EOF
[org.cinnamon.desktop.background]
picture-uri='file:///usr/share/backgrounds/tiles/default_blue.jpg'
EOF

# Provide symlink for the background-propeties.
%{__ln_s} %{_datadir}/gnome-background-properties %{buildroot}%{_datadir}/%{name}-background-properties


%check
%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%doc README.rst AUTHORS
%license COPYING
%{_bindir}/cinnamon
%{_bindir}/cinnamon-close-dialog
%{_bindir}/cinnamon-dbus-command
%{_bindir}/cinnamon-desktop-editor
%{_bindir}/cinnamon-display-changes-dialog
%{_bindir}/cinnamon-file-dialog
%{_bindir}/cinnamon-hover-click
%{_bindir}/cinnamon-install-spice
%{_bindir}/cinnamon-json-makepot
%{_bindir}/cinnamon-killer-daemon
%{_bindir}/cinnamon-launcher
%{_bindir}/cinnamon-looking-glass
%{_bindir}/cinnamon-menu-editor
%{_bindir}/cinnamon-preview-gtk-theme
%{_bindir}/cinnamon-screensaver-lock-dialog
%{_bindir}/cinnamon-session-cinnamon
%{_bindir}/cinnamon-session-cinnamon2d
%{_bindir}/cinnamon-settings
%{_bindir}/cinnamon-settings-users
%{_bindir}/cinnamon-slideshow
%{_bindir}/cinnamon-spice-updater
%{_bindir}/cinnamon-subprocess-wrapper
%{_bindir}/cinnamon-xlet-makepot
%{_bindir}/cinnamon2d
%{_bindir}/xlet-about-dialog
%{_bindir}/xlet-settings
%config(noreplace) %{_sysconfdir}/xdg/menus/*
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/org.Cinnamon.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.Cinnamon.Melange.service
%{_datadir}/dbus-1/services/org.Cinnamon.Slideshow.service
%{_datadir}/desktop-directories/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/%{name}-session/sessions/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/polkit-1/actions/org.%{name}.settings-users.policy
%{_datadir}/xsessions/*
%{_datadir}/%{name}/
%{_datadir}/%{name}-background-properties
%{_libdir}/%{name}/
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/cinnamon/cinnamon-hotplug-sniffer
%{_libexecdir}/cinnamon/cinnamon-perf-helper
%{_mandir}/man1/*
%{python3_sitelib}/%{name}/

%files calendar-server
%{_bindir}/%{name}-calendar-server
%{_libexecdir}/%{name}/%{name}-calendar-server.py
%{_datadir}/dbus-1/services/org.%{name}.CalendarServer.service

%if 0%{?fedora}
%files devel-doc
%doc %{_datadir}/gtk-doc/html/*/
%endif

%changelog
* Mon Mar 20 2023 Leigh Scott <leigh123linux@gmail.com> - 5.6.8-1
- Update to 5.6.8 release

* Thu Feb 16 2023 Leigh Scott <leigh123linux@gmail.com> - 5.6.7-1
- Update to 5.6.7 release

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 15 2022 Leigh Scott <leigh123linux@gmail.com> - 5.6.5-1
- Update to 5.6.5 release

* Wed Nov 30 2022 Leigh Scott <leigh123linux@gmail.com> - 5.6.4-1
- Update to 5.6.4 release

* Mon Nov 28 2022 Leigh Scott <leigh123linux@gmail.com> - 5.6.3-1
- Readd lost window placement modes

* Fri Nov 18 2022 Leigh Scott <leigh123linux@gmail.com> - 5.6.1-1
- Update to 5.6.1 release

* Tue Sep 06 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.12-1
- Update to 5.4.12 release

* Sun Aug 21 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.11-1
- Update to 5.4.11 release

* Sat Aug 13 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.10-2
- Fix soup version issue for applets

* Sat Aug 13 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.10-1
- Update to 5.4.10 release

* Mon Aug 01 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.9-1
- Update to 5.4.9 release

* Mon Jul 25 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.8-1
- Update to 5.4.8 release

* Sun Jul 24 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.7-1
- Update to 5.4.7 release

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.5-1
- Update to 5.4.5 release

* Fri Jul 15 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.4-1
- Update to 5.4.4 release

* Wed Jul 13 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.2-2.20220712git1fe1f52
- Update to latest snapshot

* Mon Jun 27 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.2-1
- Update to 5.4.2 release

* Mon Jun 20 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.1-1
- Update to 5.4.1 release

* Sat Jun 11 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.0-2
- Add requires gsound

* Sat Jun 11 2022 Leigh Scott <leigh123linux@gmail.com> - 5.4.0-1
- Update to 5.4.0 release

* Sun May 22 2022 Leigh Scott <leigh123linux@gmail.com> - 5.2.7-4
- The calendar-server sub-package isn't noarch due to search paths

* Mon May 16 2022 Leigh Scott <leigh123linux@gmail.com> - 5.2.7-3
- Fix calendar-server sub-package

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 01 2022 Leigh Scott <leigh123linux@gmail.com> - 5.2.7-1
- Update to 5.2.7 release

* Thu Dec 16 2021 Leigh Scott <leigh123linux@gmail.com> - 5.2.6-1
- Update to 5.2.6 release

* Tue Dec 14 2021 Leigh Scott <leigh123linux@gmail.com> - 5.2.5-3
- Tweak schema override for theme changes

* Mon Dec 13 2021 Peter Hutterer <peter.hutterer@redhat.com> - 5.2.5-2
- Rebuild for libwacom soname bump

* Thu Dec 09 2021 Leigh Scott <leigh123linux@gmail.com> - 5.2.5-1
- Update to 5.2.5 release

* Mon Dec 06 2021 Leigh Scott <leigh123linux@gmail.com> - 5.2.3-1
- Update to 5.2.3 release

* Mon Nov 29 2021 Leigh Scott <leigh123linux@gmail.com> - 5.2.1-1
- Update to 5.2.1 release

* Sat Nov 20 2021 Leigh Scott <leigh123linux@gmail.com> - 5.2.0-1
- Update to 5.2.0 release

* Thu Nov 04 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.7-1
- Update to 5.0.7 release

* Fri Oct 15 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.6-1
- Update to 5.0.6 release

* Tue Oct 05 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.5-5
- Fix python-3.10 menu-editor

* Mon Sep 27 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.5-4
- Drop fallback patches

* Mon Sep 06 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.5-3
- Add upstream fixes

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.5-1
- Update to 5.0.5 release

* Thu Jul 08 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.4-1
- Update to 5.0.4 release

* Fri Jun 25 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.3-1
- Update to 5.0.3 release

* Mon Jun 07 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.2-2
- Add python install directory patch

* Fri Jun 04 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.2-1
- Update to 5.0.2 release

* Wed Jun 02 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.1-2
- Switch fallback to metacity

* Tue Jun 01 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.1-1
- Update to 5.0.1 release

* Tue Jun 01 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.0-2
- Fix session

* Tue Jun 01 2021 Leigh Scott <leigh123linux@gmail.com> - 5.0.0-1
- Update to 5.0.0 release

* Tue Mar 23 2021 Leigh Scott <leigh123linux@gmail.com> - 4.8.6-5
- Add gnome-system-monitor to settings

* Thu Mar 04 2021 Leigh Scott <leigh123linux@gmail.com> - 4.8.6-4
- More GWL fixes

* Thu Mar 04 2021 Leigh Scott <leigh123linux@gmail.com> - 4.8.6-3
- Add upstream GWL fixes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Leigh Scott <leigh123linux@gmail.com> - 4.8.6-1
- Update to 4.8.6 release

* Sat Jan  2 2021 Leigh Scott <leigh123linux@gmail.com> - 4.8.5-1
- Update to 4.8.5 release

* Tue Dec 29 2020 Leigh Scott <leigh123linux@gmail.com> - 4.8.4-1
- Update to 4.8.4 release

* Sun Dec 13 2020 Leigh Scott <leigh123linux@gmail.com> - 4.8.3-1
- Update to 4.8.3 release

* Tue Dec  8 2020 Leigh Scott <leigh123linux@gmail.com> - 4.8.2-1
- Update to 4.8.2 release

* Tue Dec  8 2020 Leigh Scott <leigh123linux@gmail.com> - 4.8.1-1
- Update to 4.8.1 release

* Thu Nov 26 2020 Leigh Scott <leigh123linux@gmail.com> - 4.8.0-1
- Update to 4.8.0 release

* Mon Oct 19 2020 Leigh Scott <leigh123linux@gmail.com> - 4.7.0-0.1.20201019gitd077210
- Update to git master snapshot

* Sat Sep 19 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.7-2
- Switch to gjs f34+

* Tue Aug 11 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.7-1
- Update to 4.6.7 release

* Mon Aug 10 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.6-4
- Enable LTO

* Fri Jul 31 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.6-3
- Drop libcroco requirement

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.6-1
- Update to 4.6.6 release

* Sun Jun 21 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.5-1
- Update to 4.6.5 release

* Wed Jun 17 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.4-1
- Update to 4.6.4 release

* Fri Jun 12 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.3-2
- Fix applet configure with python3.9

* Sat Jun 06 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.3-1
- Update to 4.6.3 release

* Wed May 27 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.2-1
- Update to 4.6.2 release

* Thu May 21 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.1-1
- Update to 4.6.1 release

* Wed May 13 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.0-1
- Update to 4.6.0 release

* Mon Apr 20 2020 Leigh Scott <leigh123linux@gmail.com> - 4.4.8-8
- Use desktop-backgrounds-basic for background instead of fedora default

* Tue Apr 14 2020 Leigh Scott <leigh123linux@gmail.com> - 4.4.8-7
- Fix last commit

* Tue Apr 14 2020 Leigh Scott <leigh123linux@gmail.com> - 4.4.8-6
- Disable bell-mode

* Tue Apr 14 2020 Leigh Scott <leigh123linux@gmail.com> - 4.4.8-5
- Remove BuildRequires pkgconfig(gconf-2.0)

* Wed Feb 26 2020 Leigh Scott <leigh123linux@googlemail.com> - 4.4.8-4
- Bump for f33 rawhide

* Mon Feb 17 2020 Leigh Scott <leigh123linux@googlemail.com> - 4.4.8-3
- Enable notification sound
- Patch cinnamon-setting info for python-3.8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Leigh Scott <leigh123linux@googlemail.com> - 4.4.8-1
- Update to 4.4.8 release

* Mon Dec 30 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.6-1
- Update to 4.4.6 release

* Thu Dec 12 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.5-2
- Switch to xapp-status for bluetooth

* Thu Dec 12 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.5-1
- Update to 4.4.5 release

* Tue Dec 10 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.4-1
- Update to 4.4.4 release

* Sat Dec 07 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.3-1
- Update to 4.4.3 release

* Fri Nov 29 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.2-2
- Tweak applet layout

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.2-1
- Update to 4.4.2 release

* Tue Nov 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.1-1
- Update to 4.4.1 release

* Sun Nov 24 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-6
- fix cinnamon-desktop isa mistake

* Sun Nov 24 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-5
- Add missing isa

* Sun Nov 24 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-4
- Add requires python3-xapp and python3-setproctitle

* Sun Nov 24 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-3
- Add requires python3-pytz and libtimezonemap

* Sun Nov 24 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-2
- Readd polkit-cinnamon-authentication-agent-1 to autostart patch

* Fri Nov 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-1
- Update to 4.4.0 release

* Thu Nov 21 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-0.1.20191120git6a9367b
- Update to git master snapshot

* Sat Sep 14 2019 Leigh Scott <leigh123linux@gmail.com> - 4.2.4-2
- Fix cinnamon-settings default issue (rhbz#1752134)

* Wed Sep 04 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.4-1
- Update to 4.2.4 release

* Wed Aug 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.3-2
- Add notification fix
- Switch rawhide to 32

* Wed Jul 31 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.3-1
- Update to 4.2.3 release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.2-1
- Update to 4.2.2 release

* Sun Jun 30 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.0-2
- Add requires python3-tinycss

* Sat Jun 29 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.0-1
- Update to 4.2.0 release

* Sun Jun 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.0-0.1.20190614git369148f
- Update snapshot

* Wed Jun 12 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.0.11-0.4.20190611gitd7c6da5
- Update snapshot

* Wed Jun 05 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.0.11-0.3.20190604gitdf5150a
- Update snapshot

* Tue Apr 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.0.11-0.2.20190416giteccebdd
- Update snapshot

* Fri Apr 05 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.0.11-0.1.20190405gitc843f36
- Update to git master snapshot

* Wed Apr 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.0.10-1
- Update to 4.0.10 release

* Mon Mar 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.0.9-1
- Update to 4.0.9 release

* Mon Mar 04 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.0.8-5
- Bump for f30 backgrounds

* Thu Feb 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.0.8-4
- Add monospace font override

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.0.8-2
- Tweak panel layout

* Sat Dec 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.8-1
- Update to 4.0.8 release

* Sun Dec 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.7-1
- Update to 4.0.7 release

* Thu Dec 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.5-1
- Update to 4.0.5 release

* Thu Dec 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.4-1
- Update to 4.0.4 release

* Wed Nov 28 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.3-1
- Update to 4.0.3 release

* Tue Nov 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.2-1
- Update to 4.0.2 release

* Wed Nov 14 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.1-2
- Switch theme and add version to cinnamon-themes requires

* Mon Nov 12 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.1-1
- Update to 4.0.1 release

* Sat Nov 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.0-1
- Update to 4.0.0 release

