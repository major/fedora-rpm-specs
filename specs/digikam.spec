%bcond_with build_with_qt6
%if 0%{?fedora} > 39 || 0%{?rhel} > 9
%bcond_without build_with_qt6
ExclusiveArch: %{qt6_qtwebengine_arches}
%else
ExclusiveArch: %{qt5_qtwebengine_arches}
%endif

# use ninja or not
%global ninja 1

#global beta rc

Name:    digikam
Summary: A digital camera accessing & photo management application
Version: 8.5.0
Release: 2%{?beta}%{?dist}

License: GPL-2.0-or-later
URL:     http://www.digikam.org/
%if 0%{?beta:1}
Source0: http://download.kde.org/unstable/digikam/digikam-%{version}-%{beta}.tar.xz
%else
Source0: http://download.kde.org/stable/digikam/%{version}/digiKam-%{version}.tar.xz
%endif

# rawhide s390x is borked recently
#ExcludeArch: s390x

# digiKam not listed as a media handler for pictures in Nautilus (#516447)
# TODO: upstream me
Source10: digikam-import.desktop

## upstream patches

## upstreamable patches

%if 0%{?ninja}
BuildRequires: ninja-build
%endif

BuildRequires: boost-devel
BuildRequires: eigen3-devel
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: gcc-c++
BuildRequires: ImageMagick-devel
BuildRequires: ImageMagick-c++-devel >= 6.7
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: perl-generators
BuildRequires: pkgconfig(exiv2) >= 0.26
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(jasper)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libgphoto2_port) pkgconfig(libusb-1.0) pkgconfig(libusb)
BuildRequires: pkgconfig(libpng) >= 1.2.7
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(x11) pkgconfig(xproto)
%if %{with build_with_qt6}
BuildRequires: pkgconfig(Qt6NetworkAuth)
BuildRequires: pkgconfig(Qt6OpenGL)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6StateMachine)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)
BuildRequires: libksane-devel
BuildRequires: ksanecore-devel
BuildRequires: kf6-kcalendarcore-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kfilemetadata-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-threadweaver-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-solid-devel
BuildRequires: kf6-sonnet-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kbookmarks-devel
BuildRequires: kf6-rpm-macros
BuildRequires: qt6-qtbase-private-devel
%else
BuildRequires: pkgconfig(Qt5NetworkAuth)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5WebEngine)
BuildRequires: cmake(KSaneCore)
BuildRequires: kf5-libksane-devel >= 16.03
BuildRequires: kf5-kcalendarcore-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kfilemetadata-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-threadweaver-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-solid-devel
BuildRequires: kf5-sonnet-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-rpm-macros
%endif

## not actually checked-for or used -- rex
## rely on explicit cmake build options instead
#BuildRequires: mariadb-devel mariadb-server
## DNG converter
BuildRequires: expat-devel
## htmlexport plugin
BuildRequires: pkgconfig(libxslt)
## RemoveRedeye
BuildRequires: pkgconfig(opencv) >= 3.3
# Panorama plugin requires flex and bison
BuildRequires: flex
BuildRequires: bison
%if 0%{?fedora} || 0%{?rhel} > 8
BuildRequires: pkgconfig(libheif)
BuildRequires: pkgconfig(lqr-1)
# MediaPlayer dependencies
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(xext)
%endif
BuildRequires: pkgconfig(lensfun) >= 0.2.6
BuildRequires: pkgconfig(libpgf) >= 6.12.24

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Recommends: perl-Image-ExifTool
# expoblending assistant
Recommends: hugin-base
#Recommends: kf5-kipi-plugins
# thumbnailers, better default access to mtp-enabled devices
Recommends: kio-extras
%if %{with build_with_qt6}
Recommends: qt6-qtbase-mysql%{?_isa}
Recommends: qt6-qtimageformats%{?_isa}
%else
Recommends: qt5-qtbase-mysql%{?_isa}
Recommends: qt5-qtimageformats%{?_isa}
%endif

# core/libs/rawengine/libraw/
Provides: bundled(LibRaw) = 0.22.0

# no more DocBook documentation
# Sphinx documentation is published in a dedicated web site
# https://docs.digikam.org/en/index.html
Provides: %{name}-doc = %{version}-%{release}
Obsoletes: %{name}-doc < 8.0.0-3

%description
digiKam is an easy to use and powerful digital photo management application,
which makes importing, organizing and manipulating digital photos a "snap".
An easy to use interface is provided to connect to your digital camera,
preview the images and download and/or delete them.

digiKam built-in image editor makes the common photo correction a simple task.

%package libs
Summary: Runtime libraries for %{name}
# not *strictly* required, but nice -- rdieter
# see also https://bugzilla.redhat.com/show_bug.cgi?id=1973495
Recommends: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains the libraries, include files and other resources
needed to develop applications using %{name}.


%prep
%autosetup -n %{name}-%{version}%{?beta:-%{beta}} -p1

%build
%if %{with build_with_qt6}
%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=ON \
%else
%cmake_kf5 \
%endif
  %{?ninja:-G Ninja} \
  -DENABLE_APPSTYLES:BOOL=ON \
  -DENABLE_KFILEMETADATASUPPORT:BOOL=ON \
%if 0%{?rhel} && 0%{?rhel} < 9
  -DENABLE_MEDIAPLAYER:BOOL=OFF \
%endif
  -DENABLE_MYSQLSUPPORT:BOOL=ON \
  -DENABLE_INTERNALMYSQL:BOOL=ON

%cmake_build


%install
%cmake_install

desktop-file-install --vendor="" \
  --dir=%{buildroot}%{_datadir}/applications/ \
  %{SOURCE10}

%find_lang %{name}


