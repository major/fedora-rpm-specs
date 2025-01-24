Name:    qtxdg-tools
Summary: User tools for libqtxdg
Version: 4.1.0
Release: 3%{?dist}
License: LGPL-2.0-or-later
URL:     https://lxqt-project.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: pkgconfig(Qt6Xdg)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: cmake(Qt6Core)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: gcc-c++

%description
%{summary}.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/qtxdg-mat
%{_datadir}/cmake/qtxdg-tools/

%changelog
* Wed Jan 22 2025 Steve Cossette <farchord@gmail.com> - 4.1.0-3
- Rebuild for Qt update

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Steve Cossette <farchord@gmail.com> - 4.1.0-1
- 4.1.0

* Wed Apr 17 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Zamir SUN <sztsian@gmail.com> - 3.12.0-1
- Update version to 3.12.0

* Fri Jul 28 2023 Zamir SUN <sztsian@gmail.com> - 3.11.0-1
- Update version to 3.11.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Zamir SUN <sztsian@gmail.com> - 3.10.0-1
- Initial version
