Name:           gnome-2048
Version:        3.38.2
Release:        12%{?dist}
Summary:        A 2048 clone for GNOME

License:        GPL-3.0-or-later
URL:            https://wiki.gnome.org/Apps/2048
Source0:        https://download.gnome.org/sources/gnome-2048/3.38/gnome-2048-%{version}.tar.xz

Patch1:         0001-meson-drop-unused-argument-for-i18n.merge_file.patch

BuildRequires:  gcc
BuildRequires:  intltool itstool
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(libgnome-games-support-1)


%description
A GNOME clone of the popular game 2048
http://en.wikipedia.org/wiki/2048_(video_game)


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.TwentyFortyEight.desktop


%files -f %{name}.lang
%doc README.md code-of-conduct.md
%license COPYING
%{_bindir}/gnome-2048
%{_datadir}/applications/org.gnome.TwentyFortyEight.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.TwentyFortyEight.gschema.xml
%{_datadir}/metainfo/org.gnome.TwentyFortyEight.appdata.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.TwentyFortyEight*
%{_mandir}/man6/gnome-2048*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Yanko Kaneti <yaneti@declera.com> -  3.38.2-6
- Upstream fix for building with recent meson

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sat Aug 29 2020 Kalev Lember <klember@redhat.com> - 3.37.91-1
- Update to 3.37.91

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Sat Apr 25 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Tue Mar 10 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Sun Feb  2 2020 Yanko Kaneti <yaneti@declera.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Yanko Kaneti <yaneti@declera.com> - 3.35.2-1
- New development branch - 3.35

* Sat Nov 23 2019 Yanko Kaneti <yaneti@declera.com> - 3.34.4-1
- Update to 3.34.4

* Wed Oct 30 2019 Yanko Kaneti <yaneti@declera.com> - 3.34.3-1
- Update to 3.34.3

* Sun Oct 13 2019 Yanko Kaneti <yaneti@declera.com> - 3.34.2-1
- Update to 3.34.2

* Tue Oct 08 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug  5 2019 Yanko Kaneti <yaneti@declera.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-2
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Tue Feb  5 2019 Yanko Kaneti <yaneti@declera.com> - 3.31.90-1
- Update to 3.31.90
- Application ID change to org.gnome.TwentyFortyEight

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Yanko Kaneti <yaneti@declera.com> - 3.34.1-1
- Update to 3.34.1. Switch to meson

* Tue Sep  4 2018 Yanko Kaneti <yaneti@declera.com> - 3.30.0-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Yanko Kaneti <yaneti@declera.com> - 3.26.1-4
- Rebuild for libgnome-games-support soname bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Remove obsolete scriptlets

* Mon Oct  2 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.1-1
- Update to 3.26.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Yanko Kaneti <yaneti@declera.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Yanko Kaneti <yaneti@declera.com> - 3.21.92-1
- Update to 3.21.92

* Tue Aug 30 2016 Yanko Kaneti <yaneti@declera.com> - 3.21.91-1
- Update to 3.21.91

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Move desktop file validation to the check section

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Thu Apr 14 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.1-1
- Update to 3.20.1

* Mon Mar 21 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.92-1
- Update to 3.19.92

* Tue Mar  1 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.91-1
- Update to 3.19.91

* Wed Feb 17 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.90-1
- Update to 3.19.90. Drop libgames-support patch

* Tue Feb 16 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.4-3
- Patch+rebuild for libgames-support API/ABI change

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.4-1
- Update to 3.19.4

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 3.18.2-2
- Rebuilt for libgames-support soname bump

* Thu Nov 12 2015 Yanko Kaneti <yaneti@declera.com> - 3.18.2
- Update to 3.18.2

* Mon Oct 12 2015 Yanko Kaneti <yaneti@declera.com> - 3.18.1
- Update to 3.18.1. Drop upstreamed patch

* Sun Sep 27 2015 Yanko Kaneti <yaneti@declera.com> - 3.18.0-3
- Add patch to fix crash on startup. Bug #1266264

* Tue Sep 22 2015 Yanko Kaneti <yaneti@declera.com> - 3.18.0-2
- Unbundle libgames-support now that if has its first release

* Mon Sep 21 2015 Yanko Kaneti <yaneti@declera.com> - 3.18.0-1
- Update to 3.18.0. New libgames-support snapshot

* Tue Sep  1 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.91
- Update to 3.17.91

* Tue Aug 18 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.90
- Update to 3.17.90. Bundle libgames-support again

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun  7 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.1
- First official release - 3.17.1

* Tue Apr 21 2015 Yanko Kaneti <yaneti@declera.com> - 0.1.0-0.5.git3ea1464
- Unbundle libgames-support

* Tue Apr 21 2015 Yanko Kaneti <yaneti@declera.com> - 0.1.0-0.4.3ea1464
- Filter libgames-support from requires and provides

* Wed Apr 15 2015 Yanko Kaneti <yaneti@declera.com> - 0.1.0-0.3.3ea1464
- Update to upstream master.
- Temporarily bundle libgames-support until in gets in the distribution
  Review - https://bugzilla.redhat.com/show_bug.cgi?id=1195614 
- Use license macro
- Make builds verbose

* Fri Apr  3 2015 Yanko Kaneti <yaneti@declera.com> - 0.1.0-0.2.83c5a4a
- Apply upstream patch for bug 1208841

* Wed Jan 14 2015 Yanko Kaneti <yaneti@declera.com> - 0.1.0-0.1.83c5a4a
- Packaging attempt
