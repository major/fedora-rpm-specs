%global gitdate 20231009.021624
%global cmakever 5.240.0
%global commit0 89d7de22c0d0bd3593f51aff435a634624203d74
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kbookmarks

Name:    kf6-%{framework}
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for bookmarks manipulation
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)

Requires:  kf6-filesystem

%description
KBookmarks lets you access and manipulate bookmarks stored using the
XBEL format.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6WidgetsAddons)
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
%find_lang_kf6 kbookmarks6_qt



%files -f kbookmarks6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Bookmarks.so.*
%{_kf6_libdir}/libKF6BookmarksWidgets.so.5*
%{_kf6_libdir}/libKF6BookmarksWidgets.so.6*
%{_kf6_datadir}/qlogging-categories6/%{framework}widgets.categories

%files devel
%{_kf6_includedir}/KBookmarks/
%{_kf6_libdir}/libKF6Bookmarks.so
%{_kf6_libdir}/cmake/KF6Bookmarks/
%{_kf6_includedir}/KBookmarksWidgets/
%{_kf6_libdir}/libKF6BookmarksWidgets.so

%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231009.021624.89d7de2-1
- Initial release
