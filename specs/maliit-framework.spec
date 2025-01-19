Name:          maliit-framework
Version:       2.3.0
Release:       9%{?dist}
Summary:       Input method framework

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2
URL:           https://maliit.github.io/
Source0:       https://github.com/maliit/framework/archive/%{version}/%{name}-%{version}.tar.gz 

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: doxygen
BuildRequires: libX11-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libxkbcommon-devel
BuildRequires: systemd-devel

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-static
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtwayland-devel

BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

Obsoletes: maliit-framework-gtk2 < 2.0.0
Obsoletes: maliit-framework-qt4 < 2.0.0
Obsoletes: maliit-framework-gtk3 < 2.0.0

%description
Maliit provides a flexible and cross-platform input method framework. It has a
plugin-based client-server architecture where applications act as clients and
communicate with the Maliit server via input context plugins. The communication
link currently uses D-Bus.

%package qt5
Summary: Input method module for Qt 5 based on Maliit framework
## as of version 2.0.0 -- rdieter
# libQt5Gui.so.5(Qt_5.15.2_PRIVATE_API)(64bit)
# libQt5WaylandClient.so.5(Qt_5.15.2_PRIVATE_API)(64bit)
BuildRequires: qt5-qtbase-private-devel
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)
Obsoletes: maliit-plugins < 2.0.0

Requires: %{name}%{?_isa} = %{version}-%{release}

%description qt5
Input method module for Qt 4 based on Maliit framework.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# libmaliit-plugins moved to -qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%package docs
Summary: Documentation files for %{name}

%description docs
This package contains developer documentation for %{name}.

%package examples
Summary: Tests and examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}

%description examples
This package contains tests and examples for %{name}.


%prep
%autosetup -n framework-%{version} -p1

# Temporarily turn off tests for successful build - onuralp
%build
%cmake -Denable-examples=ON \
       -Denable-tests=OFF \
       -Denable-dbus-activation=ON \
       -Denable-wayland-gtk=ON

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%license LICENSE.LGPL
%doc README.md NEWS
%{_bindir}/maliit-server
%{_libdir}/libmaliit-glib.so.2*
%{_datadir}/dbus-1/services/org.maliit.server.service

%ldconfig_scriptlets qt5

%files qt5
%{_libdir}/libmaliit-plugins.so.2*
%{_libdir}/qt5/plugins/platforminputcontexts/libmaliitplatforminputcontextplugin.so
%{_libdir}/qt5/plugins/wayland-shell-integration/libinputpanel-shell.so

%files devel
%{_includedir}/maliit-2
%{_libdir}/cmake/MaliitGLib/
%{_libdir}/cmake/MaliitPlugins/
%{_libdir}/libmaliit-plugins.so
%{_libdir}/libmaliit-glib.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/qt5/mkspecs/features/*.prf

%files docs
%{_datadir}/doc/maliit-framework-doc/
%{_datadir}/doc/maliit-framework/

%files examples
%{_bindir}/maliit-exampleapp-plainqt


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.0-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 2.3.0-2
- Fix BZ#2128686 - maliit gtk3 package requirement removed from example package

* Tue Sep 20 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 2.3.0-1
- 2.3.0
- Obsoletes: maliit-framework-gtk3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 2.2.0-4
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 2.2.0-3
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 2.2.0-2
- Rebuild (qt5)

* Tue Feb 15 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 2.2.0-1
- Version 2.2.0
- Upstream patch removed
- Fix: https://github.com/maliit/framework/issues/86


* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-4
- -qt5: Obsoletes: maliit-plugins (#1992368)

* Mon Aug 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-3
- -qt5: move libmaliit-plugins, private qt5 deps, here
- drop explicit BR: make (pulled in by cmake)
- %%files: minor cleanup

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Jan Grulich <jgrulich@redhat.com> - 2.0.0-1
- 2.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 04 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 0.94.2-16
- Fix Python shebang in examples subpackage to avoid depending on Python2

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.94.2-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.94.2-9
- use %%qmake_qt4 macro to ensure proper build flags

* Sun Jul 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.2-8
- Fix ftbfs

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.94.2-5
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.94.2-3
- Fix duplicate documentation (#1001288)
- Add BR graphviz for /usr/bin/dot (missing images in documentation)
- Fix summaries, descriptions and Group tags of IM module subpackages
- Fix directory ownership

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.2-1
- New 0.94.2 release

* Wed Jan 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.1-1
- New 0.94.1 release

* Fri Jan 18 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.0-1
- New 0.94.0 release

* Fri Nov  9 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.1-1
- New 0.93.1 release

* Mon Oct 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.0-1
- New 0.93.0 release

* Tue Oct  9 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5.1-1
- 0.95.2.1 to add support for detecting tablet mode changes

* Thu Oct  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5-2
- Fix the updating of the gtk2 IM module cache

* Thu Sep 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5-1
- New 0.92.5 release, update based on review comments

* Tue Aug 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.4-1
- Initial packaging
