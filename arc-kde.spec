Name:           arc-kde
Version:        20220908
Release:        %autorelease
Summary:        Port of the popular GTK theme Arc for the Plasma 5 desktop

License:        GPL-3.0-only AND CC-BY-SA-4.0
URL:            https://github.com/PapirusDevelopmentTeam/arc-kde
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/PapirusDevelopmentTeam/arc-kde/pull/145
Patch0:         arc-kde-plasma-6-support.patch

BuildArch:      noarch

BuildRequires:  make

Recommends:     %{name}-kvantum
Recommends:     %{name}-decorations
Recommends:     %{name}-konsole
Recommends:     %{name}-konversation
Recommends:     %{name}-wallpapers
Recommends:     %{name}-yakuake
Recommends:     papirus-icon-theme


%description
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

In this package you'll find:

 - Aurorae Themes
 - Konsole Color Schemes
 - Konversation Themes
 - Kvantum Themes
 - Plasma Color Schemes
 - Plasma Desktop Themes
 - Plasma Look-and-Feel Settings
 - Wallpapers
 - Yakuake Skins
 - Extra tools


%package kvantum
Summary:    Arc-KDE Kvantum theme
License:    GPL-3.0-only
BuildArch:  noarch
Requires:   kvantum

%description kvantum
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the ArcDark ard ArcDarker Kvantum theme.


%package decorations
Summary:    Arc-KDE Aurorae theme
License:    GPL-3.0-only
BuildArch:  noarch

%description decorations
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Aurorae window decorations.


%package konsole
Summary:    Arc-KDE Konsole theme
License:    GPL-3.0-only
BuildArch:  noarch

%description konsole
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the ArcDark Konsole theme.


%package konversation
Summary:    Arc-KDE Konversation theme
License:    GPL-3.0-only
BuildArch:  noarch

%description konversation
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Konversation theme.


%package wallpapers
Summary:    Arc-KDE wallpapers
License:    CC-BY-SA-4.0
BuildArch:  noarch

%description wallpapers
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Arc wallpapers.


%package yakuake
Summary:    Arc-KDE Yakuake theme
License:    GPL-3.0-only
BuildArch:  noarch

%description yakuake
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Yakuake theme.


%prep
%autosetup -p1

cp wallpapers/Arc-Dark/LICENSE LICENSE-wallpapers


%build
# Nothing to build


%install
%make_install


%files
%license LICENSE LICENSE-wallpapers
%doc AUTHORS README.md
%{_datadir}/color-schemes/*.colors
%{_datadir}/plasma/desktoptheme/Arc-Color
%{_datadir}/plasma/desktoptheme/Arc-Dark
%{_datadir}/plasma/look-and-feel/com.github.varlesh.*


%files decorations
%license LICENSE
%{_datadir}/aurorae/themes/Arc
%{_datadir}/aurorae/themes/Arc-Dark


%files konsole
%license LICENSE
%{_datadir}/konsole/*.colorscheme


%files konversation
%license LICENSE
%{_datadir}/konversation/themes/papirus
%{_datadir}/konversation/themes/papirus-dark


%files kvantum
%license LICENSE
%{_datadir}/Kvantum/Arc
%{_datadir}/Kvantum/ArcDark
%{_datadir}/Kvantum/ArcDarker


%files wallpapers
%license LICENSE-wallpapers
%{_datadir}/wallpapers/Arc
%{_datadir}/wallpapers/Arc-Dark
%{_datadir}/wallpapers/Arc-Mountains


%files yakuake
%license LICENSE
%{_datadir}/yakuake/skins/arc
%{_datadir}/yakuake/skins/arc-dark


%changelog
%autochangelog
