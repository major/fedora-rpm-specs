%global gtk3_version 3.24.7
%global pygobject_version 3.36.1
%global gobject_introspection_version 1.35.9

# GNOME application id
%global application_id org.gnome.ActivityJournal

Name:           gnome-activity-journal
Version:        1.0.0
Release:        7%{?dist}
Summary:        Browse and search your Zeitgeist activities

#
# The sources are under the GPLv3+ license, except for the
# gnome-activity-journal icon which is CC-BY-SA
#
License:        GPLv3+ and CC-BY-SA
URL:            https://wiki.gnome.org/Apps/ActivityJournal
Source0:        https://gitlab.gnome.org/crvi/%{name}/-/raw/archive/sources/%{version}/%{name}-%{version}.tar.xz

# Fix import error caused by missing gstreamer gir libraries
Patch0:         %{name}-1.0.0-fix-import-error.patch
# Check tooltip preview object before using it
Patch1:         %{name}-1.0.0-check-tooltip.patch
# Fix incorrect specification for gstreamer gtk3 package
Patch2:         %{name}-1.0.0-gstreamer-not-gir.patch
# Update readme with updated dependencies and install steps
Patch3:         %{name}-1.0.0-update-readme.patch

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  file
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra

Requires:       gobject-introspection >= %{gobject_introspection_version}
Requires:       python3-gobject >= %{pygobject_version}
Requires:       python3-dbus
Requires:       gtk3 >= %{gtk3_version}
Requires:       python3-pyxdg
Requires:       dbus-x11
Requires:       gnome-desktop3
Requires:       libappindicator-gtk3
Requires:       librsvg2
Requires:       python3-zeitgeist >= 1.0.3
Requires:       hicolor-icon-theme

# For audio and video preview feature
Recommends:    gstreamer1-plugins-base
# For video preview feature
Recommends:    gstreamer1-plugins-good-gtk

%description
GNOME Activity Journal is a tool for easily browsing and finding files
on your computer. It shows a chronological journal of all file
activity.

%prep
%autosetup -p1

%build
%py3_build

%install
# Due to https://bugs.launchpad.net/python-distutils-extra/+bug/1045810
%{__python3} %{py_setup} install -O1 --root %{buildroot}
rm -rfv %{buildroot}%{_bindir}/__pycache__
rm -rfv %{buildroot}%{_datadir}/icons/hicolor/*/status
rm -rfv %{buildroot}%{_datadir}/pixmaps
rm -rfv %{buildroot}%{_datadir}/zeitgeist/_zeitgeist

%find_lang %{name} --with-gnome --all-name
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{application_id}.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS

# binary file
%{_bindir}/%{name}

# data files
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/applications/%{application_id}.desktop
%{_datadir}/man/man1/%{name}.1.gz
%{_datadir}/glib-2.0/schemas/%{application_id}.gschema.xml

# python files
%{python3_sitelib}/gnome_activity_journal-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.10

* Tue Apr 06 2021 crvi <crvi@fedoraproject.org> - 1.0.0-2
- Fix incorrect gobject-introspection dependency

* Sun Mar 14 2021 crvi <crvisqr@gmail.com> - 1.0.0-1
- Unretire and update to 1.0.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.0-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-12
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Mads Villadsen <maxx@krakoa.dk> - 0.8.0-4
- Add patch to fix issue running with newest version of zeitgeist. Fixes bug #821121.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 11 2011 Mads Villadsen <maxx@krakoa.dk> - 0.8.0-1
- Update to 0.8.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Mads Villadsen <maxx@krakoa.dk> - 0.6.0-1
- Update to 0.6.0
- Added drag and drop support
- Added support for XChat, Bazaar
- Added tray icon support
- Minor interface changes
- Various bug fixes

* Tue Sep 28 2010 Mads Villadsen <maxx@krakoa.dk> - 0.5.0.1-1
- Update to 0.5.0.1
- Fixes issues with hamster-applet
- Removes some debug output
- Minor bugfixes

* Mon Aug 23 2010 Mads Villadsen <maxx@krakoa.dk> - 0.5.0-1
- Update to latest release
- Add minor patch to make the version check work with zeitgeist 0.5.0

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.4.1-2.20100721bzr1010
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 21 2010 Mads Villadsen <maxx@krakoa.dk> - 0.3.4.1-1.20100721bzr1010
- Use a bzr version to get g-a-j working with new hamster-applet

* Sun May  9 2010 Mads Villadsen <maxx@krakoa.dk> - 0.3.4-1
- Update to latest release
- Fixes bugs #579024, #579148, #579144, #580740, #580309, #591444
- Don't use --skip-build in install target as it breaks various part of the installation
- Removed the install patch as the installation is better behaved now
- Removed the startup shell script as it is no longer needed

* Sun Feb 21 2010 Mads Villadsen <maxx@krakoa.dk> - 0.3.3-1
- Update to new release
- Added a patch for better installation
- spec file updated to handle GConf schema, icons, languages, more
- Add intltool to BuildRequires

* Fri Jan 22 2010 Mads Villadsen <maxx@krakoa.dk> - 0.3.2-1
- Initial package

