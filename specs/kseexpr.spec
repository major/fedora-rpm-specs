%global appname KSeExpr

Name: kseexpr
Version: 4.0.4.0
Release: 7%{?dist}

License: GPL-3.0-or-later
Summary: The embeddable expression engine fork for Krita
URL: https://invent.kde.org/graphics/%{name}
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)

BuildRequires: bison
BuildRequires: cmake
BuildRequires: extra-cmake-modules >= 5.52.0
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: sed

%description
Fork of Disney Animation's SeExpr expression library, that is used in Krita.

This fork was created as part of the GSoC 2020 project, Dynamic Fill Layers
in Krita using SeExpr, to enable the provision of fixes and translations
needed to embed SeExpr into the Krita painting suite.

This version is not ABI-compatible with projects using upstream SeExpr.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%cmake_kf5 -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_PREGENERATED_FILES:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/lib%{appname}*.so.4*

%files devel
%{_includedir}/%{appname}/
%{_includedir}/%{appname}UI/
%{_libdir}/cmake/%{appname}/
%{_libdir}/lib%{appname}*.so
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 26 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.4.0-1
- Initial SPEC release.
