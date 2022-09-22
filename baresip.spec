Summary:        Modular SIP user-agent with audio and video support
Name:           baresip
Version:        2.7.0
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/baresip/baresip
Source0:        https://github.com/baresip/baresip/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        com.github.baresip.desktop
Source10:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/1e1d692148e8ab958bfea4188f8575b673804e09/Adwaita/scalable/status/call-incoming-symbolic.svg
Source11:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/1e1d692148e8ab958bfea4188f8575b673804e09/Adwaita/scalable/status/call-outgoing-symbolic.svg
Source12:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/master/COPYING#/COPYING.adwaita-icon-theme
Source13:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/master/COPYING_CCBYSA3#/COPYING_CCBYSA3.adwaita-icon-theme
Source14:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/master/COPYING_LGPL#/COPYING_LGPL.adwaita-icon-theme
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libre-devel >= 2.7.0
BuildRequires:  librem-devel >= 2.7.0
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  openssl-devel >= 1.1.0
%else
BuildRequires:  openssl11-devel
# Atomic support in libre >= 2.1.0
BuildRequires:  devtoolset-8-toolchain
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
Recommends:     %{name}-pulse%{?_isa} = %{version}-%{release}
%else
Requires:       %{name}-pulse%{?_isa} = %{version}-%{release}
%endif
Obsoletes:      %{name}-cairo < 1.1.0-1
Obsoletes:      %{name}-rst < 2.0.0-1
Obsoletes:      %{name}-speex_pp < 2.0.0-1
Obsoletes:      %{name}-x11grab < 2.0.0-1
Obsoletes:      %{name}-gsm < 2.6.0-1
Obsoletes:      %{name}-gst_video < 2.6.0-1
Obsoletes:      %{name}-omx < 2.7.0-1

%description
A modular SIP user-agent with support for audio and video, and many IETF
standards such as SIP, SDP, RTP/RTCP and STUN/TURN/ICE for both, IPv4 and
IPv6.

Additional modules provide support for audio codecs like Codec2, G.711,
G.722, G.726, GSM, L16, MPA and Opus, audio drivers like ALSA, GStreamer,
JACK Audio Connection Kit, Portaudio, and PulseAudio, video codecs like
AV1, VP8 or VP9, video sources like Video4Linux, video outputs like SDL2
or X11, NAT traversal via STUN, TURN, ICE, and NAT-PMP, media encryption
via TLS, SRTP or DTLS-SRTP, management features like embedded web-server
with HTTP interface, command-line console and interface, and MQTT.

%if 0%{?fedora}
%package aac
Summary:        AAC audio codec module for baresip
BuildRequires:  fdk-aac-free-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description aac
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Advanced Audio Coding (AAC) audio codec.
%endif

%package alsa
Summary:        ALSA audio driver for baresip
BuildRequires:  alsa-lib-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description alsa
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Advanced Linux Sound Architecture (ALSA) audio
driver.

%package av1
Summary:        AV1 video codec module for baresip
BuildRequires:  libaom-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description av1
Baresip is a modular SIP user-agent with audio and video support.

This module provides the AV1 video codec, an open, royalty-free video
coding format developed as a successor to the VP9 video codec.

%package codec2
Summary:        Codec 2 audio codec module for baresip
BuildRequires:  codec2-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description codec2
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Codec 2 audio codec, an Open Source speech codec
designed for communications quality speech between 700 and 3200 bit/s.

%package ctrl_dbus
Summary:        D-BUS communication channel control module for baresip
BuildRequires:  %{_bindir}/gdbus-codegen
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description ctrl_dbus
Baresip is a modular SIP user-agent with audio and video support.

This module provides a communication channel to control and monitor
baresip via D-BUS.

%package g722
Summary:        G.722 audio codec module for baresip
BuildRequires:  spandsp-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description g722
Baresip is a modular SIP user-agent with audio and video support.

This module provides the G.722 audio codec, often used for HD voice.

%package g726
Summary:        G.726 audio codec module for baresip
BuildRequires:  spandsp-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description g726
Baresip is a modular SIP user-agent with audio and video support.

