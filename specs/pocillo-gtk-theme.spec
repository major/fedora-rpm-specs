%global _description %{expand:
Pocillo is a Material Design theme for the Budgie Desktop.}

Name:           pocillo-gtk-theme
Version:        0.13.0
Release:        1%{?dist}
Summary:        Pocillo is a Material Design theme for the Budgie Desktop
BuildArch:      noarch

License:        GPL-2.0-or-later
URL:            https://github.com/UbuntuBudgie/pocillo-gtk-theme
Source0:        %{url}/releases/download/v%{version}/pocillo-precompiled-papirus.tar.gz#/%{name}-%{version}-precompiled.tar.gz

Requires: (pocillo-gtk3-theme if gtk3)
Requires: (pocillo-gtk4-theme if gtk4)
Requires: (pocillo-labwc-theme if labwc)

Obsoletes: pocillo-gtk2-theme < 0.11-2
Obsoletes: pocillo-plank-theme < 0.11-2

%description %{_description}

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

%package -n pocillo-labwc-theme
Summary:        Labwc support for the Pocillo GTK theme

Recommends:     pocillo-gtk-theme
Obsoletes:      pocillo-openbox-theme < 0.11-2
Provides:       pocillo-openbox-theme = %{version}-%{release}

%description -n pocillo-labwc-theme %{_description}

This package contains the Pocillo labwc theme.

%prep
%autosetup -c
mv usr/share/themes/Pocillo/COPYING .
rm -rf usr/share/themes/Pocillo*/COPYING
rm -rf usr/share/themes/Pocillo*/INSTALL_GDM_THEME.md

%build

%install
mkdir -p %{buildroot}%{_datadir}/themes/
cp -R usr/share/themes/Pocillo* %{buildroot}%{_datadir}/themes/

%files
%license COPYING
%{_datadir}/themes/Pocillo*/index.theme

%files -n pocillo-gtk3-theme
%license COPYING
%dir %{_datadir}/themes/Pocillo*/gtk-3.0
%{_datadir}/themes/Pocillo*/gtk-3.0/*

%files -n pocillo-gtk4-theme
%license COPYING
%dir %{_datadir}/themes/Pocillo*/gtk-4.0
%{_datadir}/themes/Pocillo*/gtk-4.0/*

%files -n pocillo-labwc-theme
%license COPYING
%dir %{_datadir}/themes/Pocillo*/labwc
%{_datadir}/themes/Pocillo*/labwc/*

%changelog
* Mon Sep 28 2026 Joshua Strobl <me@joshuastrobl.com> - 0.13.0-1
- Update to 0.13.0

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jun 01 2025 Joshua Strobl <me@joshuastrobl.com> - 0.11-1
- Initial packaging of Pocillo
