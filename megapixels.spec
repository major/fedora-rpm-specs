Name:       megapixels
Version:    1.7.0
Release:    2%{?dist}
Summary:    GTK4 camera application that knows how to deal with the media request api

License:    GPLv3+
URL:        https://gitlab.com/postmarketOS/megapixels
Source0:    https://gitlab.com/postmarketOS/megapixels/-/archive/%{version}/megapixels-%{version}.tar.gz
Source1:	post_install.py

Patch0:		0000-patch-build-gschemas.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:	cmake

BuildRequires:	pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.62.0
BuildRequires:	pkgconfig(gtk4)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(libfeedback-0.0)
BuildRequires:  inih-devel
BuildRequires:	zbar-devel
BuildRequires:	/usr/bin/xvfb-run
BuildRequires:	/usr/bin/xauth
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib

Requires: hicolor-icon-theme
# for postprocess.sh
Requires: dcraw


%description
A GTK4 camera application that knows how to deal with the media request api. It uses opengl to debayer the raw sensor data for the preview.

%prep
%autosetup -p1 -n %{name}-%{version}
cp %{SOURCE1} .

%build
%meson
%meson_build

%install
%meson_install


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.postmarketos.Megapixels.metainfo.xml

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.postmarketos.Megapixels.desktop

LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test
SH


%files
%dir %{_datadir}/megapixels
%dir %{_datadir}/megapixels/config

%{_bindir}/megapixels
%{_bindir}/megapixels-camera-test
%{_bindir}/megapixels-list-devices
%{_datadir}/applications/org.postmarketos.Megapixels.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.postmarketos.Megapixels.svg
%{_datadir}/megapixels/config/pine64,pinephone-1.0.ini
%{_datadir}/megapixels/config/pine64,pinephone-1.1.ini
%{_datadir}/megapixels/config/pine64,pinephone-1.2.ini
%{_datadir}/megapixels/config/pine64,pinetab.ini
%{_datadir}/megapixels/config/xiaomi,scorpio.ini
%{_datadir}/megapixels/config/pine64,pinephone,front.dcp
%{_datadir}/megapixels/config/pine64,pinephone,rear.dcp
%{_datadir}/megapixels/postprocess.sh
%{_datadir}/metainfo/org.postmarketos.Megapixels.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.postmarketos.Megapixels.gschema.xml

%doc README.md
%license LICENSE


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

%autochangelog

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 04 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Thu Aug 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Mon Dec 06 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Fri Nov 12 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Fri Sep 10 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Fri Jul 30 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue May 04 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Mon Mar 29 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.16.0-1
- Update to 0.16.0

* Sun Feb 21 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.15.0-1
- Update to 0.15.0

* Mon Jan 11 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0

* Fri Jan 01 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.2-1
- Update to 0.13.2

* Tue Dec 15 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.1-2
- Adding license and README

* Thu Dec 10 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1

* Thu Dec 03 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.12.0-2
- Adding dependencies for postprocess.sh

* Sat Nov 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.12.0-1
- Initial packaging

