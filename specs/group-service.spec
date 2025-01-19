Name:          group-service
Version:       1.4.0
Release:       7%{?dist}
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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.0-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 26 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.4.0-1
- update to 1.4.0

* Tue Jan 24 2023 Robert Scheck <robert@fedoraproject.org> - 1.3.0-7
- Depend on pkgconfig(systemd) to ensure systemd.pc availability

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Robert Scheck <robert@fedoraproject.org> - 1.3.0-4
- Removed systemd(-rpm-macros) switch for old Fedora releases
- Removed lowering of meson version for old Fedora/RHEL releases
- Added upstream patch to fix building with meson 0.62.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 01 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.3.0-1
- update to 1.3.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.2.0-1
- update to  1.2.0

* Fri Sep 27 2019 Thomas Batten <stenstorpmc@gmail.com> - 1.1.0-7
- force older meson version on el8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.1.0-5
- Rebuild with Meson fix for #1699099

* Mon Mar 25 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.0-4
- add upsream patch to fix soname version

* Sat Mar 23 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.0-3
- update tarball and drop patch
- update shared libraries packaging

* Sat Mar 23 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.0-2
- fix source link
- fix description
- fix packaging shared libraries
- add upstream patch to fix include dir

* Mon Mar 18 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.0-1
- initial package build

