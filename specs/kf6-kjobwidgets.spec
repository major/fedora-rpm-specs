%global framework kjobwidgets

Name:           kf6-%{framework}
Version:        6.16.0
Release:        2%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon for KJobs
# The following are in the LICENSES folder, but go unused: LGPL-3.0-only, LicenseRef-KDE-Accepted-LGPL
License:        CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel

BuildRequires:  pkgconfig(xkbcommon)
Requires:       kf6-filesystem

%description
%{summary}.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6CoreAddons)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kjobwidgets6_qt

%files -f kjobwidgets6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6JobWidgets.so.*

%files -n python3-%{name}
%{python3_sitearch}/KJobWidgets.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KJobWidgets/
%{_kf6_libdir}/libKF6JobWidgets.so
%{_kf6_libdir}/cmake/KF6JobWidgets/
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jul 05 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.16.0-1
- 6.16.0

* Tue Jun 17 2025 Marie Loise Nolden <loise@kde.org> - 6.15.0-2
- 6.15 and plasma 3.4 compatibility rebuild

* Sat Jun 07 2025 Steve Cossette <farchord@gmail.com> - 6.15.0-1
- 6.15.0

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 6.14.0-2
- Rebuilt for Python 3.14

* Sat May 03 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.14.0-1
- 6.14.0

* Mon Apr 14 2025 Jan Grulich <jgrulich@redhat.com> - 6.13.0-2
- Rebuild (qt6)

* Sun Apr 06 2025 Steve Cossette <farchord@gmail.com> - 6.13.0-1
- 6.13.0

* Tue Mar 25 2025 Jan Grulich <jgrulich@redhat.com> - 6.12.0-2
- Rebuild (qt6)

* Fri Mar 07 2025 Steve Cossette <farchord@gmail.com> - 6.12.0-1
- 6.12.0

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

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231001.123235.e058145-2
- Rebuild (qt6)

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.123235.e058145-1
- Initial Release
