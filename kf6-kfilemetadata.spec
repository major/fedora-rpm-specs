%global gitdate 20231001.112804
%global cmakever 5.240.0
%global commit0 6fcc94b8139f055d960132a8cfbfd65a927b7370
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kfilemetadata

Name:           kf6-%{framework}
Summary:        A Tier 2 KDE Framework for extracting file metadata
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}

License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:  https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-karchive-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Config)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig(exiv2) >= 0.20
BuildRequires:  catdoc
Recommends:     catdoc
BuildRequires:  ebook-tools-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(xkbcommon)
# Not packaged yet -- remove once it is!
# BuildRequires:  pkgconfig(QMobipocket6)

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description devel
%{summary}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name
mkdir -p %{buildroot}%{_kf6_plugindir}/kfilemetadata/writers/

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6FileMetaData.so.*
%dir %{_kf6_plugindir}/kfilemetadata/
%{_kf6_plugindir}/kfilemetadata/kfilemetadata_*.so
%dir %{_kf6_plugindir}/kfilemetadata/writers/
%{_kf6_plugindir}/kfilemetadata/writers/kfilemetadata_taglibwriter.so

%files devel
%{_kf6_libdir}/libKF6FileMetaData.so
%{_kf6_libdir}/cmake/KF6FileMetaData
%{_kf6_includedir}/KFileMetaData/

%changelog
* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.112804.6fcc94b-1
- Initial Release
