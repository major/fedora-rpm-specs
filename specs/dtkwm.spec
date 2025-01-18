Name:           dtkwm
Version:        2.0.12
Release:        25%{?dist}
Summary:        Deepin graphical user interface library
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/linuxdeepin/dtkwm
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-static
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires: make

%description
DtkWm is used to handle double screen for deepin desktop development.
This package contains the shared libraries.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir} DTK_MODULE_NAME=%{name}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libdir}/libdtkwm.so.5*

%files devel
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dtkwm.pri
%dir %{_libdir}/cmake/DtkWm/
%{_libdir}/cmake/DtkWm/DtkWmConfig.cmake
%{_libdir}/pkgconfig/dtkwm.pc
%{_libdir}/libdtkwm.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.12-24
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 2.0.12-17
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 2.0.12-16
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 2.0.12-15
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Robin Lee <cheeselee@fedoraproject.org> - 2.0.12-11
- rebuild (dtkcore)

* Fri Nov 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.0.12-10
- drop hard-coded Qt5 runtime dependency

* Mon Nov 23 07:52:00 CET 2020 Jan Grulich <jgrulich@redhat.com> - 2.0.12-9
- rebuild (qt5)

* Wed Sep 23 2020 Robin Lee <cheeselee@fedoraproject.org> - 2.0.12-8
- rebuild (dtkcore)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 2.0.12-7
- rebuild (qt5)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.0.12-5
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 2.0.12-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 2.0.12-2
- rebuild (qt5)

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.0.12-1
- Release 2.0.12

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul  6 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.0.11-1
- Update to 2.0.11
- Requires minor Qt version

* Wed Feb 20 2019 mosquito <sensor.wen@gmail.com> - 2.0.9-3
- use %%_qt5_bindir
- add gcc-c++ BReq

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 2.0.9-1
- Update to 2.0.9

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Tue Oct 17 2017 mosquito <sensor.wen@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Sat Aug 19 2017 mosquito <sensor.wen@gmail.com> - 2.0.0-1
- Initial package build
