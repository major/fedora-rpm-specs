%global framework kconfigwidgets

Name:    kf6-%{framework}
Version: 5.248.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for creating configuration dialogs

# The following licenses are in LICENSES but go unused: BSD-3-Clause, MIT
License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-kauth-devel
BuildRequires:  kf6-kcodecs-devel
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(KF6ColorScheme)
Requires:  kf6-filesystem
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(Qt6UiPlugin)

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-kauth-devel
Requires:       kf6-kcodecs-devel
Requires:       cmake(KF6ColorScheme)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6WidgetsAddons)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

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
%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/qt6/plugins/designer/kconfigwidgets6widgets.so
%{_kf6_libdir}/libKF6ConfigWidgets.so.*
%{_datadir}/locale/*/kf6_entry.desktop

%files devel
%{_kf6_includedir}/KConfigWidgets/
%{_kf6_libdir}/libKF6ConfigWidgets.so
%{_kf6_libdir}/cmake/KF6ConfigWidgets/
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

* Fri Nov 10 2023 Alessandro Astone <ales.astone@gmail.com> - 5.245.0-2
- Add missing devel dependency on KF6ColorScheme

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.053220.dd41bb4-1
- Initial Release
