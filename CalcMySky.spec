Name: CalcMySky
Version:  0.1.0
Release:  2%{?dist}
Summary: Simulator of light scattering by planetary atmospheres 

License: GPL-3.0-only
URL: https://github.com/10110111/CalcMySky
Source0: https://github.com/10110111/CalcMySky/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: 45a3541d55f3dca27da6fbca3ba2f03349bd45bd.patch
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: glm-devel
BuildRequires: qt5-qtbase-devel
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

%patch0 -p1

%build

%cmake
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
%{_libdir}/libShowMySky.so.0*

%files devel
%{_libdir}/ShowMySky/
%{_libdir}/libShowMySky.so
%{_includedir}/ShowMySky/


%changelog
* Thu Oct 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.1.0-2
- Review fixes.

* Mon Oct 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.1.0-1
- Initial build
