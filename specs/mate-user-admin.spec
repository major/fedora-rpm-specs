# project name is different at github
%global project_name user-admin

%define _legacy_common_support 1

Name:          mate-user-admin
Version:       1.7.0
Release:       %autorelease
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
%autochangelog
