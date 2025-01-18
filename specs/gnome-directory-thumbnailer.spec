Name:           gnome-directory-thumbnailer
Version:        0.1.11
Release:        17%{?dist}
Summary:        Thumbnailer for directories

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/GnomeDirectoryThumbnailer
Source0:        https://download.gnome.org/sources/%{name}/0.1/%{name}-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/gnome-directory-thumbnailer/-/commit/8b39714ff8fd5de6643b5fdcf7fb01da35b82334
Patch1:         0001-Update-for-gnome-desktop-43-API-change.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
Buildrequires:  pkgconfig(gtk+-3.0)
Buildrequires:  pkgconfig(gnome-desktop-3.0)

BuildRequires:  intltool
BuildRequires: make

%description
Thumbnailer for directories based on some heuristics.


%prep
%autosetup -p1


%build
%configure --disable-silent-rules
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/gnome-directory-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gnome-directory-thumbnailer.thumbnailer
%doc AUTHORS NEWS README
%license COPYING


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb  2 2024 Yanko Kaneti <yaneti@declera.com> - 0.1.11-15
- SPDX migration. Replace api patch with upstream commit.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Yanko Kaneti <yaneti@declera.com> - 0.1.11-10
- Temporary workaround for recent gnome-desktop api changes

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 0.1.11-2
- Rebuilt for libgnome-desktop soname bump

* Mon Sep  2 2019 Yanko Kaneti <yaneti@declera.com> - 0.1.11-1
- Update to 0.1.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Yanko Kaneti <yaneti@declera.com> - 0.1.10-4
- Rebuilt for gnome-desktop3 soname bump

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Yanko Kaneti <yaneti@declera.com> - 0.1.10-1
- Update to 0.1.10

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 30 2017 Yanko Kaneti <yaneti@declera.com> - 0.1.9-1
- Update to 0.1.9.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Yanko Kaneti <yaneti@declera.com> - 0.1.8-1
- Update to 0.1.8.

* Tue Feb  9 2016 Yanko Kaneti <yaneti@declera.com> - 0.1.7-1
- Update to 0.1.7. Use license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 24 2015 Yanko Kaneti <yaneti@declera.com> - 0.1.6-3
- Bump for gnome-desktop3 soname change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  9 2015 Yanko Kaneti <yaneti@declera.com> - 0.1.6-1
- Update to 0.1.6

* Tue Apr 14 2015 Yanko Kaneti <yaneti@declera.com> - 0.1.5-1
- Update to 0.1.5

* Thu Jan 29 2015 Yanko Kaneti <yaneti@declera.com> - 0.1.4-1
- Update to 0.1.4

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Yanko Kaneti <yaneti@declera.com> - 0.1.2-1
- Update to 0.1.3

* Mon Feb 24 2014 Yanko Kaneti <yaneti@declera.com> - 0.1.2-2
- Update to 0.1.2

* Thu Feb 20 2014 Yanko Kaneti <yaneti@declera.com> - 0.1.1-2
- Rebuilt for gnome-desktop soname bump

* Fri Nov  8 2013 Yanko Kaneti <yaneti@declera.com> - 0.1.1-1
- Update to 0.1.1. Drop patches. Add translations

* Wed Oct 16 2013 Yanko Kaneti <yaneti@declera.com> - 0.1.0-3
- Initial packaging
- Change url
- Add upstream patches for standard directory icon overlay
- Add --disable-silent-rules
