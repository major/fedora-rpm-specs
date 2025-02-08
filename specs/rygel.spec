%global apiver 2.8

Name:          rygel
Version:       0.44.1
Release:       3%{?dist}
Summary:       A collection of UPnP/DLNA services

License:       LGPL-2.1-or-later AND CC-BY-SA-3.0
URL:           https://wiki.gnome.org/Projects/Rygel
Source0:       https://download.gnome.org/sources/%{name}/0.44/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: docbook-style-xsl
BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: libunistring-devel
BuildRequires: meson
BuildRequires: systemd-rpm-macros
BuildRequires: vala
BuildRequires: valadoc
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gst-editing-services-1.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gupnp-1.6)
BuildRequires: pkgconfig(gupnp-av-1.0)
BuildRequires: pkgconfig(gupnp-dlna-2.0)
BuildRequires: pkgconfig(libmediaart-2.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(tracker-sparql-3.0)
BuildRequires: /usr/bin/xsltproc

%description
Rygel is a home media solution that allows you to easily share audio, video and
pictures, and control of media player on your home network. In technical terms
it is both a UPnP AV MediaServer and MediaRenderer implemented through a plug-in
mechanism. Interoperability with other devices in the market is achieved by
conformance to very strict requirements of DLNA and on the fly conversion of
media to format that client devices are capable of handling.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package tracker
Summary: Tracker plugin for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tracker
A plugin for rygel to use tracker to locate media on the local machine.

%prep
%autosetup -p1

%build
%meson \
  -Dapi-docs=true \
  -Dexamples=false
%meson_build

%install
%meson_install

%find_lang %{name}

%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%check
# Verify the desktop files
desktop-file-validate %{buildroot}/%{_datadir}/applications/rygel.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/rygel-preferences.desktop

%files -f %{name}.lang
%license COPYING COPYING.logo
%doc AUTHORS NEWS README.md
%config(noreplace) %{_sysconfdir}/rygel.conf
%{_bindir}/rygel
%{_bindir}/rygel-preferences
%{_libdir}/librygel-core-%{apiver}.so.0*
%{_libdir}/librygel-db-%{apiver}.so.0*
%{_libdir}/librygel-renderer-%{apiver}.so.0*
%{_libdir}/librygel-renderer-gst-%{apiver}.so.0*
%{_libdir}/librygel-ruih-%{apiver}.so.0*
%{_libdir}/librygel-server-%{apiver}.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/RygelCore-%{apiver}.typelib
%{_libdir}/girepository-1.0/RygelRenderer-%{apiver}.typelib
%{_libdir}/girepository-1.0/RygelRendererGst-%{apiver}.typelib
%{_libdir}/girepository-1.0/RygelServer-%{apiver}.typelib
%{_libdir}/rygel-%{apiver}/engines/librygel-media-engine-gst.so
%{_libdir}/rygel-%{apiver}/engines/librygel-media-engine-simple.so
%{_libdir}/rygel-%{apiver}/engines/media-engine-gst.plugin
%{_libdir}/rygel-%{apiver}/engines/media-engine-simple.plugin
%{_libdir}/rygel-%{apiver}/plugins/librygel-external.so
%{_libdir}/rygel-%{apiver}/plugins/external.plugin
%{_libdir}/rygel-%{apiver}/plugins/librygel-gst-launch.so
%{_libdir}/rygel-%{apiver}/plugins/gst-launch.plugin
%{_libdir}/rygel-%{apiver}/plugins/librygel-media-export.so
%{_libdir}/rygel-%{apiver}/plugins/media-export.plugin
%{_libdir}/rygel-%{apiver}/plugins/librygel-mpris.so
%{_libdir}/rygel-%{apiver}/plugins/mpris.plugin
%{_libdir}/rygel-%{apiver}/plugins/librygel-ruih.so
%{_libdir}/rygel-%{apiver}/plugins/ruih.plugin
%{_libdir}/rygel-%{apiver}/plugins/librygel-playbin.so
%{_libdir}/rygel-%{apiver}/plugins/playbin.plugin
%{_libexecdir}/rygel/
%{_datadir}/rygel/
%{_datadir}/applications/rygel*
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service
%{_datadir}/icons/hicolor/*/apps/rygel*
%{_mandir}/man1/rygel.1*
%{_mandir}/man5/rygel.conf.5*
%{_userunitdir}/rygel.service

%files tracker
%{_libdir}/rygel-%{apiver}/plugins/librygel-tracker3.so
%{_libdir}/rygel-%{apiver}/plugins/tracker3.plugin

%files devel
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/librygel*
%{_libdir}/librygel-*.so
%{_includedir}/rygel-%{apiver}
%{_libdir}/pkgconfig/rygel*.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/RygelCore-%{apiver}.gir
%{_datadir}/gir-1.0/RygelRenderer-%{apiver}.gir
%{_datadir}/gir-1.0/RygelRendererGst-%{apiver}.gir
%{_datadir}/gir-1.0/RygelServer-%{apiver}.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/rygel*.deps
%{_datadir}/vala/vapi/rygel*.vapi

%changelog
* Thu Feb 06 2025 Nieves Montero <nmontero@redhat.com> - 0.44.1-3
- Rebuild for the renaming of tracker to tinysparql

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 13 2024 David King <amigadave@amigadave.com> - 0.44.1-1
- Update to 0.44.1

* Wed Sep 18 2024 nmontero <nmontero@redhat.com> - 0.44.0-1
- Update to 0.44.0

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Nieves Montero <nmontero@redhat.com> - 0.43.0-1
- Update to 0.43.0

* Tue May 07 2024 David King <amigadave@amigadave.com> - 0.42.6-1
- Update to 0.42.6

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Kalev Lember <klember@redhat.com> - 0.42.5-1
- Update to 0.42.5

* Wed Aug 02 2023 Kalev Lember <klember@redhat.com> - 0.42.4-1
- Update to 0.42.4

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 24 2023 David King <amigadave@amigadave.com> - 0.42.3-1
- Update to 0.42.3

* Mon Apr 03 2023 David King <amigadave@amigadave.com> - 0.42.2-1
- Update to 0.42.2

* Wed Feb 15 2023 David King <amigadave@amigadave.com> - 0.42.1-1
- Update to 0.42.1

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 10 2022 David King <amigadave@amigadave.com> - 0.42.0-2
- Fix devel subpackage installation (#2152302)

* Mon Nov 21 2022 David King <amigadave@amigadave.com> - 0.42.0-1
- Update to 0.42.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 David King <amigadave@amigadave.com> - 0.40.4-1
- Update to 0.40.4

* Sun Jan 23 2022 David King <amigadave@amigadave.com> - 0.40.3-1
- Update to 0.40.3
- Use pkgconfig for BuildRequires

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Kalev Lember <klember@redhat.com> - 0.40.2-1
- Update to 0.40.2

* Fri Aug 20 2021 Kalev Lember <klember@redhat.com> - 0.40.1-4
- Rebuilt for gupnp-av and gupnp-dlna soname bumps

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 20 2021 Kalev Lember <klember@redhat.com> - 0.40.1-2
- Build tracker 3.0 plugin, disable tracker 2.0
- Fix directory ownership for gtk-doc, gir and vala directories

* Sat Feb 20 2021 Kalev Lember <klember@redhat.com> - 0.40.1-1
- Update to 0.40.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 0.40.0-1
- Update to 0.40.0

* Tue Aug 18 2020 Kalev Lember <klember@redhat.com> - 0.39.2-1
- Update to 0.39.2
- Switch to the meson build system
- Tighten soname globs

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Kalev Lember <klember@redhat.com> - 0.38.3-1
- Update to 0.38.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 0.36.2-2
- Rebuilt against fixed atk (#1626575)

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 0.36.2-1
- Update to 0.36.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 06 2018 Kalev Lember <klember@redhat.com> - 0.36.1-1
- Update to 0.36.1
- Drop ldconfig scriptlets

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.36.0-3
- Switch to %%ldconfig_scriptlets

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.36.0-2
- Remove obsolete scriptlets

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 0.36.0-1
- Update to 0.36.0

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 0.35.0-1
- Update to 0.35.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 0.34.0-1
- Update to 0.34.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 0.33.92-1
- Update to 0.33.92

* Mon Mar 06 2017 Kalev Lember <klember@redhat.com> - 0.33.90-1
- Update to 0.33.90

* Tue Feb 14 2017 Richard Hughes <rhughes@redhat.com> - 0.33.1-1
- Update to 0.33.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 0.32.1-1
- Update to 0.32.1

* Tue Sep 20 2016 Kalev Lember <klember@redhat.com> - 0.32.0-1
- Update to 0.32.0

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 0.31.6-1
- Update to 0.31.6
- Move desktop file verification to the check section

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 0.31.5-1
- Update to 0.31.5
- Don't set group tags

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 0.31.4-1
- Update to 0.31.4
- Ship man pages

* Wed Jul 20 2016 Richard Hughes <rhughes@redhat.com> - 0.31.3-1
- Update to 0.31.3

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 0.31.2-1
- Update to 0.31.2

* Mon May 23 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.31.1-1
- Update to 0.31.1

* Tue Apr 26 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.31.0-1
- Update to 0.31.0

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 0.30.1-1
- Update to 0.30.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 0.30.0-1
- Update to 0.30.0

* Tue Mar 15 2016 Kalev Lember <klember@redhat.com> - 0.29.5-1
- Update to 0.29.5

* Tue Mar 01 2016 Richard Hughes <rhughes@redhat.com> - 0.29.4-1
- Update to 0.29.4

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 0.29.3-1
- Update to 0.29.3

* Thu Feb 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.29.2-1
- Update to 0.29.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 0.29.1-1
- Update to 0.29.1
- Update upstream URLs

* Mon Dec 14 2015 Debarshi Ray <rishi@fedoraproject.org> - 0.28.2-1
- Update to 0.28.2

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 0.28.1-1
- Update to 0.28.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 0.27.6-1
- Update to 0.27.6

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 0.27.5-1
- Update to 0.27.5

* Mon Aug 17 2015 Kalev Lember <klember@redhat.com> - 0.27.4-1
- Update to 0.27.4
- Use make_install macro

* Tue Jul 28 2015 Kalev Lember <klember@redhat.com> - 0.27.3-1
- Update to 0.27.3

* Tue Jun 30 2015 Kalev Lember <klember@redhat.com> - 0.27.2-1
- Update to 0.27.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 0.27.1-1
- Update to 0.27.1

* Sun May 10 2015 Kalev Lember <kalevlember@gmail.com> - 0.26.1-1
- Update to 0.26.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 0.26.0-1
- Update to 0.26.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 0.25.3-1
- Update to 0.25.3
- Use license macro for the COPYING file
- Tighten deps with the _isa macro

* Thu Feb 19 2015 Richard Hughes <rhughes@redhat.com> - 0.25.2.1-1
- Update to 0.25.2.1

* Tue Feb 17 2015 Richard Hughes <rhughes@redhat.com> - 0.25.2-1
- Update to 0.25.2

* Tue Jan 20 2015 Richard Hughes <rhughes@redhat.com> - 0.25.1-1
- Update to 0.25.1

* Fri Dec 19 2014 Richard Hughes <rhughes@redhat.com> - 0.25.0-1
- Update to 0.25.0

* Mon Nov 10 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.24.2-1
- Update to 0.24.2

* Tue Oct 14 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.24.1-1
- Update to 0.24.1

* Tue Sep 23 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.24.0-1
- Update to 0.24.0

* Tue Sep 02 2014 Pádraig Brady <pbrady@redhat.com> - 0.23.3.1-2
- rebuild for libunistring soname bump

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 0.23.3.1-1
- Update to 0.23.3.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.23.2-3
- Rebuilt once more for tracker

* Mon Jul 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.23.2-2
- rebuild (tracker)

* Wed Jul 23 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.23.2-1
- Update to 0.23.2

* Thu Jun 26 2014 Richard Hughes <rhughes@redhat.com> - 0.23.1.1-1
- Update to 0.23.1.1

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 0.23.1-1
- Update to 0.23.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.22.2-1
- Update to 0.22.2

* Mon Apr 21 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.22.1-1
- Update to 0.22.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 0.22.0-1
- Update to 0.22.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 0.21.6-1
- Update to 0.21.6

* Sat Mar 08 2014 Richard Hughes <rhughes@redhat.com> - 0.21.5-1
- Update to 0.21.5

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 0.21.4-1
- Update to 0.21.4

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 0.21.3-1
- Update to 0.21.3

* Mon Dec 23 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.21.2.1-1
- Update to 0.21.2.1
- Call ldconfig in post scriptlets (fixes RHBZ 1045745)

* Mon Nov 18 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.21.1-1
- Update to 0.21.1

* Mon Nov  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.21.0-1
- Update to 0.21.0

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 0.20.1-1
- Update to 0.20.1

* Wed Sep 25 2013 Richard Hughes <rhughes@redhat.com> - 0.20.0-1
- Update to 0.20.0

* Thu Sep 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.19.7-1
- Update to 0.19.7
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.19/rygel-0.19.7.news

* Tue Aug 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.19.5-1
- Update to 0.19.5
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.19/rygel-0.19.5.news

* Tue Jul 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.19.4-1
- Update to 0.19.4
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.19/rygel-0.19.4.news

* Mon Jun 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.19.3-1
- Update to 0.19.3

* Tue May 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.19.2-1
- Update to 0.19.2

* Tue Apr 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.19.1-1
- Update to 0.19.1

* Wed Apr 17 2013 Richard Hughes <rhughes@redhat.com> - 0.18.1-1
- Update to 0.18.1

* Tue Mar 26 2013 Richard Hughes <rhughes@redhat.com> - 0.18.0-1
- Update to 0.18.0

* Tue Mar 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.10-1
- 0.17.10 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.17/rygel-0.17.10.news

* Tue Mar  5 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.9-1
- 0.17.9 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.17/rygel-0.17.9.news

* Thu Feb 21 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.8-1
- 0.17.8 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.17/rygel-0.17.8.news

* Sat Jan 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.7-1
- 0.17.7 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.17/rygel-0.17.7.news

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 0.17.6-1
- Update to 0.17.6

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 0.17.5.1-1
- Update to 0.17.5.1

* Wed Dec 26 2012 Bruno Wolff III <bruno@wolff.to> 0.17.5-2
- Rebuild for libgupnp-dlna soname bump

* Fri Dec 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.5-1
- 0.17.5 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.17/rygel-0.17.5.news

* Thu Dec  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.4-1
- 0.17.4 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.17/rygel-0.17.4.news

* Sat Dec  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.3-1
- 0.17.3 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.17/rygel-0.17.3.news

* Sun Nov 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.2-1
- 0.17.2 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.17/rygel-0.17.2.news

* Thu Nov  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.1-1
- 0.17.1 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.17/rygel-0.17.1.news

* Sat Oct  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.17.0-1
- 0.17.0 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.17/rygel-0.17.0.news

* Tue Sep 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.16.0-1
- 0.16.0 stable release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.16/rygel-0.16.0.news

* Tue Sep 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.4-1
- 0.15.4 devel release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.15/rygel-0.15.4.news

* Tue Sep  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.3-1
- 0.15.3 devel release

* Tue Aug 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.2-1
- 0.15.2 devel release

* Sat Jul 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.1-1
- 0.15.1 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.0.1-1
- 0.15.0.1 devel release

* Tue May 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.0-1
- 0.15.0 devel release

* Sun Apr 29 2012 Zeeshan Ali <zeenix@redhat.com> - 0.14.1-1
- 0.14.1 stable release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.14/rygel-0.14.1.news

* Mon Mar 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.14.0-1
- 0.14.0 stable release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.14/rygel-0.14.0.news

* Tue Mar 20 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.4-1
- devel 0.13.4 release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.13/rygel-0.13.4.news

* Wed Mar  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.3-1
- devel 0.13.3 release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.13/rygel-0.13.3.news

* Tue Feb 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.2-1
- devel 0.13.2 release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.13/rygel-0.13.2.news

* Fri Feb 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.1-1
- devel 0.13.1 release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.13/rygel-0.13.1.news

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.0-1
- devel 0.13.0 release
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.13/rygel-0.13.0.news

* Mon Oct 24 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.5-1
- stable release 0.12.5
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.12/rygel-0.12.5.news

* Sun Oct  9 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.4-1
- stable release 0.12.4
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.12/rygel-0.12.4.news

* Tue Sep 27 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.3-1
- stable release 0.12.3
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.12/rygel-0.12.3.news

* Tue Sep 20 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.2-1
- stable release 0.12.2
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.12/rygel-0.12.2.news

* Wed Sep 14 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.1-1
- stable release 0.12.1
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.12/rygel-0.12.1.news

* Tue Sep  6 2011 Zeeshan Ali <zeenix@redhat.com> 0.12.0-3
- We don't need vala and gupnp-vala to build from release tarball.

* Tue Sep  6 2011 Zeeshan Ali <zeenix@redhat.com> 0.12.0-2
- Rebuild against latest gssdp and gupnp*.

* Mon Sep  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.0-1
- Update to stable release 0.12.0
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.12/rygel-0.12.0.news

* Fri Aug  5 2011 Peter Robinson <pbrobinson@gmail.com> 0.11.3-1
- 0.11.3
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.11/rygel-0.11.3.news

* Sun Jul 17 2011 Peter Robinson <pbrobinson@gmail.com> 0.11.2-1
- 0.11.2
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.11/rygel-0.11.2.news

* Tue Jun 21 2011 Zeeshan Ali <zali@redhat.com> 0.11.1-1
- http://ftp.gnome.org/pub/GNOME/sources/rygel/0.11/rygel-0.11.1.news

* Fri Jun 17 2011 Peter Robinson <pbrobinson@gmail.com> 0.11.0-2
- rebuild for new gupnp/gssdp

* Fri Jun 10 2011 Zeeshan Ali <zali@redhat.com> 0.11.0-1
- Update to 0.11.0
- Update description

* Tue May 31 2011 Christopher Aillon <caillon@redhat.com> 0.10.2-1
- Update to 0.10.2

* Mon Apr 18 2011 Peter Robinson <pbrobinson@gmail.com> 0.10.1-1
- Update to 0.10.1

* Fri Apr 15 2011 Peter Robinson <pbrobinson@gmail.com> 0.10.0-1
- Update to 0.10.0

* Wed Apr 13 2011 Peter Robinson <pbrobinson@gmail.com> 0.9.9-3
- bump for new gupnp-dlna

* Mon Apr 11 2011 Peter Robinson <pbrobinson@gmail.com> 0.9.9-2
- bump for new gupnp-dlna

* Tue Feb 22 2011 Peter Robinson <pbrobinson@gmail.com> 0.9.9-1
- Update to 0.9.9

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> 0.9.8-4
- Rebuild against newer gtk

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 0.9.8-2
- Rebuild against new gtk

* Mon Jan 31 2011 Peter Robinson <pbrobinson@gmail.com> 0.9.8-1
- Update to 0.9.8

* Mon Jan 31 2011 Peter Robinson <pbrobinson@gmail.com> 0.9.7-1
- Update to 0.9.7

* Thu Jan 27 2011 Peter Robinson <pbrobinson@gmail.com> 0.9.6-2
- Rebuild for new gupnp-dlna

* Wed Jan 12 2011 Peter Robinson <pbrobinson@gmail.com> 0.9.6-1
- Update to 0.9.6

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> 0.9.5-1
- Update to 0.9.5

* Sun Jan  9 2011 Matthias Clasen <mclasen@redhat.com> 0.9.4-2
- Rebuild against newer gtk

* Mon Nov 29 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.4-1
- New 0.9.4 dev release

* Wed Nov 10 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.3-1
- New 0.9.3 dev release, really support gtk3 this time ;-)

* Tue Nov  9 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.2-1
- New 0.9.2 dev release

* Mon Oct 18 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.1-1
- New 0.9.1 dev release

* Mon Oct  4 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.0-1
- New 0.9.0 dev release

* Wed Sep 29 2010 Peter Robinson <pbrobinson@gmail.com> 0.8.1-1
- New 0.8.1 release

* Tue Sep 28 2010 Peter Robinson <pbrobinson@gmail.com> 0.8.0-1
- New 0.8.0 stable release

* Tue Sep 14 2010 Peter Robinson <pbrobinson@gmail.com> 0.7.8-1
- Update to 0.7.8 development release

* Thu Sep  9 2010 Peter Robinson <pbrobinson@gmail.com> 0.7.7-1
- Update to 0.7.7 development release

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> 0.7.6-1
- Update to 0.7.6

* Mon Jul 12 2010 Peter Robinson <pbrobinson@gmail.com> 0.7.2-1
- Update to 0.7.2 development release

* Fri Jul  2 2010 Peter Robinson <pbrobinson@gmail.com> 0.7.1-2
- Update gtk dep to gtk3 for UI

* Fri Jun 25 2010 Peter Robinson <pbrobinson@gmail.com> 0.7.1-1
- Update to 0.7.1 development release

* Mon Jun  7 2010 Peter Robinson <pbrobinson@gmail.com> 0.7.0-1
- Update to 0.7.0 development release

* Sun May 16 2010 Peter Robinson <pbrobinson@gmail.com> 0.6.0-3
- Add the translations as well.

* Sun May 16 2010 Peter Robinson <pbrobinson@gmail.com> 0.6.0-2
- Increment build

* Sun May 16 2010 Peter Robinson <pbrobinson@gmail.com> 0.6.0-1
- Update to 0.6.0

* Wed Apr 14 2010 Peter Robinson <pbrobinson@gmail.com> 0.5.2-1
- Update to 0.5.2

* Wed Feb 24 2010 Peter Robinson <pbrobinson@gmail.com> 0.5.0-1
- Update to 0.5.0

* Mon Jan 25 2010 Bastien Nocera <bnocera@redhat.com> 0.4.10-1
- Update to 0.4.10

* Sat Dec 26 2009 Peter Robinson <pbrobinson@gmail.com> 0.4.8-2
- Update description

* Tue Dec 22 2009 Peter Robinson <pbrobinson@gmail.com> 0.4.8-1
- Update to 0.4.8

* Sat Nov 21 2009 Peter Robinson <pbrobinson@gmail.com> 0.4.6-1
- Update to 0.4.6

* Tue Oct 27 2009 Peter Robinson <pbrobinson@gmail.com> 0.4.4-2
- Add and change new files.

* Tue Oct 27 2009 Peter Robinson <pbrobinson@gmail.com> 0.4.4-1
- Update to 0.4.4

* Fri Oct  2 2009 Peter Robinson <pbrobinson@gmail.com> 0.4.2-1
- Update to 0.4.2

* Fri Sep 25 2009 Bastien Nocera <bnocera@redhat.com> 0.4.1-1
- Update to 0.4.1

* Thu Sep 24 2009 Bastien Nocera <bnocera@redhat.com> 0.4-5
- Make sure we rebuild the C source code from vala sources

* Thu Sep 24 2009 Bastien Nocera <bnocera@redhat.com> 0.4-4
- Make the prefs work

* Thu Sep 24 2009 Peter Robinson <pbrobinson@gmail.com> 0.4-3
- Enable new plugins, add desktop file verification, add more docs

* Thu Sep 24 2009 Peter Robinson <pbrobinson@gmail.com> 0.4-2
- Update deps for new release

* Wed Sep 23 2009 Peter Robinson <pbrobinson@gmail.com> 0.4-1
- New upstream 0.4 release

* Thu Aug 20 2009 Michel Salim <salimma@fedoraproject.org> - 0.3-6
- Rebuild against compat-libgee01

* Fri Aug  7 2009 Peter Robinson <pbrobinson@gmail.com> 0.3-5
- Own rygel include dir, some spec file cleanups

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  1 2009 Peter Robinson <pbrobinson@gmail.com> 0.3-3
- Rebuild with new libuuid build req

* Wed Jun  3 2009 Peter Robinson <pbrobinson@gmail.com> 0.3-2
- Split tracker plugin out to a sub package. Resolves RHBZ 507032

* Wed Jun  3 2009 Peter Robinson <pbrobinson@gmail.com> 0.3-1
- New upstream release

* Fri Mar 13 2009 Peter Robinson <pbrobinson@gmail.com> 0.2.2-3
- Add a dep on tracker as that is currently the way it finds media

* Mon Mar 2  2009 Peter Robinson <pbrobinson@gmail.com> 0.2.2-2
- Added some missing BuildReqs

* Mon Mar 2  2009 Peter Robinson <pbrobinson@gmail.com> 0.2.2-1
- Initial release
