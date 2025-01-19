%undefine __cmake_in_source_build

Name:    okteta
Summary: Binary/hex editor
Epoch:   1
Version: 0.26.15
Release: 4%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://cgit.kde.org/%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/okteta/%{version}/src/%{name}-%{version}.tar.xz
Patch0: okteta-gcc11.patch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gettext

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel

BuildRequires: pkgconfig(qca2-qt5)
BuildRequires: pkgconfig(Qt5Designer)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5ScriptTools)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)

# translations moved here
Conflicts: kde-l10n < 17.03

Conflicts:      kdesdk-common < 4.10.80
Obsoletes:      kdesdk-okteta < 4.10.80
Provides:       kdesdk-okteta = %{epoch}:%{version}-%{release}

Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
# struct2osd.sh deps
%if 0%{?fedora} > 20  || 0%{?rhel} > 7
Recommends: castxml libxslt
%else
Requires: castxml libxslt
%endif

%description
Okteta is a binary/hex editor for KDE

%package libs
Summary: Runtime libraries and kpart plugins for %{name}
Obsoletes: kdesdk-okteta-libs < 4.10.80
Provides:  kdesdk-okteta-libs = %{epoch}:%{version}-%{release}
Provides:  okteta5-part = %{epoch}:%{version}-%{release}
Provides:  okteta5-part%{?_isa} = %{epoch}:%{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Developer files for %{name}
Obsoletes: kdesdk-okteta-devel < 4.10.80
Provides:  kdesdk-okteta-devel = %{epoch}:%{version}-%{release}
Provides:  okteta5-devel = %{epoch}:%{version}-%{release}
Requires:  %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.okteta.appdata.xml ||:
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.okteta.desktop


%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_bindir}/okteta
%{_bindir}/struct2osd
%{_datadir}/mime/packages/okteta.xml
%{_kf5_metainfodir}/org.kde.okteta.appdata.xml
%{_kf5_datadir}/knsrcfiles/okteta-structures.knsrc
%{_datadir}/applications/org.kde.okteta.desktop
#{_datadir}/kxmlgui5/okteta/
%{_datadir}/icons/hicolor/*/apps/okteta.*

%ldconfig_scriptlets libs

%files libs
%dir %{_datadir}/okteta/
%{_datadir}/okteta/structures/
%{_datadir}/config.kcfg/structureviewpreferences.kcfg
%{_libdir}/libKasten4*.so.*
%{_libdir}/libOkteta3*.so.*
# part
%{_kf5_plugindir}/parts/oktetapart.so
%{_kf5_datadir}/kservices5/oktetapart.desktop

%files devel
%{_includedir}/Okteta*/
%{_includedir}/Kasten*/
%{_libdir}/libKasten4*.so
%{_libdir}/libOkteta3*.so
%{_libdir}/cmake/KastenControllers/
%{_libdir}/cmake/KastenCore/
%{_libdir}/cmake/KastenGui/
%{_libdir}/cmake/OktetaCore/
%{_libdir}/cmake/OktetaGui/
%{_libdir}/cmake/OktetaKastenControllers/
%{_libdir}/cmake/OktetaKastenCore/
%{_libdir}/cmake/OktetaKastenGui/
%{_libdir}/pkgconfig/Okteta*.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_Okteta*.pri
%{_qt5_plugindir}/designer/oktetawidgets.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.26.15-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 3 2024 Marie Loise Nolden <loise@kde.org> - 1:0.26.15-1
- move qt designer plugin to -devel
- update to 0.26.15

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 1:0.26.4-2
- Adjust includes for gcc-11

* Sun Aug 09 2020 Marie Loise Nolden <loise@kde.org> - 1:0.26.4-1
- 0.26.4

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Marie Loise Nolden <loise@kde.org> - 1:0.26.3-1
- 0.26.3 and cleanup

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 14 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:0.26.0-1
- 0.26.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.25.2-1
- okteta-0.25.2

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:0.25.1-1
- okteta-0.25.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:0.25.0-1
- okteta-0.25.0 (epoch++)
- use %%make_build %%ldconfig_scriptlets

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Thu Feb 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.12.1-2
- Remove obsolete scriptlets

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Fri Dec 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Thu Sep 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Thu Aug 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Sat Jun 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Thu Jan 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Wed Sep 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Sat Aug 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sat Aug 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.90-1
- 16.07.90

* Sat Jul 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.80-1
- 16.07.80

* Sun Jul 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Wed May 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-2
- Conflicts: okteta4-libs < 4.14.3-56 (%%_datadir/config.kcfg/structviewpreferences.kcfg)

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Mon Apr 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0

* Tue Mar 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-1
- 15.12.3

* Mon Feb 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.2-1
- 15.12.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.12.0-1
- 15.12.0

* Mon Nov 30 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.08.3-1
- 15.08.3

* Wed Oct 28 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.08.2-1
- 15.08.2

* Thu Aug 20 2015 Than Ngo <than@redhat.com> - 15.08.0-1
- 15.08.0

* Thu Jun 18 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.2-2
- BR: kf5-kiconthemes-devel

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.2-1
- 15.04.2

* Thu May 28 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.1-2
- rename appdata to match .desktop file

* Thu May 28 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.1-1
- 15.04.1

* Tue Apr 14 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.0-1
- 15.04.0

* Mon Apr 06 2015 Rex Dieter <rdieter@fedoraproject.org> 14.12.3-1
- kf5 okteta

* Wed Apr 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-8
- drop -part subpkg (include in -libs)
- more prep for okteta4 compat pkg

* Tue Mar 31 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-7
- move struct2osd.sh to main pkg, use Recommends for its runtime deps

* Tue Mar 31 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-6
- -part: move kbytearray here
- -libs: move kasten resources/structures here, drop dep on main pkg

* Tue Mar 31 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-5
- -devel: Provides: okteta4-devel

* Sat Mar 21 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-4
- -part subpkg, Provides: okteta4-part

* Sat Feb 28 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-3
- lack of algorithms in checksum tool (#1197339)

* Sat Jan 17 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-2
- kde-applications fixes, cleanup

* Sun Nov 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1
- 4.14.3

* Sun Oct 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.2-1
- 4.14.2

* Tue Sep 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.1-1
- 4.14.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.0-1
- 4.14.0

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.97-1
- 4.13.97

* Tue Jul 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.2-2
- optimize mimeinfo scriptlet

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.2-1
- 4.13.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.1-1
- 4.13.1

* Sat Apr 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.0-1
- 4.13.0

* Fri Apr 04 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.97-1
- 4.12.97

* Sun Mar 23 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.95-1
- 4.12.95

* Wed Mar 19 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.90-1
- 4.12.90

* Sun Mar 02 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-1
- 4.12.2

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-1
- 4.12.1

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.97-1
- 4.11.97

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.95-1
- 4.11.95

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.90-1
- 4.11.90

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Wed Sep 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-1
- 4.11.1

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Wed Aug 07 2013 Jan Grulich <jgrulich@redhat.com> - 4.10.97-2
- Remove epoch
- Add obsoletion for kdesdk-okteta < 4.10.80

* Mon Aug 05 2013 Jan Grulich <jgrulich@redhat.com> - 4.10.97-1
- Split off from kdesdk package
