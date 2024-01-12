%undefine __cmake_in_source_build

%global framework networkmanager-qt

Name:           kf6-%{framework}
Version:        5.248.0
Release:        1%{?dist}
Summary:        A Tier 1 KDE Frameworks 6 module that wraps NetworkManager DBus API
License:        LGPL-2.0-or-later AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL AND CC0-1.0
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# KDE Frameworks
BuildRequires:  extra-cmake-modules

# Fedora
Requires:       kf6-filesystem
BuildRequires:  kf6-rpm-macros

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)

# Other
BuildRequires:  pkgconfig(libnm)
Recommends:     NetworkManager

%description
A Tier 1 KDE Frameworks 6 Qt library for NetworkManager.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       pkgconfig(libnm)
%description    devel
Qt libraries and header files for developing applications
that use NetworkManager.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6NetworkManagerQt.so.5*
%{_kf6_libdir}/libKF6NetworkManagerQt.so.6
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/kde-qmlmodule.version
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/libnetworkmanagerqtqml.so
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/networkmanagerqtqml.qmltypes
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/qmldir

%files devel
%{_kf6_includedir}/NetworkManagerQt/
%{_kf6_libdir}/libKF6NetworkManagerQt.so
%{_kf6_libdir}/cmake/KF6NetworkManagerQt/
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.248.0-1
- 5.248.0

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 5.247.0-2
- add doc package for KF6 API

* Wed Dec 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.247.0-1
- 5.247.0

* Sat Dec 02 2023 Justin Zobel <justin.zobel@gmail.com> - 5.246.0-1
- Update to 5.246.0

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Wed Sep 27 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230920.135708.7f4e3a34bbe3c7db7f2d090e1bfc572a21f834a2-135
- Initial Package
