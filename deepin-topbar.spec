Name:           deepin-topbar
Version:        0.7.0
Release:        5%{?dist}
Summary:        Topbar for Deepin desktop environment
License:        GPLv3
URL:            https://github.com/justforlxz/deepin-topbar
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dde-network-utils)
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  qt5-linguist
Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%setup -q
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/dbus-1/services/*.service
%{_datadir}/polkit-1/actions/*.service

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Wed Sep  2 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.6.6-6
- Rebuild for libprocps

* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.6.6-5
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.6.6-2
- Fix installation of polkit rules

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.6.6-1
- Release 0.6.6

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.6.2-2
- Not requiring private Qt API

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 0.6.2-1
- Update to 0.6.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 0.6.0-2
- Append curdir to CMake invokation. (#1668512)

* Sun Dec 23 2018 mosquito <sensor.wen@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 0.5.1-1
- Initial build
