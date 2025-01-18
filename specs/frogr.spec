Name:           frogr
Version:        1.7
Summary:        Flickr Remote Organizer for GNOME
Summary(de):    Flickr-Verwaltung für GNOME
Release:        7%{?dist}

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://wiki.gnome.org/Apps/Frogr
Source0:        https://download.gnome.org/sources/%{name}/1.7/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%description
Frogr is a small application for the GNOME desktop that allows users
to manage their accounts in the Flickr image hosting website. It
supports all the basic tasks, including uploading pictures, adding
descriptions, setting tags and managing sets.

%description -l de
Frogr ist eine Anwendung für die GNOME-Arbeitsumgebung zur Verwaltung der
Konten des Flickr-Bilderdienstes. Unterstützt werden sämtliche grundlegende
Aufgaben, wie das Hochladen von Bildern, Hinzufügen von Beschreibungen,
Setzen von Markierungen und Verwalten von Alben.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.frogr.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.frogr.appdata.xml


%files -f %{name}.lang
%license COPYING
%doc README NEWS AUTHORS THANKS MAINTAINERS TRANSLATORS
%{_bindir}/frogr
%{_datadir}/applications/org.gnome.frogr.desktop
%{_datadir}/frogr/
%{_datadir}/icons/hicolor/*/apps/org.gnome.frogr.png
%{_datadir}/icons/hicolor/*/apps/org.gnome.frogr.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.frogr-symbolic.svg
%{_datadir}/metainfo/org.gnome.frogr.appdata.xml
%{_mandir}/man1/frogr.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 01 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1.7-1
- Update to 1.7

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Kalev Lember <klember@redhat.com> - 1.6-1
- Update to 1.6

* Mon Sep 30 2019 Kalev Lember <klember@redhat.com> - 1.5-4
- Make sure to build against gstreamer1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Kalev Lember <klember@redhat.com> - 1.5-1
- Update to 1.5

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.4-3
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.4-1
- Update to 1.4
- Switch to meson for the build

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 1.3-2
- Backport appdata fixes from upstream

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 1.3-1
- Update to 1.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 06 2016 Kalev Lember <klember@redhat.com> - 1.2-1
- Update to 1.2
- Don't set group tags
- Use make_install macro
- Move desktop-file-validate to the check section
- Update project URLs (#1380998)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Kalev Lember <klember@redhat.com> - 1.0-1
- Update to 1.0
- Switch to building with gstreamer 1.0
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Richard Hughes <richard@hughsie.com> - 0.10-1
- New upstream version.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Richard Hughes <richard@hughsie.com> - 0.9-1
- New upstream version.

* Tue Apr 22 2014 Tomáš Mráz <tmraz@redhat.com> - 0.8-6
- Rebuild for new libgcrypt

* Mon Aug 05 2013 Christophe Fergeau <cfergeau@redhat.com> 0.8-5
- Don't set -DGTK_DISABLE_DEPRECATED as this breaks the build because of
  stock icons use
- Add missing BuildRequires

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Christophe Fergeau <cfergeau@redhat.com> 0.8-3
- Don't set -DG_DISABLE_DEPRECATED as this breaks the build because of
  GStaticRecMutex use

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild


* Mon Dec 31 2012 Mario Blättermann <mario.blaettermann@gmail.com> - 0.8-1
- rebuilt for new upstream version
- Added new dependencies

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild


* Sun May 27 2012 Mario Blättermann <mariobl@fedoraproject.org> 0.7-1
- Update to release 0.7

* Sat Aug 20 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.6.1-1
- Update to bugfix release 0.6.1

* Tue Aug 16 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.6-1
- Bumped version to 0.6
- Added gnome-doc-utils dependency
- Removed %%defattr
- Removed obsolete patches

* Sun Jul 03 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.5-4
- Added intltool in BuildRequires
- Removed minimum required version from BuildRequires
- Applied some patches from upstream

* Wed Jun 01 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.5-3
- Removed unneeded stuff from %%changelog

* Tue May 31 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.5-2
- Picked the spec file from Frogr's Git repository
- Removed help files for the time being
- Added German summary and description

* Fri May 27 2011 Mario Sanchez Prada <msanchez at, igalia.com> 0.5-1
- New upstream release

* Sat Feb 05 2011 Mario Sanchez Prada <msanchez at, igalia.com> 0.4-1
- New upstream release

* Wed Dec 22 2010 Mario Sanchez Prada <msanchez at, igalia.com> 0.3-1
- Updated for 0.3

* Mon Oct 12 2009 Mario Sanchez Prada <msanchez at, igalia.com> 0.2-1
- Updated for 0.2

* Sat Aug 22 2009 Adrian Perez <aperez at, igalia.com> 0.1.1-1
- First packaged release
