# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

%bcond_without qt5
%bcond_without qt6

Name:    qwt
Summary: Qt Widgets for Technical Applications
Version: 6.2.0
Release: 9%{?dist}

License: LGPLv2 with exceptions
URL:     http://qwt.sourceforge.net
Source:  http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

## upstream patches

## upstreamable patches
# Use QT_INSTALL_ paths instead of custom prefix
Patch51: qwt-qt_install_paths.patch
# Add qt suffix to libraries to make them parallel-installable
Patch52: qwt-libsuffix.patch
# Kill rpath
Patch53: qwt-no_rpath.patch
# Fix incorrect requires in pkgconfig files
Patch54: qwt-pkgconfig.patch

BuildRequires: make

%description
The Qwt library contains GUI Components and utility classes which are primarily
useful for programs with a technical background.
Besides a 2D plot widget it provides scales, sliders, dials, compasses,
thermometers, wheels and knobs to control or display values, arrays
or ranges of type double.


%package doc
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.

%if %{with qt5}
%package qt5
Summary: Qt5 Widgets for Technical Applications
BuildRequires: pkgconfig(Qt5Concurrent) pkgconfig(Qt5PrintSupport) pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5OpenGL) pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Designer)
Provides: qwt6-qt5 = %{version}-%{release}
Provides: qwt6-qt5%{_isa} = %{version}-%{release}
%description qt5
%{summary}.

%package qt5-devel
Summary:  Development files for %{name}-qt5
Provides: qwt6-qt5-devel = %{version}-%{release}
Provides: qwt6-qt5-devel%{_isa} = %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.
%endif

%if %{with qt6}
%package qt6
Summary: Qt6 Widgets for Technical Applications
BuildRequires: pkgconfig(Qt6Concurrent) pkgconfig(Qt6PrintSupport) pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6OpenGL) pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Designer)
Provides: qwt6-qt6 = %{version}-%{release}
Provides: qwt6-qt6%{_isa} = %{version}-%{release}
%description qt6
%{summary}.

%package qt6-devel
Summary:  Development files for %{name}-qt6
Provides: qwt6-qt6-devel = %{version}-%{release}
Provides: qwt6-qt6-devel%{_isa} = %{version}-%{release}
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
%{summary}.
%endif


%prep
%autosetup -p1


%build
%if %{with qt5}
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%{qmake_qt5} QWT_CONFIG+=QwtPkgConfig ..

%make_build
popd
%endif

%if %{with qt6}
mkdir %{_target_platform}-qt6
pushd %{_target_platform}-qt6
%{qmake_qt6} QWT_CONFIG+=QwtPkgConfig ..

%make_build
popd
%endif


%install
%if %{with qt5}
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}-qt5
%endif
%if %{with qt6}
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}-qt6
%endif

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mkdir -p %{buildroot}%{_mandir}

