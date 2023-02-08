Name:		photoqt
Version:	3.0
Release:	1%{?dist}
Summary:	A fast Qt image viewer

License:	GPLv2+
URL:		http://photoqt.org/
Source0:	http://photoqt.org/pkgs/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	phonon-qt5-devel
BuildRequires:	GraphicsMagick-c++-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	LibRaw-devel
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils
BuildRequires:	zlib-devel
BuildRequires:	poppler-qt5-devel
BuildRequires:	freeimage-plus-devel
BuildRequires:	DevIL-devel
BuildRequires:	extra-cmake-modules
BuildRequires:	libarchive-devel
BuildRequires:	pugixml-devel
BuildRequires:	python3-devel
BuildRequires:	python3-chromecast

Requires:	qt5-qtquickcontrols
Requires:	qt5-qtquickcontrols2
Requires:	qt5-qtgraphicaleffects
Requires:	qt5-qtmultimedia
Requires:	qt5-qtcharts
Requires:	python3-chromecast

Recommends:	xcftools
Recommends:	kf5-kimageformats
Recommends:	qt-avif-image-plugin
   

%description
PhotoQt is a fast and highly configurable image viewer with a simple and
 nice interface.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake

%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.PhotoQt.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.%{name}.PhotoQt.metainfo.xml

%files
%doc CHANGELOG README
%license COPYING
%{_datadir}/applications/org.%{name}.PhotoQt.desktop
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/org.%{name}.PhotoQt.png

#AppData
%{_datadir}/metainfo/org.%{name}.PhotoQt.metainfo.xml

%changelog
* Mon Feb 06 2023 Jiri Eischmann <eischmann@redhat.com> - 3.0-1
- Update to 3.0
- Removed libraw patch
- Changed the name and location of AppStream metadata file

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.8-2
- LibRaw rebuild

* Tue Aug 02 2022 Jiri Eischmann <eischmann@redhat.com> - 2.8-1
- Update to 2.8
- Removed desktop file of the standalone version
- Changed names of icon files

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.6-2
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Jiri Eischmann <eischmann@redhat.com> - 2.6-1
- Update to 2.6
- Added python3-devel and python3-chromecast dependecies
- Changed name of the source directory
- Changed names of desktop and appdata files
- Added desktop file for standalone mode

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Jiri Eischmann <eischmann@redhat.com> - 2.3-1
- Update to 2.3

* Tue Apr 27 2021 Jiri Eischmann <eischmann@redhat.com> - 2.1.1-2
- Added missing dependency: qt5-qtquickcontrols2

* Thu Feb 11 2021 Jiri Eischmann <eischmann@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Jiri Eischmann <eischmann@redhat.com> - 2.0-1
- Update to 2.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.7.1-10
- Rebuild for new LibRaw

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 1.7.1-8
- Rebuild for poppler-0.84.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Jiri Eischmann <eischmann@redhat.com> - 1.7.1-6
- Patch to build against a newer exiv2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.7.1-4
- rebuild (exiv2)

* Thu Jul 19 2018 Adam Williamson <awilliam@redhat.com> - 1.7.1-3
- Rebuild for new libraw

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jiri Eischmann <eischmann@redhat.com> - 1.7.1-1
- Update to 1.7.1
- Added build dependecies: poppler, freeimage, DevIL, extra-cmake-modules, libarchive
- Added recommended dependency: kf5-kimageformats

* Fri Mar 02 2018 Jiri Eischmann <eischmann@redhat.com> - 1.6-1
- Update to 1.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-7
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.5-4
- rebuild (exiv2)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Jiri Eischmann <eischmann@redhat.com>> - 1.5-2
- Adding a missing new dependecy - qt5-qtcharts

* Fri Jan 13 2017 Jiri Eischmann <eischmann@redhat.com> - 1.5-1
- Update to 1.5

* Mon Jun 20 2016 Jiri Eischmann <eischmann@redhat.com> - 1.4.1-1
- Update to 1.4.1
- Removing downstream appdata file and using upstream one now

* Sun Jun 5 2016 Jiri Eischmann <eischmann@redhat.com> - 1.4-3
- Added missing runtime dependecies

* Tue May 31 2016 Jiri Eischmann <eischmann@redhat.com> - 1.4-2
- Fixes for review
- Removed unnecessary build requires
- Added versions to changelog
- Improved consistency of macros
- change build and install section to comply with best practises for Qt app
 
* Fri May 27 2016 Jiri Eischmann <eischmann@redhat.com> - 1.4-1
- Initial build
