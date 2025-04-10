Name:           adw-gtk3-theme
Version:        5.8
Release:        %autorelease
Summary:        The theme from libadwaita ported to GTK-3
BuildArch:      noarch

License:        LGPL-2.1-only
URL:            https://github.com/lassekongo83/adw-gtk3
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  sassc
BuildRequires:  meson
BuildRequires:  fdupes

%description
%{summary}.


%prep
%autosetup -n adw-gtk3-%{version}

%build
%meson
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}

%files
%license LICENSE
%doc README.md
%{_datadir}/themes/adw-gtk3/
%{_datadir}/themes/adw-gtk3-dark/

%changelog
%autochangelog
