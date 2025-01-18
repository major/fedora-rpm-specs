%global framework kirigami-addons

Name:           kf6-%{framework}
Version:        1.7.0
Release:        1%{?dist}
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND LicenseRef-KFQF-Accepted-GPL
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://invent.kde.org/libraries/%{framework}
Source:         https://download.kde.org/stable/%{framework}/%{framework}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)

Requires: kf6-filesystem

### Renamed from kf6-kirigami2-addons (which was at epoch 1)
Obsoletes: kf6-kirigami2-addons < 1:0.11.76-5
Provides:  kf6-kirigami2-addons = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons%{?_isa} = 1:%{version}-%{release}

### Merged subpackages back into main package
# The old name
Obsoletes: kf6-kirigami2-addons-dateandtime < 1:0.11.76-5
Provides:  kf6-kirigami2-addons-dateandtime = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons-dateandtime%{?_isa} = 1:%{version}-%{release}

Obsoletes: kf6-kirigami2-addons-treeview < 1:0.11.76-5
Provides:  kf6-kirigami2-addons-treeview = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons-treeview%{?_isa} = 1:%{version}-%{release}

# The new name
Obsoletes: kf6-kirigami-addons-dateandtime < 0.11.76-5
Provides:  kf6-kirigami-addons-dateandtime = %{version}-%{release}
Provides:  kf6-kirigami-addons-dateandtime%{?_isa} = %{version}-%{release}

Obsoletes: kf6-kirigami-addons-treeview < 0.11.76-5
Provides:  kf6-kirigami-addons-treeview = %{version}-%{release}
Provides:  kf6-kirigami-addons-treeview%{?_isa} = %{version}-%{release}

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package   devel
Summary:   Development files for %{name}
Requires:  %{name} = %{version}-%{release}
Conflicts: kf6-kirigami-addons < 1.4.0
%description devel
The %{name}-devel package contains CMake definitions, libraries
and header files for developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{version}

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install
%find_lang %{orig_name}6 --all-name

%files -f %{orig_name}6.lang
%doc README.md
%license LICENSES/
%dir %{_kf6_qmldir}/org/kde
%{_kf6_qmldir}/org/kde/kirigamiaddons
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so.{6,%{version}}

%files devel
%{_kf6_libdir}/cmake/KF6KirigamiAddons
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so
%{_includedir}/KirigamiAddonsStatefulApp/
%{_kf6_datadir}/kdevappwizard/templates/kirigamiaddons6.tar.bz2
%{_kf6_datadir}/kdevappwizard/templates/librarymanager6.tar.bz2

%changelog
* Thu Jan 16 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.7.0-1
- 1.7.0

* Sun Dec 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.6.0-1
- 1.6.0

* Sat Nov 16 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.5.0-1
- 1.5.0

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 1.4.0-2
- Rebuild (qt6)

* Thu Aug 15 2024 Alessandro Astone <ales.astone@gmail.com> - 1.4.0-1
- 1.4.0
- Split devel subpackage

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 16 2024 Marie Loise Nolden <loise@kde.org> - 1.2.1-1
- 1.2.1

* Fri May 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.2.0-1
- 1.2.0

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 1.1.0-2
- Rebuild (qt6)

* Mon Apr 01 2024 Steve Cossette <farchord@gmail.com> - 1.1.0-1
- 1.1.0

* Thu Feb 29 2024 Marie Loise Nolden <loise@kde.org> - 1.0.1-1
- 1.0.1

* Thu Feb 22 2024 Alessandro Astone <ales.astone@gmail.com> - 1.0.0-1
- 1.0.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 0.11.90-4
- Rebuild (qt6)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Alessandro Astone <ales.astone@gmail.com> - 0.11.90-1
- 0.11.90

* Wed Jan 10 2024 Alessandro Astone <ales.astone@gmail.com> - 0.11.76-3
- Remove subpackages

* Sun Dec 03 2023 Alessandro Astone <ales.astone@gmail.com> - 0.11.76-2
- Add arch-ed provides

* Thu Nov 30 2023 Alessandro Astone <ales.astone@gmail.com> - 0.11.76-1
- Renamed from kf6-kirigami2-addons

