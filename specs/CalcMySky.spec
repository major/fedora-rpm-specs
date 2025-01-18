Name: CalcMySky
Version:  0.3.3
Release:  2%{?dist}
Summary: Simulator of light scattering by planetary atmospheres 

License: GPL-3.0-only
URL: https://github.com/10110111/CalcMySky
Source0: https://github.com/10110111/CalcMySky/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: glm-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: eigen3-devel

%package devel
Summary: Development files for CalcMySky
Requires: %{name}%{?_isa} = %{version}-%{release}

%description
CalcMySky is a software package that simulates scattering of light by the
atmosphere to render daytime and twilight skies (without stars). Its primary
purpose is to enable realistic view of the sky in applications such as
planetaria. Secondary objective is to make it possible to explore
atmospheric effects such as glories, fogbows etc., as well as simulate
unusual environments such as on Mars or an exoplanet orbiting a star with
a non-solar spectrum of radiation.

%description devel
CalcMySky is a software package that simulates scattering of light by the
atmosphere to render daytime and twilight skies (without stars). Its primary
purpose is to enable realistic view of the sky in applications such as
planetaria. Secondary objective is to make it possible to explore
atmospheric effects such as glories, fogbows etc., as well as simulate
unusual environments such as on Mars or an exoplanet orbiting a star with
a non-solar spectrum of radiation.

These are the development files.

%prep
%setup -q

%build

%cmake -DQT_VERSION=6
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.mdown doc/
%license COPYING
%{_bindir}/calcmysky
%{_bindir}/showmysky
%{_datadir}/CalcMySky/
%{_libdir}/libShowMySky-Qt6.so.15*

%files devel
%{_libdir}/cmake/ShowMySky-Qt6/
%{_libdir}/libShowMySky-Qt6.so
%{_includedir}/ShowMySky/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.3.3-1
- 0.3.3

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-1
- 0.3.2

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.3.1-1
- 0.3.1

* Wed Mar 29 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.3.0-1
- 0.3.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.2.1-1
- 0.2.1

* Thu Oct 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.1.0-2
- Review fixes.

* Mon Oct 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.1.0-1
- Initial build
