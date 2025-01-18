Name: fonts-tweak-tool
Version: 0.4.8
Release: 6%{?dist}
Summary: Tool for customizing fonts per language

License: LGPL-3.0-or-later
URL: https://gitlab.com/tagoh/%{name}/
Source0: https://gitlab.com/api/v4/projects/tagoh%2F%{name}packages/generic/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: python3-devel
BuildRequires: gobject-introspection-devel pkgconfig(glib-2.0)
BuildRequires: make
Requires: libeasyfc-gobject >= 0.14.1
Requires: python3-gobject
Requires: gtk3
Requires: hicolor-icon-theme

%description
fonts-tweak-tool is a GUI tool for customizing fonts per language on desktops
using fontconfig.

%prep
%autosetup -p1
autoreconf --install

%build
%configure --disable-static PYTHON=%{__python3}
%make_build

%install
%make_install

desktop-file-install --dir=%{buildroot}%{_datadir}/applications --remove-only-show-in="GNOME;Unity;" fonts-tweak-tool.desktop

rm -f %{buildroot}%{_libdir}/lib*.so
%__brp_remove_la_files
rm -f %{buildroot}%{_datadir}/gir-*/FontsTweak-*.gir

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README AUTHORS NEWS
%license COPYING
%{_bindir}/%{name}
%{python3_sitearch}/fontstweak
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_libdir}/libfontstweak-resources.so.0*
%{_libdir}/girepository-*/FontsTweak-*.typelib


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.8-4
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov  6 2023 Akira TAGOH <tagoh@redhat.com> - 0.4.8-1
- New upstream release.
- Fix a crash when loading manual-updated config.
  Resolves: rhbz#2241364

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Akira TAGOH <tagoh@redhat.com> - 0.4.7-1
- New upstream release.

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.4.6-4
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Akira TAGOH <tagoh@redhat.com> - 0.4.6-2
- Convert License tag to SPDX.

* Thu Nov 17 2022 Akira TAGOH <tagoh@redhat.com> - 0.4.6-1
- New upstream release.
- Fix runtime error around gettext.
  Resolves: rhbz#2143065

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.5-17
- Rebuilt for Python 3.11

* Wed Mar 09 2022 Alastor Tenebris <livingnightmare@thelivingnightmare.xyz> 0.4.5-16
- Allow desktop file to be shown in other desktop environments
- Use more rpm macros
- Fix typo in build script

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.5-13
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.5-3
- Drop dep of pyxdg.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.5-1
- New upstream release.
- Use %%{__python3} macro instead of the hardcoded python3 name.

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-5
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.3-4
- Use ldconfig rpm macro.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-3
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.3-2
- R: python3-gobject instead of pygobject3.

* Thu May 24 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.3-1
- New upstream release.
- Fix invalid plural forms expression (#1568991)

* Tue Feb 20 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.2-1
- New upstream release.
- Fix the version deps check.

* Fri Feb 16 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.1-1
- New upstream release.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-12
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 11 2016 Akira TAGOH <tagoh@redhat.com> - 0.3.2-10
- Update shebang for python3.

* Wed Apr 06 2016 Parag Nemade <pnemade AT redhat DOT com>
- move to python3 as default support
- add %%license
- Remove group tag as its obsolete now

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.3.2-7
- Add an AppData file for the software center

* Thu Sep  4 2014 Akira TAGOH <tagoh@redhat.com> - 0.3.2-6
- Fix PyGTKDeprecationWarnings. (#1136177)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.3.2-4
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb  7 2014 Akira TAGOH <tagoh@redhat.com> - 0.3.2-2
- Fix the installation path for python scripts (#1062560)

* Wed Jul 31 2013 Akira TAGOH <tagoh@redhat.com> - 0.3.2-1
- New upstream release.

* Thu Apr 18 2013 Akira TAGOH <tagoh@redhat.com> - 0.3.1-1
- New upstream release.
  - Fix a crash. (#952983)

* Fri Mar 29 2013 Akira TAGOH <tagoh@redhat.com> - 0.3.0-1
- New upstream release.

* Tue Feb 26 2013 Akira TAGOH <tagoh@redhat.com> - 0.2.0-1
- New upstream release.
  - Improve UI (#909769)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Akira TAGOH <tagoh@redhat.com> - 0.1.5-1
- New upstream release.
  - Updated translations (#816378)

* Tue Dec 18 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.4-1
- New upstream release.
  - Fix file writing issue when the classification filter is turned off.
    (#886330)

* Sat Nov 24 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.2-1
- New upstream release
  - Fix broken icons issue on non-GNOME desktops (#879140)

* Wed Nov 21 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.1-3
- Fix a typo

* Wed Nov 21 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.1-2
- clean up and improve the spec file.

* Mon Oct 22 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.1-1
- New upstream release.
  - Drop the unnecessary warnings (#859455)

* Wed Sep 19 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.0-1
- New upstream release.

* Mon Aug 06 2012 James Ni <kent.neo@gmail.com> - 0.0.8-1
- Apply pull request from tagoh

* Tue Jul 24 2012 James Ni <kent.neo@gmail.com> - 0.0.7-1
- Fixed rhbz#838871, Apply button is always clickable
- Fixed rhbz#838854, existing settings in .i18n isn't reflected to initial value
- Fixed rhbz#838865, Unable to remove language in GTK Language Order tab
- Fixed rhbz#838850 - empty language added to .i18n

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 James Ni <jni@redhat.com> - 0.0.6-1
- Implement pango_language feature and bug fix

* Tue Mar 20 2012 James Ni <jni@redhat.com> - 0.0.5-1
- Fix issue of 'UnicodeWarning: Unicode equal comparison failed'

* Mon Mar 19 2012 James Ni <jni@redhat.com> - 0.0.4-1
- Bug fix and feature enhancement

* Thu Feb 23 2012 James Ni <jni@redhat.com> - 0.0.3-1
- Fix the issue of spec file

* Fri Feb 17 2012 James Ni <jni@redhat.com> - 0.0.2-3
- Fix the issue of spec file

* Wed Feb 08 2012 James Ni <jni@redhat.com> - 0.0.2-2
- Fix the issue of spec file

* Tue Feb 07 2012 James Ni <jni@redhat.com> - 0.0.2-1
- Update the licenses file and modify the spec file

* Mon Feb 06 2012 James Ni <jni@redhat.com> - 0.0.1-1
- initial package
