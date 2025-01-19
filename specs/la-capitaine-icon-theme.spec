%global giturl https://github.com/keeferrourke/%{name}
%global themename La-Capitaine

Name: la-capitaine-icon-theme
Version: 0.6.2
Release: 11%{?dist}
Summary: Icon pack designed to integrate with most desktop environments
BuildArch: noarch

# For a breakdown of the licensing, see COPYING and LICENSE
# Automatically converted from old format: GPLv3+ and MIT - review is highly recommended.
License: GPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL: https://krourke.org/projects/art/la-capitaine-icon-theme
Source0: %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: redhat-lsb-core

Requires: adwaita-icon-theme
Requires: gnome-icon-theme
Requires: hicolor-icon-theme

%description
La Capitaine is an icon pack — designed to integrate with most desktop
environments. The set of icons takes inspiration from the latest iterations of
macOS and Google's Material Design through the use of visually pleasing
gradients, shadowing, and simple icon geometry.


%prep
%autosetup -p1


%build
%configure


%install
mkdir -p %{buildroot}%{_datadir}/icons/%{themename}
cp -rp actions %{buildroot}%{_datadir}/icons/%{themename}
cp -rp animations %{buildroot}%{_datadir}/icons/%{themename}
cp -rp apps %{buildroot}%{_datadir}/icons/%{themename}
cp -rp devices %{buildroot}%{_datadir}/icons/%{themename}
cp -rp emblems %{buildroot}%{_datadir}/icons/%{themename}
cp -rp emotes %{buildroot}%{_datadir}/icons/%{themename}
cp -rp mimetypes %{buildroot}%{_datadir}/icons/%{themename}
cp -rp panel %{buildroot}%{_datadir}/icons/%{themename}
cp -rp places %{buildroot}%{_datadir}/icons/%{themename}
cp -rp status %{buildroot}%{_datadir}/icons/%{themename}
install -Dpm0644 index.theme %{buildroot}%{_datadir}/icons/%{themename}/index.theme

touch %{buildroot}%{_datadir}/icons/%{themename}/icon-theme.cache

# Remove executable bit
chmod -x %{buildroot}%{_datadir}/icons/%{themename}/apps/scalable/org.gabmus.hydrapaper.svg

%transfiletriggerin -- %{_datadir}/icons/%{themename}
gtk-update-icon-cache --force %{_datadir}/icons/%{themename} &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{themename}
gtk-update-icon-cache --force %{_datadir}/icons/%{themename} &>/dev/null || :


%files
%license COPYING LICENSE
%doc README.md Credits.md Thanks.md
%{_datadir}/icons/%{themename}/actions/
%{_datadir}/icons/%{themename}/animations/
%{_datadir}/icons/%{themename}/apps/
%{_datadir}/icons/%{themename}/devices/
%{_datadir}/icons/%{themename}/emblems/
%{_datadir}/icons/%{themename}/emotes/
%{_datadir}/icons/%{themename}/index.theme
%{_datadir}/icons/%{themename}/mimetypes/
%{_datadir}/icons/%{themename}/panel/
%{_datadir}/icons/%{themename}/places/
%{_datadir}/icons/%{themename}/status/
%dir %{_datadir}/icons/%{themename}
%ghost %{_datadir}/icons/%{themename}/icon-theme.cache


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.2-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 25 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.2-1
- build(update): 0.6.2

* Sat Apr 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-12.20210424gitd49ef94
- build(update): d49ef94 commit

* Sat Apr 17 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-11.20210331git1add5ba
- build(update): 1add5ba commit
  fix: RH#1950614

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10.20200922git9564606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-9.20200922git9564606
- Update to latest git snapshot
- build: remove fdupes

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8.20200414git36b9768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-7.20200414git36b9768
- Update to latest git snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6.20200105git90b4015
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-5.20200105git90b4015
- Update to latest git snapshot

* Fri Sep 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-4.20190904gitef79681
- Update to latest git snapshot

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3.20190418gitbc48265
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-2.20190418gitbc48265
- Initial package