This module provides the G.726 audio codec.

%package gst
Summary:        GStreamer audio source driver for baresip
BuildRequires:  pkgconfig(gstreamer-1.0)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gst
Baresip is a modular SIP user-agent with audio and video support.

This module uses the GStreamer 1.0 framework to play external media and
provides them as an internal audio source.

%package gtk
Summary:        GTK+ menu-based user interface module for baresip
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  desktop-file-utils
%if 0%{?rhel} == 7 || 0%{?rhel} == 8
License:        BSD and (LGPLv3+ or CC-BY-SA)
BuildRequires:  librsvg2
BuildRequires:  /usr/bin/gtk-encode-symbolic-svg
Requires:       adwaita-icon-theme < 3.31.91-1
%else
Requires:       adwaita-icon-theme >= 3.31.91-1
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 8
Requires:       (gnome-shell-extension-appindicator if gnome-shell)
Recommends:     libcanberra-gtk3
%else
%if 0%{?rhel} == 8
Requires:       (gnome-shell-extension-topicons-plus if gnome-shell)
Recommends:     libcanberra-gtk3
%else
Requires:       libcanberra-gtk3
%endif
%endif

%description gtk
Baresip is a modular SIP user-agent with audio and video support.

This module provides a GTK+ menu-based user interface.
%if 0%{?fedora} || 0%{?rhel} > 7
Note: GTK+ defaults to the Wayland backend, which baresip does not
support. Use 'GDK_BACKEND=x11 baresip' to override it to Xwayland.
%endif

%package jack
Summary:        JACK audio driver for baresip
BuildRequires:  pkgconfig(jack)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description jack
Baresip is a modular SIP user-agent with audio and video support.

This module provides the JACK Audio Connection Kit audio driver.

%package mpa
Summary:        MPA speech and audio codec module for baresip
BuildRequires:  twolame-devel
BuildRequires:  lame-devel
BuildRequires:  mpg123-devel
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  speexdsp-devel
%else
BuildRequires:  speex-devel
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description mpa
Baresip is a modular SIP user-agent with audio and video support.

This module provides the MPA speech and audio codec.

%package mqtt
Summary:        MQTT management module for baresip
BuildRequires:  mosquitto-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description mqtt
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Message Queue Telemetry Transport (MQTT)
management module.

%package opus
Summary:        Opus speech and audio codec module for baresip
BuildRequires:  opus-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description opus
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Opus speech and audio codec module.

%package plc
Summary:        Packet Loss Concealment module for baresip
BuildRequires:  spandsp-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plc
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Packet Loss Concealment (PLC) module.

%package portaudio
Summary:        Portaudio audio driver for baresip
BuildRequires:  portaudio-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description portaudio
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Portaudio audio driver.

%package pulse
Summary:        PulseAudio audio driver for baresip
BuildRequires:  pkgconfig(libpulse-simple)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description pulse
Baresip is a modular SIP user-agent with audio and video support.

This module provides the PulseAudio audio driver.

%package sdl
Summary:        SDL2 video output driver for baresip
BuildRequires:  SDL2-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description sdl
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Simple DirectMedia Layer 2.0 (SDL2) video output
driver.

%package snapshot
Summary:        Snapshot video filter using libpng for baresip
BuildRequires:  libpng-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description snapshot
Baresip is a modular SIP user-agent with audio and video support.

This module takes snapshots of the video stream and saves them as PNG
files using libpng.

%package sndfile
Summary:        Audio dumper module using libsndfile for baresip
BuildRequires:  libsndfile-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description sndfile
Baresip is a modular SIP user-agent with audio and video support.

This module provides an audio dumper to write WAV audio sample files
using libsndfile.

%package tools
Summary:        Collection of tools and helper scripts for baresip
BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Baresip is a modular SIP user-agent with audio and video support.

This package provides a collection of tools and helper scripts.

%package vp8
Summary:        VP8 video codec module for baresip
BuildRequires:  libvpx-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description vp8
Baresip is a modular SIP user-agent with audio and video support.

This module provides the VP8 video codec, which is compatible with the
WebRTC standard.

