Name:           kio-admin
Version:        23.03.80
Release:        1%{?dist}
Summary:        Manage files as administrator using the admin:// KIO protocol
License:        (GPL-2.0-only or GPL-3.0-only) and BSD-3-Clause and CC0-1.0 and FSFAP
URL:            https://invent.kde.org/system/kio-admin
Source:         https://download.kde.org/stable/kio-admin/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  zstd
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(PolkitQt5-1)


%description
kio-admin implements a new protocol "admin:///" 
which gives administrative access
to the entire system. This is achieved by talking, 
over dbus, with a root-level
helper binary that in turn uses 
existing KIO infrastructure to run file://
operations in root-scope.

%prep
%autosetup -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang kio5_admin %{name}.lang

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf5_metainfodir}/org.kde.kio.admin.metainfo.xml
%dir %{_kf5_plugindir}/kfileitemaction/
%{_kf5_plugindir}/kfileitemaction/kio-admin.so
%dir %{_kf5_plugindir}/kio/
%{_kf5_plugindir}/kio/admin.so
%{_kf5_libexecdir}/kio-admin-helper
%{_kf5_datadir}/dbus-1/system.d/org.kde.kio.admin.conf
%{_kf5_datadir}/dbus-1/system-services/org.kde.kio.admin.service
%{_kf5_datadir}/polkit-1/actions/org.kde.kio.admin.policy

%changelog	
* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Mon Jan 23 2023 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 1.0.0-1
- initial kio-admin package
