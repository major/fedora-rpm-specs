Name:           budgie-backgrounds
Version:        3.0
Release:        4%{?dist}
Summary:        Default set of background images for the Budgie Desktop

License:        CC0-1.0
URL:            https://github.com/BuddiesOfBudgie/budgie-backgrounds
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:        https://serebit.com/openpgp/git-at-serebit-dot-com.asc

BuildArch:      noarch
BuildRequires:  ImageMagick
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  jhead
BuildRequires:  meson

%description
Default set of background images for the Budgie Desktop.

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
%dir %{_datadir}/backgrounds/budgie
%dir %{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/budgie/*.jpg
%{_datadir}/gnome-background-properties/%{name}.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 17 2024 Joshua Strobl <me@joshuastrobl.com> - 3.0-2
- Fix sources

* Sun Mar 17 2024 Joshua Strobl <me@joshuastrobl.com> - 3.0-1
- Update to 3.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 4 2023 Joshua Strobl <me@joshuastrobl.com> - 1.0-1
- Initial inclusion of Budgie Backgrounds
