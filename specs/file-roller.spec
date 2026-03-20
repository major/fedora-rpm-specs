%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           file-roller
Version:        44.6
Release:        %autorelease
Summary:        Tool for viewing and creating archives

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/FileRoller
Source0:        https://download.gnome.org/sources/%{name}/44/%{name}-%{tarball_version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libadwaita-1)
%if 0%{?flatpak}
%else
BuildRequires:  pkgconfig(libnautilus-extension-4)
%endif
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  file-devel
BuildRequires:  (/usr/bin/gcpio or /usr/bin/cpio)
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/appstream-util

%description
File Roller is an application for creating and viewing archives files,
such as tar or zip files.

%if 0%{?flatpak}
%else
%package nautilus
Summary: File Roller extension for nautilus
Requires: %{name}%{_isa} = %{version}-%{release}

%description nautilus
This package contains the file-roller extension for the nautilus file manager.
It adds an item to the nautilus context menu that lets you compress files
or directories.
%endif

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson \
%if 0%{?flatpak}
  -Dnautilus-actions=disabled \
%endif
  %{nil}

%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.FileRoller.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.FileRoller.desktop

%files -f %{name}.lang
%doc README.md NEWS AUTHORS
%license COPYING
%{_bindir}/file-roller
%{_datadir}/file-roller
%{_datadir}/applications/org.gnome.FileRoller.desktop
%{_libexecdir}/file-roller
%{_datadir}/dbus-1/services/org.gnome.ArchiveManager1.service
%{_datadir}/dbus-1/services/org.gnome.FileRoller.service
%{_datadir}/glib-2.0/schemas/org.gnome.FileRoller.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.FileRoller*.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.FileRoller-symbolic.svg
%{_metainfodir}/org.gnome.FileRoller.metainfo.xml

%if 0%{?flatpak}
%else
%files nautilus
%{_libdir}/nautilus/extensions-4/libnautilus-fileroller.so
%endif

%changelog
%autochangelog
