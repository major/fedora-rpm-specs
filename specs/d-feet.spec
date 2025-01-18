Name: d-feet 
Version: 0.3.16
Release: 16%{?dist}
Summary: A powerful D-Bus Debugger

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://wiki.gnome.org/Apps/DFeet
Source0: https://download.gnome.org/sources/d-feet/0.3/d-feet-%{version}.tar.xz
# Fix the build with meson 0.61.0
# https://gitlab.gnome.org/GNOME/d-feet/-/merge_requests/32
Patch0: 32.patch

BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtk3-devel
BuildRequires: itstool
BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: python3-pycodestyle
BuildRequires: libappstream-glib
Requires: libwnck3
Requires: python3-gobject

%description
D-Feet is an easy to use D-Bus debugger.

D-Bus is an RPC library used on the Desktop.  D-Feet can be used to inspect
D-Bus objects of running programs and invoke methods on those objects.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang d-feet --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.dfeet.desktop

%files -f d-feet.lang
%license COPYING
%doc AUTHORS README.md NEWS
%{python3_sitelib}/dfeet/
%{_bindir}/d-feet
%{_datadir}/applications/org.gnome.dfeet.desktop
%{_datadir}/d-feet/
%{_datadir}/glib-2.0/schemas/org.gnome.dfeet.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.dfeet.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.dfeet-symbolic.svg
%{_datadir}/metainfo/org.gnome.dfeet.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.16-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.16-13
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.16-12
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 0.3.16-8
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.16-5
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.16-2
- Rebuilt for Python 3.10

* Fri May 07 2021 Kalev Lember <klember@redhat.com> - 0.3.16-1
- Update to 0.3.16

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.15-5
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.15-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.15-2
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Kalev Lember <klember@redhat.com> - 0.3.15-1
- Update to 0.3.15
- Switch to the meson build system

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.14-2
- Use python3-pycodestyle instead of python2-pep8

* Fri Oct 26 2018 Kalev Lember <klember@redhat.com> - 0.3.14-1
- Update to 0.3.14
- Use make_build macro
- Use upstream screenshots in appdata

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.13-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.13-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.13-2
- Remove obsolete scriptlets

* Fri Dec 01 2017 Kalev Lember <klember@redhat.com> - 0.3.13-1
- Update to 0.3.13

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 0.3.12-1
- Update to 0.3.12

* Tue Jun 06 2017 Debarshi Ray <rishi@fedoraproject.org> - 0.3.11-6
- Don't use Wnck on non-X11 (RH #1432996)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.11-4
- Rebuild for Python 3.6

* Tue Oct 04 2016 Kalev Lember <klember@redhat.com> - 0.3.11-3
- Update project URLs (#1380982)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.11-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 0.3.11-1
- Update to 0.3.11
- Use make_install macro
- Use license macro for COPYING
- Switch to Python 3 (#1314029)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 0.3.9-2
- Use better AppData screenshots

* Sun Jun 08 2014 Kalev Lember <kalevlember@gmail.com> - 0.3.9-1
- Update to 0.3.9
- Include the appdata file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 26 2013 Kalev Lember <kalevlember@gmail.com> - 0.3.7-1
- Update to 0.3.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 09 2013 Kalev Lember <kalevlember@gmail.com> - 0.3.5-1
- Update to 0.3.5

* Sat May 25 2013 Kalev Lember <kalevlember@gmail.com> - 0.3.4-1
- Update to 0.3.4
- Switch to the autotools build
- Add glib-compile-schemas scriptlets

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Matthias Clasen <mclasen@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 0.3.1-1
- Update to 0.3.1
- Adjust deps for the switch to gobject-introspection
- Modernize the spec file

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> - 0.1.15-1
- Update to 0.1.15
- Update the URLs; it's now a GNOME hosted project

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 John (J5) Palmieri <johnp@redhat.com> - 0.1.14-1
- update to upstream 0.1.14
- new hires icons
- fix config parsing
- remove dependency on glade
- bump requires to python 2.5

* Mon Aug 23 2010 John (J5) Palmieri <johnp@redhat.com> - 0.1.12-1
- update to upstream 0.1.12
- Add the ability to specify a bus on the command line using the --bus-address 
  or -a switch (jdahlin)
- fix up some UI bugs (jdahlin)
- move project to gnome.org

* Mon Aug 9 2010 John (J5) Palmieri <johnp@redhat.com> - 0.1.11-1
- update to upstream 0.1.11
- fix up .desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 John (J5) Palmieri <johnp@redhat.com> - 0.1.10-1
- update to upstream 0.1.10
- output now pretty printed
- all simple types supported
- ui cleanups

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.8-2
- Rebuild for Python 2.6

* Mon Jan 07 2008 John (J5) Palmieri <johnp@redhat.com> - 0.1.8-1
- update to upstream 0.1.8
- complex types are now supported in the output
- fixed a typo s/Unkown/Unknown

* Mon Jan 07 2008 John (J5) Palmieri <johnp@redhat.com> - 0.1.7-1
- update to upstream 0.1.7
- update the license for _introspect_parser.py to permissive
  since dbus-python was relicense (this just makes including this code
  easier since the GPL/AFL dual license confused some people)
- add placeholder icons to denote methods, properties and signals
  does someone want to make a standard set of programmer tool icons?
- default service icon now added to the package for distributions
  that do not ship an icon called icon-service
- argument types now show the parameter name if given in the introspect data
- selecting a property now attempts to read the propety and display a value
- prettier formatting for introspect output
- various bug fixes

* Wed Dec 12 2007 John (J5) Palmieri <johnp@redhat.com> - 0.1.6-1
- update to upstream 0.1.6 which fixes issues with .ui files not being installed

* Wed Dec 12 2007 John (J5) Palmieri <johnp@redhat.com> - 0.1.5-1
- update to upstream 0.1.5
- attach to any bus
- execute button makes executing methods more descoverable
- icons show up if app associated with a name has a toplevel window
- initial support for icons on introspect nodes 
- syntax highlighting for methods and signals
- support for property lists in the introspect data
- tabs are restored when started again

* Fri Dec 07 2007 John (J5) Palmieri <johnp@redhat.com> - 0.1.4-1
- update to upstream 0.1.4 which cleans up some bugs
- remove scrollkeeper BR
- make use description does not exceed 80 characters per line

* Wed Dec 05 2007 John (J5) Palmieri <johnp@redhat.com> - 0.1.3-1
- update to upstream 0.1.3 which cleans up the .desktop file and
  only install the icon in the hicolor theme

* Wed Dec 05 2007 John (J5) Palmieri <johnp@redhat.com> - 0.1.2-3
- pick up %%{python_sitelib}/* instead of %%{python_sitelib}/dfeet/
  in files section so we pick up the python egg stuff

* Tue Dec 04 2007 John (J5) Palmieri <johnp@redhat.com> - 0.1.2-2
- clean up spec file

* Tue Dec 04 2007 John (J5) Palmieri <johnp@redhat.com> - 0.1.2-1
- update to 0.1.2 which fixes the .desktop file so it validates

* Tue Dec 04 2007 John (J5) Palmieri <johnp@redhat.com> - 0.1.1-1
- update to 0.1.1 which fixes the .desktop file category 

* Tue Dec 04 2007 John (J5) Palmieri <johnp@redhat.com> - 0.1-1
- Initial build.
