%global framework kglobalaccel

Name:    kf6-%{framework}
Version: 5.248.0
Release: 3%{?dist}
Summary: KDE Frameworks 6 Tier 3 integration module for global shortcuts

# The following are in the LICENSES folder but go unused: LGPL-2.1-only, LGPL-3.0-only, (LGPL-2.1-only OR LGPL-3.0-only)
License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)
# for systemd-related macros
BuildRequires:  systemd
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel

Requires:       kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       qt6-qtbase-devel
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

# unpackaged files
%if 0%{?flatpak:1}
rm -fv %{buildroot}%{_prefix}/lib/systemd/user/plasma-kglobalaccel.service
%endif

%find_lang_kf6 kglobalaccel6_qt

%files -f kglobalaccel6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6GlobalAccel.so.*

%files devel
%{_kf6_includedir}/KGlobalAccel/
%{_kf6_libdir}/libKF6GlobalAccel.so
%{_kf6_libdir}/cmake/KF6GlobalAccel/
%{_kf6_datadir}/dbus-1/interfaces/*
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
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

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231003.060644.9b93514-3
- Rebuild (qt6)

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.060644.9b93514-2
- Removed -libs from the required installs at runtime (Unneeded)

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.060644.9b93514-1
- Initial Release
