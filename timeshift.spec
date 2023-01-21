# This package needs to be run as root and may
# run for a long time, thus we build with full
# hardening. This flags is enabled by default
# on recent Fedora releases, but we need to
# specify it for EPEL <= 7 explicitly.
%global _hardened_build 1


Name:           timeshift
Version:        22.11.2
Release:        %autorelease
Summary:        System restore tool for Linux

License:        GPLv3+ or LGPLv3+
URL:            https://github.com/linuxmint/timeshift
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  make
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
sed -i -e 's@--thread @@g' src/makefile
sed -i -e 's@--Xcc="-O3" @@g' src/makefile
sed -i '/${app_name}-uninstall/d' src/makefile

%build
for flag in %{optflags} %{?__global_ldflags}; do
  VALAFLAGS="$VALAFLAGS -X $flag"
done

# Inject Fedora compiler flags and the debug option to valac.
# Just dump the c-sources.
sed -i "s|^[\t ]*valac|& --ccode --save-temps -g $VALAFLAGS|" src/makefile
%make_build

# Move generated c-sources into flat tree so it can be picked
# up for -debugsource.
for f in `find src/ -type f -name '*.c'`; do
  mv -f $f src/
done

# Inject Fedora compiler flags and the debug option to valac
# Build the binaries.
sed -i "s|valac --ccode|valac|" src/makefile
%make_build


%install
%make_install
# Remove duplicate
rm -rf %{buildroot}%{_datadir}/appdata

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop


%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif


%files -f %{name}.lang
%license COPYING LICENSE.md
%doc AUTHORS README.md
%{_bindir}/*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%ghost %attr(644, root, root) %{_sysconfdir}/cron.d/%{name}-boot
%ghost %attr(644, root, root) %{_sysconfdir}/cron.d/%{name}-hourly
%ghost %attr(664, root, root) %{_sysconfdir}/%{name}.json
%config %{_sysconfdir}/%{name}/default.json



%changelog
%autochangelog