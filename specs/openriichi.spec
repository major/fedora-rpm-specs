Name:             openriichi
Version:          0.2.1.1
Release:          9%{?dist}
Summary:          Japanese Mahjong 3D game
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:          GPL-3.0-only

Requires:         google-noto-sans-cjk-jp-fonts

%global forgeurl0 https://github.com/FluffyStuff/Engine
%global commit0   0bd410550600a2a0858ca327576bdd32116da188

%global forgeurl1 https://github.com/FluffyStuff/OpenRiichi
%global version1  %{version}

%forgemeta -a

URL:              %{forgeurl}

BuildRequires:    vala
BuildRequires:    gcc-c++
BuildRequires:    meson
BuildRequires:    libgee-devel
BuildRequires:    gtk3-devel
BuildRequires:    glew-devel
BuildRequires:    pango-devel
BuildRequires:    SDL2_image-devel
BuildRequires:    SDL2_mixer-devel
BuildRequires:    SDL2-devel
BuildRequires:    desktop-file-utils

Requires:         %{name}-data = %{version}

Source0:          %{forgesource0}
Source1:          %{forgesource1}
Source2:          %{name}.desktop

# Use lower case for executable file and game directory
Patch0:           0001-Use-lowercase-for-progam-name.patch
# Load application icon from standard directory /usr/share/pixmaps
Patch1:           0002-Change-icon-path.patch
# Load fonts provided by the system
Patch2:           0003-Use-system-fonts.patch

%global common_description %{expand:
OpenRiichi is an open source Japanese Mahjong client written in the Vala 
programming language. It supports singleplayer and multiplayer, with or without 
bots. It features all the standard riichi rules, as well as some optional ones. 
It also supports game logging, so games can be viewed again.}

%description
%{common_description}

%package data
Summary:          Data files for OpenRiichi
BuildArch:        noarch
Requires:         %{name} = %{version}-%{release}

%description data
%{common_description}

This package contains the openriichi data files.

%prep
%forgesetup -a
# Use system fonts instead of provided ones
rm -r Engine bin/Data/Fonts
mv ../Engine-%{commit0} Engine
mv Engine/LICENSE ENGINE_LICENSE
%autopatch -p1

%build
%global _distro_extra_cflags -Wno-int-conversion
%meson
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/pixmaps
# Move application icon to standard directory
mv %{buildroot}%{_datadir}/%{name}/Data/Icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%check
%meson_test

%files
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc README.md CHANGELOG.md
%license LICENSE ENGINE_LICENSE

%files data
%{_datadir}/%{name}
%license LICENSE ENGINE_LICENSE

%changelog
* Thu Jan 23 2025 Julien Rische <jrische@redhat.com> - 0.2.1.1-9
- Compile ignoring integer conversion warnings
  Resolves: rhbz#2340975

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.1.1-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jul 25 2022 Julien Rische <jrische@redhat.com> - 0.2.1.1-1
- Initial package release
- Resolves: rhbz#2074401
