Name:          gupnp-tools
Version:       0.12.1
Release:       6%{?dist}
Summary:       A collection of dev tools utilising GUPnP and GTK+

License:       GPL-2.0-or-later
URL:           https://wiki.gnome.org/Projects/GUPnP
Source0:       https://download.gnome.org/sources/%{name}/0.12/%{name}-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/gupnp-tools/-/issues/27
Patch:         gupnp-tools-0.12.1-libxml2-2.12.0-deprecations.patch
# https://gitlab.gnome.org/GNOME/gupnp-tools/-/issues/28
Patch:         gupnp-tools-0.12.1-libxml2-2.12.0-includes.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: meson
BuildRequires: pkgconfig(gupnp-1.6)
BuildRequires: pkgconfig(gupnp-av-1.0)
BuildRequires: pkgconfig(gssdp-1.6)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtksourceview-4)
BuildRequires: pkgconfig(libsoup-3.0)

Requires: hicolor-icon-theme

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible. 

GUPnP-tools is a collection of developer tools utilising GUPnP and GTK+. 
It features a universal control point application as well as a sample 
DimmableLight v1.0 implementation. 

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/gupnp-av-cp.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/gupnp-network-light.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/gupnp-universal-cp.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/gupnp-tools/
%dir %{_datadir}/gupnp-tools/pixmaps/
%dir %{_datadir}/gupnp-tools/xml/
%{_bindir}/gssdp-discover
%{_bindir}/gupnp-av-cp
%{_bindir}/gupnp-event-dumper
%{_bindir}/gupnp-network-light
%{_bindir}/gupnp-universal-cp
%{_bindir}/gupnp-upload
%{_datadir}/applications/gupnp-av-cp.desktop
%{_datadir}/applications/gupnp-network-light.desktop
%{_datadir}/applications/gupnp-universal-cp.desktop
%{_datadir}/gupnp-tools/pixmaps/*.png
%{_datadir}/gupnp-tools/xml/*.xml
%{_datadir}/icons/hicolor/*/apps/av-cp.png
%{_datadir}/icons/hicolor/*/apps/network-light.png
%{_datadir}/icons/hicolor/*/apps/universal-cp.png

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 David King <amigadave@amigadave.com> - 0.12.1-2
- Fix building against libxml2 2.12.0

* Wed Aug 02 2023 Kalev Lember <klember@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 David King <amigadave@amigadave.com> - 0.12.0-1
- Update to 0.12.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 24 2022 David King <amigadave@amigadave.com> - 0.10.3-1
- Update to 0.10.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Kalev Lember <klember@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Fri Aug 20 2021 Kalev Lember <klember@redhat.com> - 0.10.1-2
- Rebuilt for gupnp-av and gupnp-dlna soname bumps

* Sun Aug 15 2021 Kalev Lember <klember@redhat.com> - 0.10.1-1
- Update to 0.10.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Kalev Lember <klember@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 0.8.15-2
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 0.8.15-1
- Update to 0.8.15
- Switch to the meson build system

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar  7 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.14-3
- Add gcc BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 10 2017 Kalev Lember <klember@redhat.com> - 0.8.14-1
- Update to 0.8.14

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Kalev Lember <klember@redhat.com> - 0.8.13-1
- Update to 0.8.13

* Tue Apr 26 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.12-1
- Update to 0.8.12
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-tools/0.8/gupnp-tools-0.8.12.news

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Kalev Lember <klember@redhat.com> - 0.8.11-1
- Update to 0.8.11

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 10 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.10-1
- Update to 0.8.10
- Use desktop-file-validate instead of desktop-file-install
- Use license macro for the COPYING file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.9-1
- Require gnome-icon-theme-legacy

* Tue Feb  4 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.9-1
- Update to 0.8.9
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-tools/0.8/gupnp-tools-0.8.9.news

* Mon Nov 11 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.8-1
- Update to 0.8.8
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-tools/0.8/gupnp-tools-0.8.8.news

* Wed Aug 21 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.7-1
- Update to 0.8.7
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-tools/0.8/gupnp-tools-0.8.7.news

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Kalev Lember <kalevlember@gmail.com> 0.8.6.1-2
- Adapt for gnome-icon-theme packaging changes

* Thu Apr  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.6.1
- Update to 0.8.6.1
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-tools/0.8/gupnp-tools-0.8.6.1.news

* Wed Mar 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.6-1
- Update to 0.8.6
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-tools/0.8/gupnp-tools-0.8.6.news

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.5-1
- Update to 0.8.5
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-tools/0.8/gupnp-tools-0.8.5.news

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.4-1
- Update to 0.8.4
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-tools/0.8/gupnp-tools-0.8.4.news

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.8.3-3
- Rebuild for new libpng

* Fri Jun 17 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.3-2
- rebuild for new gupnp/gssdp

* Fri Apr 15 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.3-1
- Update to 0.8.3

* Mon Apr 11 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.2-1
- Update to 0.8.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.8.1-2
- Rebuilt for gcc bug 634757

* Fri Sep 17 2010 Bastien Nocera <bnocera@redhat.com> 0.8.1-1
- Update to 0.8.1

* Tue Aug 17 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.8-3
- Update source URL

* Mon Mar 15 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.8-2
- Add patch to fix DSO linking. Fixes bug 564656 

* Thu Sep 17 2009 Bastien Nocera <bnocera@redhat.com> 0.8-1
- Update to 0.8

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 12 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.1-4
- Rebuild with new libuuid build req

* Tue May 12 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.1-3
- and add the GTKBuilder replacements

* Tue May 12 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.1-2
- Remove the glade files now that it uses GTKBuilder

* Tue May 12 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.1-1
- New upstream release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.7-3
- Fix package summary

* Tue Oct 28 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.7-2
- Add missing files

* Tue Oct 28 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.7-1
- New upstream release

* Sat Oct 25 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-4
- Add patch and rebuild

* Sat Oct 25 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-3
- Rebuild

* Fri Oct 24 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-2
- Add patch to fix gthread issue

* Mon Sep 29 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-1
- New upstream release

* Sat Aug 30 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6-2
- spec file review updates

* Tue Jun 17 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6-1
- Initial release
