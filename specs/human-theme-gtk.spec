Name:          human-theme-gtk
Version:       2.2.0
Release:       3%{?dist}
Summary:       Human theme for GTK
Summary(fr):   Thème Human pour GTK
License:       GPLv3+ and LGPLv2+ and CC-BY-SA
URL:           https://github.com/luigifab/human-theme
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: aspell-fr
Recommends:    dmz-cursor-themes
Recommends:    gnome-icon-theme
Recommends:    gtk-murrine-engine

%description %{expand:
This theme works with GTK 2.24 (with gtk-murrine-engine),
3.24, and 4.12. Better rendering with Pango 1.42- or 1.51+.

It is mainly intended for Mate and Xfce Desktop Environments.

After installation you must restart your session.}

%description -l fr %{expand:
Ce thème fonctionne avec : GTK 2.24 (avec gtk-murrine-engine),
3.24, et 4.12. Meilleur rendu avec Pango 1.42- ou 1.51+.

Il est principalement destiné pour les environnements de bureau Mate et Xfce.

Après l'installation vous devez redémarrer votre session.}


%prep
%setup -q -n human-theme-%{version}
sed -i 's/IconTheme=gnome/IconTheme=mate/g' src/*/index.theme

%install
mkdir -p %{buildroot}/etc/profile.d/
install -pm 644 debian/profile.sh %{buildroot}/etc/profile.d/%{name}.sh
mkdir -p %{buildroot}%{_datadir}/themes/
cp -a src/human-theme/        %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-blue/   %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-green/  %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-orange/ %{buildroot}%{_datadir}/themes/

%files
%config(noreplace) /etc/profile.d/%{name}.sh
%license LICENSE
%doc README.md
# the entire source code is GPL-3+, except metacity-1/* which is LGPL-2.1+, and gtk-2.0/* which is CC-BY-SA-3.0+
%{_datadir}/themes/human-theme/
%{_datadir}/themes/human-theme-blue/
%{_datadir}/themes/human-theme-green/
%{_datadir}/themes/human-theme-orange/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 02 2024 Fabrice Creuzot <code@luigifab.fr> - 2.2.0-1
- New upstream release

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Fabrice Creuzot <code@luigifab.fr> - 2.1.0-1
- New upstream release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Fabrice Creuzot <code@luigifab.fr> - 2.0.0-2
- Package spec update

* Tue Jun 06 2023 Fabrice Creuzot <code@luigifab.fr> - 2.0.0-1
- New upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 09 2021 Fabrice Creuzot <code@luigifab.fr> - 1.5.0-1
- New upstream version

* Wed Jul 07 2021 Fabrice Creuzot <code@luigifab.fr> - 1.4.0-1
- New upstream version

* Wed May 05 2021 Fabrice Creuzot <code@luigifab.fr> - 1.3.0-1
- New upstream version

* Sun Apr 04 2021 Fabrice Creuzot <code@luigifab.fr> - 1.2.0-1
- New upstream version

* Wed Nov 11 2020 Fabrice Creuzot <code@luigifab.fr> - 1.1.0-1
- Initial Fedora package release (Closes: rhbz#1893327)
