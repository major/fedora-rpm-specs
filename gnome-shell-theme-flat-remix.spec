%global vergit  20220622

Name:           gnome-shell-theme-flat-remix
Version:        0.0.%{vergit}
Release:        %autorelease
Summary:        Pretty simple theme inspired on material design
BuildArch:      noarch

License:        CC-BY-SA
URL:            https://drasite.com/flat-remix-gnome
Source:         https://github.com/daniruiz/flat-remix-gnome/archive/%{vergit}/%{name}-%{version}.tar.gz

# BuildRequires:  dconf
# BuildRequires:  glib2-devel
# BuildRequires:  make

Requires:       gnome-shell >= 42.0

Recommends:     flat-remix-gtk2-theme
Recommends:     flat-remix-gtk3-theme
Recommends:     flat-remix-gtk4-theme
Recommends:     flat-remix-icon-theme
Recommends:     flat-remix-theme

%description
Flat Remix GNOME theme is a pretty simple shell theme inspired on material
design following a modern design using "flat" colors with high contrasts and
sharp borders.

Themes:

  * Flat Remix
  * Flat Remix Dark
  * Flat Remix Darkest
  * Flat Remix Miami
  * Flat Remix Miami Dark

Variants:

  * Full Panel: No topbar spacing


%prep
%autosetup -n flat-remix-gnome-%{vergit}


%build
echo "Skip building for now. It's broken".
%dnl %make_build


%install
mkdir -p %{buildroot}%{_datadir}/themes/
cp -ap themes/Flat-Remix* %{buildroot}%{_datadir}/themes/


%files
%license LICENSE
%doc README.md CHANGELOG
%{_datadir}/themes/Flat-Remix-*/


%changelog
%autochangelog
