%global commit 84f30e6153301eeb14196b85ef3bc9f81d46cfd0
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20251225

Name:           labwc-tweaks
Version:        0.1.0~git%{commitdate}.%{shortcommit}
Release:        2%{?dist}
Summary:        GUI configuration app for labwc

License:        GPL-2.0-only and BSD-3-Clause
URL:            https://github.com/labwc/labwc-tweaks
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  perl-interpreter

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       labwc

%description
labwc-tweaks is a GUI configuration application for the labwc wayland
compositor

%prep
%autosetup -n %{name}-%{commit}


%build
%cmake
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/labwc_tweaks.desktop

%files -f %{name}.lang
%license LICENSE BSD-3-Clause
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/labwc_tweaks.appdata.xml


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20251225.84f30e6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Dec 26 2025 Shawn W Dunn <sfalken@opensuse.org> - 0.1.0~git20251225.84f30e6-1
- Update to current 84f30e6 commit

* Sat Jan 11 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 0.1.0~git20241022.d97f0a2-1
- Initial Packaging