%package vp9
Summary:        VP9 video codec module for baresip
BuildRequires:  pkgconfig(vpx) >= 1.3.0
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description vp9
Baresip is a modular SIP user-agent with audio and video support.

This module provides the VP9 video codec, which is compatible with the
WebRTC standard.

%package v4l2
Summary:        Video4Linux video source driver for baresip
BuildRequires:  libv4l-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description v4l2
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Video4Linux video source driver.

%package x11
Summary:        X11 video output driver for baresip
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description x11
Baresip is a modular SIP user-agent with audio and video support.

This module provides the X11 video output driver.

%prep
%setup -q

%build
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-8/enable
RPM_OPT_FLAGS="$RPM_OPT_FLAGS $(pkg-config --cflags-only-I openssl11)"
RPM_LD_FLAGS="$RPM_LD_FLAGS $(pkg-config --libs-only-L openssl11)"
%endif

%make_build \
  SHELL='sh -x' \
  RELEASE=1 \
  PREFIX=%{_prefix} \
  MOD_PATH=%{_libdir}/%{name}/modules \
  EXTRA_CFLAGS="$RPM_OPT_FLAGS -DDEFAULT_CAFILE='\"%{_sysconfdir}/pki/tls/certs/ca-bundle.crt\"' -DDEFAULT_AUDIO_DEVICE='\"pulse\"'" \
  EXTRA_LFLAGS="$RPM_LD_FLAGS"

%install
%make_install LIBDIR=%{_libdir}

# Correct module permissions to add executable bit
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*.so

# Install com.github.baresip.desktop file
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ %{SOURCE1}

# Missing status icons for RHEL 7 and 8 (included since adwaita-icon-theme >= 3.31.91)
%if 0%{?rhel} == 7 || 0%{?rhel} == 8
cp -pf %{SOURCE12} %{SOURCE13} %{SOURCE14} .

install -D -p -m 0644 %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/icons/Adwaita/scalable/status/call-incoming-symbolic.svg
install -D -p -m 0644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/icons/Adwaita/scalable/status/call-outgoing-symbolic.svg

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/Adwaita/16x16/status/
gtk-encode-symbolic-svg %{SOURCE10} 16x16 -o $RPM_BUILD_ROOT%{_datadir}/icons/Adwaita/16x16/status/
gtk-encode-symbolic-svg %{SOURCE11} 16x16 -o $RPM_BUILD_ROOT%{_datadir}/icons/Adwaita/16x16/status/
%endif

# Install (optional) helper script manually
install -p -m 0755 tools/fritzbox2%{name} $RPM_BUILD_ROOT%{_bindir}/fritzbox2%{name}

%check
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-8/enable
RPM_OPT_FLAGS="$RPM_OPT_FLAGS $(pkg-config --cflags-only-I openssl11)"
RPM_LD_FLAGS="$RPM_LD_FLAGS $(pkg-config --libs-only-L openssl11)"
%endif

make test \
  SHELL='sh -x' \
  EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
  EXTRA_LFLAGS="$RPM_LD_FLAGS"

%if 0%{?rhel} == 7
%post gtk
touch --no-create %{_datadir}/icons/Adwaita &>/dev/null || :

%postun gtk
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/Adwaita &>/dev/null
  gtk-update-icon-cache %{_datadir}/icons/Adwaita &>/dev/null || :
fi

%posttrans gtk
gtk-update-icon-cache %{_datadir}/icons/Adwaita &>/dev/null || :
%endif

%if 0%{?rhel} == 8
%transfiletriggerin -- %{_datadir}/icons/Adwaita
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/Adwaita
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :
%endif

