%global appid com.interversehq.qView
%global upstream_name qView

Name:           qview
Version:        6.1
Release:        6%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
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
BuildRequires:  cmake(Qt5X11Extras)

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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 6.1-5
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 17 2023 Justin Zobel <justin.zobel@gmail.com> - 6.1-2
- Update to 6.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 17 2022 Justin Zobel <justin@1707.io> - 5.0-1
- Fedora Review Fixes

* Sat Mar 26 2022 Justin Zobel <justin@1707.io> - 5.0-1
- Initial version of package
