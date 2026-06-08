# RHEL 10 won't ship with GTK 2, don't build bit there, but build them elsewhere
%if 0%{?rhel} > 9
%bcond_with gtk2
%else
%bcond_without gtk2
%endif

Name: libcanberra
Version: 0.30
Release: %autorelease
Summary: Portable Sound Event Library
Source0: http://0pointer.de/lennart/projects/libcanberra/libcanberra-%{version}.tar.xz
Patch0: 0001-gtk-Don-t-assume-all-GdkDisplays-are-GdkX11Displays-.patch
Patch1: 0001-canberra-boot-use-plughw-ALSA-device.patch
License: LGPL-2.1-or-later
URL: https://git.0pointer.net/libcanberra.git/
BuildRequires: gcc
%if %{with gtk2}
BuildRequires: gtk2-devel
%endif
BuildRequires: gtk3-devel
BuildRequires: alsa-lib-devel
BuildRequires: libvorbis-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: gtk-doc
BuildRequires: pulseaudio-libs-devel >= 0.9.15
BuildRequires: gstreamer1-devel
BuildRequires: libtdb-devel
BuildRequires: gettext-devel
BuildRequires: systemd-devel
BuildRequires: make
Requires: sound-theme-freedesktop

Recommends: libcanberra-backend-alsa
Recommends: libcanberra-backend-gstreamer
Recommends: libcanberra-backend-pulse

%description
A small and lightweight implementation of the XDG Sound Theme Specification
(http://0pointer.de/public/sound-theme-spec.html).

%package backend-alsa
Summary: ALSA backend for libcanberra
Requires: %{name}%{?_isa} = %{version}-%{release}

%description backend-alsa
The ALSA backend module for libcanberra

%package backend-gstreamer
Summary: GStreamer backend for libcanberra
Requires: %{name}%{?_isa} = %{version}-%{release}

%description backend-gstreamer
The GStreamer backend module for libcanberra

%package backend-pulse
Summary: PulseAudio backend for libcanberra
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pulseaudio-libs >= 0.9.15

%description backend-pulse
The PulseAudio backend module for libcanberra

%if %{with gtk2}
%package gtk2
Summary: Gtk+ 2.x Bindings for libcanberra
Requires: %{name}%{?_isa} = %{version}-%{release}
# Some other stuff is included in the gtk3 package, so always pull that in.
Requires: %{name}-gtk3%{?_isa} = %{version}-%{release}

%description gtk2
Gtk+ 2.x bindings for libcanberra
%endif

%package gtk3
Summary: Gtk+ 3.x Bindings for libcanberra
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gtk3
Gtk+ 3.x bindings for libcanberra

%package devel
Summary: Development Files for libcanberra Client Development
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk3%{?_isa} = %{version}-%{release}
%if %{with gtk2}
Requires: %{name}-gtk2%{?_isa} = %{version}-%{release}
Requires: gtk2-devel
%endif

%description devel
Development Files for libcanberra Client Development

%post
%systemd_post canberra-system-bootup.service canberra-system-shutdown.service canberra-system-shutdown-reboot.service

%preun
%systemd_preun canberra-system-bootup.service canberra-system-shutdown.service canberra-system-shutdown-reboot.service

%prep
%autosetup -p1

%build
%configure \
    --disable-static \
    --enable-pulse \
    --enable-alsa \
%if %{without gtk2}
    --disable-gtk \
%endif
    --enable-null \
    --disable-oss \
    --with-builtin=dso \
    --with-systemdsystemunitdir=%{_unitdir}
%make_build

%install
%make_install
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;
rm $RPM_BUILD_ROOT%{_docdir}/libcanberra/README

%files
%license LGPL
%doc README LGPL
%{_libdir}/libcanberra.so.*
%dir %{_libdir}/libcanberra-%{version}
%{_libdir}/libcanberra-%{version}/libcanberra-null.so
%{_libdir}/libcanberra-%{version}/libcanberra-multi.so
%{_prefix}/lib/systemd/system/canberra-system-bootup.service
%{_prefix}/lib/systemd/system/canberra-system-shutdown-reboot.service
%{_prefix}/lib/systemd/system/canberra-system-shutdown.service
%{_bindir}/canberra-boot

%files backend-alsa
%{_libdir}/libcanberra-%{version}/libcanberra-alsa.so

%files backend-gstreamer
%{_libdir}/libcanberra-%{version}/libcanberra-gstreamer.so

%files backend-pulse
%{_libdir}/libcanberra-%{version}/libcanberra-pulse.so

%if %{with gtk2}
%files gtk2
%{_libdir}/libcanberra-gtk.so.*
%{_libdir}/gtk-2.0/modules/libcanberra-gtk-module.so
%endif

%files gtk3
%{_libdir}/libcanberra-gtk3.so.*
%{_libdir}/gtk-3.0/modules/libcanberra-gtk3-module.so
%{_libdir}/gtk-3.0/modules/libcanberra-gtk-module.so
%{_bindir}/canberra-gtk-play
# RHBZ#2283279
%dir %{_datadir}/gnome/autostart/
%dir %{_datadir}/gnome/shutdown/
%{_datadir}/gnome/autostart/libcanberra-login-sound.desktop
%{_datadir}/gnome/shutdown/libcanberra-logout-sound.sh
# co-own these directories to avoid requiring GDM (#522998)
%dir %{_datadir}/gdm/
%dir %{_datadir}/gdm/autostart/
%dir %{_datadir}/gdm/autostart/LoginWindow/
%{_datadir}/gdm/autostart/LoginWindow/libcanberra-ready-sound.desktop
# co-own these directories to avoid requiring g-s-d
%dir %{_libdir}/gnome-settings-daemon-3.0/
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules/
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/canberra-gtk-module.desktop

%files devel
%doc %{_datadir}/gtk-doc
%{_includedir}/canberra-gtk.h
%{_includedir}/canberra.h
%{_libdir}/libcanberra.so
%{_libdir}/pkgconfig/libcanberra.pc
%if %{with gtk2}
%{_libdir}/libcanberra-gtk.so
%{_libdir}/pkgconfig/libcanberra-gtk.pc
%endif
%{_libdir}/libcanberra-gtk3.so
%{_libdir}/pkgconfig/libcanberra-gtk3.pc
# co-own these directories to avoid requiring vala
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libcanberra-gtk.vapi
%{_datadir}/vala/vapi/libcanberra.vapi

%changelog
%autochangelog
