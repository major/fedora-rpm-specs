%global commit cc2a72fdf4bbcd56edf4cc339cce02c12af4ccf4

Name: remmina
Version: 1.4.39
Release: 1%{?dist}
Summary: Remote Desktop Client
License: GPL-2.0-or-later and MIT
URL: https://remmina.org

Source0: https://gitlab.com/Remmina/Remmina/-/archive/v%{version}/Remmina-%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Cmake helper file to easy build plugins outside remmina source tree
# See http://www.muflone.com/remmina-plugin-rdesktop/english/install.html which
# use http://www.muflone.com/remmina-plugin-builder/ with remmina bundled source.
# So we can't use it directly only as instructions.
Source1: pluginBuild-CMakeLists.txt

BuildRequires: cmake >= 3.2
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: harfbuzz-devel
BuildRequires: intltool
BuildRequires: kf5-kwallet-devel
BuildRequires: libappstream-glib
BuildRequires: libgcrypt-devel
BuildRequires: libsodium-devel
BuildRequires: python3-devel
BuildRequires: xdg-utils
BuildRequires: pkgconfig(appindicator3-0.1)
%if 0%{?fedora} || 0%{?rhel} == 8
BuildRequires: pkgconfig(avahi-ui)
BuildRequires: pkgconfig(avahi-ui-gtk3)
%endif
BuildRequires: pkgconfig(freerdp3) >= 3.3.0
BuildRequires: freerdp
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsecret-1)
%if 0%{?fedora} >= 37
BuildRequires: pkgconfig(libsoup-3.0)
%else
BuildRequires: pkgconfig(libsoup-2.4)
%endif
BuildRequires: pkgconfig(libssh) >= 0.8.0
BuildRequires: pkgconfig(libvncserver)
BuildRequires: pkgconfig(libpcre2-8)
%if 0%{?fedora} || 0%{?rhel} == 8
BuildRequires: pkgconfig(spice-client-gtk-3.0)
%endif
BuildRequires: pkgconfig(vte-2.91)
%if 0%{?fedora} >= 37
BuildRequires: pkgconfig(webkit2gtk-4.1)
%else
BuildRequires: pkgconfig(webkit2gtk-4.0)
%endif
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(fuse3)

# We don't ship these remmina plugins any longer.
Obsoletes: %{name}-plugins-nx < %{version}-%{release}
Obsoletes: %{name}-plugins-st < %{version}-%{release}
Obsoletes: %{name}-plugins-xdmcp < %{version}-%{release}

Recommends: %{name}-plugins-exec
Recommends: %{name}-plugins-rdp
Recommends: %{name}-plugins-secret
Recommends: %{name}-plugins-vnc

%if 0%{?fedora}
Recommends: openh264
%endif

%description
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

Remmina supports multiple network protocols in an integrated and consistent
user interface. Currently RDP, VNC and SSH are supported.

Please don't forget to install the plugins for the protocols you want to use.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The %{name}-devel package contains header files for developing plugins for
%{name}.

%package plugins-exec
Summary: External execution plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-exec
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin to execute external processes (commands or
applications) from the Remmina window.

%package plugins-secret
Summary: Keyring integration for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-plugins-gnome < %{version}-%{release}
Provides: %{name}-plugins-gnome%{?_isa} = %{version}-%{release}

%description plugins-secret
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin with keyring support for the Remmina remote
desktop client.

%package plugins-rdp
Summary: RDP plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-rdp
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the Remote Desktop Protocol (RDP) plugin for the Remmina
remote desktop client.

%package plugins-vnc
Summary: VNC plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-vnc
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the VNC plugin for the Remmina remote desktop
client.

%if 0%{?fedora} || 0%{?rhel} == 8
%package plugins-spice
Summary: SPICE plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-spice
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the SPICE plugin for the Remmina remote desktop
client.
%endif

%package plugins-www
Summary: WWW plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-www
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the WWW plugin (web browser with authentication) for the
Remmina remote desktop client.

