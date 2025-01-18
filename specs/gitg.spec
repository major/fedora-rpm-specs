%global glib2_version 2.68.0
%global libgit2_glib_version 1.2.0

Name:           gitg
Version:        44
Release:        9%{?dist}
Summary:        GTK+ graphical interface for the git revision control system

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Gitg
Source0:        https://download.gnome.org/sources/%{name}/44/%{name}-%{version}.tar.xz

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/chrpath
BuildRequires:  /usr/bin/desktop-file-validate

BuildRequires:  gettext
BuildRequires:  meson

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= %{libgit2_glib_version}
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  python3-devel
BuildRequires:  vala

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# PeasGtk typelib required by the plugins engine
Requires:       libpeas-gtk%{?_isa}

%description
gitg is the GNOME GUI client to view git repositories.


%package libs
Summary:        Backend Library for gitg
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       libgit2-glib%{?_isa} >= %{libgit2_glib_version}

%description libs
libgitg is a GObject based library that provides an easy access to git methods
through GObject based methods


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.


%prep
%autosetup -p1


%build
%meson \
        -Dpython=true

%meson_build


%install
%meson_install

# Remove lib64 rpaths
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/gitg
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gitg/plugins/libdiff.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gitg/plugins/libfiles.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libgitg-ext-1.0.so.0.0.0

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.gitg.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/org.gnome.gitg.appdata.xml


%ldconfig_scriptlets libs


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/gitg
%{_datadir}/applications/org.gnome.gitg.desktop
%{_datadir}/gitg/
%{_datadir}/glib-2.0/schemas/org.gnome.gitg.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gitg.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gitg-symbolic.svg
%{_metainfodir}/org.gnome.gitg.appdata.xml
%{_mandir}/man1/gitg.1*

%files libs
%license COPYING
%{_libdir}/libgitg-*.so.*
%{_libdir}/gitg/
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gitg*-1.0.typelib
%{python3_sitelib}/gi/overrides/*

%files devel
%{_includedir}/libgitg-1.0/
%{_includedir}/libgitg-ext-1.0/
%{_libdir}/libgitg-*.so
%{_libdir}/pkgconfig/libgitg*-1.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gitg-1.0.gir
%{_datadir}/gir-1.0/GitgExt-1.0.gir
%dir %{_datadir}/glade
%dir %{_datadir}/glade/catalogs
%{_datadir}/glade/catalogs/gitg-glade.xml
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgitg-1.0.vapi
%{_datadir}/vala/vapi/libgitg-ext-1.0.vapi


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 44-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 26 2024 David King <amigadave@amigadave.com> - 44-8
- Rebuild against gspell

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 44-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 44-5
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 44-4
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 25 2023 Kalev Lember <klember@redhat.com> - 44-1
- Update to 44

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 41-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Kalev Lember <klember@redhat.com> - 41-4
- Fix the build with meson 0.61.0 (rhbz#2113239)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 41-2
- Rebuilt for Python 3.11

* Thu Jan 20 2022 David King <amigadave@amigadave.com> - 41-1
- Update to 41 (#2035775)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.32.1-9
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.32.1-5
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.32.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.32.1-2
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Pete Walter <pwalter@fedoraproject.org> - 3.32.1-1
- Update to 3.32.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Fabio Valentini <decathorpe@gmail.com> - 3.32.0-2
- Update dependency version constraints and validate appdata file.

* Thu May 23 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Pete Walter <pwalter@fedoraproject.org> - 3.30.1-3
- Add missing libpeas-gtk runtime dependency (#1658682)

* Mon Nov 12 2018 Pete Walter <pwalter@fedoraproject.org> - 3.30.1-2
- Fix the build with latest libgit2-glib

* Fri Oct 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Wed Oct 10 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0
- Switch to the meson build system

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-8
- Rebuild for libgit2 0.27.x

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.26.0-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-4
- Switch to %%ldconfig_scriptlets

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-3
- Remove obsolete scriptlets

* Sat Nov 18 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.26.0-2
- rebuild for python liblarch rebuild

* Wed Aug 09 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.24.0-4
- Fix conflicts with current libgit2-glib

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.24.0-2
- Rebuild for libgit2 0.26.x

* Tue May 09 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Thu Feb 16 2017 Kalev Lember <klember@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Thu Feb 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.23.0-1
- Update to 3.23

* Thu Feb 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.22.0-4
- Rebuild for libgit2-0.25.x

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.22.0-3
- Rebuild for Python 3.6

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.0-2
- BR vala instead of obsolete vala-tools subpackage

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Sat Aug 27 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91
- Set minimum libgit2-glib version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.20.0-1
- Update to 3.20.0
- Rebuilt for libgit2 0.24.0

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.6-1
- Update to 3.19.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Richard Hughes <rhughes@redhat.com> - 3.19.5-1
- Update to 3.19.5

* Mon Jan 11 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Tue Dec 29 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Use make_install macro

* Tue Aug 11 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.17.1-1
- Update to 3.17.1

* Fri Jul 31 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@Foobar.org> - 3.17.0-0.20150731gitbb22c05
- Update to git snapshot

* Fri Jul 31 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.16.1-3
- Rebuilt for libgit2-0.23.0 and libgit2-glib-0.23

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2
- Use license macro for the COPYING file

* Mon Feb 09 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.15.1-1
- Update to latest upstream release
- Add libsecret BR
- Fix building with vala 0.25
- Bump libgit2-glib to 0.22.0
- Implement basic history search
- Implement basic fetch
- Implement remote state tracking
- Add remote management
- Show hunk context in diff
- Implement configuring of mainlines
- Implement preserving mainlines on history lanes
- Implement opening file from staging area
- Allow choosing merge diff parent
- Implement submodule patch stage/unstage
- Implement workdir submodule stage/unstage
- Show submodules in dash
- Updated translations


* Fri Dec 12 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Wed Sep 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Fri Aug 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-2
- Switch to webkitgtk4
- Remove lib64 rpaths

* Wed Aug 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91
- Enable python support

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.3.3-2
- Rebuilt for gobject-introspection 1.41.4

* Mon Jun 30 2014 Ignacio Casal Quinteiro <icq@gnome.org> - 0.3.3-1
- update to 0.3.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 22 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.3.2-1
- New upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 05 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 0.2.7-1
- update to 0.2.7

* Thu Mar 28 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 0.2.6-1
- update to 0.2.6

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.5-6
- Rebuilt for gtksourceview3 soname bump

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 0.2.5-3
- Silence rpm scriptlet output

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 04 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 0.2.5-1
- update to 0.2.5

* Thu Jul 21 2011 James Bowes <jbowes@redhat.com> 0.2.3-1
- update to 0.2.3

* Fri Apr 22 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.2-3
- Fix Obsoletes/Provides

* Thu Apr 21 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.2-2
- Remove libtool archive and static library
- Rename libgitg(-devel) package to follow naming guidelines

* Fri Apr 01 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 0.2.2-1
- update to 0.2.2

* Tue Feb 08 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 0.2.0-1
- update to 0.2.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr 13 2010 James Bowes <jbowes@redhat.com> 0.0.6-3
- update icon cache

* Tue Apr 13 2010 James Bowes <jbowes@redhat.com> 0.0.6-2
- Remove pixmaps dir

* Tue Apr 13 2010 James Bowes <jbowes@redhat.com> 0.0.6-1
- Update to 0.0.6

* Tue Sep 15 2009 James Bowes <jbowes@redhat.com> 0.0.5-1
- Update to 0.0.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 02 2009 James Bowes <jbowes@redhat.com> 0.0.3-1
- Initial packaging for Fedora.

