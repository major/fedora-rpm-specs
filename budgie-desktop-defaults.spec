Name:           budgie-desktop-defaults
Version:        0.5.1
Release:        3%{?dist}
Summary:        Budgie Desktop Defaults for Fedora

License:        CC-BY-SA-4.0
URL:            https://github.com/BuddiesOfBudgie/fedora-budgie-desktop-defaults
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:        https://joshuastrobl.com/pubkey.gpg

BuildArch:      noarch
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
Requires:       budgie-backgrounds
Requires:       budgie-desktop
Requires:       desktop-backgrounds-budgie
Requires:       materia-gtk-theme
Requires:       papirus-icon-theme
Requires:       slick-greeter


%description
Budgie Desktop Defaults for Fedora.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/glib-2.0/schemas
%{_datadir}/glib-2.0/schemas/10_budgie_*.gschema.override

%changelog
* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 6 2023 Joshua Strobl <me@joshuastrobl.com> - 0.5.1-1
- Update to 0.5.1 for schema rename and background removal

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 17 2023 Joshua Strobl <me@joshuastrobl.com> - 0.4-1
- Update to 0.4 for gedit color scheme change

* Sun Feb 5 2023 Joshua Strobl <me@joshuastrobl.com> - 0.3-1
- Initial inclusion of Budgie Desktop Defaults for Fedora 