%package plugins-kwallet
Summary: KDE Wallet plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-kwallet
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the KDE Wallet plugin for the Remmina remote desktop
client. It will be activated automatically if KDE Wallet is installed and
running.

%if 0%{?fedora} || 0%{?rhel} == 8
%package plugins-x2go
Summary: x2go plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pyhoca-cli

%description plugins-x2go
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the x2go plugin for the Remmina remote desktop client.
%endif

%package plugins-python
Summary: Python plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-python
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the python plugin for the Remmina remote desktop client.

%package gnome-session
Summary: Gnome Shell session for Remmina kiosk mode
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnome-session

%description gnome-session
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains Remmina kiosk mode, including a Gnome Shell session
that shows up under the display manager session menu.

%prep
%autosetup -p1 -n Remmina-v%{version}-%{commit}

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DHAVE_LIBAPPINDICATOR=ON \
%if 0%{?fedora} || 0%{?rhel} == 8
    -DWITH_AVAHI=ON \
%else
    -DWITH_AVAHI=OFF \
%endif
    -DWITH_FREERDP3=ON \
    -DWITH_GCRYPT=ON \
    -DWITH_GETTEXT=ON \
    -DWITH_KF5WALLET=ON \
    -DWITH_KIOSK_SESSION=ON \
    -DWITH_LIBSSH=ON \
    -DWITH_NEWS=OFF \
    -DWITH_PYTHONLIBS=ON \
%if 0%{?fedora} || 0%{?rhel} == 8
    -DWITH_SPICE=ON \
%else
    -DWITH_SPICE=OFF \
%endif
    -DWITH_VTE=ON \
%if 0%{?fedora} || 0%{?rhel} == 8
    -DWITH_X2GO=ON
%else
    -DWITH_X2GO=OFF
