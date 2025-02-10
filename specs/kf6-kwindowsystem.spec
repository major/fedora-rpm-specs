%global		framework kwindowsystem

Name:		kf6-%{framework}
Version:	6.11.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 integration module with classes for windows management
License:	CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	make
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	cmake(Qt6Qml)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xrender)
BuildRequires:  wayland-devel
BuildRequires:  egl-wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:	fdupes
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  qt6-qtbase-private-devel
Requires:	kf6-filesystem

%description
KDE Frameworks Tier 1 integration module that provides classes for managing and
working with windows.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kwindowsystem6_qt
%fdupes %{buildroot}%{_kf6_includedir}

%files -f kwindowsystem6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6WindowSystem.so.*
%dir %{_kf6_plugindir}/kwindowsystem/
%{_kf6_plugindir}/kwindowsystem/KF6WindowSystemX11Plugin.so
%{_kf6_qmldir}/org/kde/kwindowsystem
%{_qt6_plugindir}/kf6/kwindowsystem/KF6WindowSystemKWaylandPlugin.so

%files devel
%{_kf6_includedir}/KWindowSystem/
%{_kf6_libdir}/libKF6WindowSystem.so
%{_kf6_libdir}/cmake/KF6WindowSystem/
%{_qt6_docdir}/*.tags
%{_kf6_libdir}/pkgconfig/KF6WindowSystem.pc

 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Fri Feb 07 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.11.0-1
- 6.11.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 03 2025 Steve Cossette <farchord@gmail.com> - 6.10.0-1
- 6.10.0

* Sat Dec 14 2024 Steve Cossette <farchord@gmail.com> - 6.9.0-1
- 6.9.0

* Sat Nov 02 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.8.0-1
- 6.8.0

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.0-2
- Rebuild (qt6)

* Fri Oct 04 2024 Steve Cossette <farchord@gmail.com> - 6.7.0-1
- 6.7.0

* Mon Sep 16 2024 Steve Cossette <farchord@gmail.com> - 6.6.0-1
- 6.6.0

* Sat Aug 10 2024 Steve Cossette <farchord@gmail.com> - 6.5.0-1
- 6.5.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.4.0-1
- 6.4.0

* Sat Jun 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.0-1
- 6.3.0

* Sat May 04 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Wed Apr 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 6.0.0-3
- Rebuild (qt6)

* Sat Mar 09 2024 Marie Loise Nolden <loise@kde.org> - 6.0.0-2
- add missing BuildArch: noarch to -doc package

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 5.249.0-2
- Rebuild (qt6)

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

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 5.245.0-2
- Rebuild (qt6)

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231003.213655.0aa4d07-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20231003.213655.0aa4d07-2
- Rebuild for Qt Private API

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.213655.0aa4d07-1
- Fix for build on s390x arch

* Tue Sep 26 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230905.004205.b59a819-1
- Initial Release
