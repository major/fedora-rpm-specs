%global krita_python 1
%global kf5_ver 5.44.0
%global versiondir %(echo %{version} | cut -d. -f1-3)

# Work around for eigen3 trying to enforce power10.
# https://bugzilla.redhat.com/show_bug.cgi?id=1996330
%ifarch ppc64 ppc64le
%global optflags %(echo %{optflags} -DEIGEN_ALTIVEC_DISABLE_MMA)
%endif

Name:           krita
Version:        5.1.4
Release:        3%{?dist}

Summary:        Krita is a sketching and painting program
License:        GPL-2.0-or-later
URL:            https://krita.org
Source0:        https://download.kde.org/%{?pre:un}stable/krita/%{versiondir}%{?pre:-%{pre}}/krita-%{version}%{?pre:-%{pre}}.tar.xz

## downstream patches
#org.kde.krita.appdata.xml: failed to parse org.kde.krita.appdata.xml: Error on line 505 char 110: <caption> already set 'Atau' and tried to replace with ' yang aktif'
#org.kde.krita.appdata.xml: failed to parse org.kde.krita.appdata.xml: Error on line 514 char 120: <caption> already set 'xxOr the active' and tried to replace with 'xx'
Patch1: krita-5.1.1-appstream_validate.patch
Patch2: libraw.patch

## upstream patches


BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)

BuildRequires:  qt5-qtbase-devel >= 5.12.0
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5X11Extras)

BuildRequires:  boost-devel
BuildRequires:  giflib-devel >= 5
BuildRequires:  libtiff-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(kseexpr)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(OpenColorIO)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xi)
BuildRequires:  quazip-qt5-devel
BuildRequires:  zlib-devel

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%if 0%{?krita_python}
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-sip-devel
BuildRequires:  sip

Requires: python3-qt5-base
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%endif

Obsoletes:      calligra-krita < 3.0
Provides:       calligra-krita = %{version}-%{release}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Krita is a sketching and painting program.
It was created with the following types of art in mind:
- concept art
- texture or matte painting
- illustrations and comics

%package        libs
Summary:        Shared libraries for %{name}
Obsoletes:      calligra-krita-libs < 3.0
Provides:       calligra-krita-libs = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}

%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.


%prep
%autosetup -n %{name}-%{version}%{?pre:-%{pre}} -p1


%build
%cmake_kf5 -G Ninja

%cmake_build


%install
%cmake_install