%endif
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}/%{_libdir}/cmake/%{name}/
cp -pr cmake/*.cmake %{buildroot}/%{_libdir}/cmake/%{name}/
cp -pr config.h.in %{buildroot}/%{_includedir}/%{name}/
cp -p %{SOURCE1} %{buildroot}/%{_includedir}/%{name}/

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-file-wrapper
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/actions/*.*
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/icons/hicolor/*/emblems/org.remmina.Remmina-*.svg
%{_datadir}/icons/hicolor/*/status/org.remmina.Remmina-status.svg
%{_datadir}/icons/hicolor/apps/*.svg
%{_datadir}/mime/packages/*.xml
%{_datadir}/%{name}/
%dir %{_libdir}/remmina/
%dir %{_libdir}/remmina/plugins/
%{_mandir}/man1/%{name}.*
%{_mandir}/man1/%{name}-file-wrapper.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake

%files plugins-exec
%{_libdir}/remmina/plugins/remmina-plugin-exec.so

%files plugins-secret
%{_libdir}/remmina/plugins/remmina-plugin-secret.so

%files plugins-rdp
%{_libdir}/remmina/plugins/remmina-plugin-rdp.so
%{_datadir}/icons/hicolor/*/emblems/org.remmina.Remmina-rdp-ssh-symbolic.svg
%{_datadir}/icons/hicolor/*/emblems/org.remmina.Remmina-rdp-symbolic.svg

%files plugins-vnc
%{_libdir}/remmina/plugins/remmina-plugin-vnc.so
%{_datadir}/icons/hicolor/*/emblems/org.remmina.Remmina-vnc-ssh-symbolic.svg
%{_datadir}/icons/hicolor/*/emblems/org.remmina.Remmina-vnc-symbolic.svg

%if 0%{?fedora} || 0%{?rhel} == 8
%files plugins-spice
%{_libdir}/remmina/plugins/remmina-plugin-spice.so
%{_datadir}/icons/hicolor/*/emblems/org.remmina.Remmina-spice-ssh-symbolic.svg
%{_datadir}/icons/hicolor/*/emblems/org.remmina.Remmina-spice-symbolic.svg
%endif

%files plugins-www
%{_libdir}/remmina/plugins/remmina-plugin-www.so

%files plugins-kwallet
%{_libdir}/remmina/plugins/remmina-plugin-kwallet.so

%files plugins-python
%{_libdir}/remmina/plugins/remmina-plugin-python_wrapper.so

%if 0%{?fedora} || 0%{?rhel} == 8
%files plugins-x2go
%{_libdir}/remmina/plugins/remmina-plugin-x2go.so
%{_datadir}/icons/hicolor/*/emblems/org.remmina.Remmina-x2go-ssh-symbolic.svg
%{_datadir}/icons/hicolor/*/emblems/org.remmina.Remmina-x2go-symbolic.svg
%endif

%files gnome-session
%{_bindir}/gnome-session-remmina
%{_bindir}/remmina-gnome
%{_datadir}/gnome-session/sessions/remmina-gnome.session
%{_datadir}/xsessions/remmina-gnome.desktop
%{_mandir}/man1/gnome-session-remmina.1*
%{_mandir}/man1/remmina-gnome.1*

%changelog
* Mon Dec 23 2024 Daniel Milnes <daniel@daniel-milnes.uk> - 1.4.37-1
- Update to 1.4.37 rhbz#2333334

* Sat Dec 07 2024 Daniel Milnes <daniel@daniel-milnes.uk> - 1.4.36-2
- Backport fix for SSH crash

* Mon Nov 18 2024 Daniel Milnes <daniel@daniel-milnes.uk> - 1.4.36-1
- Update to 1.4.36 rhbz#2316118

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.35-2
- Rebuilt for Python 3.13

* Thu Apr 4 2024 Daniel Milnes <daniel@daniel-milnes.uk> - 1.4.35-1
- Update to 1.4.35 rhbz#2263194
- Migrate to FreeRDP3 rhbz#2263485 rhbz#2261649

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 10 2023 Jonathan Wright <jonathan@almalinux.org> - 1.4.33-1
- Update to 1.4.33 rhbz#2240240
- Recommends openh264 on Fedora rhbz#2242462

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 1.4.32-2
- rebuild for new libsodium

* Fri Sep 15 2023 Jonathan Wright <jonathan@almalinux.org> - 1.4.32-1
- Update to 1.4.32 rhbz#2239158

* Tue Aug 22 2023 René Genz <liebundartig@freenet.de> - 1.4.31-4
- Fix typing mistake
 
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.4.31-2
- Rebuilt for Python 3.12

* Wed Jun 07 2023 Phil Wyett <philip.wyett@kathenas.org> - 1.4.31-1
- New upstream version 1.4.31.
- Remove no longer needed patches.

* Tue Jun 06 2023 Phil Wyett <philip.wyett@kathenas.org> - 1.4.30-3
- Remove some old workarounds from spec file.

* Thu Apr 20 2023 Phil Wyett <philip.wyett@kathenas.org> - 1.4.30-2
- Add patch: 0001_remmina_fix_vnc_crash_domain_socket.patch

* Mon Apr 10 2023 Phil Wyett <philip.wyett@kathenas.org> - 1.4.30-1
- New upstream version 1.4.30.
- Use SPDX license identifiers.
- Remove no longer needed patches.

* Tue Feb 28 2023 Phil Wyett <philip.wyett@kathenas.org> - 1.4.29-5
- Add patch: 0003_remmina_rdp_monitor_get_fix_maxw_maxh_and_monitorids_calculation.patch

* Mon Jan 23 2023 Phil Wyett <philip.wyett@kathenas.org> - 1.4.29-4
- Fix flatpak build - Yaakov Selkowitz <yselkowi@redhat.com>.
- Make Fedora greater than or equal to 37 use libsoup3 and webkit2gtk-4.1.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Phil Wyett <philip.wyett@kathenas.org> - 1.4.29-2
- Add patch: 0001_add_mime_text_formats_for_rdp_clibpoard.patch
- Add patch: 0002_fix_unlock_crash.patch

* Wed Dec 21 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.29-1
- New upstream version 1.4.29.

* Sat Dec 03 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.28-1
- New upstream version 1.4.28.

* Mon Oct 10 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.27-6
- Add patch: libsoup_2_and_3_support.patch

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.27-4
- Install CHANGELOG.md not no longer updated ChangeLog file.

* Wed Jun 29 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.27-3
- Enable libappindicator on all, including EL 9.

* Sat Jun 25 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.27-2
- Add patch: various_rdp_fixes_from_upstream.patch

* Mon Jun 20 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.27-1
- New upstream version 1.4.27.
- Drop patches as no longer needed.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.26-4
- Rebuilt for Python 3.11

* Mon Jun 06 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.26-3
- Add patch: 0001_paste_as_keystrokes_fix_git_partial_eb3d59fb.patch
- Add libssh BuildRequires minimum required version of 0.8.0.
- Remove EL7 build support due to new libssh minimum required version.
- Remove telepathy plugin activation switch as no longer required.
- Eliminate cmake build folder warning.

* Thu May 19 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.26-2
- Add some missing BuildRequires for calrity.
- Correctly disable spice plugin on EL9.

* Wed May 18 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.26-1
- New upstream version 1.4.26.
  - New python plugin enabled.
- Drop patches as no longer needed.
- EL9
  - Disable avahi-ui and avahi-ui-gtk support.
  - Disable libappindicator support.
  - Disable spice plugin.
  - Disable x2go plugin.

* Mon Mar 28 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.25-2
- Add patch: 0001_vnc_close_all_close_git_55e2324a.patch
- Add patch: 0002_rdp_possible_segv_git_3620efda.patch

* Fri Mar 11 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.25-1
- New upstream version 1.4.25.

* Wed Mar 09 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.24-4
- Add patch: 0003_honour_soft_links_git_ee00da15.patch
- Add patch: 0004_freerdp_offscreen_support_level_type_git_f58d22d6.patch

* Sun Feb 27 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.24-3
- Add patch: 0001_fix_rare_crash_git_2609548e_and_9ed4c438.patch.
- Add patch: 0002_drop_gnome_mediakeys_plugin_git_c901beef.patch.
- Remove unneeded creation of 'build' folder.

* Sat Feb 12 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.24-2
- Remove XDMCP reference from remmina package description.
- Remove pyhoca-cli BuildRrequires. Only Requires on x2go now required.
- Use upstream projects HTTPS URL.

* Thu Feb 10 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.24-1
- New upstream version 1.4.24.

* Sun Jan 23 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.23-4
- Add missing xdg-utils BuildRequires for generation of icon and theme caches.
- Modify conditional to exclude el7 only from aarch64 builds. Will
  now enable building for el8 and above.
- Add scriptlets for updating of icon cache on el7 as not automatic.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.23-2
- Remove unneeded BuildRequires for gtk-vnc-2.0.
  libvncserver is the preferred for VNC and disables the gvnc plugin if found.
  We have not in the recent past built the gvnc plugin.

* Wed Jan 19 2022 Phil Wyett <philip.wyett@kathenas.org> - 1.4.23-1
- New upstream version 1.4.23.
- Enable x2go plugin.

* Wed Nov 10 2021 Simone Caronni <negativo17@gmail.com> - 1.4.21-1
- Update to 1.4.21.

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.4.20-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Simone Caronni <negativo17@gmail.com> - 1.4.20-1
- Update to 1.4.20.
- Remove unmaintained nx, st, xdmcp plugins.

* Wed Jun 30 2021 Simone Caronni <negativo17@gmail.com> - 1.4.19-1
- Update to 1.4.19.

* Sat Jun 05 2021 Simone Caronni <negativo17@gmail.com> - 1.4.18-1
- Update to 1.4.18.

* Wed May 26 2021 Simone Caronni <negativo17@gmail.com> - 1.4.17-1
- Update to 1.4.17.
- Disable news at every update.

* Tue May 11 2021 Simone Caronni <negativo17@gmail.com> - 1.4.16-1
- Update to 1.4.16.

* Tue May 11 2021 Simone Caronni <negativo17@gmail.com> - 1.4.15-1
- Update to 1.4.15.

* Mon May 10 2021 Simone Caronni <negativo17@gmail.com> - 1.4.14-1
- Update to 1.4.14.

* Thu Apr 15 2021 Simone Caronni <negativo17@gmail.com> - 1.4.13-2
- Rebuild for updated FreeRDP.

* Tue Mar 30 2021 Simone Caronni <negativo17@gmail.com> - 1.4.13-1
- Update to 1.4.13.

* Thu Mar 11 2021 Simone Caronni <negativo17@gmail.com> - 1.4.12-1
- Update to 1.4.12.

* Wed Feb 03 2021 Simone Caronni <negativo17@gmail.com> - 1.4.11-1
- Update to 1.4.11.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Simone Caronni <negativo17@gmail.com> - 1.4.10-1
- Update to 1.4.10.

* Mon Nov 30 2020 Simone Caronni <negativo17@gmail.com> - 1.4.9-2
- Fix build on CentOS/RHEL 7.

* Mon Nov 30 2020 Simone Caronni <negativo17@gmail.com> - 1.4.9-1
- Update to 1.4.9.

* Fri Sep 11 2020 Simone Caronni <negativo17@gmail.com> - 1.4.8-1
- Update to 1.4.8.

* Mon Sep 07 2020 Than Ngo <than@redhat.com> - 1.4.7-4
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Simone Caronni <negativo17@gmail.com> - 1.4.7-1
- Update to 1.4.7.

* Fri May 22 2020 Simone Caronni <negativo17@gmail.com> - 1.4.4-1
- Update to 1.4.4.

* Tue Feb 25 2020 Simone Caronni <negativo17@gmail.com> - 1.4.1-1
- Update to 1.4.1.

* Sun Feb 09 2020 Simone Caronni <negativo17@gmail.com> - 1.3.10-2
- Backport patch to fix build with default GCC 10 options.

* Fri Feb 07 2020 Simone Caronni <negativo17@gmail.com> - 1.3.10-1
- Update to 1.3.10.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Simone Caronni <negativo17@gmail.com> - 1.3.6-1
- Update to 1.3.6.

* Fri Sep 06 2019 Simone Caronni <negativo17@gmail.com> - 1.3.5-3
- Allow building on RHEL/CentOS 7.

* Tue Aug 20 2019 Simone Caronni <negativo17@gmail.com> - 1.3.5-2
- Enable KDE Wallet plugin.

* Tue Aug 20 2019 Simone Caronni <negativo17@gmail.com> - 1.3.5-1
- Update to 1.3.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Simone Caronni <negativo17@gmail.com> - 1.3.4-1
- Update to 1.3.4.

* Thu Feb 28 2019 Simone Caronni <negativo17@gmail.com> - 1.3.3-1
- Update to 1.3.3.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Simone Caronni <negativo17@gmail.com> - 1.2.32.1-1
- Update to 1.2.32.1.

* Mon Oct 15 2018 Simone Caronni <negativo17@gmail.com> - 1.2.32-1
- Update to 1.2.32, new Simple Terminal plugin.
- Project moved to Gitlab, update spec file accordingly.

* Mon Aug 20 2018 Simone Caronni <negativo17@gmail.com> - 1.2.31.3-1
- Update to 1.2.31.3.

* Tue Aug 14 2018 Mike DePaulo <mikedep333@gmail.com> - 1.2.31.2-1
- Update to latest stable release 1.2.31.2
- Add remmina-gnome-session subpackage for new Kiosk mode

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.52.20180408.git.6b62986
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.51.20180408.git.6b62986
- Update to latest snapshot (rcgit.29).

* Wed Mar 21 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.50.20180321.git.f467f19
- New snapshot, removes duplicate icon.

* Mon Mar 19 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.49.20180319.git.5f3cc40
- Move checks in the check section.
- New source snapshot (#1553098, #1557572).

* Thu Mar 15 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.48.20180314.git.04e4a99
- Update to latest snapshot post rc27.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.47.20180107.git.d70108c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-0.46.20180107.git.d70108c
- Remove obsolete scriptlets

* Tue Jan 16 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.45.20180107.git.d70108c
- Update to latest snapshot.

* Fri Jan 05 2018 Pavel Alexeev <Pahan@Hubbitus.info> - 1.2.0-0.44.rcgit.26
- Update to version v1.2.0-rcgit.26.
- Drop remmina-format-security.patch which seams handled upstream in different way.

* Wed Dec 20 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.43.20171220git08f5b4b
- Update to latest 1.2.0 snapshot (rcgit.25).
- Gnome plugin renamed to secret.
- Add new executor plugin.

* Mon Sep 11 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.42.20170908git205df66
- Update to latest snapshot.
- Trim changelog.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.41.20170724git0387ee0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.40.20170724git0387ee0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 27 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.39.20170724git0387ee0
- Update to latest snapshot (matching with rcgit 19).

* Wed Jul 12 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.38.20170710git89009c8
- Update to latest snapshot.

* Mon Jun 26 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.37.20170622git7e82138
- Rebuild for FreeRDP update.

* Mon Jun 26 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.36.20170622git7e82138
- Update to latest snapshot.

* Mon May 15 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.35.20170510git41c8de6
- Update to latest snapshot.

* Mon Apr 24 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.34.20170424git2c0a77e
- Update to latest snapshot.

* Wed Mar 22 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.33.20170317git4d8d257
- Update to latest snapshot.

* Thu Mar 09 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.32.20170302git1da1fb6
- Remove non-working telepathy plugin.

* Thu Mar 02 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.31.20170302git1da1fb6
- Update to latest snapshot.

* Wed Feb 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0-0.30.20161226gitd1a4a73
- rebuild (libvncserver)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.29.20161226gitd1a4a73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.28.20161226gitd1a4a73
- Switch to latest snapshot of the next branch.

* Sat Dec 03 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.27.20161126git35604d5
- Update to latest code drop from the libfreerdp_updates branch.

* Fri Nov 04 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.26.20161104git80a77b8
- Update to latest snapshot.
- Still not building properly with FreeRDP:
  https://github.com/FreeRDP/Remmina/issues/1028

* Fri Oct 14 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.25.20161010gitaeaae39
- Update to latest snapshot.

* Sat Oct 08 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.24.20161004git88f490d
- Update to latest snapshot.

* Tue Sep 20 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.23.20160914git42f5a87
- Update to latest snapshot, update release to follow packaging guidelines.

* Sat Aug 27 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 1.2.0-0.22.git.679bb8e
- Provide GIT_REVISION to cmake for use in version.

* Tue Aug 16 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 1.2.0-0.21.git.679bb8e
- Update to try solve issues with tray icons - https://github.com/FreeRDP/Remmina/issues/944#issuecomment-239913278
- Drop old issue 292 hack.
- Conditionally allow build by hash or pre-releases.

* Fri Aug 12 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.20.git.cbcb19e
- Update to latest snapshot.

* Thu Jun 23 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.19.rcgit.14
- Rebuild for spice-gtk upgrade.

* Tue Jun 21 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.18.rcgit.14
- Update to version 1.2.0-rcgit.14.

* Tue Jun 07 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.17.rcgit.13
- Use "snapshot" name only once in the SPEC file.

* Tue Jun 07 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.16.rcgit.12
- Update to version 12.0-rcgit.13, enable SPICE plugin, update cmake options.

* Fri May 20 2016 David Woodhouse <dwmw2@infradead.org> - 1.2.0-0.15.rcgit.12
- Disable survey, as it has build problems

* Fri May 20 2016 David Woodhouse <dwmw2@infradead.org> - 1.2.0-0.14.rcgit.12
- Update to version 12.0-rcgit.12.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.13.rcgit.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 02 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 1.2.0-0.12.rcgit.7
- Update to version 1.2.0-rcgit.7.

* Fri Jan 01 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 1.2.0-0.11.git.b43697d
- Recommends all plugins by suggestion bz#1241658.
