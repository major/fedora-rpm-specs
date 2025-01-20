%global __python %{__python3}
%global gstreamer1_min_version 1.18.0

Name:           pitivi
Version:        2023.03
Release:        12%{?dist}
Summary:        Non-linear video editor

License:        LGPL-2.0-or-later
URL:            http://www.pitivi.org/
Source0:        https://download.gnome.org/sources/pitivi/2023/pitivi-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  python3
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  gettext
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer1_min_version}
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  %{_bindir}/desktop-file-validate
BuildRequires:  %{_bindir}/appstream-util
BuildRequires:  gst-devtools-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel

Requires:	gstreamer1 >= %{gstreamer1_min_version}
Requires:	gstreamer1-plugins-good >= %{gstreamer1_min_version}
Requires:	gstreamer1-plugins-bad-free >= %{gstreamer1_min_version}
Requires:	gstreamer1-plugins-bad-free-gtk >= %{gstreamer1_min_version}
Requires:       gstreamer1-plugin-libav >= %{gstreamer1_min_version}
Requires:       gstreamer1-plugins-bad-free-opencv >= %{gstreamer1_min_version}
Requires:	python3-gstreamer1 >= 1.6.0
Requires:	gst-editing-services >= %{gstreamer1_min_version}
Requires:	hicolor-icon-theme
Requires:	gnome-desktop3
Requires:	frei0r-plugins
Requires:	python3-numpy
Requires:	python3-matplotlib
Requires:	python3-matplotlib-gtk3
Requires:	yelp
Requires:	python3-cairo >= 1.0.0
Requires:	libnotify
Requires:	python3-inotify
Requires:	python3-canberra
Requires:	python3-gobject
Requires:       python3-scipy
Requires:	gobject-introspection
Requires:	opus-tools
Requires:       gsound
%if 0%{?fedora} >= 39
Requires:       libpeas1
%else
Requires:       libpeas
%endif

%description
Pitivi is an application using the GStreamer multimedia framework to
manipulate a large set of multimedia sources.

At this level of development it can be compared to a classic video editing
program.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup

# https://gitlab.gnome.org/GNOME/pitivi/commit/0f3e399e387e64dcc3c5015a8aacb26fbe49800f
sed -i -e "/Pycairo_CAPI/d" pitivi/coptimizations/renderer.c

