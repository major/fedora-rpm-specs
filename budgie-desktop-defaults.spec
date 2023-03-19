Name:           budgie-desktop-defaults
Version:        0.4
Release:        1%{?dist}
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
Requires:       materia-gtk-theme
Requires:       papirus-icon-theme
Requires:       slick-greeter


%description
Budgie Desktop Defaults for Fedora .

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
%{_datadir}/glib-2.0/schemas/90_budgie_*.gschema.override

%changelog
* Fri Mar 17 2023 Joshua Strobl <me@joshuastrobl.com> - 0.4-1
- Update to 0.4 for gedit color scheme change

* Sun Feb 5 2023 Joshua Strobl <me@joshuastrobl.com> - 0.3-1
- Initial inclusion of Budgie Desktop Defaults for Fedora 
