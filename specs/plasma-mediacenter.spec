Name:    plasma-mediacenter
Version: 5.7.5
Release: 25%{?dist}
Summary: A mediacenter user interface written with the Plasma framework

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://cgit.kde.org/plasma-mediacenter.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
Patch0: plasma-mediacenter-5.7.5-ctaglib.patch

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-baloo-devel
BuildRequires:  kf5-kactivities-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  taglib-devel

Obsoletes: plasma-mediacenter-devel < 5.0.0

Requires:       qt5-qtmultimedia%{?_isa}

%description
Plasma Media Center is designed to provide an easy and comfortable
way to watch your videos, browse your photo collection and listen to
your music, all in one place. This release brings many refinements
and a host of new features, making consuming media even easier and
more fun.


%prep
%autosetup -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install

%find_lang all --all-name


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/plasma-mediacenter.desktop


%ldconfig_scriptlets

%files -f all.lang
%license COPYING COPYING.LIB
%doc README
%{_kf5_libdir}/libplasmamediacenter.so.*
%{_kf5_qtplugindir}/plasma/mediacenter/
%{_kf5_qmldir}/org/kde/plasma/mediacenter/
%{_kf5_datadir}/applications/plasma-mediacenter.desktop
%{_kf5_datadir}/kservices5/plasma-shell-org.kde.plasma.mediacenter.desktop
%{_kf5_metainfodir}/org.kde.plasma.mediacenter.appdata.xml
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/plasma/shells/org.kde.plasma.mediacenter/
%{_datadir}/xsessions/plasma-mediacenter.desktop
%{_datadir}/icons/hicolor/*/*/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 5.7.5-24
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Than Ngo <than@redhat.com> - 5.7.5-14
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.7.5-9
- update URL, %%files, use %%make_build %%ldconfig_scriptlets

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.7.5-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.5-1
- 5.7.5

* Tue Aug 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.3-1
- 5.7.3

* Tue Jul 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.2-1
- 5.7.2

* Tue Jul 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-1
- 5.7.1

* Thu Jun 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-1
- 5.7.0

* Sat Jun 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.95-1
- 5.6.95

* Tue Jun 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.5-1
- 5.6.5

* Sat May 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.4-1
- 5.6.4

* Tue Apr 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.3-1
- 5.6.3

* Sat Apr 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.2-1
- 5.6.2

* Fri Apr 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.1-1
- 5.6.1

* Tue Mar 01 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.5-1
- Plasma 5.5.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.4-1
- Plasma 5.5.4

* Thu Jan 07 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.3-1
- Plasma 5.5.3

* Thu Dec 31 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.5.2-1
- 5.5.2

* Fri Dec 18 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.1-1
- Plasma 5.5.1

* Fri Dec 11 2015 Rex Dieter <rdieter@fedoraproject.org> 5.5.0-2
- .spec cosmetics, Obsoletes: plasma-mediacenter-devel (#1290669)

* Thu Dec 03 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.0-1
- Plasma 5.5.0

* Wed Nov 25 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.4.3-1
- Update to Plasma 5.4.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Sinny Kumari<ksinny@gmail.com> - 1.3.0-1
- New release 1.3.0

* Sat Nov 23 2013 siddharth sharma<siddharth.kde@gmail.com> - 1.1.9-1
- New Release 1.1.9
- Patch include translations sub-directory

* Fri Sep 13 2013 siddharth <siddharth.kde@gmail.com> - 1.1.0a-2
- New Release 1.1.0a
- Add gettext for BuildRequires

* Mon Aug 12 2013 siddharth sharma <siddharth.kde@gmail.com> - 1.0.95-1
- new release plasma-mediacenter-1.0.95

* Thu Aug 01 2013 siddharth sharma <siddharth.kde@gmail.com> - 1.0.90-1
- new release plasma-mediacenter-1.0.90
- remove kdenetwork-fileshare-samba
- Adding youtube icon
- Changing Requires

* Wed Jul 31 2013 siddharth sharma <siddharth.kde@gmail.com> - 1.0.0-3
- remove plasma-mobile from buildrequires

* Wed Mar 20 2013 siddharth <siddharths@fedoraproject.org> - 1.0.0-2
- rebuilt, Fixing missing BuildRequires for new package

* Wed Mar 20 2013 siddharth sharma <siddharths@fedoraproject.org> -1.0.0-1
- new upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.90-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 24 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.8.90-6
- %%files cleanup
- remove deprecated .spec
- remove unneccessary hacks (in particular, move plugins back to where they belong)

* Wed Oct 24 2012 siddharth <siddharth.kde@gmail.com> - 0.8.90-5
- Removed unwanted Requires and BuildRequires
- Removed Hicolor icons

* Wed Sep 12 2012 siddharth <siddharth.kde@gmail.com> - 0.8.90-4
- Fix installing plugins path

* Thu Jun 14 2012 Siddharth Sharma <siddharth.kde@gmail.com> - 0.8.90-3
- Packaging Fixes
- Package update Beta Release

* Sun Jun 03 2012 siddharth <siddharth.kde@gmail.com> - 0.9-2
- rebuilt for devel package split

* Sat Jun 2 2012 siddharth Sharma <siddharths@fedoraproject.org> - 0.9-1
- Initial Release 1

