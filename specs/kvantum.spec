%global _vpath_srcdir Kvantum
%bcond  qt5           1

Name:           kvantum
Version:        1.1.5
Release:        %autorelease
Summary:        SVG-based theme engine for Qt, KDE and LXQt

License:        GPL-3.0-or-later
URL:            https://github.com/tsujan/Kvantum
Source0:        %{url}/releases/download/V%{version}/Kvantum-%{version}.tar.xz
Source1:        %{url}/releases/download/V%{version}/Kvantum-%{version}.tar.xz.asc
Source2:        https://github.com/tsujan.gpg

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
%if 0%{?fedora} >= 40
BuildRequires:  cmake(KF6WindowSystem)
%endif
%if %{with qt5}
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  cmake(KF5WindowSystem)
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  kde-filesystem

Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}

%if %{with qt5}
Recommends:     (%{name}-qt5 if qt5-qtbase-gui)
%endif

# Qt6 is default since 1.1.0
Provides:  kvantum-qt6 = %{version}-%{release}
Obsoletes: kvantum-qt6 < 1.1.0

%description
Kvantum is an SVG-based theme engine for Qt, tuned to KDE and LXQt, with an
emphasis on elegance, usability and practicality.

Kvantum has a default dark theme, which is inspired by the default theme of
Enlightenment. Creation of realistic themes like that for KDE was the first
reason to make Kvantum but it goes far beyond its default theme: you could
make themes with very different looks and feels for it, whether they be
photorealistic or cartoonish, 3D or flat, embellished or minimalistic, or
something in between, and Kvantum will let you control almost every aspect of
Qt widgets.

Kvantum also comes with many other themes that are installed as root and can
be selected and activated by using Kvantum Manager.

%if %{with qt5}
%package qt5
Summary:   SVG-based theme engine for Qt5
Requires:  %{name}-data = %{version}-%{release}

%description qt5
Kvantum is an SVG-based theme engine for Qt, tuned to KDE and LXQt, with an
emphasis on elegance, usability and practicality.

This package contains the Qt5 integration plugin.
%endif

%package data
Summary:    SVG-based theme engine for Qt5, KDE and LXQt
BuildArch:  noarch

%description data
Kvantum is an SVG-based theme engine for Qt, tuned to KDE and LXQt, with an
emphasis on elegance, usability and practicality.

This package contains the data needed Kvantum.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n Kvantum-%{version}

%build
%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake -DENABLE_QT5:BOOL=ON
%cmake_build
%endif

%global _vpath_builddir %{_target_platform}-qt6
%cmake \
    -DENABLE_QT5:BOOL=OFF \
%if 0%{?fedora} < 40
    -DWITHOUT_KF=ON
%endif
%cmake_build

%install
%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%endif

%global _vpath_builddir %{_target_platform}-qt6
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
%{_qt6_plugindir}/styles/libkvantum.so
%{_datadir}/applications/kvantummanager.desktop
%{_datadir}/icons/hicolor/scalable/apps/kvantum.svg
%dir %{_datadir}/kvantumpreview
%dir %{_datadir}/kvantumpreview/translations
%dir %{_datadir}/kvantummanager
%dir %{_datadir}/kvantummanager/translations

%if %{with qt5}
%files qt5
%{_qt5_plugindir}/styles/libkvantum.so
%endif

%files data
%license Kvantum/COPYING
%{_datadir}/Kvantum/
%{_datadir}/color-schemes/Kv*.colors

%changelog
%autochangelog
