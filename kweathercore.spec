%bcond docs %{undefined flatpak}

Name:           kweathercore
Version:        0.8.0
Release:        2%{?dist}
License:        LGPLv2+
Summary:        Library to facilitate retrieval of weather information
Url:            https://invent.kde.org/libraries/kweathercore
Source0:        https://download.kde.org/stable/kweathercore/%{version}/%{name}-%{version}.tar.xz
                

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Holidays)


%description
Get weather forecast and alerts anywhere on the earth easy. KWeatherCore
provides you a highly abstracted library for things related to weather:
Get local weather forecast, get weather of a location by name or coordinate,
get sunrise/set moonrise/set and many more informations about a location.

%package devel
Summary:        Development headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildRequires:  doxygen
BuildRequires:  qt6-doctools
BuildRequires:  qt6-qttools-libs-help
BuildArch: noarch

%description docs
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf6 \
  -DBUILD_QCH:BOOL=%{?with_docs:ON}%{!?with_docs:OFF}

%cmake_build

%install
%cmake_install

%find_lang kweathercore6


%files -f kweathercore6.lang
%license LICENSES/*.txt
%{_kf6_libdir}/libKWeatherCore.so.%{version}
%{_kf6_libdir}/libKWeatherCore.so.6

%files devel
%license LICENSES/*.txt
%{_includedir}/KWeatherCore/
%{_includedir}/kweathercore_version.h
%{_kf6_libdir}/cmake/KWeatherCore/
%{_kf6_libdir}/libKWeatherCore.so
%{_kf6_archdatadir}/mkspecs/modules/qt_KWeatherCore.pri


%if %{with docs}
%files docs
%doc README.md
%license LICENSES/*.txt
%{_qt6_docdir}/KWeatherCore.qch
%{_qt6_docdir}/KWeatherCore.tags
%endif

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 0.8.0-1
- 0.8.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 0.7-1
- Update to 0.7

* Tue Sep 20 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.6-1
- version bump 0.6

* Tue Sep 20 2022 Justin Zobel <justin@1707.io> - 0.5-4
- Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.5-1
- version bump 0.5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-3
-  Clean up un needed command from build process 

* Sat Jul 17 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-2
-  KF5_VERSION changed to 0.3.0 for kweather

* Wed May 5 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-1
- initial version of package