%files
%license docs/COPYING
%doc docs/ChangeLog docs/THANKS docs/examples
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/modules/
%{_libdir}/%{name}/modules/account.so
%{_libdir}/%{name}/modules/aubridge.so
%{_libdir}/%{name}/modules/auconv.so
%{_libdir}/%{name}/modules/aufile.so
%{_libdir}/%{name}/modules/auresamp.so
%{_libdir}/%{name}/modules/ausine.so
%{_libdir}/%{name}/modules/cons.so
%{_libdir}/%{name}/modules/contact.so
%{_libdir}/%{name}/modules/ctrl_tcp.so
%{_libdir}/%{name}/modules/debug_cmd.so
%{_libdir}/%{name}/modules/dtls_srtp.so
%{_libdir}/%{name}/modules/ebuacip.so
%{_libdir}/%{name}/modules/echo.so
%{_libdir}/%{name}/modules/evdev.so
%{_libdir}/%{name}/modules/fakevideo.so
%{_libdir}/%{name}/modules/g711.so
%{_libdir}/%{name}/modules/httpd.so
%{_libdir}/%{name}/modules/httpreq.so
%{_libdir}/%{name}/modules/ice.so
%{_libdir}/%{name}/modules/l16.so
%{_libdir}/%{name}/modules/menu.so
%{_libdir}/%{name}/modules/mixausrc.so
%{_libdir}/%{name}/modules/mixminus.so
%{_libdir}/%{name}/modules/multicast.so
%{_libdir}/%{name}/modules/mwi.so
%{_libdir}/%{name}/modules/natpmp.so
%{_libdir}/%{name}/modules/netroam.so
%{_libdir}/%{name}/modules/presence.so
%{_libdir}/%{name}/modules/rtcpsummary.so
%{_libdir}/%{name}/modules/selfview.so
%{_libdir}/%{name}/modules/serreg.so
%{_libdir}/%{name}/modules/srtp.so
%{_libdir}/%{name}/modules/stdio.so
%{_libdir}/%{name}/modules/stun.so
%{_libdir}/%{name}/modules/syslog.so
%{_libdir}/%{name}/modules/turn.so
%{_libdir}/%{name}/modules/uuid.so
%{_libdir}/%{name}/modules/vidbridge.so
%{_libdir}/%{name}/modules/vidinfo.so
%{_libdir}/%{name}/modules/vumeter.so
%{_datadir}/%{name}/

%if 0%{?fedora}
%files aac
%{_libdir}/%{name}/modules/aac.so
%endif

%files alsa
%{_libdir}/%{name}/modules/alsa.so

%files av1
%{_libdir}/%{name}/modules/av1.so

%files codec2
%{_libdir}/%{name}/modules/codec2.so

%files ctrl_dbus
%{_libdir}/%{name}/modules/ctrl_dbus.so

%files g722
%{_libdir}/%{name}/modules/g722.so

%files g726
%{_libdir}/%{name}/modules/g726.so

%files gst
%{_libdir}/%{name}/modules/gst.so

%files gtk
%{_libdir}/%{name}/modules/gtk.so
%{_datadir}/applications/com.github.baresip.desktop
%if 0%{?rhel} == 7 || 0%{?rhel} == 8
%license COPYING*.adwaita-icon-theme
%{_datadir}/icons/Adwaita/16x16/status/call-incoming-symbolic.symbolic.png
%{_datadir}/icons/Adwaita/16x16/status/call-outgoing-symbolic.symbolic.png
%{_datadir}/icons/Adwaita/scalable/status/call-incoming-symbolic.svg
%{_datadir}/icons/Adwaita/scalable/status/call-outgoing-symbolic.svg
%endif

%files jack
%{_libdir}/%{name}/modules/jack.so

%files mpa
%{_libdir}/%{name}/modules/mpa.so

%files mqtt
%{_libdir}/%{name}/modules/mqtt.so

%files opus
%{_libdir}/%{name}/modules/opus.so
%{_libdir}/%{name}/modules/opus_multistream.so

%files plc
%{_libdir}/%{name}/modules/plc.so

%files portaudio
%{_libdir}/%{name}/modules/portaudio.so

%files pulse
%{_libdir}/%{name}/modules/pulse.so
%{_libdir}/%{name}/modules/pulse_async.so

%files sdl
%{_libdir}/%{name}/modules/sdl.so

%files snapshot
%{_libdir}/%{name}/modules/snapshot.so

%files sndfile
%{_libdir}/%{name}/modules/sndfile.so

%files tools
%{_bindir}/fritzbox2%{name}

