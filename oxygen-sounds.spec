%global kf5_version_min 5.98.0

Name:           oxygen-sounds
Version:        5.26.4
Release:        1%{?dist}
Summary:        The Oxygen Sound Theme

License:        LGPLv3+,CC0,BSD
URL:            https://invent.kde.org/plasma/oxygen-sounds

%global verdir %(echo %{version} | cut -d. -f1-3)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global majmin_ver %(echo %{version} | cut -d. -f1,2).50
%global stable unstable
%else
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{verdir}/%{name}-%{version}.tar.xz

Provides:       oxygen-sound-theme = %{version}-%{release}
Obsoletes:      oxygen-sound-theme <= 5.24.50

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros >= %{kf5_version_min}
BuildRequires:  qt5-qtbase-devel

BuildArch:      noarch

%description
%{summary}.


%prep
%autosetup

%build
%{cmake_kf5}
%{cmake_build}

%install
%{cmake_install}


%files
%license LICENSES/*.txt
%{_kf5_datadir}/sounds/Oxygen-*


%changelog
* Tue Nov 29 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.4-1
- 5.26.4

* Wed Nov 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.3.1-1
- 5.26.3.1

* Wed Oct 26 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.2-1
- 5.26.2

* Tue Oct 18 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.1-1
- 5.26.1

* Thu Oct 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.0-1
- 5.26.0

* Sat Sep 17 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.90-1
- 5.25.90

* Wed Sep 07 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.5-1
- 5.25.5

* Thu Aug 04 2022 Justin Zobel <justin@1707.io> - 5.25.4-1
- Update to 5.25.4

%autochangelog

