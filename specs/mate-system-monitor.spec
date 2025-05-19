Name:           mate-system-monitor
Version:        1.28.1
Release:        %autorelease
Summary:        Process and resource monitor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk3-devel
BuildRequires: gtkmm30-devel
BuildRequires: libgtop2-devel
BuildRequires: librsvg2-devel
BuildRequires: libwnck3-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: pkgconfig(libsystemd)
BuildRequires: polkit-devel

Requires: mate-desktop

%description
mate-system-monitor allows to graphically view and manipulate the running
processes on your system. It also provides an overview of available resources
such as CPU and memory.

%prep
%autosetup -p1

%build
%configure \
        --disable-static \
        --disable-schemas-compile \
        --enable-systemd \
        --enable-wnck

make %{?_smp_mflags} V=1


%install
%{make_install}

desktop-file-install --delete-original             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-system-monitor.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS NEWS COPYING README
%{_bindir}/mate-system-monitor
%{_libexecdir}/mate-system-monitor/
%{_datadir}/polkit-1/actions/org.mate.mate-system-monitor.policy
%{_datadir}/metainfo/mate-system-monitor.appdata.xml
%{_datadir}/applications/mate-system-monitor.desktop
%{_datadir}/pixmaps/mate-system-monitor/
%{_datadir}/glib-2.0/schemas/org.mate.system-monitor.*.xml
%{_mandir}/man1/*


%changelog
%autochangelog
