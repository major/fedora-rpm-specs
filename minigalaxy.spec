Name:           minigalaxy
Version:        1.2.5
Release:        %autorelease
Summary:        GOG client for Linux that lets you download and play your GOG Linux games
BuildArch:      noarch

# CC-BY:        Logo image (data/minigalaxy.png)
License:        GPLv3+ and CC-BY
URL:            https://github.com/sharkwouter/minigalaxy
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

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
Requires:       webkit2gtk3

Recommends:     dosbox
Recommends:     gamemode
Recommends:     innoextract
Recommends:     mangohud
Recommends:     wine
Recommends:     wine-dxvk

Suggests:       scummvm

%description
A simple GOG client for Linux that lets you download and play your GOG Linux
games.


%prep
%autosetup


%build
%py3_build


%install
%py3_install


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
