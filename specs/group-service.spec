Name:          group-service
Version:       1.4.0
Release:       %autorelease
Summary:       Dbus Group management CLI tool
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later 
URL:           https://github.com/zhuyaliang/%{name}

# downloading the tarball
# spectool -g group-service.spec
Source0:       %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: dbus-devel
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: libxcrypt-devel
BuildRequires: meson >= 0.50.0
BuildRequires: polkit-devel
BuildRequires: pkgconfig(systemd)
BuildRequires: systemd-rpm-macros

%{?systemd_requires}

%description
Dbus Group management CLI tool

%package devel
Summary:  Support for developing back-ends for group-service
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files needed for
group-service back-ends development.


%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome --all-name

%post
%systemd_post group-admin-daemon.service

%preun
%systemd_preun group-admin-daemon.service

%postun
%systemd_postun group-admin-daemon.service


%files -f %{name}.lang
%doc README.md
%license COPYING
%{_sysconfdir}/dbus-1/system.d/org.group.admin.conf
%{_libdir}/libgroup-service.so.1*
%{_libexecdir}/group-admin-daemon
%{_datadir}/dbus-1/interfaces/org.group.admin.list.xml
%{_datadir}/dbus-1/interfaces/org.group.admin.xml
%{_datadir}/dbus-1/system-services/org.group.admin.service
%{_datadir}/polkit-1/actions/org.group.admin.policy
%{_unitdir}/group-admin-daemon.service

%files devel
%{_includedir}/group-service-1.0/
%{_libdir}/libgroup-service.so
%{_libdir}/pkgconfig/group-service.pc


%changelog
%autochangelog
