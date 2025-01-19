Name:    kdiagram
Summary: Powerful libraries (KChart, KGantt) for creating business diagrams
Version: 3.0.1
Release: 7%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
Url:     https://invent.kde.org/graphics/kdiagram

Source0: http://download.kde.org/stable/kdiagram/%{version}/kdiagram-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Help)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)

# For AutoReq cmake-filesystem
BuildRequires: cmake

%description
Powerful libraries (KChart, KGantt) for creating business diagrams.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Svg)
Requires: cmake(Qt6Widgets)
Requires: cmake(Qt6PrintSupport)
%description devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kchart6_qt
%find_lang_kf6 kgantt6_qt
cat kchart6_qt.lang kgantt6_qt.lang > %{name}.lang

%files -f %{name}.lang
%license LICENSE.GPL.txt
%{_kf6_libdir}/libKChart6.so.3*
%{_kf6_libdir}/libKGantt6.so.3*

%files devel
%{_includedir}/KChart6/
%{_includedir}/KGantt6/
%{_kf6_libdir}/libKChart6.so
%{_kf6_libdir}/libKGantt6.so
%{_kf6_libdir}/cmake/KChart6/
%{_kf6_libdir}/cmake/KGantt6/
%{_kf6_archdatadir}/mkspecs/modules/qt_KChart6.pri
%{_kf6_archdatadir}/mkspecs/modules/qt_KGantt6.pri
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 09 2024 Marie Loise Nolden <loise@kde.org> - 3.0.1-5
- add missing BuildArch: noarch to -doc package

* Wed Feb 7 2024 Steve Cossette <farchord@gmail.com> - 3.0.1-4
- Added -doc subpackage

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Alessandro Astone <ales.astone@gmail.com> - 3.0.1-1
- 3.0.1

* Wed Dec 27 2023 Alessandro Astone <ales.astone@gmail.com> - 3.0.0-2
- Backport patch to fix cmake(KChart6)

* Wed Dec 6 2023 Steve Cossette <farchord@gmail.com> - 3.0.0-1
- 3.0.0

* Wed Dec 6 2023 Steve Cossette <farchord@gmail.com> - 2.8.0^20231206.021638.8f51a2d-1
- Update to qt6 from git

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 2.8.0-1
- 2.8.0
- %%check: use %%ctest (with some hackery)
- update URL
- drop 'BR: make', cmake pulls it in

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.7.0-1
- 2.7.0

* Mon Apr 13 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.6.3-1
- 2.6.3

* Sun Mar 29 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.6.2-1
- 2.6.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.6.1-1
- 2.6.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 2.6.0-7
- Rebuilt for AutoReq cmake-filesystem

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 2.6.0-4
- Add -devel dependencies

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.6.0-2
- add library scriptlets, reduce test time to 20 sec

* Sat Dec 31 2016 Rex Dieter <rdieter@math.unl.edu> - 2.6.0-1
- kdiagram-2.6.0

