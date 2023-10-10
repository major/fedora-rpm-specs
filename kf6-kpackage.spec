%global gitdate 20231003.152541
%global cmakever 5.240.0
%global commit0 40b9c7e7b5e66df8b6f9d2846284e0f6f426855b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kpackage

Name:           kf6-%{framework}
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 library to load and install packages as plugins

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:  https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-karchive-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  qt6-qtbase-devel
Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 2 library to load and install non-binary packages as
if they were plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-man

# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/kpackage/packagestructure/
mkdir -p %{buildroot}%{_kf6_datadir}/kpackage/

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Package.so.*
%{_kf6_qtplugindir}/kpackage/
%{_kf6_datadir}/kpackage/
%{_kf6_bindir}/kpackagetool6
%{_mandir}/man1/kpackagetool6.1*

%files devel
%{_kf6_includedir}/KPackage/
%{_kf6_libdir}/libKF6Package.so
%{_kf6_libdir}/cmake/KF6Package/


%changelog
* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.152541.40b9c7e-1
- Initial Release
