%global framework kstatusnotifieritem

Name:           kf6-%{framework}
Version:        6.0.0
Release:        2%{?dist}
Summary:        Implementation of Status Notifier Items

License:        CC0-1.0 AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)
Requires:  kf6-filesystem

%description
%summary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{framework}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kstatusnotifieritem6_qt

%files -f kstatusnotifieritem6_qt.lang
%{_kf6_libdir}/libKF6StatusNotifierItem.so.*
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.StatusNotifierItem.xml
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.StatusNotifierWatcher.xml
%{_kf6_datadir}/qlogging-categories6/kstatusnotifieritem.categories

%files devel
%{_kf6_includedir}/KStatusNotifierItem
%{_kf6_libdir}/cmake/KF6StatusNotifierItem
%{_kf6_libdir}/libKF6StatusNotifierItem.so
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Thu Feb 22 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-2
- Rebuild due to sources re-spin

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.249.0-1
- 5.249.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

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

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.024138.6035342-1
- Initial release
