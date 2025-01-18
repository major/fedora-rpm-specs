%global systemd_unit_handover gnome-remote-desktop-handover.service
%global systemd_unit_headless gnome-remote-desktop-headless.service
%global systemd_unit_system gnome-remote-desktop.service
%global systemd_unit_user gnome-remote-desktop.service

%global tarball_version %%(echo %{version} | tr '~' '.')

%bcond rdp %[0%{?fedora} || 0%{?rhel} >= 10]
%bcond vnc %[0%{?fedora} || 0%{?rhel} < 10]

%global libei_version 1.0.901
%global pipewire_version 0.3.49

Name:           gnome-remote-desktop
Version:        47.2
Release:        2%{?dist}
Summary:        GNOME Remote Desktop screen share service

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-remote-desktop
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

# Adds encryption support (requires patched LibVNCServer)
Patch0:         gnutls-anontls.patch

BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  meson >= 0.47.0
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ffnvcodec)
%if %{with rdp}
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(freerdp3)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(winpr3)
%endif
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0) >= 2.68
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libei-1.0) >= %{libei_version}
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libsecret-1)
%if %{with vnc}
BuildRequires:  pkgconfig(libvncserver) >= 0.9.11-7
%endif
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(tss2-mu)
BuildRequires:  pkgconfig(tss2-rc)
BuildRequires:  pkgconfig(tss2-tctildr)

Requires:       libei%{?_isa} >= %{libei_version}
Requires:       pipewire%{?_isa} >= %{pipewire_version}

Obsoletes:      vino < 3.22.0-21

%description
GNOME Remote Desktop is a remote desktop and screen sharing service for the
GNOME desktop environment.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson \
%if %{with rdp}
    -Drdp=true \
%else
    -Drdp=false \
%endif
%if %{with vnc}
    -Dvnc=true \
%else
    -Dvnc=false \
%endif
    -Dsystemd=true \
    -Dtests=false
%meson_build


%install
%meson_install

%find_lang %{name}


%post
%systemd_post %{systemd_unit_system}
%systemd_user_post %{systemd_unit_handover}
%systemd_user_post %{systemd_unit_headless}
%systemd_user_post %{systemd_unit_user}


%preun
%systemd_preun %{systemd_unit_system}
%systemd_user_preun %{systemd_unit_handover}
%systemd_user_preun %{systemd_unit_headless}
%systemd_user_preun %{systemd_unit_user}


%postun
%systemd_postun_with_restart %{systemd_unit_system}
%systemd_user_postun_with_restart %{systemd_unit_handover}
%systemd_user_postun_with_restart %{systemd_unit_headless}
%systemd_user_postun_with_restart %{systemd_unit_user}


%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/grdctl
%{_libexecdir}/gnome-remote-desktop-daemon
%{_libexecdir}/gnome-remote-desktop-enable-service
%{_libexecdir}/gnome-remote-desktop-configuration-daemon
%{_userunitdir}/%{systemd_unit_user}
%{_userunitdir}/%{systemd_unit_headless}
%{_userunitdir}/%{systemd_unit_handover}
%{_unitdir}/%{systemd_unit_system}
%{_unitdir}/gnome-remote-desktop-configuration.service
%{_datadir}/applications/org.gnome.RemoteDesktop.Handover.desktop
%{_datadir}/dbus-1/system-services/org.gnome.RemoteDesktop.Configuration.service
%{_datadir}/dbus-1/system.d/org.gnome.RemoteDesktop.conf
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml
%{_datadir}/polkit-1/actions/org.gnome.remotedesktop.configure-system-daemon.policy
%{_datadir}/polkit-1/actions/org.gnome.remotedesktop.enable-system-daemon.policy
%{_datadir}/polkit-1/rules.d/20-gnome-remote-desktop.rules
%{_sysusersdir}/gnome-remote-desktop-sysusers.conf
%{_tmpfilesdir}/gnome-remote-desktop-tmpfiles.conf

%if %{with rdp}
%{_datadir}/gnome-remote-desktop/
%endif
%{_mandir}/man1/grdctl.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 nmontero <nmontero@redhat.com> - 47.2-1
- Update to 47.2

* Tue Oct 22 2024 nmontero <nmontero@redhat.com> - 47.1-1
- Update to 47.1

* Mon Sep 16 2024 nmontero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Sun Sep 01 2024 David King <amigadave@amigadave.com> - 47~rc-1
- Update to 47.rc

* Wed Aug 14 2024 nmontero <nmontero@redhat.com> - 47~beta-1
- Update to 47.beta

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 David King <amigadave@amigadave.com> - 47~alpha-1
- Update to 47.alpha

* Thu May 23 2024 Nieves Montero <nmontero@redhat.com> - 46.2-1
- Update to 46.2

* Thu Apr 18 2024 David King <amigadave@amigadave.com> - 46.1-1
- Update to 46.1

* Thu Mar 28 2024 Adam Williamson <awilliam@redhat.com> - 46.0-2
- Correct systemd macros

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 24 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 45.1-2
- Disable VNC in RHEL 10+

* Sun Oct 22 2023 Kalev Lember <klember@redhat.com> - 45.1-1
- Update to 45.1

* Sat Oct 21 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Tue Sep 05 2023 Kalev Lember <klember@redhat.com> - 45.rc-1
- Update to 45.rc

* Fri Aug 11 2023 Kalev Lember <klember@redhat.com> - 45.beta-1
- Update to 45.beta

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 45.alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Jonas Ådahl <jadahl@redhat.com> - 45~alpha-1
- Update to 45.alpha

* Wed May 31 2023 Kalev Lember <klember@redhat.com> - 44.2-1
- Update to 44.2

