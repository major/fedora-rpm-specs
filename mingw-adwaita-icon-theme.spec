%{?mingw_package_header}

Name:           mingw-adwaita-icon-theme
Version:        43
Release:        2%{?dist}
Summary:        Adwaita icon theme for MingGW

License:        LGPLv3+ or CC-BY-SA
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/adwaita-icon-theme/43/adwaita-icon-theme-%{version}.tar.xz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  intltool
BuildRequires:  librsvg2
BuildRequires:  /usr/bin/gtk-encode-symbolic-svg

%description
This package contains the Adwaita icon theme used by the GNOME desktop.
This is the MinGW version of this package.

%package -n mingw32-adwaita-icon-theme
Summary:        MinGW Adwaita icon theme for MingGW
Requires:       pkgconfig

%description -n mingw32-adwaita-icon-theme
This package contains the icons and pkgconfig file for applications that use
the Adwaita icon theme.

%package -n mingw64-adwaita-icon-theme
Summary:        MinGW Adwaita icon theme for MingGW
Requires:       pkgconfig

%description -n mingw64-adwaita-icon-theme
This package contains the icons and pkgconfig file for applications that use
the Adwaita icon theme.

%prep
%autosetup -p1 -n adwaita-icon-theme-%{version}


%build
%mingw_configure
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-adwaita-icon-theme
%license COPYING*
%{mingw32_datadir}/pkgconfig/adwaita-icon-theme.pc
%dir %{mingw32_datadir}/icons/Adwaita
%{mingw32_datadir}/icons/Adwaita/8x8
%{mingw32_datadir}/icons/Adwaita/16x16
%{mingw32_datadir}/icons/Adwaita/22x22
%{mingw32_datadir}/icons/Adwaita/24x24
%{mingw32_datadir}/icons/Adwaita/32x32
%{mingw32_datadir}/icons/Adwaita/48x48
%{mingw32_datadir}/icons/Adwaita/64x64
%{mingw32_datadir}/icons/Adwaita/96x96
%{mingw32_datadir}/icons/Adwaita/256x256
%{mingw32_datadir}/icons/Adwaita/512x512
%{mingw32_datadir}/icons/Adwaita/scalable
%{mingw32_datadir}/icons/Adwaita/scalable-up-to-32
%{mingw32_datadir}/icons/Adwaita/index.theme
%{mingw32_datadir}/icons/Adwaita/cursors
%ghost %{mingw32_datadir}/icons/Adwaita/icon-theme.cache

%files -n mingw64-adwaita-icon-theme
%license COPYING*
%{mingw64_datadir}/pkgconfig/adwaita-icon-theme.pc
%dir %{mingw64_datadir}/icons/Adwaita
%{mingw64_datadir}/icons/Adwaita/8x8
%{mingw64_datadir}/icons/Adwaita/16x16
%{mingw64_datadir}/icons/Adwaita/22x22
%{mingw64_datadir}/icons/Adwaita/24x24
%{mingw64_datadir}/icons/Adwaita/32x32
%{mingw64_datadir}/icons/Adwaita/48x48
%{mingw64_datadir}/icons/Adwaita/64x64
%{mingw64_datadir}/icons/Adwaita/96x96
%{mingw64_datadir}/icons/Adwaita/256x256
%{mingw64_datadir}/icons/Adwaita/512x512
%{mingw64_datadir}/icons/Adwaita/scalable
%{mingw64_datadir}/icons/Adwaita/scalable-up-to-32
%{mingw64_datadir}/icons/Adwaita/index.theme
%{mingw64_datadir}/icons/Adwaita/cursors
%ghost %{mingw64_datadir}/icons/Adwaita/icon-theme.cache

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Sandro Mani <manisandro@gmail.com> - 43-1
- Update to 43

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Sandro Mani <manisandro@gmail.com> - 42.0-1
- Update to 42.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 41.0-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Sandro Mani <manisandro@gmail.com> - 41.0-1
- Update to 41.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Sandro Mani <manisandro@gmail.com> - 40.1.1-1
- Update to 40.1.1

* Sat Apr 17 2021 Sandro Mani <manisandro@gmail.com> - 40.0-1
- Update to 40.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Sandro Mani <manisandro@gmail.com> - 3.38.0-1
- Update to 3.38.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Sandro Mani <manisandro@gmail.com> - 3.36.1-1
- Update to 3.36.1

* Tue Mar 10 2020 Sandro Mani <manisandro@gmail.com> - 3.36.0-1
- Update to 3.36.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Sandro Mani <manisandro@gmail.com> - 3.34.3-1
- Update to 3.34.3

* Tue Nov 05 2019 Sandro Mani <manisandro@gmail.com> - 3.34.1-1
- Update to 3.34.1

* Mon Sep 16 2019 Sandro Mani <manisandro@gmail.com> - 3.34.0-1
- Update to 3.34.0

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Thu Apr 21 2016 Kalev Lember <klember@redhat.com> - 3.20-1
- Update to 3.20

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Sat Aug 22 2015 Kalev Lember <klember@redhat.com> - 3.17.4-1
- Update to 3.17.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0
- Use license macro for the COPYING file
- Don't use obsolete mingw_make_install macro
- Fix file listed twice rpmbuild warnings

* Wed Nov 19 2014 Richard Hughes <richard@hughsie.com> - 3.14.1-1
- Initial packaging attempt