%files v4l2
%{_libdir}/%{name}/modules/v4l2.so

%files vp8
%{_libdir}/%{name}/modules/vp8.so

%files vp9
%{_libdir}/%{name}/modules/vp9.so

%files x11
%{_libdir}/%{name}/modules/x11.so

%changelog
* Thu Sep 01 2022 Robert Scheck <robert@fedoraproject.org> 2.7.0-1
- Upgrade to 2.7.0 (#2123475)

* Wed Aug 03 2022 Robert Scheck <robert@fedoraproject.org> 2.6.0-2
- Rebuilt for libre 2.6.1

* Tue Aug 02 2022 Robert Scheck <robert@fedoraproject.org> 2.6.0-1
- Upgrade to 2.6.0 (#2113067)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Robert Scheck <robert@fedoraproject.org> 2.5.1-1
- Upgrade to 2.5.1 (#2107946)

* Sat Jul 16 2022 Robert Scheck <robert@fedoraproject.org> 2.5.0-3
- Added upstream patch to fix missing free-line signal regression

* Sat Jul 09 2022 Richard Shaw <hobbes1069@gmail.com> - 2.5.0-2
- Rebuild for codec2 1.0.4.

* Sat Jul 02 2022 Robert Scheck <robert@fedoraproject.org> 2.5.0-1
- Upgrade to 2.5.0 (#2103207)

* Wed Jun 22 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.4.0-2
- Rebuilt for new AOM

* Wed Jun 01 2022 Robert Scheck <robert@fedoraproject.org> 2.4.0-1
- Upgrade to 2.4.0 (#2092576)

* Mon May 02 2022 Robert Scheck <robert@fedoraproject.org> 2.3.0-1
- Upgrade to 2.3.0 (#2080905)

* Sat Apr 09 2022 Robert Scheck <robert@fedoraproject.org> 2.0.2-1
- Upgrade to 2.0.2 (#2073684)

* Mon Mar 28 2022 Robert Scheck <robert@fedoraproject.org> 2.0.1-1
- Upgrade to 2.0.1 (#2068919)

* Sun Mar 13 2022 Robert Scheck <robert@fedoraproject.org> 2.0.0-1
- Upgrade to 2.0.0 (#2063451)

* Thu Jan 27 2022 Tom Callaway <spot@fedoraproject.org> - 1.1.0-8
- rebuild for libvpx

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-6
- Rebuild for codec2 1.0.1.

* Wed Sep 29 2021 Robert Scheck <robert@fedoraproject.org> 1.1.0-5
- Added upstream feature patch for GTK+ attended transfers

* Wed Aug 11 2021 Robert Scheck <robert@fedoraproject.org> 1.1.0-4
- Rebuilt for codec2 1.0.0 (#1991468)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Robert Scheck <robert@fedoraproject.org> 1.1.0-2
- Enable baresip-mpa subpackage on RHEL 8 since twolame-devel is
  available since RHEL >= 8.4 (#1843275)

* Sat Apr 24 2021 Robert Scheck <robert@fedoraproject.org> 1.1.0-1
- Upgrade to 1.1.0 (#1953196)
- Added upstream feature patch for GTK+ call history

* Sun Apr 11 2021 Robert Scheck <robert@fedoraproject.org> 1.0.0-4
- Rebuilt for libre 2.0.0 and librem 1.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Robert Scheck <robert@fedoraproject.org> 1.0.0-2
- Added weak run-time dependency for libcanberra-gtk2 to the gtk
  subpackage (thanks to Jochen Steudinger)

* Sat Oct 10 2020 Robert Scheck <robert@fedoraproject.org> 1.0.0-1
- Upgrade to 1.0.0 (#1887059)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Robert Scheck <robert@fedoraproject.org> 0.6.6-2
- Include latest features and fixes from upstream
- Changes to match the Fedora Packaging Guidelines (#1843279 #c1)

* Thu May 28 2020 Robert Scheck <robert@fedoraproject.org> 0.6.6-1
- Upgrade to 0.6.6 (#1843279)
- Initial spec file for Fedora and Red Hat Enterprise Linux
