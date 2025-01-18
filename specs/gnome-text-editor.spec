%global glib2_version 2.80
%global gtk4_version 4.15
%global gtksourceview_version 5.10.0
%global enchant_version 2.2.0
%global libadwaita_version 1.6~alpha
%global libspelling_version 0.3.0

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:		gnome-text-editor
Version:	47.2
Release:	2%{?dist}
Summary:	A simple text editor for the GNOME desktop

# Code is GPL-3.0-or-later and the Appdata is CC0-1.0
License:	GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:		https://gitlab.gnome.org/GNOME/gnome-text-editor
Source0:	https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildRequires:	pkgconfig(editorconfig)
BuildRequires:	pkgconfig(enchant-2) >= %{enchant_version}
BuildRequires:	pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:	pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:	pkgconfig(gtksourceview-5) >= %{gtksourceview_version}
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:	pkgconfig(libspelling-1) >= %{libspelling_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	itstool
BuildRequires:	meson
BuildRequires:	/usr/bin/appstream-util

Requires:	glib2%{?_isa} >= %{glib2_version}
Requires:	enchant2%{?_isa} >= %{enchant_version}
Requires:	gtk4%{?_isa} >= %{gtk4_version}
Requires:	gtksourceview5%{?_isa} >= %{gtksourceview_version}
Requires:	libadwaita%{?_isa} >= %{libadwaita_version}
Requires:	libspelling%{?_isa} >= %{libspelling_version}

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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 nmontero <nmontero@redhat.com> - 47.2-1
- Update to 47.2

* Sat Oct 19 2024 David King <amigadave@amigadave.com> - 47.1-1
- Update to 47.1

* Mon Sep 16 2024 nmontero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Mon Aug 05 2024 nmontero <nmontero@redhat.com> - 47~beta-1
- Update to 47.beta

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 David King <amigadave@amigadave.com> - 47~alpha-1
- Update to 47.alpha

* Sat May 11 2024 David King <amigadave@amigadave.com> - 46.3-1
- Update to 46.3

* Sat Apr 13 2024 David King <amigadave@amigadave.com> - 46.1-1
- Update to 46.1

* Sat Mar 16 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Mon Mar 04 2024 David King <amigadave@amigadave.com> - 46~rc-1
- Update to 46.rc

* Wed Feb 14 2024 David King <amigadave@amigadave.com> - 46~beta-1
- Update to 46.beta

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 46~alpha-3
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 David King <amigadave@amigadave.com> - 46~alpha-1
- Update to 46.alpha

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 30 2023 Kalev Lember <klember@redhat.com> - 45.1-1
- Update to 45.1

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0
- Add minimum required libadwaita version

* Tue Aug 08 2023 Kalev Lember <klember@redhat.com> - 45~beta-1
- Update to 45.beta

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 45~alpha-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 45~alpha-3
- Rebuilt for ICU 73.2

* Wed Jul 05 2023 Adam Williamson <awilliam@redhat.com> - 45~alpha-2
- Backport an upstream commit to focus Document Type search box on open

* Mon Jul 03 2023 Kalev Lember <klember@redhat.com> - 45~alpha-1
- Update to 45.alpha

* Tue Jun 06 2023 David King <amigadave@amigadave.com> - 44.0-2
- Drop unnecessary libpcre BuildRequires (#2212743)

* Sat Mar 18 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Sat Mar 04 2023 David King <amigadave@amigadave.com> - 44~rc-1
- Update to 44.rc

* Thu Feb 16 2023 David King <amigadave@amigadave.com> - 44~beta-1
- Update to 44.beta

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