%check
for i in %{buildroot}%{_datadir}/applications/*.desktop ; do
desktop-file-validate $i ||:
done

%if 0%{?rhel} && 0%{?rhel} < 8
%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &> /dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
  update-desktop-database -q &> /dev/null
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null
%endif


%ldconfig_scriptlets libs


%if %{with build_with_qt6}
%files -f %{name}.lang
%doc AUTHORS ChangeLog
%doc NEWS README.md
%license LICENSES/GPL-2.0-or-later.txt
%{_kf6_bindir}/digikam
%{_kf6_bindir}/digitaglinktree
%{_kf6_bindir}/cleanup_digikamdb
%{_kf6_bindir}/showfoto
%{_kf6_datadir}/kxmlgui5/digikam/
%{_kf6_datadir}/kxmlgui5/showfoto/
%{_kf6_datadir}/knotifications6/digikam.notifyrc
%{_kf6_datadir}/digikam/
%{_kf6_datadir}/showfoto/
%{_kf6_datadir}/solid/actions/digikam*.desktop
%{_kf6_metainfodir}/org.kde.digikam.appdata.xml
%{_kf6_metainfodir}/org.kde.showfoto.appdata.xml
%{_kf6_datadir}/applications/digikam-import.desktop
%{_kf6_datadir}/applications/org.kde.digikam.desktop
%{_kf6_datadir}/applications/org.kde.showfoto.desktop
%{_mandir}/man1/digitaglinktree.1*
%{_mandir}/man1/cleanup_digikamdb.1*
%{_kf6_datadir}/icons/hicolor/*/*/*

%files libs
%{_kf6_libdir}/libdigikamcore.so.*
%{_kf6_libdir}/libdigikamdatabase.so.*
%{_kf6_libdir}/libdigikamgui.so.*
%{_kf6_qtplugindir}/digikam/

%files devel
%{_kf6_libdir}/libdigikamcore.so
%{_kf6_libdir}/libdigikamdatabase.so
%{_kf6_libdir}/libdigikamgui.so
%{_kf6_libdir}/cmake/Digikam*/
%{_includedir}/digikam/

%else
%files -f %{name}.lang
%doc AUTHORS ChangeLog
%doc NEWS README.md
%license LICENSES/GPL-2.0-or-later.txt
%{_kf5_bindir}/digikam
%{_kf5_bindir}/digitaglinktree
%{_kf5_bindir}/cleanup_digikamdb
%{_kf5_bindir}/showfoto
%{_kf5_datadir}/kxmlgui5/digikam/
%{_kf5_datadir}/kxmlgui5/showfoto/
%{_kf5_datadir}/knotifications5/digikam.notifyrc
%{_kf5_datadir}/digikam/
%{_kf5_datadir}/showfoto/
%{_kf5_datadir}/solid/actions/digikam*.desktop
%{_kf5_metainfodir}/org.kde.digikam.appdata.xml
%{_kf5_metainfodir}/org.kde.showfoto.appdata.xml
%{_kf5_datadir}/applications/digikam-import.desktop
%{_kf5_datadir}/applications/org.kde.digikam.desktop
%{_kf5_datadir}/applications/org.kde.showfoto.desktop
%{_mandir}/man1/digitaglinktree.1*
%{_mandir}/man1/cleanup_digikamdb.1*
%{_kf5_datadir}/icons/hicolor/*/*/*

%files libs
%{_kf5_libdir}/libdigikamcore.so.*
%{_kf5_libdir}/libdigikamdatabase.so.*
%{_kf5_libdir}/libdigikamgui.so.*
%{_kf5_qtplugindir}/digikam/

%files devel
%{_kf5_libdir}/libdigikamcore.so
%{_kf5_libdir}/libdigikamdatabase.so
%{_kf5_libdir}/libdigikamgui.so
%{_kf5_libdir}/cmake/Digikam*/
%{_includedir}/digikam/
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 16 2024 Alexey Kurov <nucleo@fedoraproject.org> - 8.5.0-1
- digiKam-8.5.0

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 8.4.0-5
- Rebuild (qt6)

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 8.4.0-4
- Rebuild for ffmpeg 7

* Thu Jul 25 2024 Sérgio Basto <sergio@serjux.com> - 8.4.0-3
- Rebuild for opencv 4.10.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 13 2024 Alexey Kurov <nucleo@fedoraproject.org> - 8.4.0-1
- digiKam-8.4.0
- build only on QtWebEngine arches

* Tue Jun 18 2024 Robert-André Mauchin <zebob.m@gmail.com> - 8.3.0-3
- Rebuilt for exiv2 0.28.2

* Sat Apr  6 2024 Alexey Kurov <nucleo@fedoraproject.org> - 8.3.0-2
- Rebuild for qt6 6.7.0

* Fri Mar 15 2024 Alexey Kurov <nucleo@fedoraproject.org> - 8.3.0-1
- digiKam-8.3.0

* Sat Feb 17 2024 Jan Grulich <jgrulich@redhat.com> - 8.2.0-7
- Rebuild (qt6)

* Mon Feb 05 2024 Sérgio Basto <sergio@serjux.com> - 8.2.0-6
- Rebuild for opencv 4.9.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 13 2023 Alessandro Astone <ales.astone@gmail.com> - 8.2.0-3
- Rebuild (libksane)

* Thu Nov 30 2023 Alexey Kurov <nucleo@fedoraproject.org> - 8.2.0-2
- Build with Qt6 for F40+ and qt6_qtwebengine_arches

* Thu Nov 30 2023 Alexey Kurov <nucleo@fedoraproject.org> - 8.2.0-1
- digiKam-8.2.0

* Tue Nov 28 2023 Orion Poplawski <orion@nwra.com> - 8.1.0-4
- Rebuild for jasper 4.1

* Mon Aug 07 2023 Sérgio Basto <sergio@serjux.com> - 8.1.0-3
- Rebuild for opencv 4.8.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Alexey Kurov <nucleo@fedoraproject.org> - 8.1.0-1
- digiKam-8.1.0
- BR: kf5-kcalendarcore-devel

