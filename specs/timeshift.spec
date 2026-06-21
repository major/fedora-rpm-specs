Name:           timeshift
Version:        25.12.4
Release:        %autorelease
Summary:        System restore tool for Linux

# Automatically converted from old format: GPLv3+ or LGPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later OR LGPL-3.0-or-later
URL:            https://github.com/linuxmint/timeshift
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  meson
BuildRequires:  make
BuildRequires:  help2man
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(xapp)
BuildRequires:  vala

Requires:       cronie
Requires:       hicolor-icon-theme
Requires:       polkit
Requires:       psmisc
Requires:       rsync

# For btrfs systems
Recommends:     btrfs-progs

%description
Timeshift for Linux is an application that provides functionality similar to
the System Restore feature in Windows and the Time Machine tool in Mac OS.
Timeshift protects your system by taking incremental snapshots of the file
system at regular intervals. These snapshots can be restored at a later date
to undo all changes to the system.

In RSYNC mode, snapshots are taken using rsync and hard-links. Common files
are shared between snapshots which saves disk space. Each snapshot is a full
system backup that can be browsed with a file manager.

In BTRFS mode, snapshots are taken using the in-built features of the BTRFS
filesystem. BTRFS snapshots are supported only on BTRFS systems having an
Ubuntu-type subvolume layout (with @ and @home subvolumes).


%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build


%install
# Install timeshift.json to /etc/timeshift build sucessfuly
mkdir -p %{buildroot}/etc/%{name}
install -m 644 files/%{name}.json %{buildroot}/etc/%{name}/
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop


%files -f %{name}.lang
%license LICENSES/*
%doc AUTHORS README.md
%{_bindir}/timeshift
%{_bindir}/timeshift-gtk
%{_bindir}/timeshift-launcher
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/polkit-1/actions/in.teejeetech.pkexec.%{name}.policy
%{_datadir}/%{name}/images/*
%{_datadir}/applications/%{name}-gtk.desktop
%{_metainfodir}/com.linuxmint.%{name}.metainfo.xml
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-gtk.1*
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.json
%{_sysconfdir}/%{name}/default.json

%changelog
%autochangelog
