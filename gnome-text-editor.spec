%global glib2_version 2.73
%global gtk4_version 4.7
%global gtksourceview_version 5.5.0
%global enchant_version 2.2.0

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:		gnome-text-editor
Version:	44~alpha
Release:	1%{?dist}
Summary:	A simple text editor for the GNOME desktop

License:	GPLv3+
URL:		https://gitlab.gnome.org/GNOME/gnome-text-editor
Source0:	https://download.gnome.org/sources/%{name}/44/%{name}-%{tarball_version}.tar.xz

BuildRequires:	pkgconfig(editorconfig)
BuildRequires:	pkgconfig(enchant-2) >= %{enchant_version}
BuildRequires:	pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:	pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:	pkgconfig(gtksourceview-5) >= %{gtksourceview_version}
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	itstool
BuildRequires:	meson
BuildRequires:	/usr/bin/appstream-util

Requires:	glib2%{?_isa} >= %{glib2_version}
Requires:	enchant2%{?_isa} >= %{enchant_version}
Requires:	gtk4%{?_isa} >= %{gtk4_version}
Requires:	gtksourceview5%{?_isa} >= %{gtksourceview_version}

%description
GNOME Text Editor is a simple text editor that focuses on session management.
It works hard to keep track of changes and state even if you quit the application.
You can come back to your work even if you've never saved it to a file.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson -Ddevelopment=false
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.TextEditor.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.TextEditor.desktop


%files -f %{name}.lang
%doc README.md NEWS
%license COPYING
%{_bindir}/gnome-text-editor
%{_metainfodir}/org.gnome.TextEditor.appdata.xml
%{_datadir}/applications/org.gnome.TextEditor.desktop
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/org.gnome.TextEditor.service
%{_datadir}/glib-2.0/schemas/org.gnome.TextEditor.gschema.xml
%{_datadir}/gnome-text-editor/
%{_datadir}/icons/hicolor/*/*/*.svg


%changelog
* Mon Feb 06 2023 David King <amigadave@amigadave.com> - 44~alpha-1
- Update to 44.alpha

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 43.1-3
- Rebuild for ICU 72

* Thu Oct 06 2022 Kalev Lember <klember@redhat.com> - 43.1-2
- Backport upstream patch to fix the release number in appdata

* Tue Oct 04 2022 Kalev Lember <klember@redhat.com> - 43.1-1
- Update to 43.1

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Tue Aug 09 2022 Kalev Lember <klember@redhat.com> - 43~alpha1-1
- Update to 43.alpha1

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 43~alpha0-3
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 43~alpha0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kalev Lember <klember@redhat.com> - 43~alpha0-1
- Update to 43.alpha0

* Tue Jun 14 2022 David King <amigadave@amigadave.com> - 42.2-1
- Update to 42.2 (#2096085)

* Fri May 27 2022 Link Dupont <link@sub-pop.net> - 42.1-2
- Patch to fix session handling crash (RHBZ#2071116)

* Fri Apr 22 2022 David King <amigadave@amigadave.com> - 42.1-1
- Update to 42.1 (#2077673)

* Sat Mar 19 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Tue Mar 08 2022 David King <amigadave@amigadave.com> - 42~rc1-1
- Update to 42.rc1

* Thu Jan 20 2022 David King <amigadave@amigadave.com> - 42~alpha2-1
- Update to 42.alpha2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Neal Gompa <ngompa@fedoraproject.org> - 41.1-1
- Update to 41.1

* Tue Oct 05 2021 Neal Gompa <ngompa@fedoraproject.org> - 41.0-1
- Initial packaging

