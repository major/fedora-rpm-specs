Name:           adwaita-qt
Version:        1.4.2
Release:        2%{?dist}
License:        LGPLv2+ and GPLv2+
Summary:        Adwaita theme for Qt-based applications

Url:            https://github.com/FedoraQt/adwaita-qt
Source0:        https://github.com/FedoraQt/adwaita-qt/archive/%{version}/adwaita-qt-%{version}.tar.gz

BuildRequires:  cmake

BuildRequires:  libxcb-devel

Obsoletes:      adwaita-qt4 < 1.1.90
Obsoletes:      adwaita-qt-common < 1.1.90

Requires:       (adwaita-qt5 if qt5-qtbase)
Requires:       (adwaita-qt6 if qt6-qtbase)

%description
Theme to let Qt applications fit nicely into Fedora Workstation

%package -n adwaita-qt5
Summary:        Adwaita Qt5 theme
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

Requires:       libadwaita-qt5%{?_isa} = %{version}-%{release}

%description -n adwaita-qt5
Adwaita theme variant for applications utilizing Qt5.

%package -n libadwaita-qt5
Summary:        Adwaita Qt5 library

%description -n libadwaita-qt5
%{summary}.

%package -n libadwaita-qt5-devel
Summary:        Development files for libadwaita-qt5
Requires:       libadwaita-qt5%{?_isa} = %{version}-%{release}

%description -n libadwaita-qt5-devel
The libadwaita-qt5-devel package contains libraries and header files for
developing applications that use libadwaita-qt5.

%package -n adwaita-qt6
Summary:        Adwaita Qt6 theme
BuildRequires:  qt6-qtbase-devel

Requires:       libadwaita-qt6%{?_isa} = %{version}-%{release}

%description -n adwaita-qt6
Adwaita theme variant for applications utilizing Qt6.

%package -n libadwaita-qt6
Summary:        Adwaita Qt6 library

%description -n libadwaita-qt6
%{summary}.

%package -n libadwaita-qt6-devel
Summary:        Development files for libadwaita-qt6
Requires:       libadwaita-qt6%{?_isa} = %{version}-%{release}

%description -n libadwaita-qt6-devel
The libadwaita-qt6-devel package contains libraries and header files for
developing applications that use libadwaita-qt6.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%global _vpath_builddir %{_target_platform}-qt5
%if 0%{?flatpak} && 0%{?fedora} >= 36
%cmake -DQT_PLUGINS_DIR=%{_libdir}/qt5/plugins
%else
%cmake
%endif
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
%cmake -DUSE_QT6=true
%cmake_build

%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

rm -rf %{buildroot}%{_libdir}/pkgconfig/adwaita-qt6.pc

%files -n adwaita-qt5
%doc LICENSE.LGPL2 README.md
%{_qt5_plugindir}/styles/adwaita.so

%files -n libadwaita-qt5
%{_libdir}/libadwaitaqt.so.*
%{_libdir}/libadwaitaqtpriv.so.*