* Mon Apr 24 2023 David King <amigadave@amigadave.com> - 44.1-1
- Update to 44.1

* Sun Mar 19 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Thu Mar 16 2023 Jonas Ådahl <jadahl@redhat.com> - 44~rc-2
- Enable RDP in ELN

* Sun Mar 05 2023 David King <amigadave@amigadave.com> - 44~rc-1
- Update to 44.rc

* Mon Feb 06 2023 David King <amigadave@amigadave.com> - 44~alpha-1
- Update to 44.alpha

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 David King <amigadave@amigadave.com> - 43.2-1
- Update to 43.2

* Tue Nov 08 2022 Stephen Gallagher <sgallagh@redhat.com> - 43.1-2
- Fix build on RHEL 9+/ELN

* Thu Oct 27 2022 David King <amigadave@amigadave.com> - 43.1-1
- Update to 43.1

* Tue Sep 20 2022 Jonas Ådahl <jadahl@redhat.com> - 43.0
- Update to 43.0

* Thu Aug 18 2022 Jonas Ådahl <jadahl@redhat.com> - 43~beta-4
- Drop dependency on tpm2-abrmd

* Tue Aug 16 2022 Kalev Lember <klember@redhat.com> - 43~beta-3
- Avoid manual requires on tss2* and rely on automatic soname deps instead

* Mon Aug 15 2022 Simone Caronni <negativo17@gmail.com> - 43~beta-2
- Rebuild for updated FreeRDP.

* Thu Aug 11 2022 Jonas Ådahl <jadahl@redhat.com> - 43~beta
- Update to 43.beta

* Fri Jul 29 2022 Tomas Popela <tpopela@redhat.com> - 43~alpha-2
- FreeRDP is built without server support in RHEL and ELN so we should disable
  the RDP there

* Thu Jul 28 2022 Jonas Ådahl <jadahl@redhat.com> - 43~alpha
- Update to 43.alpha

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 David King <amigadave@amigadave.com> - 42.3-1
- Update to 43.3 (#2091415)

* Sun May 29 2022 David King <amigadave@amigadave.com> - 42.2-1
- Update to 42.2

* Wed May 11 2022 David King <amigadave@amigadave.com> - 42.1.1-1
- Update to 42.1.1 (#2061546)

* Wed Apr 27 2022 David King <amigadave@amigadave.com> - 42.1-2
- Fix isa macro in Requires

* Tue Apr 26 2022 David King <amigadave@amigadave.com> - 42.1-1
- Update to 42.1 (#2061546)

* Mon Mar 21 2022 Jonas Ådahl <jadahl@redhat.com> - 42.0
- Update to 42.0

* Mon Mar 14 2022 Jonas Ådahl <jadahl@redhat.com> - 42~rc-1
- Update to 42.rc

* Wed Feb 16 2022 Jonas Ådahl <jadahl@redhat.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Jonas Ådahl <jadahl@redhat.com> - 41.2-1
- Update to 41.2

* Mon Nov 01 2021 Kalev Lember <klember@redhat.com> - 41.1-1
- Update to 41.1

* Mon Sep 20 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Tue Sep 07 2021 Jonas Ådahl <jadahl@redhat.com> - 41~rc-1
- Bump to 41.rc

* Wed Aug 04 2021 Kalev Lember <klember@redhat.com> - 40.1-3
- Avoid systemd_requires as per updated packaging guidelines

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 03 2021 Jonas Ådahl <jadahl@redhat.com> - 40.1-1
- Bump to 40.1

* Thu Apr 15 2021 Simone Caronni <negativo17@gmail.com> - 40.0-2
- Rebuild for updated FreeRDP.

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Thu Mar 18 2021 Michael Catanzaro <mcatanzaro@redhat.com> - 40.0~rc-2
- Add Obsoletes: vino

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 40.0~rc-1
- Update to 40.rc

* Thu Mar 04 2021 Jonas Ådahl <jadahl@redhat.com> - 40.0~beta-1
- Bump to 40.beta

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Jonas Ådahl <jadahl@redhat.com> - 0.1.9-2
- Copy using the right destination stride

* Mon Sep 14 2020 Jonas Ådahl <jadahl@redhat.com> - 0.1.9-1
- Update to 0.1.9
- Backport race condition crash fix
- Rebase anon-tls patches

* Thu Aug 27 2020 Ray Strode <rstrode@redhat.com> - 0.1.8-3
- Fix crash
  Related: #1844993

* Mon Jun 1 2020 Felipe Borges <feborges@redhat.com> - 0.1.8-2
- Fix black screen issue in remote connections on Wayland

* Wed Mar 11 2020 Jonas Ådahl <jadahl@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 4 2019 Jonas Ådahl <jadahl@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 2 2018 Jonas Ådahl <jadahl@redhat.com> - 0.1.6-2
- Don't crash when PipeWire disconnects (rhbz#1632781)

* Tue Aug 7 2018 Jonas Ådahl <jadahl@redhat.com> - 0.1.6
- Update to 0.1.6
- Apply ANON-TLS patch
- Depend on pipewire 0.2.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Jonas Ådahl <jadahl@redhat.com> - 0.1.4-1
- Update to new version

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-5
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.2-3
- Use %%autosetup
- Install licence file

* Tue Aug 22 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.2-2
- Remove gschema compilation step as that had been deprecated

* Mon Aug 21 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.2-1
- Update to 0.1.2
- Changed tabs to spaces
- Added systemd user macros
- Install to correct systemd user unit directory
- Compile gsettings schemas after install and uninstall

* Mon Aug 21 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.1-1
- First packaged version
