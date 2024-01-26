Name:           deepin-screenshot
Version:        5.0.0
Release:        13%{?dist}
Summary:        Deepin Screenshot Tool
Summary(zh_CN): 深度截图工具
License:        GPLv3
Url:            https://github.com/linuxdeepin/deepin-screenshot
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-appdata.xml
# follow changes from Arch
Patch0:         https://raw.githubusercontent.com/archlinux/svntogit-community/e244b11755511b0eb84636302993a84a7bc7273c/trunk/deepin-screenshot-no-notification.patch

BuildRequires:  cmake
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       desktop-file-utils
Requires:       hicolor-icon-theme
Recommends:     deepin-shortcut-viewer

%description
Provide a quite easy-to-use screenshot tool. Features:
  * Global hotkey to triggle screenshot tool
  * Take screenshot of a selected area
  * Easy to add text and line drawings onto the screenshot

%description -l zh_CN
简单易用的截图工具. 特性:
  * 支持全局热键激活截图工具
  * 支持区域截图
  * 支持为截图添加文本和图形

%prep
%setup -q
# fix for Qt 5.15
sed -i '1i #include <QPainterPath>' src/widgets/shapeswidget.cpp
# Disable using deepin-turbo, which is not yet available in Fedora
sed -i 's/deepin-turbo-invoker.*deepin/deepin/' \
       src/dbusservice/com.deepin.Screenshot.service deepin-screenshot.desktop

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build

%install
%cmake_install
install -Dm644 %SOURCE1 %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%preun
if [ $1 -eq 0 ]; then
  /usr/sbin/alternatives --remove x-window-screenshot %{_bindir}/%{name}
fi

%post
if [ $1 -eq 1 ]; then
  /usr/sbin/alternatives --install %{_bindir}/x-window-screenshot \
    x-window-screenshot %{_bindir}/%{name} 20
fi

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/dbus-1/services/com.deepin.Screenshot.service
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-5
- Rebuild for DTK5

* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-4
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.1.8-2
- Disable using deepin-turbo, which is not yet available in Fedora

* Tue Feb 26 2019 mosquito <sensor.wen@gmail.com> - 4.1.8-1
- Update to 4.1.8

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 4.1.7-1
- Update to 4.1.7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 4.1.5-2
- Append curdir to CMake invokation. (#1668512)

* Sun Dec 23 2018 mosquito <sensor.wen@gmail.com> - 4.1.5-1
- Update to 4.1.5

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 4.1.4-1
- Update to 4.1.4

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 4.1.2-1
- Update to 4.1.2

* Fri Jul 20 2018 mosquito <sensor.wen@gmail.com> - 4.0.16-1
- Update to 4.0.16

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.10.4-2
- Remove obsolete scriptlets

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 4.0.10.4-1
- Update to 4.0.10.4

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 4.0.10-1
- Update to 4.0.10

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 4.0.9-1
- Update to 4.0.9

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 4.0.8-1.gitb7483cf
- Update to 4.0.8

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 4.0.0-1.gitcb50df2
- Update to 4.0.0

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.1.10-1.gitb0cc9f8
- Update to 3.1.10

* Fri Jul  3 2015 mosquito <sensor.wen@gmail.com> - 3.0.2-1.git753410c
- Update version to 3.0.2-1.git753410c

* Wed Dec 31 2014 mosquito <sensor.wen@gmail.com> - 2.1git20141231-1
- Update version to 2.1git20141231

* Mon Dec 15 2014 mosquito <sensor.wen@gmail.com> - 2.1git20141212-1
- Update version to 2.1git20141212

* Tue Nov  4 2014 mosquito <sensor.wen@gmail.com> - 2.1git20141104-1
- Update version to 2.1git20141104

* Mon Oct  6 2014 mosquito <sensor.wen@gmail.com> - 2.1git20140926-2
- Fixed depends

* Sun Oct  5 2014 mosquito <sensor.wen@gmail.com> - 2.1git20140926-1
- Initial build
