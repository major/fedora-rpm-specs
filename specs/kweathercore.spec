Name:           kweathercore
Version:        24.12.1
Release:        1%{?dist}
License:        LGPL-2.0-or-later
Summary:        Library to facilitate retrieval of weather information
Url:            https://invent.kde.org/libraries/kweathercore
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
                

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


%package        doc
Summary:        Developer Documentation files for %{name}
Obsoletes:      kweathercore-docs < 0.8.0-4
BuildArch:      noarch

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang kweathercore6


%files -f kweathercore6.lang
%license LICENSES/*.txt
%{_kf6_libdir}/libKWeatherCore.so.*.*
%{_kf6_libdir}/libKWeatherCore.so.6

%files devel
%license LICENSES/*.txt
%{_includedir}/KWeatherCore/
%{_includedir}/kweathercore_version.h
%{_kf6_libdir}/cmake/KWeatherCore/
%{_kf6_libdir}/libKWeatherCore.so
%{_kf6_archdatadir}/mkspecs/modules/qt_KWeatherCore.pri
%{_qt6_docdir}/KWeatherCore.tags

%files doc
%{_qt6_docdir}/KWeatherCore.qch


%changelog
* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Wed Aug 14 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.07.90-1
- 24.07.90

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 10 2024 Marie Loise Nolden <loise@kde.org> - 0.8.0-4
- convert -docs package to -doc for API documentation automatically generated now
- SPDX license notice

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

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
