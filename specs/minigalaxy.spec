%global forgeurl https://github.com/sharkwouter/minigalaxy
%global tag %{version}

Name:           minigalaxy
Version:        1.4.0
%forgemeta
Release:        %autorelease
Summary:        Simple GOG client for Linux
BuildArch:      noarch

# CC-BY-3.0:    Logo image (data/minigalaxy.png)
License:        GPL-3.0-or-later and CC-BY-3.0
URL:            https://sharkwouter.github.io/minigalaxy
Source0:        %{forgesource}

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel >= 3.30
BuildRequires:  python3-setuptools

BuildRequires:  python3dist(requests)

Requires:       hicolor-icon-theme
Requires:       python3-requests
Requires:       unzip
Requires:       webkit2gtk4.1

Recommends:     dosbox
Recommends:     gamemode
Recommends:     innoextract
Recommends:     libvkd3d
Recommends:     mangohud
Recommends:     wine
Recommends:     wine-dxvk

Suggests:       scummvm

%description
A simple GOG client for Linux.


%prep
%forgeautosetup -p1


%build
%py3_build


%install
%py3_install
# Dirty: remove test files for quick update current ver
rm -rf %{buildroot}%{python3_sitelib}/tests/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE THIRD-PARTY-LICENSES.md
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/


%changelog
%autochangelog
