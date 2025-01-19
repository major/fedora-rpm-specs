Name:           numberstation
Version:        1.4.0
Release:        2%{?dist}
Summary:        TOTP Authenticator application
License:        GPL-3.0-or-later
URL:            https://sr.ht/~martijnbraam/%{name}/
Source0:        https://git.sr.ht/~martijnbraam/%{name}/archive/%{version}.tar.gz
Requires:       libhandy
Requires:       python3-gobject
Requires:       python3-keyring
Requires:       python3-pyotp
Requires:       hicolor-icon-theme
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  git
BuildRequires:  libhandy-devel
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
%{summary}

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.postmarketos.Numberstation.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.postmarketos.Numberstation.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_metainfodir}/org.postmarketos.Numberstation.appdata.xml
%{_datadir}/applications/org.postmarketos.Numberstation.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.postmarketos.Numberstation.svg
%{_datadir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 23 2024 Tomi Lähteenmäki <lihis@lihis.net> - 1.4.0-1
- Update to v1.4.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Tomi Lähteenmäki <lihis@lihis.net> - 1.3.0-1
- Update to v1.3.0

* Thu Feb 02 2023 Tomi Lähteenmäki <lihis@lihis.net> - 1.2.0-4
- Fix review comments (bugzilla #2151289)

* Thu Jan 19 2023 Tomi Lähteenmäki <lihis@lihis.net> - 1.2.0-3
- Fix directory ownership

* Thu Jan 19 2023 Tomi Lähteenmäki <lihis@lihis.net> - 1.2.0-2
- Fix review comments (see: https://bugzilla.redhat.com/show_bug.cgi?id=2151289#c3)

* Mon Nov 28 2022 Tomi Lähteenmäki <lihis@lihis.net> - 1.2.0-1
- Initial version of the package