# Move docs to proper dirs
%if %{with qt5}
# Last build "wins"
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/html %{buildroot}%{_mandir}/*
mv %{buildroot}%{_qt5_docdir}/html/html %{buildroot}%{_defaultdocdir}/%{name}/html
mv %{buildroot}%{_qt5_docdir}/html/man/man3 %{buildroot}%{_mandir}/

%if %{with qt6}
# Last build "wins"
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/html %{buildroot}%{_mandir}/*
mv %{buildroot}%{_qt6_docdir}/html/html %{buildroot}%{_defaultdocdir}/%{name}/html
mv %{buildroot}%{_qt6_docdir}/html/man/man3 %{buildroot}%{_mandir}/
%endif
%endif


%files doc
%doc %{_defaultdocdir}/%{name}/
%{_mandir}/man3/*

%if %{with qt5}
%files qt5
%license COPYING
%doc README
%{_qt5_libdir}/libqwt-qt5.so.6*

%files qt5-devel
%{_qt5_headerdir}/qwt/
%{_qt5_libdir}/libqwt-qt5.so
%{_qt5_libdir}/pkgconfig/Qt5Qwt6.pc
%{_qt5_archdatadir}/mkspecs/features/qwt*
%{_qt5_plugindir}/designer/libqwt_designer_plugin.so
%endif

%if %{with qt6}
%files qt6
%license COPYING
%doc README
%{_qt6_libdir}/libqwt-qt6.so.6*

%files qt6-devel
%{_qt6_headerdir}/qwt/
%{_qt6_libdir}/libqwt-qt6.so
%{_qt6_libdir}/pkgconfig/Qt6Qwt6.pc
%{_qt6_archdatadir}/mkspecs/features/qwt*
%{_qt6_plugindir}/designer/libqwt_designer_plugin.so
%endif


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 6.2.0-7
- Fix qwt-qt6-devel dependencies

* Sun Mar 3 2024 Marie Loise Nolden <loise@kde.org> - 6.2.0-6
- move qt designer plugin to -devel

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0
- Add qt6 build

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Marie Loise Nolden <loise@kde.org - 6.1.5-1
- Update to 6.1.5 (compatibility to Qt 5.15)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Sandro Mani <manisandro@gmail.com> - 6.1.4-1
- Update to 6.1.4

* Sat Nov 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 6.1.3-12
- make qt4 conditional, no on el8+ (#1773581)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 6.1.3-9
- use %%_qt5_archdatadir/mkspecs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 6.1.3-7
- use %%make_build %%license %%ldconfig_scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.1.3-3
- changelog cosmetics (whitespace mostly)

* Wed Mar 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.1.3-2
- no_rpath.patch

* Wed Mar 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.1.3-1
- qwt-6.1.3 (#1430378)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.1.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> - 6.1.2-2
- rebuild (gcc5)

* Fri Dec 12 2014 Rex Dieter <rdieter@fedoraproject.org> 6.1.2-1
- qwt-6.1.2

* Mon Dec 01 2014 Rex Dieter <rdieter@fedoraproject.org> - 6.1.1-3
- %%build: use %%qmake-qt? macro variant
- RFE: Qwt build for Qt5 (#1164515)

* Tue Oct 28 2014 Rex Dieter <rdieter@fedoraproject.org> 6.1.1-2
- do out-of-src build (prep for qt5 build maybe coming someday)

* Sat Sep 20 2014 Rex Dieter <rdieter@fedoraproject.org> 6.1.1-1
- qwt-6.1.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 29 2013 Rex Dieter <rdieter@fedoraproject.org> - 6.1.0-1
- qwt-6.1.0
- QtDesigner plugin doesn't link to the proper header directory path (#824447)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Rex Dieter <rdieter@fedoraproject.org> 6.0.1-2
- qwtbuild.pri: drop CONFIG+=silent

* Tue Aug 14 2012 Rex Dieter <rdieter@fedoraproject.org> - 6.0.1-1
- qwt-6.0.1 (#697168)
- add pkgconfig support

* Fri Aug 03 2012 Rex Dieter <rdieter@fedoraproject.org> 5.2.2-6
- qwt*.pc : +Requires: QtGui QtSvg

* Thu Aug 02 2012 Rex Dieter <rdieter@fedoraproject.org> 5.2.2-5
- pkgconfig support

* Tue Jul 31 2012 Rex Dieter <rdieter@fedoraproject.org> - 5.2.2-4
- Provides: qwt5-qt4(-devel)
- pkgconfig-style deps
 
- * Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 07 2011 Rex Dieter <rdieter@fedoraproject.org> 5.2.2-1
- 5.2.2

* Thu Jul 14 2011 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-3
- .spec cosmetics
- use %%_qt4_ macros
- -doc subpkg here (instead of separately built)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 16 2010 Frank Büttner <frank-buettner@gmx.net> - 5.2.1-1
- update to 5.2.1 

* Fri Feb 05 2010 Frank Büttner <frank-buettner@gmx.net> - 5.2.0-1
- fix wrong lib names

* Fri Feb 05 2010 Frank Büttner <frank-buettner@gmx.net> - 5.2.0-0
- update to 5.2.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 04 2009 Frank Büttner <frank-buettner@gmx.net> - 5.1.1-2
- modify path patch

* Sun Jan 04 2009 Frank Büttner <frank-buettner@gmx.net> - 5.1.1-1
- update to 5.1.1

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.0.2-6
- Autorebuild for GCC 4.3

* Sat Sep 29 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.2-5
- add EPEL support

* Sat Sep 29 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.2-4
- remove parallel build, because it will fail sometimes

* Fri Sep 28 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.2-3
- fix some errors in the spec file

* Fri Jul 06 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.2-2
- fix some errors in the spec file

* Mon Jun 11 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.2-1
- update to 5.0.2
- split doc

* Tue May 15 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.1-1
- start
