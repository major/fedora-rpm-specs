Name:           libqtxdg
Summary:        QtXdg, a Qt5 implementation of XDG standards
Version:        4.1.0

Release:        3%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://lxqt-project.org
Source0:        https://github.com/lxqt/libqtxdg/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  file-devel
BuildRequires:  lxqt-build-tools
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

Requires:       xdg-user-dirs
Requires:       xdg-utils
Obsoletes:      libqtxdg-qt5 <= 1.1.0

%description
%{summary}.

%package devel
Summary:        Qt - development files for qtxdg
Obsoletes:      libqtxdg-qt5-devel <= 1.1.0
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Files used for developing and building software that uses qtxdg.


%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS
%license COPYING
%{_libdir}/libQt6Xdg.so.4
%{_libdir}/libQt6Xdg.so.%{version}
%{_libdir}/libQt6XdgIconLoader.so.4
%{_libdir}/libQt6XdgIconLoader.so.%{version}
%{_sysconfdir}/xdg/lxqt-qtxdg.conf
%{_sysconfdir}/xdg/qtxdg.conf

%files devel
%{_libdir}/libQt6Xdg.so
%{_libdir}/libQt6XdgIconLoader.so
%{_libdir}/pkgconfig/Qt6Xdg.pc
%{_libdir}/pkgconfig/Qt6XdgIconLoader.pc
%{_includedir}/qt6xdg/
%{_includedir}/qt6xdgiconloader/
%{_datadir}/cmake/qt6xdg/
%{_datadir}/cmake/qt6xdgiconloader/
%{_qt6_archdatadir}/plugins/iconengines/libQt6XdgIconPlugin.so

%changelog
* Mon Feb 03 2025 Jan Grulich <jgrulich@redhat.com> - 4.1.0-3
- Rebuild (qt6)

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Steve Cossette <farchord@gmail.com> - 4.1.0-1
- 4.1.0

* Thu Oct 17 2024 Steve Cossette <farchord@gmail.com> - 4.0.1-1
- 4.0.1

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 4.0.0-3
- Rebuild (qt6)

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0.0-2
- convert license to SPDX

* Tue Jul 16 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0

* Fri Apr 19 2024 Steve Cossette <farchord@gmail.com> - 3.12.0-4
- Removed qtxdg configs to fix co-installability with the qt6 variant

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Zamir SUN <sztsian@gmail.com> - 3.12.0-1
- Update version to 3.12.0

* Fri Jul 28 2023 Zamir SUN <sztsian@gmail.com> - 3.11.0-1
- Update version to 3.11.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Zamir SUN <sztsian@gmail.com> - 3.10.0-1
- Update version to 3.10.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Zamir SUN <sztsian@gmail.com> - 3.9.0-2
- Re-apply the change for the qt5 dependency

* Sat Jul 16 2022 Zamir SUN <sztsian@gmail.com> - 3.9.0-1
- new version

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 3.8.0-5
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 3.8.0-4
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 3.8.0-3
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 zsun <sztsian@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Mon Nov 23 07:53:33 CET 2020 Jan Grulich <jgrulich@redhat.com> - 3.5.0-6
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 3.5.0-5
- rebuild (qt5)

* Tue Aug 11 2020 Zamir SUN <sztsian@gmail.com> - 3.5.0-4
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.3.1-9
- rebuild (qt5)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 3.3.1-7
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 3.3.1-6
- rebuild (qt5)

* Fri Sep 20 2019 Zamir SUN <sztsian@gmail.com> - 3.3.1-5
- Modify to improve compatibility with epel7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 3.3.1-3
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 3.3.1-2
- rebuild (qt5)

* Mon Apr 15 2019 Zamir SUN <zsun@fedoraproject.org>  - 3.3.1-1
- Update to 3.3.1

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.3.0-2
- rebuild (Qt5)

* Tue Feb 12 2019 Zamir SUN <zsun@fedoraproject.org>  - 3.3.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-3
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 3.2.0-2
- rebuild (qt5)

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-14
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-13
- rebuild (qt5)

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-12
- .spec cleanup, BR: gcc-c++, use %%license %%make_build

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 2.0.0-11
- rebuild (qt5)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 2.0.0-9
- rebuild (qt5)

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-8
- rebuild (qt5)

* Thu Oct 19 2017 Christian Dersch <lupinix@mailbox.org> - 2.0.0-7
- rebuilt

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-6
- BR: qt5-qtbase-private-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Helio Chissini de Castro <helio@kde.org> - 2.0.0-2
- Add proper dependencies to xdg-utils and xdg-user-dirs

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - * Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 2.0.0-1
- New upstream release tied to lxqt 0.11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Helio Chissini de Castro <helio@kde.org> - 1.3.0-2
- Prepare to use new cmake3 package from epel

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 1.3.0-1
- New upstream release
- No more Qt4 releases

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Helio Chissini de Castro <helio@kde.org> - 1.2.0-1
- New upstream version

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 1.1.0-4
- Rebuild (gcc5)

* Thu Feb 12 2015 Helio Chissini de Castro <helio@kde.org> - 1.1.0-3
- Restore Qt4 due to maintenance of RazorQt

* Wed Feb 11 2015 Helio Chissini de Castro <helio@kde.org> - 1.1.0-2
- Upstream patch for qiconfix

* Mon Feb 09 2015 Helio Chissini de Castro <helio@kde.org> - 1.1.0-1
- New upstream version 1.1.0
- Only Qt5 now

* Thu Oct 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-1
- libqtxdg-1.0.0, soname bump (#1147204)

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.5.3-4
- Provide qt4 support (#1147204)
- rename libqtxdg-qt4 -> libqtxdg, libqtxdg-qt4-devel -> libqtxdg to ease/simplify upgrade path
- use %%find_lang for translations
- -devel: drop cmake dep

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.5.3-1
- Update to a later upstream release

* Tue Dec 03 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.5.0-1
- Initial packaging
