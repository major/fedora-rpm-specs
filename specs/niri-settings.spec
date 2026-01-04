%global commit db3337c1f30c1e90cb83ffb89f3679bddf6cd0a9
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20251226

Name:           niri-settings
Version:        0.1.0~git%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        GUI configuration app for Niri

License:        GPL-2.0-only
URL:            https://github.com/stefonarch/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:         0001-adjust-paths.patch
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  git-core

Requires:       hicolor-icon-theme
Requires:       niri >= 25.11
Requires:       python3-pyqt6
Requires:       (qt6-qtwayland if qt6-qtbase < 6.10)

%description
niri-settings is a GUI configuration application for the niri wayland
compositor

%prep
%autosetup -C -S git_am


%build


%install
install -Dm755 niri-settings %{buildroot}%{_bindir}/niri-settings
install -Dm644 niri-settings.desktop %{buildroot}%{_datadir}/applications/niri-settings.desktop
install -d %{buildroot}%{_libexecdir}/%{name}/ui
install -Dm755 niri_settings.py %{buildroot}%{_libexecdir}/%{name}/niri_settings.py
install -Dm644 ui/*.py %{buildroot}%{_libexecdir}/%{name}/ui
install -d %{buildroot}%{_datadir}/%{name}/translations
install -Dm644 translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/
install -Dm644 niri-settings.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/niri-settings.svg

%find_lang %{name} --all-name --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/ui
%{_bindir}/%{name}
%{_libexecdir}/%{name}/niri_settings.py
%{_libexecdir}/%{name}/ui/*.py
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Sat Dec 27 2025 Shawn W Dunn <sfalken@opensuse.org> - 0.1.0~git20251226.db3337c-1
- Initial Packaging

