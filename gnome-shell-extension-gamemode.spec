Name:           gnome-shell-extension-gamemode
Version:        8
Release:        3%{?dist}
Summary:        GameMode integration for GNOME Shell
License:        LGPLv2
URL:            https://github.com/gicmo/gamemode-extension
Source0:        %{url}/archive/v%{version}/gamemode-extension-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gettext >= 0.19.6
Requires:       gnome-shell >= 3.38
Suggests:       gamemode
BuildArch:      noarch

%description
GNOME Shell extension to integrate with GameMode. Can display
an icon when GameMode is active and also emit notifications
when the global GameMode status changes.


%prep
%autosetup -p1 -n gamemode-extension-%{version}%{?prerelease:-%{prerelease}}


%build
%meson
%meson_build


%install
%meson_install

%find_lang gamemode-extension


%files -f gamemode-extension.lang
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/gamemode*/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.gamemode.gschema.xml


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 09 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 8-1
- Upstream release 8

* Thu Sep 15 2022 Vladimir Ulrich <wedmer@gmail.com> - 7-1
- Upstream release 7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Christian Kellner <christian@kellner.me> - 6-1
- Upstream release 6

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Christian Kellner <christian@kellner.me> - 1-1
- Initial package
  Resolves rhbz#1725103
- Include patche to adapt for GNOME Shell 3.33 API changes.

