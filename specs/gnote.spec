%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnote
Version:        47.2
Release:        2%{?dist}
Summary:        Note-taking application

License:        GPL-3.0-or-later AND GFDL-1.1-only AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Gnote
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(giomm-2.68)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(uuid)

%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/*/.*\\.so$

%description
Gnote is a desktop note-taking application which is simple and easy to use.
It lets you organize your notes intelligently by allowing you to easily link
ideas together with Wiki style interconnects. It is a port of Tomboy to C++ 
and consumes fewer resources.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Gnote.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Gnote.appdata.xml

%files -f %{name}.lang
%license COPYING COPYING-DOCS
%doc AUTHORS NEWS README.md
%{_bindir}/gnote
%{_libdir}/gnote/
%exclude %{_libdir}/libgnote-*.so
%{_libdir}/libgnote-*.so.*
%{_datadir}/applications/org.gnome.Gnote.desktop
%{_datadir}/gnote/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Gnote.png
%{_datadir}/icons/hicolor/*/apps/org.gnome.Gnote.svg
%{_datadir}/dbus-1/services/org.gnome.Gnote.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnote.gschema.xml
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/org.gnome.Gnote.search-provider.ini
%{_mandir}/man1/gnote.1*
%{_metainfodir}/org.gnome.Gnote.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 nmontero <nmontero@redhat.com> - 47.2-1
- Update to 47.2

* Mon Sep 23 2024 David King <amigadave@amigadave.com> - 47.0-1
- Update to 47.0

* Sat Jul 27 2024 David King <amigadave@amigadave.com> - 46.1-1
- Update to 46.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 26 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Mon Mar 18 2024 David King <amigadave@amigadave.com> - 46~rc-1
- Update to 46.rc

* Mon Mar 11 2024 David King <amigadave@amigadave.com> - 46~beta-1
- Update to 46.beta

* Tue Jan 30 2024 David King <amigadave@amigadave.com> - 46~alpha-1
- Update to 46.alpha

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Kalev Lember <klember@redhat.com> - 45.1-1
- Update to 45.1

* Wed Sep 27 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 45~rc-1
- Update to 45.rc

* Mon Jul 31 2023 Kalev Lember <klember@redhat.com> - 45~alpha-1
- Update to 45.alpha

* Sun Jul 23 2023 David King <amigadave@amigadave.com> - 44.1-1
- Update to 44.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Thu Mar 16 2023 David King <amigadave@amigadave.com> - 43.1-2
- Use SPDX for License field
- Fix excluding private libraries from Provides

