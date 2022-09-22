%global vergit 20220527

Name: flat-remix-theme
Version: 0.0.%{vergit}
Release: %autorelease
Summary: Pretty simple theme inspired on material design
BuildArch: noarch

License: GPLv3+
URL: https://drasite.com/flat-remix-gtk
Source: https://github.com/daniruiz/flat-remix-gtk/archive/%{vergit}/%{name}-%{version}.tar.gz

BuildRequires: make

Requires: flat-remix-gtk2-theme
Requires: flat-remix-gtk3-theme
Requires: flat-remix-gtk4-theme
Requires: flat-remix-icon-theme

Recommends: gnome-shell-theme-flat-remix

%global _description %{expand:
Flat Remix GTK theme is a pretty simple GTK window theme inspired on material
design following a modern design using "flat" colors with high contrasts and
sharp borders.

Themes:
  * Flat Remix GTK
  * Flat Remix GTK Dark
  * Flat Remix GTK Darker
  * Flat Remix GTK Darkest

Variants:
  * Solid: Theme without transparency
  * No Border: Darkest theme without white window border}

%description %{_description}

This meta package contains complete Flat Remix theme.


%package -n flat-remix-gtk2-theme
Summary: GTK+ 2 support for the Flat Remix GTK theme

Requires: adwaita-gtk2-theme
Requires: gtk2
Recommends: flat-remix-gtk3-theme
Recommends: flat-remix-gtk4-theme

%description -n flat-remix-gtk2-theme %{_description}

This package contains GTK+ 2 theme.


%package -n flat-remix-gtk3-theme
Summary: GTK+ 3 support for the Flat Remix GTK theme

Requires: gtk3
Recommends: flat-remix-gtk2-theme
Recommends: flat-remix-gtk4-theme
Suggests: flat-remix-theme

%description -n flat-remix-gtk3-theme %{_description}

This package contains GTK+ 3 theme.


%package -n flat-remix-gtk4-theme
Summary: GTK+ 3 support for the Flat Remix GTK theme

Requires: gtk4
Recommends: flat-remix-gtk2-theme
Recommends: flat-remix-gtk3-theme
Suggests: flat-remix-theme

%description -n flat-remix-gtk4-theme %{_description}

This package contains GTK 4 theme.


%prep
%autosetup -n flat-remix-gtk-%{vergit}


%install
%make_install


%files
%{_datadir}/themes/*/cinnamon/
%{_datadir}/themes/*/index.theme
%{_datadir}/themes/*/metacity-1/
%{_datadir}/themes/*/xfwm4/
%dir %{_datadir}/themes/*/

%files -n flat-remix-gtk2-theme
%license LICENSE
%doc README.md CHANGELOG
%{_datadir}/themes/*/gtk-2.0/
%dir %{_datadir}/themes/*/

%files -n flat-remix-gtk3-theme
%license LICENSE
%doc README.md CHANGELOG
%{_datadir}/themes/*/gtk-3.0/
%dir %{_datadir}/themes/*/

%files -n flat-remix-gtk4-theme
%license LICENSE
%doc README.md CHANGELOG
%{_datadir}/themes/*/gtk-4.0/
%{_datadir}/themes/Flat-Remix-LibAdwaita-*/*
%dir %{_datadir}/themes/*/


%changelog
%autochangelog
