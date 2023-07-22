%{!?docs: %global docs 1}

%if 0%{?flatpak}
%global docs 0
%endif

%global libver 6

Name:           kweathercore
Version:        0.7
Release:        3%{?dist}
License:        LGPLv2+
Summary:        Library to facilitate retrieval of weather information
Url:            https://invent.kde.org/libraries/kweathercore
Source0:        https://download.kde.org/stable/kweathercore/%{version}/%{name}-%{version}.tar.xz
                

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Holidays)


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
BuildRequires:  qt5-doctools
BuildRequires:  qt5-qttools-libs-help
BuildArch: noarch

%description docs
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf5 \
  %if 0%{?flatpak}
  %{?docs:-DBUILD_QCH:BOOL=OFF} \
  %else
  %{?docs:-DBUILD_QCH:BOOL=ON} \
  %endif

%cmake_build

%install
%cmake_install


%files
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5KWeatherCore.so.%{version}.0
%{_kf5_libdir}/libKF5KWeatherCore.so.5

%files devel
%license LICENSES/*.txt
%{_kf5_includedir}/KWeatherCore/
%{_kf5_libdir}/cmake/KF5KWeatherCore/
%{_kf5_includedir}/kweathercore_version.h
%{_kf5_libdir}/libKF5KWeatherCore.so
%{_kf5_archdatadir}/mkspecs/modules/qt_KWeatherCore.pri


%if 0%{?docs}
%files docs
%doc README.md
%license LICENSES/*.txt
%{_qt5_docdir}/KF5KWeatherCore.qch
%{_qt5_docdir}/KF5KWeatherCore.tags
%endif

%changelog
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
