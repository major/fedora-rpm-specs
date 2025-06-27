Name: hicolor-icon-theme
Version: 0.18
Release: %autorelease
Summary: Basic requirement for icon themes

License: GPL-2.0-or-later
URL: https://www.freedesktop.org/wiki/Software/icon-theme/
Source0: https://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildArch: noarch

BuildRequires: meson

%description
Contains the basic directories and files needed for icon theme support.

%prep
%autosetup -p1

# for some reason this file is executable in the tarball
chmod 0644 COPYING

%build
%meson
%meson_build

%install
%meson_install

rm $RPM_BUILD_ROOT%{_datadir}/pkgconfig/default-icon-theme.pc
touch $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license COPYING
%doc README.md
%dir %{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/16x16/
%{_datadir}/icons/hicolor/16x16@2/
%{_datadir}/icons/hicolor/22x22/
%{_datadir}/icons/hicolor/22x22@2/
%{_datadir}/icons/hicolor/24x24/
%{_datadir}/icons/hicolor/24x24@2/
%{_datadir}/icons/hicolor/32x32/
%{_datadir}/icons/hicolor/32x32@2/
%{_datadir}/icons/hicolor/36x36/
%{_datadir}/icons/hicolor/36x36@2/
%{_datadir}/icons/hicolor/48x48/
%{_datadir}/icons/hicolor/48x48@2/
%{_datadir}/icons/hicolor/64x64/
%{_datadir}/icons/hicolor/64x64@2/
%{_datadir}/icons/hicolor/72x72/
%{_datadir}/icons/hicolor/72x72@2/
%{_datadir}/icons/hicolor/96x96/
%{_datadir}/icons/hicolor/96x96@2/
%{_datadir}/icons/hicolor/128x128/
%{_datadir}/icons/hicolor/128x128@2/
%{_datadir}/icons/hicolor/192x192/
%{_datadir}/icons/hicolor/192x192@2/
%{_datadir}/icons/hicolor/256x256/
%{_datadir}/icons/hicolor/256x256@2/
%{_datadir}/icons/hicolor/512x512/
%{_datadir}/icons/hicolor/512x512@2/
%{_datadir}/icons/hicolor/scalable/
%{_datadir}/icons/hicolor/symbolic/
%{_datadir}/icons/hicolor/index.theme
%ghost %{_datadir}/icons/hicolor/icon-theme.cache

%changelog
%autochangelog
