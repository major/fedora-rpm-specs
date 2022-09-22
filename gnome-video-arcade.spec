### Abstract ###

Name: gnome-video-arcade
Version: 0.8.8
Release: 13%{?dist}
License: GPLv3+
Summary: GNOME Video Arcade is a MAME front-end for GNOME
URL: https://wiki.gnome.org/Apps/GnomeVideoArcade
Source: http://download.gnome.org/sources/%{name}/0.8/%{name}-%{version}.tar.xz

### Dependencies ###

Requires: mame

### Build Dependencies ###

BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: intltool
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig(sqlite3)
BuildRequires: yelp-tools
BuildRequires: make

%description
GNOME Video Arcade is a MAME front-end for GNOME.

%prep
%setup -q

%build
export MAME=/usr/bin/mame
%configure
%make_build

%install
%make_install

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Remove GTK-Doc files
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gtk-doc/html/%{name}

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/GConf/gsettings/%{name}.convert
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/glib-2.0/schemas/org.gnome.VideoArcade.gschema.xml
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.8-2
- Remove obsolete scriptlets

* Tue Oct 31 2017 Matthew Barnes <mbarnes@redhat.com> - 0.8.8-1
- Update to 0.8.8
- Drop requirement on mame-data since it no longer provides the
  supplemental data files we need (history.dat, etc.).

* Sun Apr 16 2017 Sérgio Basto <sergio@serjux.com> - 0.8.6-1
- Update gnome-video-arcade to 0.8.6

* Mon Sep 14 2015 Matthew Barnes <mbarnes@redhat.com> - 0.8.5-1
- Update to 0.8.5

* Wed Aug 26 2015 Matthew Barnes <mbarnes@redhat.com> - 0.8.4-1
- Update to 0.8.4

* Mon Sep 24 2012 Matthew Barnes <mbarnes@redhat.com> - 0.8.3-2
- Require mame instead of sdlmame.

* Thu Feb 16 2012 Matthew Barnes <mbarnes@redhat.com> - 0.8.3-1
- Update to 0.8.3

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan 15 2012 Matthew Barnes <mbarnes@redhat.com> - 0.8.1-1
- Update to 0.8.1
- Drop libX11 patch.

* Sun May 15 2011 Matthew Barnes <mbarnes@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Mon May 31 2010 Matthew Barnes <mbarnes@redhat.com> - 0.7.1-1
- Update to 0.7.1
- Add build requirement for unique-devel.

* Thu Mar 11 2010 Matthew Barnes <mbarnes@redhat.com> - 0.7.0-1
- Update to 0.7.0
- Bump gtk2_version to 2.18.
- Add gstreamer-plugins-base build requirement.

* Sat Jan 23 2010 Matthew Barnes <mbarnes@redhat.com> - 0.6.8-1
- Update to 0.6.8

* Sun Apr 26 2009 Matthew Barnes <mbarnes@redhat.com> - 0.6.7-1
- Update to 0.6.7

* Sun Apr 05 2009 Matthew Barnes <mbarnes@redhat.com> - 0.6.6-2
- Explicitly require libXres-devel to work around a build issue in F-10.

* Sun Apr 05 2009 Matthew Barnes <mbarnes@redhat.com> - 0.6.6-1
- Update to 0.6.6
- Update URL tag to GitHub home page.
- Update Source tag to download.gnome.org.
- Add --with-nplayers-file configure option.
- Require sdlmame-data >= 0.130-1 for nplayers.ini (#416).

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.6.5-2
- rebuild for new F11 features

* Fri Nov 21 2008 Matthew Barnes <mbarnes@redhat.com> - 0.6.5-1
- Update to 0.6.5

* Sat Sep 27 2008 Matthew Barnes <mbarnes@redhat.com> - 0.6.4-1
- Update to 0.6.4

* Tue Aug 19 2008 Matthew Barnes <mbarnes@redhat.com> - 0.6.3-3
- Fix name of category file (Catver.ini, not catver.ini).

* Tue Jul 29 2008 Matthew Barnes <mbarnes@redhat.com> - 0.6.3-2
- First upload to rpmfusion.
- Add build requirement for intltool.

* Sun Jun 29 2008 Matthew Barnes <mbarnes@redhat.com> - 0.6.3-1
- Update to 0.6.3

* Mon Jun 16 2008 Matthew Barnes <mbarnes@redhat.com> - 0.6.2-1
- Update to 0.6.2
- Add build requirement for libwnck-devel.

* Sun May 25 2008 Matthew Barnes <mbarnes@redhat.com> - 0.6.1.1-1
- Update to 0.6.1.1

* Sat May 17 2008 Matthew Barnes <mbarnes@redhat.com> - 0.6.1-1
- Update to 0.6.1

* Sat Apr 19 2008 Matthew Barnes <mbarnes@redhat.com> - 0.6.0-1
- Update to 0.6.0
- Bump GTK+ requirement to 2.12.

* Sun Mar 02 2008 Matthew Barnes <mbarnes@redhat.com> - 0.5.6-2
- Add build requirement for gnome-icon-theme.

* Sat Mar 01 2008 Matthew Barnes <mbarnes@redhat.com> - 0.5.6-1
- Update to 0.5.6

* Fri Jan 11 2008 Matthew Barnes <mbarnes@redhat.com> - 0.5.5-1
- Update to 0.5.5

* Thu Dec 27 2007 Matthew Barnes <mbarnes@redhat.com> - 0.5.4-1
- Update to 0.5.4
- Require sdlmame-data >= 0.122-2 for catver.ini (#125).

* Sun Dec 09 2007 Matthew Barnes <mbarnes@redhat.com> - 0.5.3-3
- Fix a scrollkeeper issue on Fedora 7 (patch by Ian Chapman).

* Sat Dec 08 2007 Matthew Barnes <mbarnes@redhat.com> - 0.5.3-2
- Use full URL for Source tag, add missing BRs, install ChangeLog.

* Mon Dec 03 2007 Matthew Barnes <mbarnes@redhat.com> - 0.5.3-1
- Initial packaging for Dribble repository.
