%global libcall_ui_commit 619dd91561ad470db3d0e0e263ebc35d787afd2e

Name:		calls
Version:	43.0
Release:	1%{?dist}
Summary:	A phone dialer and call handler

License:	GPLv3+ and MIT
URL:		https://gitlab.gnome.org/GNOME/calls
Source0:	https://gitlab.gnome.org/GNOME/calls/-/archive/v43.0/%{name}-v43.0.tar.gz
Source1:	https://gitlab.gnome.org/World/Phosh/libcall-ui/-/archive/%{libcall_ui_commit}/libcall-ui-%{libcall_ui_commit}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	gcc-c++

BuildRequires:	pkgconfig(libcallaudio-0.1)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libhandy-1) >= 1.0.0
BuildRequires:	pkgconfig(gsound)
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(gom-1.0)
BuildRequires:	pkgconfig(libebook-contacts-1.2)
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(mm-glib)
BuildRequires:	pkgconfig(libfeedback-0.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	gstreamer1-plugins-good-gtk
BuildRequires:	sofia-sip-glib-devel

BuildRequires:	desktop-file-utils
BuildRequires:	/usr/bin/xvfb-run
BuildRequires:	/usr/bin/xauth
BuildRequires:	libappstream-glib
BuildRequires:  python3-docutils

Requires: hicolor-icon-theme

%description
A phone dialer and call handler.

%prep
%setup -a1 -q -n %{name}-v43.0

mv libcall-ui-%{libcall_ui_commit}/* subprojects/libcall-ui/

%build
%meson
%meson_build


%install
%meson_install

# Remove call-ui translations
rm %{buildroot}%{_datadir}/locale/ca/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/pt_BR/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/ro/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/uk/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fa/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fur/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/nl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/pt/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/sv/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/gl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/it/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/sl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fi/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/he/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/ka/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/oc/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/sr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/tr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/el/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/hr/LC_MESSAGES/call-ui.mo

# We do not support the ofono backend
rm -rf %{buildroot}%{_libdir}/calls/plugins/provider/ofono/

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Calls.metainfo.xml

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Calls.desktop

# Some tests are failing in the build environment, so we manually just run a handful for now.
LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test plugins
SH


%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/org.gnome.Calls-daemon.desktop
%{_bindir}/gnome-%{name}

%dir %{_libdir}/calls/plugins/provider

%dir %{_libdir}/calls/plugins/provider/mm
%dir %{_libdir}/calls/plugins/provider/dummy
%dir %{_libdir}/calls/plugins/provider/sip

%{_libdir}/calls/plugins/provider/mm/libmm.so
%{_libdir}/calls/plugins/provider/mm/mm.plugin
%{_libdir}/calls/plugins/provider/dummy/dummy.plugin
%{_libdir}/calls/plugins/provider/dummy/libdummy.so
%{_libdir}/calls/plugins/provider/sip/libsip.so
%{_libdir}/calls/plugins/provider/sip/sip.plugin

%{_datadir}/dbus-1/services/org.gnome.Calls.service
%{_datadir}/glib-2.0/schemas/org.gnome.Calls.gschema.xml
%{_datadir}/applications/org.gnome.Calls.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Calls.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Calls-symbolic.svg
%{_datadir}/metainfo/org.gnome.Calls.metainfo.xml

%{_mandir}/man1/gnome-calls.1*

%doc README.md
%license COPYING

%changelog
* Wed Sep 21 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 43.0-1
- Update to v43.0

* Sun Sep 04 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 43~rc.0-1
- Update to 43 rc 0

* Sat Aug 06 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 43~beta.0-1
- Update to 43 beta 0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 43~alpha.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kalev Lember <klember@redhat.com> - 43~alpha.1-2
- Rebuilt for evolution-data-server soname bump

* Thu Jun 02 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 43~.alpha.1-1
- Update to 43.alpha.1

* Sun Apr 24 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 42.0-1
- Update to 42.0

* Tue Mar 08 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 42.rc.1-1
- Update to 42.rc.1

* Fri Feb 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 42.rc.0-1
- Update to 42.rc.0

* Wed Jan 26 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 42~.beta.1-1
- update to 42.beta.1

* Tue Jan 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 42~.beta.0-1
- update to 42.beta.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42~.alpha.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 42~.alpha.0-1
- Update to 42.alpha.0

* Sat Oct 30 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 41.1-1
- Update to 41.1

* Mon Sep 20 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 41.0-1
- Update to 41.0

* Fri Sep 10 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 41.rc-1
- Update to 41.rc

* Sat Aug 14 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 41~.beta-1
- Update to 41.beta

* Sat Aug 07 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 41~.alpha-1
- Change source to new upstream location https://gitlab.gnome.org/GNOME/calls
- Update to 41.alpha

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 12 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Thu May 20 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.3-1
- Update version 0.3.3

* Mon May 03 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.2-1
- Update version 0.3.2

* Tue Feb 16 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.1-1
- Update version 0.3.1

* Sat Feb 13 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.0-1
- Update version 0.3.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-3
- Patch for callaudiod-0.1

* Tue Jan 12 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-2
- Bump for libcallaudio-0.1.so

* Wed Jan 06 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-1
- Update version 0.2.0

* Sun Nov 08 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.9-1
- Update version 0.1.9

* Fri Sep 18 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.8-1
- Update version 0.1.8

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.7-1
- Update version 0.1.7

* Wed Jun 24 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.6-2
- Rebuild for broken libebook-contacts

* Fri Jun 12 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.6-1
- Update version 0.1.6

* Mon May 18 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.5-1
- Owning the directories for calls, plugins, and mm.
- Update version 0.1.5.
- Adding MIT to License
- Upstream changed "appdata" to "metainfo"

* Fri Apr 24 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.4-1
- Updating version 0.1.4. Fixing comments from review regarding ofono and appdata.

* Fri Mar 27 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.3-1 
- Updating version 0.1.3. Adding tests

* Wed Mar 25 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.2-2
- Adding license and meson_test. Remove buildid

* Sun Mar 08 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.2-1
- Initial packaging
