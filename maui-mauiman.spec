Name:           maui-mauiman
Version:        3.0.2
Release:        1%{?dist}
License:        LGPL-3.0-or-later
Summary:        Maui Manager Library
Url:            https://invent.kde.org/maui/mauiman
Source:         https://invent.kde.org/maui/mauiman/-/archive/v%{version}/mauiman-v%{version}.tar.gz
# Add a soname to the library
Patch:          libsoname.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  dbus-common

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)

# Make sure there is an owner for /usr/share/dbus-1
# and /usr/share/dbus-1/services
Requires: dbus-common

%description
MauiMan stands for Maui Manager, and exists for setting,
saving, and syncing the configuration preferences for the
Maui Apps & Shell ecosystem.

%package devel
Summary:        MauiMan development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components using
MauiMan.

%prep
%autosetup -n mauiman-v%{version} -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON -DBUILD_WITH_QT5=OFF
%cmake_build

%install
%cmake_install


%files
%doc README.md
%license LICENSES/LGPL-3.0.txt
%{_bindir}/MauiManServer4
%{_datadir}/dbus-1/services/org.mauiman.Manager4.service
%{_libdir}/libMauiMan4.so.0*

%files devel
%{_libdir}/libMauiMan4.so
%dir %{_includedir}/MauiMan4
%{_includedir}/MauiMan4/settingsstore.h
%{_includedir}/MauiMan4/backgroundmanager.h
%{_includedir}/MauiMan4/thememanager.h
%{_includedir}/MauiMan4/screenmanager.h
%{_includedir}/MauiMan4/formfactormanager.h
%{_includedir}/MauiMan4/accessibilitymanager.h
%{_includedir}/MauiMan4/inputdevicesmanager.h
%{_includedir}/MauiMan4/mauimanutils.h
%{_includedir}/MauiMan4/mauiman_export.h
%dir %{_libdir}/cmake/MauiMan4
%{_libdir}/cmake/MauiMan4/*.cmake

%changelog
* Sun Feb 11 2024 Benson Muite <benson_muite@emailplus.org> - 3.0.2-1
- Initial packaging