* Tue Feb 07 2023 David King <amigadave@amigadave.com> - 43.1-1
- Update to 43.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 07 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Mon Sep 26 2022 Kalev Lember <klember@redhat.com> - 43~rc-1
- Update to 43.rc

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43~beta-2
- Drop no longer needed pcre-devel buildrequires (#2128301)

* Fri Sep 16 2022 Kalev Lember <klember@redhat.com> - 43~beta-1
- Update to 43.beta

* Fri Aug 19 2022 Kalev Lember <klember@redhat.com> - 43~alpha-1
- Update to 43.alpha

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 42.1-1
- Update to 42.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar 27 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Tue Mar 15 2022 David King <amigadave@amigadave.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 09 2022 David King <amigadave@amigadave.com> - 41.2-1
- Update to 41.2

* Mon Nov 01 2021 Kalev Lember <klember@redhat.com> - 41.1-1
- Update to 41.1

* Sun Sep 26 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Fri Sep 17 2021 Gustavo Costa <xfgusta@fedoraproject.com> - 41~alpha-2
- Use _metainfodir macro
- Add appdata check

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 41~beta-1
- Update to 41.beta

* Mon Aug 23 2021 Kalev Lember <klember@redhat.com> - 41~alpha-1
- Update to 41.alpha
- Switch to meson build system

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Kalev Lember <klember@redhat.com> - 40.2-1
- Update to 40.2

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 40.1-1
- Update to 40.1

* Fri Mar 26 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc

* Sun Feb 21 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta

* Fri Feb 19 2021 Kalev Lember <klember@redhat.com> - 40~alpha-1
- Update to 40.alpha

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Sat Sep 19 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Thu Sep 17 2020 Jeff Law <law@redhat.com> - 3.37.0-4
- Fix missing #include for gcc-11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Kalev Lember <klember@redhat.com> - 3.37.0-1
- Update to 3.37.0

* Sun Mar 15 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Sun Feb 23 2020 Kalev Lember <klember@redhat.com> - 3.35.0-1
- Update to 3.35.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Sat Sep 21 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Kalev Lember <klember@redhat.com> - 3.33.0-1
- Update to 3.33.0

* Sun Apr 14 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 18 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Kalev Lember <klember@redhat.com> - 3.31.0-1
- Update to 3.31.0

* Sun Sep 23 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0
- Remove ldconfig scriptlets

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.26.0-4
- Add g++ to BRs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-2
- Remove obsolete scriptlets

* Mon Sep 18 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Wed Aug 30 2017 Kalev Lember <klember@redhat.com> - 3.25.0-1
- Update to 3.25.0

* Mon Aug 21 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 3.24.0-3
- Rebuilt for Boost 1.64

* Wed May 17 2017 Owen Taylor <otaylor@redhat.com> - 3.24.0-2
- Filter out provides of private dynamically loaded libraries

* Mon Apr 03 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Mon Feb 27 2017 Richard Hughes <rhughes@redhat.com> - 3.23.0-1
- Update to 3.23.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 3.22.1-2
- Rebuilt for Boost 1.63

* Sun Nov 27 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Mon Sep 26 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.21.1-1
- Update to 3.21.1
- Don't set group tags
- Update project URLs
- Use make_install macro
- Move desktop-file-validate to the check section

* Sun Aug 21 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.21.0-1
- Update to latest upstream release

* Sun May 15 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.20.1-1
- Update to latest upstream release

* Sun Mar 27 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.19.0-2
- bug fix

* Mon Feb 01 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.19.0-1
- Update to 3.19.0

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 3.18.1-2
- Rebuilt for Boost 1.60

* Sat Dec 05 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 28 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Sun Sep 13 2015 Kalev Lember <klember@redhat.com> - 3.17.1-1
- Update to 3.17.1
- Use license macro for COPYING

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.17.0-4
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.17.0-2
- rebuild for Boost 1.58

* Mon Jul 13 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.17.0-1
- Update to latest upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.16.1-1
- Update to latest upstream release.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 30 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.16.0-2
- Forgot to update SourceURL

* Mon Mar 30 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.16.0-1
- Update to 3.16.0

* Sat Mar 07 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.1-1
- Update to 3.15.1

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.14.0-2
- Rebuild for boost 1.57.0

* Sun Sep 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 3.13.0-3
- Rebuild for boost 1.55.0

* Wed May 07 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.13.0-2
- Enable optional x11 support for hotkeys
- rhbz 1094089

* Fri May 02 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.0-1
- Update to 3.13.0

* Wed Mar 26 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.12.0-1
- Update to latest upstream release

* Thu Mar 06 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.11.1-1
- Update to latest upstream release
- Correct changelog date

* Sat Nov 09 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.10.1-1
- Update to 3.10.1
- News: http://ftp.gnome.org/pub/GNOME/sources/gnote/3.10/gnote-3.10.1.news

* Sun Aug 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.3-1
- Update to 3.9.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 3.9.1-2
- Rebuild for boost 1.54.0

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> 3.9.1-1
- Update to 3.9.1
- Drop upstreamed patch
- Package the new gnome-shell search provider

* Fri May 24 2013 Rahul Sundaram <sundaram@fedoraproject.org> 3.9.0-2
- drop soname symlink.  Resolves rhbz#889242

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> 3.9.0-1
- Update to 3.9.0

* Wed Mar 27 2013 Kalev Lember <kalevlember@gmail.com> 3.8.0-1
- Update to 3.8.0

* Thu Mar 07 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.7.3-5
- Complete patch. Tested as scratch build. Builds!

* Tue Mar 05 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.7.3-4
- Spec bump, update patch, retry build

* Tue Mar 05 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.7.3-3
- Spec bump

* Tue Mar 05 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.7.3-2
- Add patch for missing -lpthread that broke koji build

* Tue Mar 05 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.7.3-1
- Update to 3.7.3 rhbz#917584
- Add gtkspell3 to BR for spell check support

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.7.2-1
- Update to latest: 3.7.2

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.0-1
- Update to 3.7.0

* Wed Sep 26 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0
- Use desktop-file-validate

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.1-1
- update to 0.9.1
- http://ftp.gnome.org/pub/GNOME/sources/gnote/0.9/gnote-0.9.1.news

* Thu Mar 29 2012 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.0-1
- update to 0.9.0
- https://mail.gnome.org/archives/gnote-list/2012-March/msg00000.html

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.8.2-3
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 30 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.2-1
- update to 0.8.2
- https://mail.gnome.org/archives/gnote-list/2011-December/msg00001.html

* Mon Oct 24 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.0-2
- Update scriplets for gsettings schema and icon cache. Fixes rhbz#743580
- Drop obsolete dependency on Gconf and dbus-c++-devel
- Update build requires to gtkmm30-devel instead of gtkmm24-devel
- Fix source url

* Wed Sep 28 2011 Ray <rstrode@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Tue Aug 02 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.5-1
- New upstream release
- http://mail.gnome.org/archives/gnote-list/2011-July/msg00001.html
- Drop all patches since they are now upstream

* Sun May 01 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.4-1
- New upstream bug fix release
- http://mail.gnome.org/archives/gnote-list/2011-April/msg00011.html
- Drop couple of no longer needed patches

* Sun Apr 17 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.3-9
- Rebuilt for Boost soname bump
- Added rarian-compat as build requires

* Thu Feb 10 2011 Bastien Nocera <bnocera@redhat.com> 0.7.3-8
- Make sure that gnote shows up on first launch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb  6 2011 Michel Salim <salimma@fedoraproject.org> - 0.7.3-6
- Rebuild for Boost 1.46

* Thu Feb 03 2011 Bastien Nocera <bnocera@redhat.com> 0.7.3-5
- Disable panel applet
- Rebuild against newer GTK+
- Add patch from Petr Machata <pmachata@redhat.com> to fix the build

* Fri Dec 17 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.3-4
- Add the patch

* Fri Dec 17 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.3-3
- Fix gnote losing add-in status when running as app
- Resolves rhbz#654562

* Sat Nov 06 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.3-2
- Explicit build requires on libxslt-devel

* Sat Nov 06 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.3-1
- New upstream bug fix release with translation updates
- http://mail.gnome.org/archives/gnote-list/2010-November/msg00002.html
- Drop backported patch

* Fri Jul 30 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.2-2
- Rebuild for Boost 1.44
- Drop the clean section

* Fri Mar 12 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.2-1
- Ability to search for phrases, prompt while renaming notes, bug fixes
- Add a patch from upstream master to replace deprecated macros 
- Drop upstreamed patch to fix dso linking
- http://mail.gnome.org/archives/gnote-list/2010-March/msg00010.html

* Tue Feb 16 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.1-3
- Fix implicit DSO linking (thanks to Ankur Sinha)
- Fixes bz#564774

* Wed Jan 20 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.1-2
- Rebuild for new Boost soname bump

* Tue Jan 05 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.1-1
- Mostly minor bug fixes
- http://mail.gnome.org/archives/gnote-list/2010-January/msg00004.html

* Fri Jan 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.0-1
- Add a Note of the Day addin, addins can be disabled now
- http://mail.gnome.org/archives/gnote-list/2009-December/msg00013.html

* Tue Dec 29 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.3-3
- Upstream patches adding a fix for Bugzilla add-in and other minor bug fixes

* Tue Dec 22 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.3-2
- Several patches from upstream for additional translations
- Gnote now confirm to XDG specification

* Tue Dec 01 2009 Bastien Nocera <bnocera@redhat.com> 0.6.3-1
- Update to 0.6.3

* Thu Aug 13 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.2-1
- Very minor bug fixes
- http://mail.gnome.org/archives/gnote-list/2009-August/msg00006.html

* Sat Aug 01 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.1-1
- D-Bus support enabled, many new features and bug fixes
- http://mail.gnome.org/archives/gnote-list/2009-July/msg00016.html
- 0.6.0 skipped due to applet breakage fixed in this release
- http://mail.gnome.org/archives/gnote-list/2009-July/msg00020.html

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.3-1
- Few minor bug fixes
- http://mail.gnome.org/archives/gnote-list/2009-July/msg00002.html

* Sat Jul 04 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.2-2
- Build requires libuuid-devel instead of e2fsprogs-devel

* Sat Jul 04 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.2-1
- New upstream bug fix release
- http://mail.gnome.org/archives/gnote-list/2009-July/msg00000.html

* Thu Jun 25 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.1-1
- Fixes a regression and some bugs
- http://mail.gnome.org/archives/gnote-list/2009-June/msg00002.html

* Wed Jun 17 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.0-1
- Adds the ability to import Tomboy notes on first run 
- http://mail.gnome.org/archives/gnote-list/2009-June/msg00000.html
 
* Thu May 28 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.4.0-1
- Many minor bug fixes from new upstream release
  http://www.figuiere.net/hub/blog/?2009/05/27/670-gnote-040

* Wed May 06 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.3.1-1
- new upstream release. Fixes rhbz #498739. Fix #499227

* Fri May 01 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.3.0-1
- new upstream release. Includes applet and more plugins.

* Fri Apr 24 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.0-2
- enable spell checker

* Thu Apr 23 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.0-1
- new upstream release

* Thu Apr 16 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.1.2-2
- Add BR on gnome-doc-utils

* Wed Apr 15 2009 Jesse Keating <jkeating@redhat.com> - 0.1.2-1
- Update to 0.1.2 to fix many upstream bugs
  http://www.figuiere.net/hub/blog/?2009/04/15/660-gnote-012

* Fri Apr 10 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.1.1-4
- Drop a unnecessary require, BR and fix summary

* Wed Apr 08 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.1.1-3
- Fix review issues

* Wed Apr 08 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.1.1-2
- include pre script for gconf schema

* Wed Apr 08 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.1.1-1
- Initial spec file