## unpackaged files
# omit headers, avoid need for -devel subpkg for now
rm -fv %{buildroot}%{_includedir}/*

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.krita.appdata.xml 
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.krita.desktop


%files -f %{name}.lang
%doc README.md
%license COPYING*
%config(noreplace) %{_sysconfdir}/xdg/kritarc
%{_kf5_bindir}/krita
%{_kf5_bindir}/krita_version
%{_kf5_libdir}/kritaplugins/
%{_kf5_metainfodir}/org.kde.krita.appdata.xml
%{_kf5_datadir}/applications/org.kde.krita.desktop
%{_kf5_datadir}/applications/krita*.desktop
%{_kf5_datadir}/color-schemes/*
%{_kf5_datadir}/color/icc/*
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/krita/
%{_kf5_datadir}/kritaplugins/
# fixme:  /org/krita -> /org/kde/krita ?
%{_kf5_qmldir}/org/krita/
%if 0%{?krita_python}
%{_kf5_bindir}/kritarunner
%{_kf5_libdir}/krita-python-libs/
%endif

%files libs
%{_kf5_libdir}/libkrita*.so.*

#files devel
%{_kf5_libdir}/libkrita*.so
#{_includedir}/*.h*


%changelog
* Fri Jan 13 2023 Richard Shaw <hobbes1069@gmail.com> - 5.1.4-3
- Rebuild for OpenColorIO.

* Tue Dec 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 5.1.4-2
- LibRaw rebuild

* Sat Dec 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 5.1.4-1
- Updated to version 5.1.4.

* Tue Nov 08 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 5.1.3-1
- Updated to version 5.1.3.

* Sat Sep 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 5.1.1-1
- Updated to version 5.1.1.

* Tue Sep 06 2022 Rex Dieter <rdieter@gmail.com> - 5.1.0-2
- validate appstream (#2123966)

* Fri Aug 26 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 5.1.0-1
- Updated to version 5.1.0.

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.8-5
- Rebuild for gsl-2.7.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.0.8-3
- enable G'Mic plugin support
- drop heif (not in fedora)

* Wed Jul 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.0.8-2
- enable heif, openjpeg, webp support

* Mon Jun 27 2022 Rex Dieter <rdieter@fedoraproject.org> 5.0.8-1
- 5.0.8

* Mon Jun 27 2022 Rex Dieter <rdieter@fedoraproject.org> 5.0.6-1
- 5.0.6

* Mon Apr 18 2022 Miro Hrončok <mhroncok@redhat.com> - 5.0.2-2
- Rebuilt for quazip 1.3

* Sat Jan 22 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.2-1
- Updated to version 5.0.2.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.0-1
- Updated to version 5.0.0.

* Fri Nov 12 2021 Rex Dieter <rdieter@fedoraproject.org> - 4.4.8-3
- disable python bindings

* Sat Oct 30 2021 Rex Dieter <rdieter@fedoraproject.org> - 4.4.8-2
- -libs: revert part of the "SPEC cleanup", we don't want main pkg pulled in for multilib

* Sun Sep 26 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 4.4.8-1
- Updated to version 4.4.8.
- Performed minor SPEC cleanup.

* Mon Aug 23 2021 Richard Shaw <hobbes1069@gmail.com> - 4.4.5-10
- Rebuild with opencolorio1 compat package.

* Sun Aug 22 2021 Richard Shaw <hobbes1069@gmail.com> - 4.4.5-9
- Rebuild with opencolorio1 compat package.

* Sun Aug 22 2021 Richard Shaw <hobbes1069@gmail.com> - 4.4.5-8
- Rebuild for OpenEXR/Imath 3.1.

* Thu Aug 19 2021 Björn Esser <besser82@fedoraproject.org> - 4.4.5-7
- Rebuild (quazip)

* Fri Aug 13 2021 Richard Shaw <hobbes1069@gmail.com> - 4.4.5-6
- Rebuild with opencolorio1 compat package.

* Sun Aug 01 2021 Rex Dieter <rdieter@fedoraproject.org> - 4.4.5-5
- Pull in upstream OpenEXR-3 build fix

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Scott Talbert <swt@techie.net> - 4.4.5-3
- Revert back to building with sip 4 due to no sip 6 support

* Sat Jul 03 2021 Scott Talbert <swt@techie.net> - 4.4.5-2
- Update to build with sip5

* Mon Jun 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 4.4.5-1
- 4.4.5

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.4.3-0.3.beta1
- Rebuilt for Python 3.10

* Thu Mar 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 4.4.3-0.2.beta1
- rebuild without -gcc11.patch (fixes landed in qt5-qtbase instead)

* Mon Mar 08 2021 Rex Dieter <rdieter@fedoraproject.org> - 4.4.3-0.1.beta1
- 4.4.3-beta1

* Mon Mar 08 2021 Rex Dieter <rdieter@fedoraproject.org> - 4.4.2-4
- .spec cleanup
- backport crash fix for scaled displays

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Rex Dieter <rdieter@fedoraproject.org> - 4.4.2-2
- 4.4.2

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 4.4.1-2
- Rebuild for OpenEXR 2.5.3.

* Tue Nov 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.4.1-1
- 4.4.1

* Wed Oct 28 2020 Marie Loise Nolden <loise@kde.org> - 4.4.0-1
- 4.4.0

* Wed Oct 28 2020 Jeff Law <law@redhat.com> - 4.3.0-3
- Fix missing #includes for gcc-11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-1
- 5.3.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.9-4
- Rebuilt for Python 3.9

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 4.2.9-3
- Rebuild for new LibRaw

* Mon Mar 30 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.2.9-2
- drop _legacy_common_support FTBFS workaround

* Mon Mar 23 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.2.9-1
- 4.2.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 4.2.8.2-2
- Rebuild for poppler-0.84.0

* Sat Nov 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.8.2-1
- 4.2.8.2

* Fri Oct 18 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.6-2
- Restore python support (#1735972)

* Wed Sep 11 2019 Rex Dieter <rdieter@fedoraproject.org> 4.2.6-1
- 4.2.6

* Wed Aug 21 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.5-5
- disable python support on f32+ until FTBFS issues are sorted out

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.5-4
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.2.5-3
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.5-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.5-1
- 4.2.5

* Tue Aug 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.3-1
- 4.2.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-1
- 4.2.2

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-1
- 4.2.1

* Sun May 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.1.8-5
- add PyQt5-related runtime dep(s)

* Sat May 11 2019 Rex Dieter <rdieter@fedoraproject.org> 4.1.8-4
- enable python support

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.8-3
- Rebuild for OpenEXR 2.3.0.

* Thu Apr 04 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.8-2
- Rebuild for OpenColorIO 1.1.1.

* Wed Mar 06 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.1.8-1
- 4.1.8

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 4.1.7-6
- Rebuilt for Boost 1.69

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.1.7-5
- rebuild (exiv2)

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 4.1.7-4
- Rebuilt for Boost 1.69

* Tue Jan 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.1.7-3
- rebuild

* Mon Dec 17 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.7-2
- pull in upstream fixes

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.7-1
- 4.1.7

* Sun Oct 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.5-1
- 4.1.5

* Tue Aug 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.1-2
- pull in candidate upstream LibRaw-0.19/FTBFS fix

* Mon Jul 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.1-1
- krita-4.1.1 (#1601439)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.0-1
- krita-4.1.0 (#1595237)

* Wed Jun 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.0.4-1
- krita-4.0.4 (#1590798)

* Sat May 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.0.3-1
- krita-4.0.3

* Tue May 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.0.2-1
- krita-4.0.2 (#1575789)

* Mon Apr 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.0.1-1
- krita-4.0.1 (#1557986)

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 4.0.0-2
- Rebuild for poppler-0.63.0

* Tue Mar 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.0.0-1
- krita-4.0.0 (#1557986)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.3.3-1
- krita-3.3.3 (#1532426)

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 3.3.2.1-4
- Rebuilt for Boost 1.66

* Sat Jan 13 2018 Richard Shaw <hobbes1069@gmail.com> - 3.3.2.1-3
- Rebuild for OpenColorIO 1.1.0.

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.2.1-2
- Remove obsolete scriptlets

* Thu Nov 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.3.2.1-1
- krita-3.3.2.1

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.3.1-1
- krita-3.3.1

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.3.0-1
- krita-3.3.0

* Fri Aug 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.2.1-1
- krita-3.2.1

* Wed Aug 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-1
- krita-3.2.0, clean/update build deps

* Mon Jul 31 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.1.4-6
- rebuild (gsl)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 3.1.4-4
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 3.1.4-3
- Rebuilt for Boost 1.64

* Fri May 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.1.4-2
- backport Qt 5.9 FTBFS fix, more robust %%find_lang usage

* Fri May 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.1.4-1
- 3.1.4 (#1448598)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.1.2.1-2
- rebuild (exiv2)

* Mon Mar 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.1.2.1-1
- krita-3.1.2.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Rich Mattes <richmattes@gmail.com> - 3.1.1-3
- Rebuild for eigen3-3.3.1

* Wed Dec 28 2016 Jon Ciesla <limburgher@gmail.com> - 3.1.1-2
- Rebuild for new LibRaw.

* Mon Dec 19 2016 Helio Chissini de Castro <helio@kde.org> - 3.1.1-1
- New upstream version

* Sun Oct 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-1
- 3.0.1

* Sun Oct 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.0-4
- -libs: fix Obsoletes, drop %%exclude

* Thu Jun 02 2016 Than Ngo <than@redhat.com> - 3.0-3
- rebuild against new kf5 (workaround for the build failure on arm with gcc6 bz#1342095)

* Tue May 31 2016 Helio Chissini de Castro <helio@kde.org> - 3.0-2
- Fixed requested changes to package reviewing
- Added official tarball.

* Mon May 30 2016 Helio Chissini de Castro <helio@kde.org> - 3.0-1
- Krita 3.0 upstream release

* Tue May 24 2016 Helio Chissini de Castro <helio@kde.org> - 2.99.91-1
- New upstream devel release
- Krita sketch gone

* Mon May 09 2016 Helio Chissini de Castro <helio@kde.org> - 2.99.90-1
- Initial new Krita package
