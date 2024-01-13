Name:    plasma5support
Summary: Support components for porting from KF5/Qt5 to KF6/Qt6
Version: 5.92.0
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{name}

Source0:  https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  pkgconfig(xkbcommon)
Requires:  kf6-filesystem

# Renamed from kf6-plasma5support
Obsoletes:      kf6-plasma5support < 1:%{version}-%{release}
Provides:       kf6-plasma5support = 1:%{version}-%{release}

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Obsoletes:      kf6-plasma5support-devel < 1:%{version}-%{release}
Provides:       kf6-plasma5support-devel = 1:%{version}-%{release}
%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang libplasma5support

%files -f libplasma5support.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libPlasma5Support.so
%{_qt6_qmldir}/org/kde/plasma/plasma5support/
%{_datadir}/plasma5support/
%{_datadir}/qlogging-categories6/plasma5support.categories
%{_datadir}/qlogging-categories6/plasma5support.renamecategories

%files devel
%{_includedir}/Plasma5Support/
%{_kf6_libdir}/cmake/Plasma5Support/
%{_qt6_docdir}/*.tags
%{_kf6_libdir}/libPlasma5Support.so.%{version}
%{_kf6_libdir}/libPlasma5Support.so.6

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.92.0-1
- 5.92.0

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 5.91.0-2
- add doc package for KF6 API

* Thu Dec 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.91.0-1
- 5.91.0

* Sun Dec 03 2023 Justin Zobel <justin.zobel@gmail.com> - 5.90.0-1
- Update to 5.90.0

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 5.27.80-3
- Rebuild (qt6)

* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-2
- Add Obsoletes/Provides to the devel subpackage

* Fri Nov 10 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- Renamed from kf6-plasma5support
- 5.27.80

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.222045.245b3dd-1
- Initial release
