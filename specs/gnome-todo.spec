%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-todo
Version:        41.0
Release:        12%{?dist}
Summary:        Personal task manager for GNOME

License:        GPL-3.0-or-later
URL:            https://git.gnome.org/browse/gnome-todo/
Source0:        https://download.gnome.org/sources/%{name}/41/%{name}-%{tarball_version}.tar.xz
Patch0:         gnome-todo-41.0-libportal-0.5.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libecal-2.0) >= 3.33.2
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%description
GNOME To Do is a small application to manage your personal tasks. It
uses GNOME technologies, and so it has complete integration with the
GNOME desktop environment.

%package devel
Summary:        Development files needed to write plugins for GNOME To Do

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Todo.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Todo.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%{_bindir}/gnome-todo
%{_datadir}/applications/org.gnome.Todo.desktop
%{_datadir}/metainfo/org.gnome.Todo.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Todo.service
%{_datadir}/glib-2.0/schemas/org.gnome.todo.*.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Todo*.svg
%{_datadir}/icons/hicolor/symbolic/actions/*.svg
%{_libdir}/girepository-1.0/Gtd-1.0.typelib

%files devel
%{_includedir}/gnome-todo/
%{_libdir}/pkgconfig/gnome-todo.pc
%{_datadir}/gir-1.0/Gtd-1.0.gir

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Milan Crha <mcrha@redhat.com> - 41.0-8
- Rebuilt for evolution-data-server soname version bump

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kalev Lember <klember@redhat.com> - 41.0-4
- Rebuilt for evolution-data-server soname bump

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 David King <amigadave@amigadave.com> - 41.0-2
- Build against libportal 0.5

* Thu Sep 16 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Wed Sep 15 2021 Kalev Lember <klember@redhat.com> - 41~rc-1
- Update to 41.rc

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 12 2021 Milan Crha <mcrha@redhat.com> - 3.28.1-12
- Rebuilt for evolution-data-server soname version bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Milan Crha <mcrha@redhat.com> - 3.28.1-8
- Rebuilt for evolution-data-server soname version bump

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Milan Crha <mcrha@redhat.com> - 3.28.1-5
- Add patch to build against newer evolution-data-server (libecal-2.0)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Milan Crha <mcrha@redhat.com> - 3.28.1-3
- Rebuilt for evolution-data-server soname bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.90-1
- Update to 3.27.90

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 3.26.2-3.1
- Rebuilt for evolution-data-server soname bump

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-2.1
- Remove obsolete scriptlets

* Wed Nov 08 2017 Milan Crha <mcrha@redhat.com> - 3.26.2-2
- Rebuild for newer libical

* Wed Nov 01 2017 David King <amigadave@amigadave.com> - 3.26.2-1
- Update to 3.26.2 (#1508187)

* Sun Oct 01 2017 David King <amigadave@amigadave.com> - 3.26.1-1
- Update to 3.26.1 (#1494293)

* Fri Aug 11 2017 David King <amigadave@amigadave.com> - 3.25.90-1
- Update to 3.25.90 (#1480399)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 David King <amigadave@amigadave.com> - 3.25.3-1
- Update to 3.25.3 (#1463023)

* Tue Apr 25 2017 David King <amigadave@amigadave.com> - 3.25.1-1
- Update to 3.25.1 (#1445102)

* Mon Apr 24 2017 David King <amigadave@amigadave.com> - 3.24.0-1
- Update to 3.24.0 (#1444840)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Wed Nov 02 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 3.20.2-3
- Rebuild for newer evolution-data-server

* Wed Jun 22 2016 Milan Crha <mcrha@redhat.com> - 3.20.2-2
- Rebuild for newer evolution-data-server

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Tue Apr 26 2016 Igor Gnatenko <ignatenko@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 3.20.0-2
- rebuild for ICU 57.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 David King <amigadave@amigadave.com> - 3.19.92-1
- Update to 3.19.92 (#1317712)

* Thu Mar 03 2016 David King <amigadave@amigadave.com> - 3.19.91-1
- Update to 3.19.91

* Wed Feb 17 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90 (#1309142)

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 3.19.5-2
- Rebuild for libcamel bump

* Fri Feb 12 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.19.5-1
- Update to 3.19.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David Tardon <dtardon@redhat.com> - 3.18.1-2
- rebuild for libical 2.0.0

* Wed Oct 14 2015 David King <amigadave@amigadave.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 28 2015 David King <amigadave@amigadave.com> - 3.18.0-3
- Update patch for service file (#1266868)

* Mon Sep 28 2015 David King <amigadave@amigadave.com> - 3.18.0-2
- Fix launching from GNOME Shell (#1266868)

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Wed Sep 02 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Tue Jul 21 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Thu Jun 25 2015 David King <amigadave@amigadave.com> - 3.17.3.1-1
- Update to 3.17.3.1

* Tue Jun 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.17.3-1
- Initial package
