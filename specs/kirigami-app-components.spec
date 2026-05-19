Name:           kirigami-app-components
Version:        1.0.0
Release:        1%{?dist}
Summary:        Kirigami extra addons and modules

License:        BSD-3-Clause AND CC0-1.0 AND FSFAP AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/libraries/kirigami-app-components
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QuickControls2)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6I18n)

%description
Kirigami addons and modules necessary to do a full featured
KDE application, such as integration with configurable
keyboard shortcuts and standard actions.

%package        devel
Summary:        Development files for %{name}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKirigamiActionCollection.so.%{version}
%{_kf6_libdir}/libKirigamiActionCollection.so.6
%{_kf6_qmldir}/org/kde/kirigami/actioncollection/

%files devel
%{_kf6_includedir}/Kirigami/ActionCollection/
%{_kf6_libdir}/libKirigamiActionCollection.so
%{_kf6_libdir}/cmake/KF6KirigamiAppComponents/

%changelog
* Sun May 17 2026 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- Initial Release
