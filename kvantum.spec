%global _vpath_srcdir Kvantum

Name:           kvantum
Version:        1.0.3
Release:        %autorelease
Summary:        SVG-based theme engine for Qt5, KDE and LXQt

License:        GPL-3.0-only
URL:            https://github.com/tsujan/Kvantum
Source0:        %url/archive/V%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  desktop-file-utils
BuildRequires:  kde-filesystem
Requires:       %{name}-data
Requires:       hicolor-icon-theme

%description
Kvantum is an SVG-based theme engine for Qt5, KDE and LXQt, with an emphasis
on elegance, usability and practicality.

Kvantum has a default dark theme, which is inspired by the default theme of
Enlightenment. Creation of realistic themes like that for KDE was the first
reason to make Kvantum but it goes far beyond its default theme: you could
make themes with very different looks and feels for it, whether they be
photorealistic or cartoonish, 3D or flat, embellished or minimalistic, or
something in between, and Kvantum will let you control almost every aspect of
Qt widgets.

Kvantum also comes with extra themes that are installed as root with Qt5
installation and can be selected and activated by using Kvantum Manager.

%package data
Summary:    SVG-based theme engine for Qt5, KDE and LXQt
BuildArch:  noarch
Requires:   kvantum

%description data
Kvantum is an SVG-based theme engine for Qt5, KDE and LXQt, with an emphasis
on elegance, usability and practicality.

This package contains the data needed Kvantum.

%prep
%autosetup -n Kvantum-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

# desktop-file-validate doesn't recognize LXQt
sed -i "s|LXQt|X-LXQt|" %{buildroot}%{_datadir}/applications/kvantummanager.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/kvantummanager.desktop

%find_lang %{name} --all-name --with-qt

%files -f %{name}.lang
%license Kvantum/COPYING
%doc Kvantum/ChangeLog Kvantum/NEWS Kvantum/README.md
%{_bindir}/kvantummanager
%{_bindir}/kvantumpreview
%{_qt5_plugindir}/styles/libkvantum.so

%files data
%{_datadir}/Kvantum/
%{_datadir}/applications/kvantummanager.desktop
%{_datadir}/color-schemes/Kv*.colors
%{_datadir}/icons/hicolor/scalable/apps/kvantum.svg
%{_datadir}/themes/Kv*/
%dir %{_datadir}/kvantumpreview
%dir %{_datadir}/kvantumpreview/translations
%dir %{_datadir}/kvantummanager
%dir %{_datadir}/kvantummanager/translations

%changelog
%autochangelog
