%global _description %{expand:
Pocillo is a Material Design theme for the Budgie Desktop.}

Name:           pocillo-gtk-theme
Version:        0.11
Release:        1%{?dist}
Summary:        Pocillo is a Material Design theme for the Budgie Desktop
BuildArch:      noarch

License:        GPL-2.0-or-later
URL:            https://github.com/UbuntuBudgie/pocillo-gtk-theme
Source0:        %{url}/releases/download/v%{version}/pocillo-precompiled.tar.gz#/%{name}-%{version}-precompiled.tar.gz

Requires: (pocillo-gtk2-theme if gtk2)
Requires: (pocillo-gtk3-theme if gtk3)
Requires: (pocillo-gtk4-theme if gtk4)
Requires: (pocillo-openbox-theme if openbox)
Requires: (pocillo-plank-theme if plank)

%description %{_description}

%package -n pocillo-gtk2-theme
Summary:        GTK+2 support for the Pocillo GTK theme
Requires:       gtk-murrine-engine

Recommends:     pocillo-gtk-theme

%description -n pocillo-gtk2-theme %{_description}

This package contains the Pocillo GTK+2 theme.

%package -n pocillo-gtk3-theme
Summary:        GTK3 support for the Pocillo GTK theme
Requires:       gtk3

Recommends:     pocillo-gtk-theme

%description -n pocillo-gtk3-theme %{_description}

This package contains the Pocillo GTK3 theme.

%package -n pocillo-gtk4-theme
Summary:        GTK4 support for the Pocillo GTK theme
Requires:       gtk4

Recommends:     pocillo-gtk-theme

%description -n pocillo-gtk4-theme %{_description}

This package contains the Pocillo GTK4 theme.

%package -n pocillo-openbox-theme
Summary:        Openbox support for the Pocillo GTK theme

Recommends:     pocillo-gtk-theme

%description -n pocillo-openbox-theme %{_description}

This package contains the Pocillo Openbox theme.

%package -n pocillo-plank-theme
Summary:        Plank support for the Pocillo GTK theme
Requires:       plank

Recommends:     pocillo-gtk-theme

%description -n pocillo-plank-theme  %{_description}

This package contains the Pocillo Plank theme.

%prep
%autosetup -c
mv Pocillo/COPYING .
rm -rf Pocillo-*/COPYING
rm -rf **/INSTALL_GDM_THEME.md

%build

%install
mkdir -p %{buildroot}%{_datadir}/themes/
cp -R Pocillo* %{buildroot}%{_datadir}/themes/

%files
%license COPYING
%dir %{_datadir}/themes/Pocillo*/chrome
%{_datadir}/themes/Pocillo*/chrome/*
%{_datadir}/themes/Pocillo*/index.theme

%files -n pocillo-gtk2-theme
%license COPYING
%dir %{_datadir}/themes/Pocillo*/gtk-2.0
%{_datadir}/themes/Pocillo*/gtk-2.0/*

%files -n pocillo-gtk3-theme
%license COPYING
%dir %{_datadir}/themes/Pocillo*/gtk-3.0
%{_datadir}/themes/Pocillo*/gtk-3.0/*

%files -n pocillo-gtk4-theme
%license COPYING
%dir %{_datadir}/themes/Pocillo*/gtk-4.0
%{_datadir}/themes/Pocillo*/gtk-4.0/*

%files -n pocillo-openbox-theme
%license COPYING
%dir %{_datadir}/themes/Pocillo*/openbox-3
%{_datadir}/themes/Pocillo*/openbox-3/*

%files -n pocillo-plank-theme
%license COPYING
%dir %{_datadir}/themes/Pocillo*/plank
%{_datadir}/themes/Pocillo*/plank/*

%changelog
* Sun Jun 01 2025 Joshua Strobl <me@joshuastrobl.com> - 0.11-1
- Initial packaging of Pocillo
