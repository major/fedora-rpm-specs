Name:           gnome-themes-extra
Version:        3.28
Release:        22%{?dist}
Summary:        GNOME Extra Themes

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://gitlab.gnome.org/GNOME/gnome-themes-extra
Source0:        https://download.gnome.org/sources/%{name}/3.28/%{name}-%{version}.tar.xz
Source1:        gtkrc

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  /usr/bin/gtk-update-icon-cache

Recommends: (adwaita-gtk2-theme = %{version}-%{release} if gtk2)
Requires: adwaita-icon-theme
Requires: highcontrast-icon-theme = %{version}-%{release}

# Renamed in F28
Obsoletes: gnome-themes-standard < 3.28
Provides: gnome-themes-standard = %{version}-%{release}
Provides: gnome-themes-standard%{_isa} = %{version}-%{release}

%description
This module houses themes and theme-y tidbits that don’t really fit in anywhere
else, or deserve their own module. At the moment this consists of:

 * The GTK+ 2 version of Adwaita
 * Adwaita-dark as a separate theme, along with its GTK+ 2 equivalent
 * GTK+ 2 versions of the HighContrast themes
 * The legacy HighContrast icon theme
 * Index files needed for Adwaita to be used outside of GNOME

Once named gnome-themes-standard, this module used to contain various
components of the default GNOME 3 theme. However, at this point, most it has
moved elsewhere. The GTK+ 3 versions of the Adwaita and HighContrast themes are
now part of GTK+ 3 itself, and the HighContrastInverse and LowConstrast themes
have been discontinued.

Not to be confused with gnome-themes-extras.

%package -n adwaita-gtk2-theme
Summary: Adwaita gtk2 theme
Requires: gtk2%{_isa}
# cursor and icon themes required for the theme
Requires: adwaita-cursor-theme
Requires: adwaita-icon-theme
Requires: highcontrast-icon-theme = %{version}-%{release}

%description -n adwaita-gtk2-theme
The adwaita-gtk2-theme package contains a gtk2 theme for presenting widgets
with a GNOME look and feel.

%package -n highcontrast-icon-theme
Summary: HighContrast icon theme
BuildArch: noarch
# Split out to a new subpackage in gnome-themes-standard 3.28-12
Conflicts: gnome-themes-standard < 3.28-12

%description -n highcontrast-icon-theme
This package contains the HighContrast icon theme used by the GNOME desktop.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/HighContrast/icon-theme.cache
touch $RPM_BUILD_ROOT%{_datadir}/icons/HighContrast/icon-theme.cache

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-2.0
cp -a $RPM_SOURCE_DIR/gtkrc $RPM_BUILD_ROOT%{_datadir}/gtk-2.0/gtkrc

%transfiletriggerin -n highcontrast-icon-theme -- %{_datadir}/icons/HighContrast
gtk-update-icon-cache --force %{_datadir}/icons/HighContrast &>/dev/null || :

%transfiletriggerpostun -n highcontrast-icon-theme -- %{_datadir}/icons/HighContrast
gtk-update-icon-cache --force %{_datadir}/icons/HighContrast &>/dev/null || :

%files
%license LICENSE
%doc NEWS README.md
%{_datadir}/themes/Adwaita/gtk-3.0/
%{_datadir}/themes/Adwaita-dark/gtk-3.0/
%{_datadir}/themes/HighContrast/gtk-3.0/

%files -n highcontrast-icon-theme
%license LICENSE
%dir %{_datadir}/icons/HighContrast
%{_datadir}/icons/HighContrast/16x16/
%{_datadir}/icons/HighContrast/22x22/
%{_datadir}/icons/HighContrast/24x24/
%{_datadir}/icons/HighContrast/32x32/
%{_datadir}/icons/HighContrast/48x48/
%{_datadir}/icons/HighContrast/256x256/
%{_datadir}/icons/HighContrast/scalable/
%{_datadir}/icons/HighContrast/index.theme
%ghost %{_datadir}/icons/HighContrast/icon-theme.cache

%files -n adwaita-gtk2-theme
%license LICENSE
%{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.so
%{_datadir}/gtk-2.0/gtkrc
%dir %{_datadir}/themes/Adwaita
%{_datadir}/themes/Adwaita/gtk-2.0/
%{_datadir}/themes/Adwaita/index.theme
%dir %{_datadir}/themes/Adwaita-dark
%{_datadir}/themes/Adwaita-dark/gtk-2.0/
%{_datadir}/themes/Adwaita-dark/index.theme
%dir %{_datadir}/themes/HighContrast
%{_datadir}/themes/HighContrast/gtk-2.0/
%{_datadir}/themes/HighContrast/index.theme

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.28-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Kalev Lember <klember@redhat.com> - 3.28-12
- Split highcontrast-icon-theme out to a new subpackage
- Explicitly require cursor and icon themes required for the gtk2 themes

* Mon Feb 08 2021 Kalev Lember <klember@redhat.com> - 3.28-11
- Make adwaita-gtk2-theme recommends conditional on gtk2 being installed

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.28-5
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Pete Walter <pwalter@fedoraproject.org> - 3.28-4
- Drop font requires

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Pete Walter <pwalter@fedoraproject.org> - 3.28-1
- Rename gnome-themes-standard to gnome-themes-extra
