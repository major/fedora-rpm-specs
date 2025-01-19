%global commit      c0355ea31e5cfdb6b44d8108f602d66817546a09
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190530

%global tname       Moka

Name:           moka-icon-theme
Version:        5.4.0
Release:        15.%{date}git%{shortcommit}%{?dist}
Summary:        Moka Icon Theme

# Automatically converted from old format: CC-BY-SA and GPLv3 - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA AND GPL-3.0-only
URL:            https://snwh.org/moka
Source0:        https://github.com/snwh/%{name}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  meson
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
Moka is a stylized FreeDesktop icon set, created with simplicity in mind.
It uses simple geometry & bright colours and has been designed and optimized to
achieve the a pixel-perfect look for your desktop.

Also, one of the most comprehensive icon sets available, Moka provides thousands
of icons for many applications. So no matter which Linux desktop you are using,
Moka has you covered.


%prep
%autosetup -p1 -n %{name}-%{commit}
chmod 644 COPYING LICENSE_CC-BY-SA LICENSE_GPL \
    README.md AUTHORS CONTRIBUTING.md


%build
%meson
%meson_build


%install
%meson_install
chmod -x %{buildroot}%{_datadir}/icons/%{tname}/index.theme


%transfiletriggerin -- %{_datadir}/icons/%{tname}
gtk-update-icon-cache --force %{_datadir}/icons/%{tname} &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}
gtk-update-icon-cache --force %{_datadir}/icons/%{tname} &>/dev/null || :


%files
%license COPYING LICENSE_CC-BY-SA LICENSE_GPL
%doc README.md AUTHORS CONTRIBUTING.md
%{_datadir}/icons/%{tname}
%ghost %{_datadir}/icons/%{tname}/icon-theme.cache


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-15.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 5.4.0-14.20190530gitc0355ea
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-13.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-12.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-11.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-10.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-9.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-8.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-7.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-6.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-5.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-4.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 5.4.0-2.20190530gitc0355ea
- Minor packaging fixes

* Tue Sep 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 5.4.0-1.20190530gitc0355ea
- Update to latest git snapshot
- Switch to Meson build system
- Packaging fixes

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep  4 2017 Allisson Azevedo <allisson@gmail.com> - 5.3.6-1
- Initial RPM release
