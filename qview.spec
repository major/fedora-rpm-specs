%global appid com.interversehq.qView
%global upstream_name qView

Name:           qview
Version:        5.0
Release:        2%{?dist}
License:        GPLv3+
Summary:        Practical and minimal image viewer
URL:            https://interversehq.com/qview/
Source:         https://github.com/jurplel/%{upstream_name}/releases/download/%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-rpm-macros

BuildRequires:  cmake(Qt5Core)

Requires: hicolor-icon-theme
Requires: kf5-kimageformats
Requires: qt5-qtimageformats
Requires: qt5-qtsvg


%description
qView is a Qt image viewer designed with minimalism and usability in mind. It
is designed to get out of your way and let you view your image without excess
GUI elements, while also being flexible enough for everyday use.


%prep
%autosetup -n %{upstream_name}

%build
PREFIX=%{_prefix} %qmake_qt5
%make_build

%install
INSTALL_ROOT="%{buildroot}" %make_install

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{appid}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop

%files
%doc README.md

%license LICENSE

%{_bindir}/%{name}

%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appid}.*
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg

%{_metainfodir}/%{appid}.appdata.xml

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 17 2022 Justin Zobel <justin@1707.io> - 5.0-1
- Fedora Review Fixes

* Sat Mar 26 2022 Justin Zobel <justin@1707.io> - 5.0-1
- Initial version of package