* Fri May 19 2023 Alexey Kurov <nucleo@fedoraproject.org> - 8.0.0-4
- updated rhel conditionals
- Recommends: perl-Image-ExifTool

* Sun May  7 2023 Alexey Kurov <nucleo@fedoraproject.org> - 8.0.0-3
- backport thumbbar fix (kde#468593)
- removed BR phonon4qt5
- obsoleted -doc subpackage
- simplify find_lang (only digikam.mo installed)

* Sat Apr 15 2023 Alexey Kurov <nucleo@fedoraproject.org> - 8.0.0-2
- fixed crash in MediaPlayer

* Thu Apr 13 2023 Alexey Kurov <nucleo@fedoraproject.org> - 8.0.0-1
- digiKam-8.0.0
- enabled MediaPlayer
- BR: kf5-sonnet-devel

* Sun Mar 26 2023 Alexey Kurov <nucleo@fedoraproject.org> - 7.10.0-1
- digiKam-7.10.0
- BR: ksanecore-devel
- BR: libheif-devel

* Tue Feb 21 2023 Than Ngo <than@redhat.com> - 7.9.0-6
- migrated to SPDX license

* Mon Feb 13 2023 Orion Poplawski <orion@nwra.com> - 7.9.0-5
- Add patch to add missing includes for gcc 13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 7.9.0-3
- Rebuild for opencv 4.7.0

* Thu Jan 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 7.9.0-2
- Rebuild for ImageMagick 7

* Tue Dec 06 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 7.9.0-1
- Update to digiKam-7.9.0 - (resolves rhbz#2150497)

* Thu Sep 01 2022 Rex Dieter <rdieter@gmail.com> - 7.8.0-1
- 7.8.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 7.7.0-1
- digikam-7.7.0

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 7.6.0-2
- Rebuilt for opencv 4.6.0

* Wed Mar 02 2022 Rex Dieter <rdieter@fedoraproject.org> - 7.6.0-1
- digikam-7.6.0

* Sun Feb 13 2022 Josef Ridky <jridky@redhat.com> - 7.5.0-3
- Rebuilt for libjasper.so.6

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Alexey Kurov <nucleo@fedoraproject.org> - 7.5.0-1
- digiKam-7.5.0

* Fri Jan 07 2022 Alexey Kurov <nucleo@fedoraproject.org> - 7.4.0-1
- digiKam-7.4.0

* Fri Nov 05 2021 Rex Dieter <rdieter@fedoraproject.org> - 7.3.0-4
- rebuild (ImageMagick)

* Thu Nov 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 7.3.0-3
- backport exiv2-related upstream fixes (kde#439785, rh#2019835)

* Fri Oct 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 7.3.0-2
- rebuild (ImageMagick)

* Tue Jul 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 7.3.0-1
- 7.3.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Rex Dieter <rdieter@fedoraproject.org> - 7.2.0-4
- -libs: Recommends %%name (instead of Requires) (#1973495)

* Fri Apr 30 2021 Alexey Kurov <nucleo@fedoraproject.org> - 7.2.0-3
- BuildRequires: pkgconfig(glu) (enables OpenGL in presentation tool)

* Wed Apr 07 2021 Alexey Kurov <nucleo@fedoraproject.org> - 7.2.0-2
- Rebuilt for OpenCV 4.5.2

* Mon Apr 05 2021 Alexey Kurov <nucleo@fedoraproject.org> - 7.2.0-1
- digikam-7.2.0

* Thu Feb 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 7.2.0-0.4.rc
- 7.2.0-rc

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 7.2.0-0.3.beta1
- rebuild (marble)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 7.2.0-0.1.beta1
- 7.2.0-beta1

* Thu Oct 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 7.1.0-2
- Rebuilt for OpenCV 4.5

* Wed Sep 09 2020 Marie Loise Nolden <loise@kde.org> - 7.1.0-1
- digikam-7.1.0

* Tue Aug 25 2020 Rex Dieter <rdieter@fedoraproject.org> - 7.0.0-5
- new cmake macros handle ninja too

* Tue Aug 25 2020 Than Ngo <than@redhat.com> - 7.0.0-4
- fixed bz#1863424, FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 7.0.0-1
- digikam-7.0.0

* Fri May 29 2020 Rex Dieter <rdieter@fedoraproject.org> - 7.0.0-0.7.beta3
- rebuild (opencv)

* Sat May 09 2020 Rex Dieter <rdieter@fedoraproject.org> - 7.0.0-0.6.beta3
- bump opencv,ImageMagick deps
- make weak deps unconditional

* Mon Apr 27 2020 Rex Dieter <rdieter@fedoraproject.org> 7.0.0-0.5.beta3
- 7.0.0-beta3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-0.4.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 7.0.0-0.3.beta2
- Rebuild for OpenCV 4.2

* Mon Jan 27 2020 Nicolas Chauvet <kwizart@gmail.com> - 7.0.0-0.2.beta2
- Update to beta2

* Tue Dec 31 2019 Rex Dieter <rdieter@fedoraproject.org> - 7.0.0-0.1.beta1
- digkam-7.0.0-beta1
- use ninja
- (re)enable s390x arch

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 6.4.0-2
- Rebuilt for opencv4

* Tue Nov 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 6.4.0-1
- digikam-6.4.0

* Tue Sep 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 6.3.0-1
- digikam-6.3.0

* Wed Jul 31 2019 Rex Dieter <rdieter@fedoraproject.org> - 6.2.0-1
- digikam-6.2.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 6.1.0-7
- enable qwebengine support where available (#1728036)

* Fri May 10 2019 Rex Dieter <rdieter@fedoraproject.org> - 6.1.0-6
- digikam-6.1.0
- drop kf5-kipi-plugins (now packaged separately

* Tue Mar 05 2019 Rex Dieter <rdieter@fedoraproject.org> -  6.0.0-5
- ExcludeArch: ppc64le (#1674809)

* Tue Feb 26 2019 Rex Dieter <rdieter@fedoraproject.org> - 6.0.0-5
- digikam-6.0.0
- include kipi-plugins-5.9.0 here (for now)
- %build: use ninja

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.9.0-3
- rebuild (exiv2)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.9.0-1
- 5.9.0

* Fri Mar 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.8.0-6
- BR: gcc-c++, use %%make_build %%ldconfig_scriptlets

* Fri Mar 02 2018 Adam Williamson <awilliam@redhat.com> - 5.8.0-5
- Rebuild for opencv 3.4.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.8.0-3
- backport mysql schema fixes

* Thu Jan 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.8.0-2
- rebuild (marble)

* Wed Jan 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.8.0-1
- 5.8.0

* Mon Jan 08 2018 Sérgio Basto <sergio@serjux.com> - 5.7.0-7
- Rebuild (opencv-3.3.1)

* Fri Dec 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-6
- move Recommends: hugin-base to main

* Mon Dec 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-5
- backport bundled(libraw) updates

* Sun Dec 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-4
- rebuild (kf5-kcalendarcore)

* Tue Nov 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-3
- upstream qt-5.9.3 fix
- kipi-plugins: make hugin-base dep soft

* Sun Sep 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-2
- drop mariadb build deps, rely on exlicit cmake build options only
- drop empty kipi-plugins-doc

* Sat Sep 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-1
- 5.7.0

* Wed Sep 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.6.0-4
- rebuild (marble)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.6.0-1
- 5.6.0

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.5.0-3
- rebuild (exiv2)

* Fri Apr 14 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.5.0-2
- Provides: bundled(LibRaw) = 0.18.2

* Tue Mar 14 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.5.0-1
- digikam-5.5.0 (#1432042)

* Tue Mar 14 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.4.0-6
- drop %%build debugging

* Wed Mar 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.4.0-5
- drop unused BR: libkdcraw libkface
- pull in upstream FTBFS fix

* Sun Mar 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.4.0-4
- rebuild (opencv)

* Tue Feb 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.4.0-3
- backport upstream FTBFS fix (#1423329)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.4.0-2
- rebuild (marble)

* Mon Jan 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.4.0-1
- digikam-5.4.0 (#1411549)

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 5.3.0-5
- Rebuild for eigen3-3.3.1

* Mon Dec 05 2016 Than Ngo <than@redhat.com> - - 5.3.0-4
- rebuild against new jasper-2.0.0

* Mon Nov 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.3.0-3
- pull in crash-on-wayland fix (#1384618)

* Fri Nov 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.3.0-2
- -DENABLE_APPSTYLES=ON

* Wed Nov 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.3.0-1
- digikam-5.3.0 (#1392645)

* Fri Sep 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.2.0-1
- digikam-5.2.0 (#1378866)

* Wed Aug 24 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.1.0-4
- fix digikamhelperdir (kde#367675)

* Fri Aug 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.1.0-3
- Recommends: qt5-qtimageformats

* Tue Aug 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.1.0-2
- Provides: bundled(LibRaw) = 0.18.0

* Tue Aug 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.1.0-1
- digikam-5.1.0 (#1365508)

* Fri Jul 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-3
- rebuild (kde-apps-16.07.80)

* Fri Jul 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-2
- ENABLE_MEDIAPLAYER=ON

* Sun Jul 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-1
- digikam-5.0.0, enable mysql support

* Sat Jun 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-0.12.beta7
- digikam-5.0.0-beta7

* Tue Apr 26 2016 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-0.11.beta5
- Rebuild for OpenCV 3.1

* Fri Apr 22 2016 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-0.10.beta6
- rebuild (marble)

* Thu Apr 14 2016 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-0.9.beta6
- rename kipi-plugins -> kf5-kipi-plugins (not -doc subpkg)
  allows for shipping a kde4-based kipi-plugins too

* Wed Apr 13 2016 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-0.8.beta5
- digikam-5.0.0-beta5

* Fri Mar 18 2016 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-0.7.beta3
- BR: marble-astro-devel

* Wed Mar 09 2016 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-0.6.beta3
- drop bad MarbleQt5.patch

* Thu Feb 11 2016 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-0.5.beta3
- digikam-5.0.0-beta3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Rex Dieter <rdieter@fedoraproject.org> 4.14.0-6
- backport lensfun-0.3.2 fix (kde#356672)

* Sun Jan 03 2016 Rex Dieter <rdieter@fedoraproject.org> 4.14.0-5
- rebuild (lensfun)

* Tue Dec 29 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.0-4
- support kf5 solid/actions

* Tue Dec 22 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.0-3
- Requires: kde-runtime (simpler)

* Sat Nov 07 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.0-2
- use kde_runtime_requires macro, Recommends: qt-mysql (#1279080)

* Thu Oct 15 2015 Alexey Kurov <nucleo@fedoraproject.org> - 4.14.0-1
- digikam-4.14.0

* Sat Sep  5 2015 Alexey Kurov <nucleo@fedoraproject.org> - 4.13.0-1
- digikam-4.13.0

* Wed Jul 29 2015 Alexey Kurov <nucleo@fedoraproject.org> - 4.12.0-1
- digikam-4.12.0
- old PicasaWeb export removed
- renamed googledrive to googleservices

* Mon Jun 22 2015 Rex Dieter <rdieter@fedoraproject.org> 4.11.0-2
- drop BR: pkgconfig(exiv2), only need libkexiv2-devel these days

* Tue Jun 16 2015 Alexey Kurov <nucleo@fedoraproject.org> - 4.11.0-1
- digikam-4.11.0

* Sat May 23 2015 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-5
- hugin-base not available in epel-7

* Mon May 18 2015 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-4
- merge epel-7 mods (#1194901)

* Sat May 16 2015 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-3
- export menu wont appear (#1222225)

* Thu May 14 2015 Nils Philippsen <nils@redhat.com> - 4.10.0-2
- rebuild for lensfun-0.3.1

* Tue May 12 2015 Alexey Kurov <nucleo@fedoraproject.org> - 4.10.0-1
- digikam-4.10.0
- added more kipiplugin translations

* Mon Apr 20 2015 Alexey Kurov <nucleo@fedoraproject.org> - 4.9.0-2
- build against system libkface and libkgeomap

* Tue Apr  7 2015 Alexey Kurov <nucleo@fedoraproject.org> - 4.9.0-1
- digikam-4.9.0
- removed libkgeomap translations

* Mon Feb 23 2015 Alexey Kurov <nucleo@fedoraproject.org> - 4.8.0-1
- digikam-4.8.0

* Tue Feb  3 2015 Alexey Kurov <nucleo@fedoraproject.org> - 4.7.0-2
- rebuild

* Tue Feb  3 2015 Alexey Kurov <nucleo@fedoraproject.org> - 4.7.0-1
- digikam-4.7.0

* Wed Jan 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 4.6.0-3
- Rebuild (libgpohoto2)

* Tue Jan 20 2015 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-2
- bump release

* Tue Jan 20 2015 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-1.1
- rebuild (marble, f20/f21)

* Thu Dec 18 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.6.0-1
- digikam-4.6.0

* Wed Dec 10 2014 Rex Dieter <rdieter@fedoraproject.org> 4.5.0-3
- rebuild (marble)
- drop libjpeg-turbo workarounds (not needed anymore)

* Mon Nov 17 2014 Rex Dieter <rdieter@fedoraproject.org> 4.5.0-2
- fix/workaround FTBFS against newer libjpeg-turbo (kde#340944)

* Fri Nov 14 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.5.0-1
- digikam-4.5.0

* Thu Oct  9 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.4.0-1
- digikam-4.4.0

* Sat Sep 20 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.3.0-2
- backport job crash fix (kde bugs 325580, 339210)

* Tue Sep 16 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.3.0-1
- digikam-4.3.0
- add BR: baloo-devel kfilemetadata-devel

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Rex Dieter <rdieter@fedoraproject.org> 4.2.0-5
- core/CMakeLists.txt too (#1119036)

* Wed Aug 13 2014 Rex Dieter <rdieter@fedoraproject.org> 4.2.0-4
- hack to allow build with older opencv (#1119036)

* Thu Aug 07 2014 Rex Dieter <rdieter@fedoraproject.org> 4.2.0-3
- rebuild (marble)

* Wed Aug  6 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-2
- enable kdepimlibs support disabled by default in 4.2.0 (kde#338055)

* Mon Aug  4 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-1
- digikam-4.2.0

* Sun Aug 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-4
- make kio_mtp fedora only

* Wed Jul 23 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.1.0-3
- apply upstream patch to handle QtGstreamer API 1.0 in VideoSlideShow tool;
  whether to build against QtGStreamer 0.10 or 1.x is autodetected (#1092659)

* Mon Jul 14 2014 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-2
- rebuild (marble)

* Sun Jun 29 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.1.0-1
- digikam-4.1.0
- OpenCV >= 2.4.9 required for libkface

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-3
- BR: kdelibs4-webkit-devel

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-1
- digikam-4.0.0

* Mon Apr 28 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.8.rc
- digikam-4.0.0-rc

* Sat Apr 26 2014 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-0.7.beta4
- rebuild (opencv)

* Mon Mar 31 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.6.beta4
- rebuild for ImageMagick-6.8.8.10
- drop BR: nepomuk-core-devel (Nepomuk disabled by default kde#332665)

* Thu Mar 27 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.5.beta4
- digikam-4.0.0-beta4
- add BR: nepomuk-core-devel

* Thu Mar 20 2014 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-0.4.
- rebuild (kde-4.13)

* Tue Feb 25 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.3.beta3
- digikam-4.0.0-beta3

* Tue Jan 14 2014 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.2.beta2
- digikam-4.0.0-beta2

* Mon Dec  9 2013 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.1.beta1
- digikam-4.0.0-beta1

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.5.0-4
- rebuild (exiv2)

* Sat Nov 16 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.0-3
- rebuilt for libkdcraw-4.11.90

* Thu Oct 10 2013 Rex Dieter <rdieter@fedoraproject.org> 3.5.0-2
- include (upstreamable) patch to omit libPropertyBrowser from packaging (kde#319664)

* Wed Oct  9 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.0-1
- digikam-3.5.0

* Fri Sep  6 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.4.0-1
- digikam-3.4.0
- BuildRequires: pkgconfig(libusb)

* Thu Sep 05 2013 Rex Dieter <rdieter@fedoraproject.org> 3.3.0-2
- rebuild (kde-4.11.x)

* Mon Aug  5 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.3.0-1
- digikam-3.3.0

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.3.0-0.6.beta3
- Perl 5.18 rebuild

* Mon Jul  8 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.3.0-0.5.beta3
- digikam-3.3.0-beta3

* Fri Jun 28 2013 Rex Dieter <rdieter@fedoraproject.org> 3.3.0-0.4.beta2
- rebuild (marble)

* Thu Jun 27 2013 Rex Dieter <rdieter@fedoraproject.org> 3.3.0-0.3.beta2
- rebuild (libkipi)

* Sat Jun 22 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.3.0-0.2.beta2
- digikam-3.3.0-beta2

* Tue Jun  4 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.3.0-0.1.beta1
- digikam-3.3.0-beta1

* Fri May 31 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.0-5
- more fixes for bars hiding in fullscreen mode kde#319876

* Thu May 30 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.0-4
- fix thumbbar visibility after fullscreen mode kde#319876

* Wed May 29 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.0-3
- fix sidebar in fullscreen mode kde#319876

* Wed May 29 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.0-2
- fix fullscreen settings loading kde#320016

* Tue May 14 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.0-1
- digikam-3.2.0

* Wed May  1 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.0-0.2.beta2
- digikam-3.2.0-beta2

* Mon Apr  8 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.0-0.1.beta1
- digikam-3.2.0-beta1
- BR: eigen3-devel instead of atlas-devel, drop clapack patch

* Sun Mar 17 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.1.0-2
- rebuild for ImageMagick-6.8.3.9

* Tue Mar 12 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.1.0-1
- digikam-3.1.0
- drop BR: pkgconfig(sqlite3) mysql-devel

* Wed Mar 06 2013 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-2
- rebuild (marble)

* Fri Feb  8 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.0-1
- digikam-3.0.0
- BR: flex bison for Panorama plugin

* Mon Jan 28 2013 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-0.16.rc
- Requires: kio_mtp

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.0.0-0.15.rc
- rebuild due to "jpeg8-ABI" feature drop

* Thu Jan 3 2013 Lukáš Tinkl <ltinkl@redhat.com> -  - 3.0.0-0.14.rc
- Resolves #891515, build marble deps on Fedora only

* Sat Dec 29 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.0-0.13.rc
- digikam-3.0.0-rc
- disable local kdegraphics build enabled in rc by default

* Thu Dec 13 2012 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-0.12.beta3
- cleanup, remove old conditionals, Conflicts

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-0.11.beta3
- rebuild (marble)

* Tue Nov 27 2012 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-0.10.beta3
- rebuild (qjson)

* Fri Nov 23 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.0-0.9.beta3
- rebuild for qjson-0.8.0

* Sun Nov 11 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.0-0.8.beta3
- digikam-3.0.0-beta3

* Mon Nov 05 2012 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-0.6.beta2
- rebuild (opencv)

* Wed Oct 24 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.0-0.5.beta2
- rebuild for libjpeg8

* Sat Oct 13 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.0-0.4.beta2
- digikam-3.0.0-beta2

* Wed Sep 26 2012 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-0.3.beta1a
- rebuild for updated FindKipi.cmake in kdelibs (kde#307213)

* Sat Sep 22 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.0-0.2.beta1a
- rebuild for updated FindKipi.cmake in kdelibs (kde#307213)

* Fri Sep 21 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.0-0.1.beta1a
- digikam-3.0.0-beta1a

* Sun Sep  2 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.9.0-1
- digikam-2.9.0

* Fri Aug 17 2012 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-3
- rev libgphoto2-2.5 patch (kde#303427)

* Fri Aug 10 2012 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-2
- rebuild (libimobiledevice)

* Mon Aug  6 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.8.0-1
- digikam-2.8.0

* Tue Jul 24 2012 Rex Dieter <rdieter@fedoraproject.org> 2.7.0-5
- digikam FTBFS against libgphoto2-2.5 (#841615)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.7.0-3
- rebuild for libgphoto2-2.5.0

* Tue Jul 10 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.7.0-2
- rebuild for opencv-2.4.2

* Sun Jul  8 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.7.0-1
- digikam-2.7.0

* Thu Jun 28 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-3
- fix build for newer lensfun-0.2.6+

* Tue Jun 26 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.6.0-2
- rebuild for libpgf-6.12.24

* Tue Jun  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.6.0-1
- digikam-2.6.0

* Tue May 29 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-0.10.rc
- rebuild (kde-4.9beta)

* Wed May 16 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.6.0-0.9.rc
- switch to lcms2, fix dkCmsTakeProfileID allocation size (kde#299886)

* Tue May 15 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.6.0-0.8.rc
- switch back to lcms1 for now (kde#299886)

* Wed May  9 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.6.0-0.7.rc
- digikam-software-compilation-2.6.0-rc

* Tue May 08 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-0.6.beta3
- rebuild (libtiff)

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 2.6.0-0.5.beta3
- rebuild (exiv2)

* Thu Apr 12 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-0.4.beta3.1
- rebuild (usbmuxd)

* Mon Apr  2 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.6.0-0.4.beta3
- digikam-2.6.0-beta3

* Tue Mar  6 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.6.0-0.3.beta2
- digikam-2.6.0-beta2

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-0.2.beta1
- Rebuilt for c++ ABI breakage

* Tue Feb  7 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.6.0-0.1.beta1
- digikam-2.6.0-beta1
- drop upstreamed patches gcc-4.7.0, dngconverter_hicolor_icons, libkipi, boost

* Thu Feb 02 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-5
- Requires: kcm_colors (kde48+)

* Thu Feb 02 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-4
- -doc, kipi-plugins-doc subpkgs for largish HTML handbooks
- upstreamed dng patch

* Sat Jan  7 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.5.0-3
- update boost patch

* Thu Jan  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.5.0-2
- fix build with gcc-4.7.0 (kde#290642) and boost-1.48 (kde#287772)

* Tue Jan  3 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.5.0-1
- digikam-2.5.0

* Fri Dec 09 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.1-2
- make dngconverter app icons to hicolor so usable outside of kde (#682055)

* Mon Dec  5 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.4.1-1
- digikam-2.4.1
- drop icons and tooltips patches (in upstream now)

* Mon Nov 21 2011 Rex Dieter <rdieter@fedoraproject.org> 2.3.0-4
- Unreadable text on tooltips in KDE 4.7 (kde#283572)

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 2.3.0-3
- BR: libjpeg-devel

* Tue Nov  8 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.3.0-2
- fix collision of digiKam icons with Oxygen

* Mon Nov  7 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.3.0-1
- digikam-2.3.0
- drop libpgf-api patch

* Sat Oct 29 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.0-2
- rebuild for libpgf-6.11.42
- bacport fix for changed libpgf API

* Tue Oct  4 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.0-1
- digikam-2.2.0
- drop libkvkontakte-libdir patch
- added photolayoutseditor in kipi-plugins

* Wed Sep 28 2011 Rex Dieter <rdieter@fedoraproject.org> 2.1.1-5
- include marble epoch in deps

* Mon Sep 26 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.1.1-4
- BR: pkgconfig(libpgf)

* Mon Sep 26 2011 Rex Dieter <rdieter@fedoraproject.org> 2.1.1-3
- pkgconfig-style deps

* Fri Sep 23 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.1-2
- BuildRequires: atlas-devel (for clapack, instead of the bundled version)
- fix FindCLAPACK.cmake to search %%{_libdir}/atlas
- patch matrix.cpp for the ATLAS clapack API

* Wed Sep 14 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.1.1-1
- digikam-2.1.1

* Fri Sep  9 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.1.0-1
- digikam-2.1.0
- drop qt_rasterengine patch
- add libkvkontakte subpkg

* Sun Aug 21 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-4
- rebuild (opencv)

* Thu Aug 18 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-3
- digikam crashes with "-graphicssystem raster" (#726971)

* Tue Aug 02 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-2
- new libkface, libkgeomap, libmediawiki subpkgs (#727570)
- remove rpm cruft (%%clean, %%defattr, Group:, BuildRoot:)

* Fri Jul 29 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.0.0-1
- digikam-2.0.0
- drop s390 patch included upstream
- bundled code not used by default (DIGIKAMSC_USE_PRIVATE_KDEGRAPHICS not defined)

* Thu Jul 07 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-0.2.rc
- use pkgconfig()-style deps for libkdcraw, libkexiv2, libkipi, libksane
- -libs: drop (versioned) dep on kdegraphics-libs

* Thu Jun 30 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.0.0-0.1.rc
- digikam-2.0.0-rc
- merge with kipi-plugins.spec

* Wed Jun 15 2011 Rex Dieter <rdieter@fedoraproject.org> 1.9.0-2
- rebuild (marble)

* Thu Mar 17 2011 Rex Dieter <rdieter@fedoraproject.org> 1.9.0-1
- 1.9.0

* Thu Mar 03 2011 Rex Dieter <rdieter@fedoraproject.org> 1.8.0-3
- use safer check for libjpeg version, using cmake_try_compile (kde#265431)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Rex Dieter <rdieter@fedoraproject.org> 1.8.0-1
- 1.8.0

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.7.0-1
- digikam-1.7.0

* Tue Nov 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-1
- digikam-1.6.0 (#628156)

* Tue Nov 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.5.0-1.1
- -libs: add minimal kdegraphics-libs dep (#648741)

* Mon Oct 11 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.5.0-1
- digikam-1.5.0

* Wed Aug 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.4.0-1
- digikam-1.4.0

* Tue Jun 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-1
- digikam-1.3.0

* Tue Mar 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0-2
- crash on startup in RatingWidget (kde#232628)

* Mon Mar 29 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0-1
- digikam-1.2.0

* Mon Mar 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-3
- -libs: drop extraneous deps
- -devel: Req: kdelibs4-devel

* Wed Feb 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-2
- touch up marble-related deps

* Mon Feb 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-1
- digikam-1.1.0

* Thu Jan 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-2
- use %%{_kde4_version}

* Mon Dec 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-1
- digikam-1.0.0

* Mon Nov 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.11.rc
- digikam-1.0.0-rc

* Wed Nov 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.10.beta6
- rebuild (kdegraphics)

* Sat Nov 14 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.9.beta6
- digiKam not listed as a media handler for pictures in Nautilus (#516447)

* Sun Nov 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.8.beta6
- digikam-1.0.0-beta6

* Tue Oct 06 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.7.beta5
- digikam-1.0.0-beta5
- tweak marble deps (again)

* Tue Sep 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.6.beta4
- fix marble dep(s)

* Mon Aug 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.5.beta4
- digikam-1.0.0-beta4
- BR: liblqr-1-devel

* Wed Aug 05 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.4.beta3
- drop xdg-utils references 
- tighten -libs related deps via %%{?_isa}

* Fri Jul 24 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.3.beta3
- digikam-1.0.0-beta3

* Mon Jul 06 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.2.beta2
- digikam-1.0.0-beta2

* Fri Jun 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.1.beta1
- digikam-1.0.0-beta1

* Tue Mar 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-1
- digikam-0.10.0 (final)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-0.18.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.17.rc2
- digikam-0.10.0-rc2

* Mon Feb 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.16.rc1
- Req: kdebase-runtime

* Wed Feb 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.15.rc1
- BR: kdeedu-devel >= 4.2.0, Req: kdeedu-marble >= 4.2.0
- add min Req: kdelibs4 dep too 

* Thu Jan 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10-0-0.14.rc1
- digikam-0.10.0-rc1

* Mon Jan 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10-0.13.beta8
- re-enable marble integration, kde42+ (bug #470578)

* Mon Jan 05 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.12.beta8
- digikam-0.10.0-beta8

* Mon Dec 22 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.11.beta7
- BR: libkipi-devel >= 0.3.0

* Thu Dec 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.9.beta7
- digikam-0.10.0-beta7

* Mon Dec 01 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.8.beta6
- omit kde42 (icon) conflicts

* Tue Nov 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.7.beta6
- digikam-0.10.0-beta6
- lensfun support

* Mon Oct 27 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.6.beta5
- digikam-0.10.0-beta5

* Mon Oct 06 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.10.0-0.5.beta4
- update to 0.10.0 beta 4
- build against latest kdegraphics

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.4.beta3
- digikam-0.10.0-beta3

* Mon Aug 04 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.3.beta2
- disable marble integration

* Sat Aug 02 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.2.beta2
- omit conflicts with oxygen-icon-theme

* Thu Jul 31 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-0.1.beta2
- digikam-0.10.0-beta2

* Fri Jul 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.9.4-2
- --without-included-sqlite3, BR: sqlite-devel

* Thu Jul 17 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.9.4-1
- digikam-0.9.4

* Mon Jul 07 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.3-5
- Don't lose some photos during import (#448235)

* Fri Mar 14 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-3
- respin (for libkdcraw)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.3-2
- Autorebuild for GCC 4.3

* Sat Dec 22 2007 Marcin Garski <mgarski[AT]post.pl> 0.9.3-1
- Update to 0.9.3
- BR: libkexiv2-devel >= 0.1.6 libkdcraw-devel >= 0.1.2

* Sat Dec 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.3-0.5.rc1
- digikam-0.9.3-rc1
- BR: kdelibs3-devel

* Tue Nov 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.3-0.2.beta3
- digikam-0.9.3-beta3

* Tue Nov 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.3-0.1.beta2
- digikam-0.9.3-beta2

* Tue Sep 18 2007 Marcin Garski <mgarski[AT]post.pl> 0.9.2-5
- Rebuild

* Wed Aug 29 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.3-4
- License: GPLv2+
- lcms patch (kde bug #148930)

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.9.2-3
- Rebuild for selinux ppc32 issue.

* Fri Jun 22 2007 Marcin Garski <mgarski[AT]post.pl> 0.9.2-2
- Create symlinks in pixmaps directory (#242978)

* Tue Jun 19 2007 Marcin Garski <mgarski[AT]post.pl> 0.9.2-1
- Update to version 0.9.2-final
- Remove digikam-0.9.2-beta3-fix-exiv2-dep.patch, merged upstream

* Wed Jun 06 2007 Marcin Garski <mgarski[AT]post.pl> 0.9.2-0.3.beta3
- Fix .desktop category

* Wed Jun 06 2007 Marcin Garski <mgarski[AT]post.pl> 0.9.2-0.2.beta3
- Fix broken compilation caused by Exiv2 dependency

* Tue Jun 05 2007 Marcin Garski <mgarski[AT]post.pl> 0.9.2-0.1.beta3
- Update to version 0.9.2-beta3 (merge with digikamimageplugins)
- Update description

* Mon May 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.1-3
- respin against libkexiv2-0.1.5
- preserve upstream .desktop vendor (f7 branch at least)

* Mon Apr 02 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.1-2
- exiv2-0.14 patch
- cleanup/simplify BR's,Requires,d-f-i usage

* Fri Mar 09 2007 Marcin Garski <mgarski[AT]post.pl> 0.9.1-1
- Update to version 0.9.1
- Update BuildRequires

* Mon Dec 18 2006 Marcin Garski <mgarski[AT]post.pl> 0.9.0-1
- Update to version 0.9.0

* Tue Nov 28 2006 Marcin Garski <mgarski[AT]post.pl> 0.9.0-0.2.rc1
- Rebuild

* Tue Nov 28 2006 Marcin Garski <mgarski[AT]post.pl> 0.9.0-0.1.rc1
- Update to version 0.9.0-rc1

* Fri Sep 01 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.2-3
- Rebuild for Fedora Core 6

* Wed Aug 16 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.2-2
- Release bump (#201756)

* Tue Aug 01 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.2-1
- Update to version 0.8.2 (#200932)

* Tue Feb 14 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.1-3
- Rebuild

* Wed Feb 08 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.1-2
- Exclude x-raw.desktop (bug #179754)
- Don't own icons directory

* Mon Jan 23 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.1-1
- Add --enable-final
- Remove GCC 4.1 patch, applied upstream
- Update to version 0.8.1

* Mon Jan 23 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.0-16
- Add some stuff to BuildRequires (finally fix bug #178031)

* Tue Jan 17 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.0-15
- Remove redundant BuildRequires (bug #178031)

* Mon Jan 16 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.0-14
- Remove --disable-dependency-tracking

* Mon Jan 16 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.0-13
- Remove --enable-final (caused compilation errors)

* Sun Jan 15 2006 Marcin Garski <mgarski[AT]post.pl> 0.8.0-12
- Change "/etc/profile.d/qt.sh" to "%%{_sysconfdir}/profile.d/qt.sh"
- Add --disable-dependency-tracking & --enable-final

* Wed Dec 14 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-11
- Add libart_lgpl-devel and gamin-devel to BR

* Wed Dec 14 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-10
- Add libacl-devel to BR

* Wed Dec 14 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-9
- Add libidn-devel to BR

* Wed Dec 14 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-8
- Fix compile on GCC 4.1

* Tue Dec 13 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-7
- Remove autoreconf

* Tue Dec 13 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-6
- Remove patch

* Tue Dec 13 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-5
- Last chance to make it right (modular X.Org)

* Tue Dec 13 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-4
- Try to build for modular X.Org

* Tue Dec 13 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-3
- Add new paths for modular X.Org

* Fri Dec 09 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-2
- Work around for modular X.Org paths

* Thu Dec 01 2005 Marcin Garski <mgarski[AT]post.pl> 0.8.0-1
- Add description about digikamimageplugins and kipi-plugins
- Remove 64 bit patch, applied upstream
- Update to version 0.8.0

* Sat Oct 22 2005 Marcin Garski <mgarski[AT]post.pl> 0.7.4-4
- Exclude libdigikam.la (bug #171503)

* Sat Sep 17 2005 Marcin Garski <mgarski[AT]post.pl> 0.7.4-3
- Change confusing warning about Big Endian Platform

* Tue Sep 13 2005 Marcin Garski <mgarski[AT]post.pl> 0.7.4-2
- Spec improvements

* Mon Sep 12 2005 Marcin Garski <mgarski[AT]post.pl> 0.7.4-1
- Updated to version 0.7.4 & clean up for Fedora Extras

* Sat Jun 26 2004 Marcin Garski <mgarski[AT]post.pl> 0.6.2-1.fc2
- Updated to version 0.6.2

* Wed Jun 09 2004 Marcin Garski <mgarski[AT]post.pl> 0.6.2RC-1.fc2
- Initial specfile
