Name:           labwc-menu-generator
Version:        0.1.0
Release:        3%{?dist}
Summary:        Menu generator for labwc

# Tests are GPL-2.0-or-later
SourceLicense:  GPL-2.0-only AND GPL-2.0-or-later
License:        GPL-2.0-only
URL:            https://github.com/labwc/labwc-menu-generator
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  /usr/bin/prove
BuildRequires:  scdoc
Supplements:    labwc


%description
%{summary}.


%prep
%autosetup -n %{name}-%{version}


%build
%meson
%meson_build


%install
%meson_install

%check
%meson_test


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/labwc-menu-generator.1.gz


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 20 2024 Steve Cossette <farchord@gmail.com> - 0.1.0-2
- Fixed a packaging issue with disabling debug packages

* Tue Aug 20 2024 Steve Cossette <farchord@gmail.com> - 0.1.0-1
- 0.1.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20231031.d7c8107-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20231031.d7c8107-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20231031.d7c8107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 23 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20231031.d7c8107-1
- Initial package
