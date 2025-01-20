Name:           regextester
Version:        1.1.1
Release:        10%{?dist}
Summary:        Regex Tester for elementary OS

# For license file: https://github.com/artemanufrij/regextester/issues/25
License:        GPL-2.0-or-later
URL:            https://github.com/artemanufrij/regextester
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         appdata.patch
Patch1:         regextester-appdata.patch

BuildRequires:  desktop-file-utils
BuildRequires:  vala vala-devel
BuildRequires:  granite-devel
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
Regex Tester for elementary OS


%prep
%setup -q

%patch -P0 -p0
%patch -P1 -p0

%build
%meson
%meson_build

%install
%meson_install

%find_lang com.github.artemanufrij.regextester

%check
%meson_test


%files -f com.github.artemanufrij.regextester.lang
%doc README.md
%{_bindir}/com.github.artemanufrij.regextester
%{_datadir}/applications/com.github.artemanufrij.regextester.desktop
%{_datadir}/com.github.artemanufrij.regextester/
%{_datadir}/metainfo/com.github.artemanufrij.regextester.appdata.xml
%{_datadir}/glib-2.0/schemas/com.github.artemanufrij.regextester.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.artemanufrij.regextester.*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-5
- Add --nonet to appdata validation

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-4
- BR libappstream-glib

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-3
- Relax appdata validation.

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-2
- Review fixes.

* Mon Feb 27 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-1
- Initial package.
