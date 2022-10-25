Name:           materia-kde
Version:        20220823
Release:        %autorelease
Summary:        Port of the popular GTK theme Materia for the Plasma 5 desktop

License:        GPL-3.0-only
URL:            https://github.com/PapirusDevelopmentTeam/materia-kde
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
Recommends:     %{name}-kvantum
Recommends:     %{name}-decorations
Recommends:     %{name}-konsole
Recommends:     %{name}-wallpapers
Recommends:     %{name}-yakuake
Recommends:     papirus-icon-theme

%description
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

In this package you'll find:

 - Aurorae Themes
 - Konsole Color Schemes
 - Kvantum Themes
 - Plasma Color Schemes
 - Plasma Desktop Themes
 - Plasma Look-and-Feel Settings
 - Wallpapers
 - Yakuake Skins

%package decorations
Summary:    Materia-KDE Aurorae theme

%description decorations
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the Aurorae window decorations.

%package konsole
Summary:    Materia-KDE Konsole theme

%description konsole
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the MateriaDark Konsole theme.

%package kvantum
Summary:    Materia-KDE Kvantum theme
Requires:   kvantum

%description kvantum
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the MateriaDark and MateriaLight Kvantum theme.

%package sddm
Summary:    Materia-KDE SDDM theme
Requires:   sddm

%description sddm
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the MateriaDark and Materia SDDM theme.

%package wallpapers
Summary:    Materia-KDE wallpapers

%description wallpapers
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the Materia wallpapers.

%package yakuake
Summary:    Materia-KDE Yakuake theme

%description yakuake
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the Yakuake theme.

%prep
%autosetup

%build
# Nothing to build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_datadir}/color-schemes/*.colors
%{_datadir}/plasma/desktoptheme/Materia
%{_datadir}/plasma/desktoptheme/Materia-Color
%{_datadir}/plasma/look-and-feel/com.github.varlesh.materia
%{_datadir}/plasma/look-and-feel/com.github.varlesh.materia-dark
%{_datadir}/plasma/look-and-feel/com.github.varlesh.materia-light

%files decorations
%license LICENSE
%{_datadir}/aurorae/themes/Materia
%{_datadir}/aurorae/themes/Materia-Dark
%{_datadir}/aurorae/themes/Materia-Light

%files konsole
%license LICENSE
%{_datadir}/konsole/*.colorscheme

%files kvantum
%license LICENSE
%{_datadir}/Kvantum/Materia
%{_datadir}/Kvantum/MateriaDark
%{_datadir}/Kvantum/MateriaLight

%files sddm
%license LICENSE
%{_datadir}/sddm/themes/materia
%{_datadir}/sddm/themes/materia-dark
%{_datadir}/sddm/themes/materia-light

%files wallpapers
%license LICENSE
%{_datadir}/wallpapers/Materia
%{_datadir}/wallpapers/Materia-Dark

%files yakuake
%license LICENSE
%{_datadir}/yakuake/skins/materia-dark
%{_datadir}/yakuake/skins/materia-light

%changelog
%autochangelog
