Name:           deepin-menu
Version:        5.0.1
Release:        9%{?dist}
Summary:        Deepin menu service
License:        GPLv3+
URL:            https://github.com/linuxdeepin/deepin-menu
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires: make

%description
Deepin menu service for building beautiful menus.

%prep
%autosetup

# Modify lib path to reflect the platform
sed -i 's|/usr/bin|%{_libexecdir}|' data/com.deepin.menu.service \
    deepin-menu.desktop deepin-menu.pro

%build
%qmake_qt5 DEFINES+=QT_NO_DEBUG_OUTPUT
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

%files
%doc README.md
%license LICENSE
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/com.deepin.menu.service

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.1-7
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.1-6
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.1-5
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.1-1
- new upstream release: 5.0.1

* Thu Aug  6 2020 Robin Lee <cheeselee@fedoraproject.org> - 3.4.8-4
- BR: qt5-qtbase-private-devel

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.8-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.4.8-1
- Release 3.4.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 3.3.10-1
- Update to 3.3.10

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 3.1.7-1
- Update to 3.1.7

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 3.1.6-1
- Update to 3.1.6

* Wed Jul 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.5-1
- Update to 3.1.5

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 3.1.5-1.git3ab1c65
- Update to 3.1.5

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 3.1.4-1.gita4c0bf8
- Update to 3.1.4

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 3.1.2-1.git3aee346
- Update to 3.1.2

* Tue Feb 21 2017 mosquito <sensor.wen@gmail.com> - 3.0.10-1.git3750b2f
- Update to 3.0.10

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.0.7-1.git6038c51
- Update to 3.0.7

* Wed Jul 01 2015 mosquito <sensor.wen@gmail.com> - 2.90.0-1.git7557d46
- Update version to 2.90.0-1.git7557d46

* Wed Dec 03 2014 mosquito <sensor.wen@gmail.com> - 1.1git20141202-1
- Update version to 1.1git20141202

* Mon Dec 01 2014 mosquito <sensor.wen@gmail.com> - 1.1git20141124-1
- Update version to 1.1git20141124

* Tue Nov 18 2014 mosquito <sensor.wen@gmail.com> - 1.1git20141113-1
- Update version to 1.1git20141113

* Tue Nov 4 2014 mosquito <sensor.wen@gmail.com> - 1.1git20141028-1
- Update version to 1.1git20141028

* Thu Oct 9 2014 mosquito <sensor.wen@gmail.com> - 1.1git20140923-2
- Fixed depends

* Mon Sep 29 2014 mosquito <sensor.wen@gmail.com> - 1.1git20140923-1
- Initial build
