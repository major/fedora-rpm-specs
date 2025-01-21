%global commit      2d8102084eaf194f04076ec6949feacb0eb4a1ba
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20180927

Name:           suru-icon-theme
Version:        0
Release:        16.%{date}git%{shortcommit}%{?dist}
Summary:        Suru icon and cursor set

# For a breakdown of the licensing, see COPYING LICENSE_CCBYSA LICENSE_GPL3
# Automatically converted from old format: GPLv3 and CC-BY-SA - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-CC-BY-SA
URL:            https://snwh.org/suru
Source0:        https://github.com/snwh/suru-icon-theme/tarball/%{commit}#/%{name}-%{version}%{date}git%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  meson

Requires:       adwaita-icon-theme
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
This project is a revitalization of the Suru icon set that was designed for
Ubuntu Touch. The principles and styles created for Suru now serve as the basis
for a new FreeDesktop icon theme.

%prep
%autosetup -n snwh-%{name}-%{shortcommit}

%build
%meson
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}%{_datadir}
touch %{buildroot}/%{_datadir}/icons/Suru/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/Suru
gtk-update-icon-cache --force %{_datadir}/icons/Suru &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/Suru
gtk-update-icon-cache --force %{_datadir}/icons/Suru &>/dev/null || :

%files
%doc AUTHORS README.md CONTRIBUTING.md
%license COPYING LICENSE_CCBYSA LICENSE_GPL3
%{_datadir}/icons/Suru
%ghost %{_datadir}/icons/Suru/icon-theme.cache

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 4 2024 Miroslav Suchý <msuchy@redhat.com> - 0-15.20180927git2d81020
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-3.20180927git2d81020
- Update spec file

* Thu Jul 12 2018 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20180927git2d81020
- Initial package
