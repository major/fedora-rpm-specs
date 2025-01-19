# project name is different at github
%global project_name user-admin

%define _legacy_common_support 1

Name:          mate-user-admin
Version:       1.7.0
Release:       7%{?dist}
Summary:       User management tool
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later 
URL:           https://github.com/zhuyaliang/%{project_name}

# downloading the tarball
# spectool -g mate-user-admin.spec
# wget https://github.com/zhuyaliang/user-admin/archive/refs/tags/v1.7.0.tar.gz -O mate-user-admin-1.7.0.tar.gz
Source0:       %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: accountsservice-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: group-service-devel
BuildRequires: gtk3-devel
BuildRequires: libpwquality-devel
BuildRequires: libxcrypt-devel
BuildRequires: mate-desktop-devel
BuildRequires: meson
BuildRequires: polkit-devel

%description
Mate User management tool


%prep
%autosetup -p1 -n %{project_name}-%{version}
sed -i -e 's/OnlyShowIn=MATE;/OnlyShowIn=MATE;XFCE;LXDE;/g' data/mate-user-admin.desktop.in
sed -i -e 's/nugroups =mail;audio;video;lightdm;/#nugroups =mail;audio;video;lightdm/g' data/mate-user-admin/nuconfig

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install                               \
  --delete-original                                \
  --dir %{buildroot}%{_datadir}/applications    \
  %{buildroot}%{_datadir}/applications/mate-user-admin.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/mate-user-admin
%dir %{_sysconfdir}/mate-user-admin
%config %{_sysconfdir}/mate-user-admin/nuconfig
%{_datadir}/applications/mate-user-admin.desktop
%{_datadir}/metainfo/mate-user-admin.appdata.xml
%{_datadir}/mate-user-admin/
%{_datadir}/icons/hicolor/*/apps/user-admin.png
%{_datadir}/polkit-1/actions/org.mate.user.admin.policy


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.0-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 26 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.7.0-1
- update to 1.7.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 01 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.6.0-1
- update to 1.6.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.5.1-3
- fix building for f32

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.5.1-1
- update to  1.15.1

* Sun Jul 28 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.4.2-1
- update to  1.14.2
- add LXFCE and XFCE to desktop file

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.4.1-2
- Rebuild with Meson fix for #1699099

* Mon Mar 25 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.4.1-1
- update to 1.4.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.3.1-1
- update to 1.2.1

* Thu Dec 13 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.2.1-1
- update to 1.2.1

* Tue Sep 11 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.1-1
- update to 1.1.1

* Mon Sep 03 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.0.0-1
- initial package build

