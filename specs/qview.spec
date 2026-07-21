%global appid com.interversehq.qView
%global upstream_name qView

Name:           qview
Version:        7.1
Release:        %autorelease
License:        GPL-3.0-only
Summary:        Practical and minimal image viewer
URL:            https://interversehq.com/qview/
Source:         https://github.com/jurplel/%{upstream_name}/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6LinguistTools)

Requires: hicolor-icon-theme
Requires: kf6-kimageformats
Requires: qt6-qtimageformats
Requires: qt6-qtsvg


%description
qView is a Qt image viewer designed with minimalism and usability in mind. It
is designed to get out of your way and let you view your image without excess
GUI elements, while also being flexible enough for everyday use.


%prep
%autosetup -n %{upstream_name}-%{version}

%build
PREFIX=%{_prefix} %qmake_qt6
%make_build

%install
INSTALL_ROOT="%{buildroot}" %make_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appid}.*
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_metainfodir}/%{appid}.appdata.xml

%changelog
%autochangelog