%files -n libadwaita-qt5-devel
%dir %{_includedir}/AdwaitaQt
%{_includedir}/AdwaitaQt/*.h
%dir %{_libdir}/cmake/AdwaitaQt
%{_libdir}/cmake/AdwaitaQt/*.cmake
%{_libdir}/pkgconfig/adwaita-qt.pc
%{_libdir}/libadwaitaqt.so
%{_libdir}/libadwaitaqtpriv.so

%files -n adwaita-qt6
%{_qt6_plugindir}/styles/adwaita.so

%files -n libadwaita-qt6
%{_libdir}/libadwaitaqt6.so.*
%{_libdir}/libadwaitaqt6priv.so.*

%files -n libadwaita-qt6-devel
%dir %{_includedir}/AdwaitaQt6
%{_includedir}/AdwaitaQt6/*.h
%dir %{_libdir}/cmake/AdwaitaQt
%{_libdir}/cmake/AdwaitaQt6/*.cmake
%{_libdir}/libadwaitaqt6.so
%{_libdir}/libadwaitaqt6priv.so

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Jan Grulich <jgrulich@redhat.com> - 1.4.2-1
- 1.4.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 19 2022 Jan Grulich <jgrulich@redhat.com> - 1.4.1-5
- Fix Flatpak installation path for Adwaita style plugin

* Thu Apr 21 2022 Jan Grulich <jgrulich@redhat.com> - 1.4.1-4
- Rebuild (Qt6)

* Sat Mar 05 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.4.1-3
- Small cleanups to the packaging

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Jan Grulich <jgrulich@redhat.com> - 1.4.1-1
- 1.4.1
  + Add Qt6 version

* Tue Aug 24 2021 Jan Grulich <jgrulich@redhat.com> - 1.4.0-1
- 1.4.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Jan Grulich <jgrulich@redhat.com> - 1.3.1-1
- 1.3.1

* Wed Jun 02 2021 Jan Grulich <jgrulich@redhat.com> - 1.3.0-1
- 1.3.0

* Mon Mar 22 2021 Jan Grulich <jgrulich@redhat.com> - 1.2.1-1
- 1.2.1

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Jan Grulich <jgrulich@redhat.com> - 1.2.0-1
- 1.2.0

* Wed Sep 30 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.90-1
- 1.1.90

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.3-2
- Views: do not set color to views which don't use our palette

* Fri May 15 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.3-1
- 1.1.3

* Mon May 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.2-1
- 1.1.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.1-2
- Set correct Light, Midlight, Dark and Mid colors

* Wed Nov 20 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Mon Oct 21 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-5
- Actually apply all the fixes

* Mon Sep 02 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-4
- Pull in upstream fixes

* Tue Aug 13 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-3
- Pull in upstream fixes

* Tue Jul 30 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-2
- Pull in upstream fixes

* Mon Jul 29 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Jan Grulich <jgrulich@redhat.com> - 1.0.91-1
- Update to 1.0.91

* Mon Jul 08 2019 Jan Grulich <jgrulich@redhat.com> - 1.0.90-2
- Fix Qt4 item view widgets

* Tue Jul 02 2019 Jan Grulich <jgrulich@redhat.com. - 1.0.90-1
- Update to 1.0.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 26 2017 Martin Bříza <mbriza@redhat.com> - 1.0-1
- Update to 1.0

* Mon Feb 27 2017 Martin Briza <mbriza@redhat.com> - 0.98-1
- Update to 0.98
- Fixes #1410597

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.97-2
- drop hardcoded Requires: qt4/qt5-qtbase

* Wed Dec 14 2016 Martin Briza <mbriza@redhat.com> - 0.97-1
- Update to 0.97

* Tue Dec 13 2016 Martin Briza <mbriza@redhat.com> - 0.95-1
- Update to 0.95

* Thu Jun 30 2016 Jan Grulich <jgrulich@redhat.com> - 0.4-3
- Properly fix missing menubar in QtCreator

* Wed Jun 22 2016 Jan Grulich <jgrulich@redhat.com> - 0.4-2
- Attempt to fix missing menubar issue in QtCreator

* Thu Apr 21 2016 Jan Grulich <jgrulich@redhat.com> - 0.4-1
- Update to version 0.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Martin Briza <mbriza@redhat.com> - 0.3-1
- Updated to the latest release
- Added a Qt5 build

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20141216git024b00bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.6.20141216git024b00bf
- Rebuilt for GCC 5 C++11 ABI change

* Fri Jan 16 2015 Martin Briza <mbriza@redhat.com> - 0-0.5
- Package review cleanup
- Split into a base and a subpackage
- Fedora import

* Tue Dec 16 2014 Martin Briza <mbriza@redhat.com> - 0-0.4.copr
- Update to latest commit

* Fri Dec 05 2014 Martin Briza <mbriza@redhat.com> - 0-0.3.copr
- Update to latest commit

* Mon Sep 15 2014 Martin Briza <mbriza@redhat.com> - 0-0.2.copr
- Update to latest commit

* Mon Sep 15 2014 Martin Briza <mbriza@redhat.com> - 0-0.1.copr
- Initial build