rm -rf subprojects/gst-transcoder
sed -i "/subproject('gst-transcoder')/d" meson.build
sed -i "/gst_transcoder_dep/d" meson.build

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{python3_sitearch}/pitivi
mv %{buildroot}%{_libdir}/pitivi/python/pitivi %{buildroot}%{python3_sitearch}/
rmdir %{buildroot}%{_libdir}/pitivi/python

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.pitivi.Pitivi.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.pitivi.Pitivi.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/org.pitivi.Pitivi.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/org.pitivi.Pitivi-mime.xml
%{_datadir}/help/*
%{_datadir}/metainfo/org.pitivi.Pitivi.appdata.xml
%{python3_sitearch}/pitivi/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2023.03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2023.03-10
- Rebuilt for Python 3.13

* Sat May 25 2024 Fabio Valentini <decathorpe@gmail.com> - 2023.03-9
- Rebuild for gstreamer-plugins-bad 1.24.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Kalev Lember <klember@redhat.com> - 2023.03-6
- Require libpeas1 compat package rather than libpeas in F39+

* Fri Oct 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 2023.03-5
- Require opencv plugin

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2023.03-3
- Rebuilt for Python 3.12

* Mon Apr 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 2023.03-2
- require libpeas

* Mon Mar 27 2023 Gwyn Ciesla <gwync@protonmail.com> - 2023.03-1
- 2023.03

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 2022.06.0-5
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.06.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 2022.06.0-3
- Require gstreamer1-plugin-libav.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.06.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Gwyn Ciesla <gwync@protonmail.com> - 2022.06.0-1
- 2022.06.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2021.05.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.05.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 2021.05.0-5
- Require gsound

* Thu Aug 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 2021.05.0-4
- Patch collections for Python 3.10

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.05.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2021.05.0-2
- Rebuilt for Python 3.10

* Tue Jun 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 2021.05-1
- 2021.05

* Mon Feb 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 2021.01-1
- 2021.01

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.09.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 2020.09.2-1
- 2020.09.2

* Wed Oct 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 2020.09.1-1
- 2020.09.1

* Mon Sep 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.999-12
- gst-transcoder deprecated.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.999-10
- Rebuilt for Python 3.9

* Thu Mar 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.999-9
- Patch for https://gitlab.gnome.org/GNOME/pitivi/issues/2429

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.999-7
- Update for Python 3.9

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.999-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.999-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.999-3
- Fix FTBFS for python 3.8.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Gwyn Ciesla <limburgher@gmail.com> - 0.999-1
- 0.999

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.99-6
- Require python3-gobject instead of python2-gobject

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.99-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.99-2
- Remove obsolete scriptlets

* Thu Sep 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.99-1
- 0.99

* Wed Aug 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.98.1-4
- Require opus-tools

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.98.1-1
- 0.98.1 BZ 1466972.

* Fri Jun 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.98-7
- Fix for renamed gstgtk module, BZ 1460256.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.98-5
- Rebuild for Python 3.6

* Tue Dec 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.98-3
- Fix crash due to wrong paths

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.98-3
- Rebuild for Python 3.6

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.98-2
- Use proper macro
- Cleanup spec

* Wed Dec 07 2016 Jon Ciesla <limburgher@gmail.com> - 0.98-1
- 0.98, BZ 1402176

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.1-5
- Fix python3-cairo dependency

* Thu Nov 03 2016 Jon Ciesla <limburgher@gmail.com> - 0.97.1-4
- Move completely to Python3, BZ 1390784, except for nose.

* Fri Oct 14 2016 Jon Ciesla <limburgher@gmail.com> - 0.97.1-3
- Requires fix for f25+ BZ 1383068.

* Wed Aug 10 2016 Wim Taymans <wtaymans@redhat.com> - 0.97.1-2
- Add python3-inotify and gnome-desktop3 to requires (#1288860)

* Tue Aug 9 2016 Wim Taymans <wtaymans@redhat.com> - 0.97.1-1
- update to 0.97.1
- Drop configure macro, doesn't work with meson (new BR)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 14 2016 Jon Ciesla <limburgher@gmail.com> - 0.96-2
- Requires gst-transcoder.

* Fri Jul 01 2016 Wim Taymans <wtaymans@redhat.com> - 0.96-1
- update to 0.96

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Wim Taymans <wtaymans@redhat.com> - 0.95-2
- Remove pygtk2 dependency

* Mon Nov 23 2015 Wim Taymans <wtaymans@redhat.com> - 0.95-1
- update to 0.95
- update python3-gstreamer1 required version
- update matlib requires
- remove clutter requirement

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Jon Ciesla <limburgher@gmail.com> - 0.94-4
- Move arch-specific Python module to the proper place, BZ 1167119.

* Mon Nov 10 2014 Debarshi Ray <rishi@fedoraproject.org> - 0.94-3
- Require python3-canberra and python3-gstreamer, instead of their python2
  counterparts.

* Fri Nov 07 2014 Jon Ciesla <limburgher@gmail.com> - 0.94-2
- Requires fixes.

* Tue Nov 04 2014 Jon Ciesla <limburgher@gmail.com> - 0.94-1
- 0.94, BZ 1160285.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.93-6
- update mime scriptlet
- %%check: validate .desktop/appdata

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Jon Ciesla <limburgher@gmail.com> - 0.93-4
- Require clutter-gst2, BZ 1093933.

* Wed Apr 02 2014 Jon Ciesla <limburgher@gmail.com> - 0.93-3
- Updated GES Requires to reflect reality.

* Fri Mar 28 2014 Jon Ciesla <limburgher@gmail.com> - 0.93-2
- Updated gnonlin Requires to reflect reality.

* Fri Mar 21 2014 Jon Ciesla <limburgher@gmail.com> - 0.93-1
- New upstream to support latest GES.

* Fri Mar 07 2014 Jon Ciesla <limburgher@gmail.com> - 0.92-2
- Drop unneeded Requires pygoocanvas and python-zope-interface,
- added gobject-introspection, pygobject3, BZ 1059916.
- added clutter-gtk, BZ 1073726.

* Fri Dec 06 2013 Jon Ciesla <limburgher@gmail.com> - 0.92-1
- Latest upstream, BZ 1013686.

* Fri Oct 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.91-1
- Latest upstream, BZ 1013686.

* Tue Sep 03 2013 Jon Ciesla <limburgher@gmail.com> - 0.15.2-5
- Add Video category to .desktop file.
- Date fix.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Jon Ciesla <limburgher@gmail.com> - 0.15.2-1
- New upstream, BZ 818690, regression fix.

* Mon Apr 09 2012 Jon Ciesla <limburgher@gmail.com> - 0.15.1-1
- New upstream, BZ 810765, multiple bugfixes.

* Tue Mar 27 2012 Jon Ciesla <limburgher@gmail.com> - 0.15.0-3
- Patch for unknown stream types, BZ 723653.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 27 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 0.15.0-1
- Update to 0.15.0
- Drop previously backported patches
- Disable tests since most of them require gtk

* Sun Sep 11 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 0.14.2-1
- Update to 0.14.2

* Thu Jun 30 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 0.14.0-3
- Do not allow presets to have the same name, fixes rhbz #717328

* Sun Jun 12 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 0.14.0-2
- Allow using "Default" as preset name, fixes rhbz #712700
- Lower pygtk2 min version to 2.17.0 so that we can push 0.14.0 to f14

* Thu Jun 02 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 0.14.0-1
- Update to 0.14
- Drop backported patches
- Remove BuildRoot tag and clean section
- Add patch to make sure welcome dialog apprears after the UI is loaded
- Fix license in some files headers

* Wed Dec 15 2010 Hicham HAOUARI <hicham.haouari@gmail.com> - 0.13.5-4
- Initialize pending new_segment to none, fixes rhbz #653062

* Wed Dec 08 2010 Hicham HAOUARI <hicham.haouari@gmail.com> - 0.13.5-3
- Add buildroot tag
- Clean buildroot in %%install section
- Add patch from lp #640630 to fix rhbz #654119
- Add man page
- Add %%check section
- Add pygobject2, gstreamer-python, gnonlin and gstreamer-plugins-good
  to BR so that we can run %%check

* Tue Dec 07 2010 Hicham HAOUARI <hicham.haouari@gmail.com> - 0.13.5-2
- Add scriptlet to update icon cache (rhbz #625580)

* Wed Sep 22 2010 Chen Lei <supercyper@163.com> - 0.13.5-1
- Update to 0.13.5

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.13.4-3
- recompiling .py files against Python 2.7 (rhbz#623347)

* Mon Mar 15 2010 Benjamin Otte <otte@redhat.com> - 0.13.4-2
- Make sure Pitivi has an icon in the menu.

* Wed Mar 10 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.4-1.1
- Upload new tarball :)

* Wed Mar 10 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.4-1
- Update to 0.13.4

* Tue Mar  9 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.3.2-0.1
- Update to 0.13.3.2

* Fri Dec 11 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.3-3.3.837f0d73
- Make sure we have the correct source uploaded.

* Thu Dec 10 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.3-3.2.837f0d73
- Update to git master to see if this fixes anyone's problems
- Call update-desktop-database/update-mime-database in post/postun

* Thu Dec  3 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.3-3
- Add Req on python-setuptools for BZ#540192

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.13.3-2
- Update desktop file according to F-12 FedoraStudio feature

* Mon Sep 14 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.3-1
- 0.13.3 Release : ... we shall never (sur)render
-
- The PiTiVi team is proud to announce the second release in the
- unstable 0.13 PiTiVi series.
-
- Due to its dependency on GStreamer, The PiTiVi team strongly
- recommends users have all official latest gstreamer libraries and
- plugins installed for the best user experience.
-
- Title is from a quote by Winston Churchill “We shall defend our
- island, whatever the cost may be, we shall fight on the beaches, we
- shall fight on the landing grounds, we shall fight in the fields and
- in the streets, we shall fight in the hills; we shall never
- surrender.”
-
- Features of this release
-
-    * Fix rendering failures
-    * UI beautifications
-    * Switch to themeable ruler
-    * Speed optimisations
-    * Show the project name in the window title 

* Sat Aug 29 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.2.2-0.1
- Update to prerelease for 0.13.3
- Streamline BuildRequires

* Fri Aug 14 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.2-2
- Bump required version of gstreamer-python

* Thu Aug 13 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.2-1
- Update to 0.13.2 "Jailbreak (out of Deadlock City)"
- 
- The PiTiVi team is proud to announce the second release in the
- unstable 0.13 PiTiVi series.
- 
- Due to its dependency on GStreamer, The PiTiVi team strongly
- recommends users have all official latest gstreamer libraries and
- plugins installed for the best user experience.
- 
- Features of this release
- 
-    * Undo/Redo support
-    * Audio mixing
-    * Ripple/Roll edit
-    * misc fixes everywhere 

* Wed Aug 12 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.1.3-1
- Update to latest prerelease.

* Mon Jul 27 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.1.2-1
- Update to prerelease

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 28 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.1-1
- 0.13.1 Release "L'Aquila Immota Manet : The eagle remains unmoved"
- ------------------------------------------------------------------
- 
- The PiTiVi team is proud to announce the first release in the unstable 0.13
- PiTiVi series.
- 
- This release is in memory of those who have lost their lives, friends,
- houses in the April 6th 2009 earthquake in l'Aquila, Italy.
- 
- Due to its dependency on GStreamer, The PiTiVi team strongly
- recommends users have all official latest gstreamer libraries and
- plugins installed for the best user experience.
- 
- 
- * Features of this release
- 
-  * core rewrite
-  * multi-layered timeline
-  * trimming features
-  * audio waveforms and video thumbnails in timeline
-  * picture support
-  * New project file format support

* Thu May 21 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13.0.2-1
- Upgrade to 0.13.1 prerelease

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.3-2
- Add patch from Denis Leroy to fix running with Python 2.6

* Mon Dec 15 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.3-1
- Update to 0.11.3

* Thu Dec  4 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.2.2-2
- Upload the sources

* Thu Dec  4 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.2.2-1
- Update to 0.11.2.2

* Sat Nov 29 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.2-2
- Rebuild for Python 2.6

* Wed Oct 15 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.2-1
- Update to 0.11.2

* Mon Oct 13 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.1.4-1
- Update to 0.11.1.4

* Mon Jan 14 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.1-2
- Add requirement for python-setuptools. (BZ#426855)

* Sat Dec  8 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.1-1
- Update to 0.11.1

* Sun Nov 11 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.0-2
- Add missing BR

* Wed Oct 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.0-1
- Update to 0.11.0

* Wed Jun 27 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.3-2
- Add versioned requires for gnonlin. (BZ#245981)

* Fri Jun 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.3-1
- Update to 0.10.3

* Mon May 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.2.2-3
- BR gettext

* Mon May 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.2.2-2
- BR perl(XML::Parser)
