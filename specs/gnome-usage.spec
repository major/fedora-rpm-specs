%global tarball_version	%%(echo %{version} | tr '~' '.')
%global url_ver	%%(echo %{version} | cut -d. -f1,2)

%global gtk_version 4.11.3
%global libadwaita_version 1.5

Name:		gnome-usage
Version:	46.0
Release:	3%{?dist}
Summary:	A GNOME app to view information about use of system resources

License:	GPL-3.0-or-later AND CC0-1.0
URL:		https://wiki.gnome.org/Apps/Usage
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{tarball_version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk4) >= %{gtk_version}
BuildRequires:	pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(tracker-sparql-3.0)
BuildRequires:	vala

Requires:	adwaita-icon-theme
Requires:	gtk4 >= %{gtk_version}
Requires:	libadwaita >= %{libadwaita_version}

%description
gnome-usage lets you easily visualize the use of system resources such as
CPU, memory, and storage.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Usage.desktop

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS README.md NEWS
%{_bindir}/gnome-usage
%{_datadir}/applications/org.gnome.Usage.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Usage.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Usage.svg
%{_metainfodir}/org.gnome.Usage.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 20 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0 (#2270368)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 19 2021 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0
- Switch to tracker3

* Tue Aug 18 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jul 30 2019 Felipe Borges <feborges@redhat.com> - 3.33.2-1
- Update to 3.33.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Felipe Borges <feborges@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Fri Mar 22 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Feliep Borges <feborges@redhat.com> - 3.30.1-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Fri Mar 09 2018 Felipe Borges <feborges@redhat.com> - 3.27.92-1
- Initial import
