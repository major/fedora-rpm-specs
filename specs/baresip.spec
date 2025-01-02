Summary:        Modular SIP user-agent with audio and video support
Name:           baresip
Version:        3.18.0
Release:        3%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/baresip/baresip
Source0:        https://github.com/baresip/baresip/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/1e1d692148e8ab958bfea4188f8575b673804e09/Adwaita/scalable/status/call-incoming-symbolic.svg
Source11:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/1e1d692148e8ab958bfea4188f8575b673804e09/Adwaita/scalable/status/call-outgoing-symbolic.svg
Source12:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/master/COPYING#/COPYING.adwaita-icon-theme
Source13:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/master/COPYING_CCBYSA3#/COPYING_CCBYSA3.adwaita-icon-theme
Source14:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/master/COPYING_LGPL#/COPYING_LGPL.adwaita-icon-theme
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libre-devel >= 3.18.0
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  openssl-devel
Recommends:     %{name}-pipewire%{?_isa} = %{version}-%{release}
%else
# https://github.com/baresip/re/pull/1015
BuildRequires:  openssl3-devel
Recommends:     %{name}-pulse%{?_isa} = %{version}-%{release}
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

%package devel
Summary:        Development files for the baresip library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
The baresip-devel package includes header files and libraries necessary
for developing programs which use the baresip C library.

%if 0%{?fedora} || 0%{?rhel} >= 9
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

%if 0%{?fedora} || 0%{?rhel} >= 9
%package avcodec
Summary:        AVCodec video codec module for baresip
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description avcodec
Baresip is a modular SIP user-agent with audio and video support.

This module implements H.264 and H.265 video codecs using libavcodec from
the FFmpeg project.

%package avfilter
Summary:        AVFilter video filter for baresip
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description avfilter
Baresip is a modular SIP user-agent with audio and video support.

This module allows to dynamically apply complex video filter graphs to
the outcoming stream using libavfilter from the FFmpeg project.

%package avformat
Summary:        AVFormat video source driver for baresip
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description avformat
Baresip is a modular SIP user-agent with audio and video support.

This module provides a video source driver using libavformat from the
FFmpeg project.
%endif

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
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires:       adwaita-icon-theme >= 3.31.91-1
Requires:       (gnome-shell-extension-appindicator if gnome-shell)
%else
License:        BSD-3-Clause AND (LGPL-3.0-or-later OR CC-BY-SA-3.0)
BuildRequires:  librsvg2
BuildRequires:  %{_bindir}/gtk-encode-symbolic-svg
Requires:       adwaita-icon-theme < 3.31.91-1
Requires:       (gnome-shell-extension-topicons-plus if gnome-shell)
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     libcanberra-gtk3

%description gtk
Baresip is a modular SIP user-agent with audio and video support.

This module provides a GTK+ menu-based user interface.

Note: GTK+ defaults to the Wayland backend, which baresip does not
support. Use 'GDK_BACKEND=x11 baresip' to override it to Xwayland.

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
BuildRequires:  speexdsp-devel
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

%if 0%{?fedora} || 0%{?rhel} >= 9
%package pipewire
Summary:        PipeWire audio driver for baresip
BuildRequires:  pkgconfig(libpipewire-0.3)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description pipewire
Baresip is a modular SIP user-agent with audio and video support.

This module provides the PipeWire audio driver.
%endif

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
BuildRequires:  pkgconfig(libpulse)
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

%if 0%{?fedora} || 0%{?rhel} >= 9
%package swscale
Summary:        SWScale video filter for baresip
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description swscale
Baresip is a modular SIP user-agent with audio and video support.

This module provides a video filter for scaling and pixel conversion
using libswscale from the FFmpeg project.
%endif

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
%autosetup -p1

%build
%cmake \
  -DDEFAULT_CAFILE:PATH="%{_sysconfdir}/pki/tls/certs/ca-bundle.crt" \
  -DDEFAULT_CAPATH:PATH="%{_sysconfdir}/pki/tls/certs" \
%if 0%{?fedora} || 0%{?rhel} >= 9
  -DDEFAULT_AUDIO_DEVICE:STRING="pipewire" \
%else
  -DDEFAULT_AUDIO_DEVICE:STRING="pulse" \
%endif
%if 0%{?rhel} == 8
  -DOPENSSL_ROOT_DIR:PATH="%{_includedir}/openssl3;%{_libdir}/openssl3"
%endif

%cmake_build

%install
%cmake_install

# Missing status icons for RHEL 8 (included since adwaita-icon-theme >= 3.31.91)
%if 0%{?rhel} == 8
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
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/com.github.baresip.desktop

%if !0%{?__cmake_in_source_build}
cd %{__cmake_builddir}
%endif
./test/selftest -d %{!?__cmake_in_source_build:../}test/data/ -v

%ldconfig_scriptlets

%if 0%{?rhel} == 8
%transfiletriggerin -- %{_datadir}/icons/Adwaita
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/Adwaita
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :
%endif

%files
%license LICENSE
%doc CHANGELOG.md docs/THANKS docs/examples
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.19*
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/modules/
%{_libdir}/%{name}/modules/account.so
%{_libdir}/%{name}/modules/aubridge.so
%{_libdir}/%{name}/modules/auconv.so
%{_libdir}/%{name}/modules/aufile.so
%{_libdir}/%{name}/modules/augain.so
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
%{_libdir}/%{name}/modules/in_band_dtmf.so
%{_libdir}/%{name}/modules/l16.so
%{_libdir}/%{name}/modules/menu.so
%{_libdir}/%{name}/modules/mixausrc.so
%{_libdir}/%{name}/modules/mixminus.so
%{_libdir}/%{name}/modules/mwi.so
%{_libdir}/%{name}/modules/natpmp.so
%{_libdir}/%{name}/modules/netroam.so
%{_libdir}/%{name}/modules/pcp.so
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

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/lib%{name}.pc

%if 0%{?fedora} || 0%{?rhel} >= 9
%files aac
%{_libdir}/%{name}/modules/aac.so
%endif

%files alsa
%{_libdir}/%{name}/modules/alsa.so

%files av1
%{_libdir}/%{name}/modules/av1.so

%if 0%{?fedora} || 0%{?rhel} >= 9
%files avcodec
%{_libdir}/%{name}/modules/avcodec.so

%files avfilter
%{_libdir}/%{name}/modules/avfilter.so

%files avformat
%{_libdir}/%{name}/modules/avformat.so
%endif

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
%if 0%{?rhel} == 8
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

%if 0%{?fedora} || 0%{?rhel} >= 9
%files pipewire
%{_libdir}/%{name}/modules/pipewire.so
%endif

%files plc
%{_libdir}/%{name}/modules/plc.so

%files portaudio
%{_libdir}/%{name}/modules/portaudio.so

%files pulse
%{_libdir}/%{name}/modules/pulse.so

%files sdl
%{_libdir}/%{name}/modules/sdl.so

%files snapshot
%{_libdir}/%{name}/modules/snapshot.so

%files sndfile
%{_libdir}/%{name}/modules/sndfile.so

%if 0%{?fedora} || 0%{?rhel} >= 9
%files swscale
%{_libdir}/%{name}/modules/swscale.so
%endif

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
* Tue Dec 31 2024 Robert Scheck <robert@fedoraproject.org> 3.18.0-3
- Add the baresip-avcodec, baresip-avfilter, baresip-avformat and
  baresip-swscale subpackages for Fedora and RHEL 9 (and newer)

* Tue Dec 24 2024 Robert Scheck <robert@fedoraproject.org> 3.18.0-2
- Enable baresip-aac subpackage on RHEL 9 and later

* Thu Dec 12 2024 Robert Scheck <robert@fedoraproject.org> 3.18.0-1
- Upgrade to 3.18.0 (#2331640)

* Sat Nov 09 2024 Robert Scheck <robert@fedoraproject.org> 3.17.1-1
- Upgrade to 3.17.1 (#2324903)

* Fri Nov 08 2024 Robert Scheck <robert@fedoraproject.org> 3.17.0-1
- Upgrade to 3.17.0 (#2324341)

* Thu Oct 03 2024 Robert Scheck <robert@fedoraproject.org> 3.16.0-1
- Upgrade to 3.16.0 (#2316283)

* Sat Sep 14 2024 Robert Scheck <robert@fedoraproject.org> 3.15.0-1
- Upgrade to 3.15.0 (#2309007)

* Tue Jul 23 2024 Robert Scheck <robert@fedoraproject.org> 3.14.0-1
- Upgrade to 3.14.0 (#2299492)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Robert Scheck <robert@fedoraproject.org> 3.13.0-1
- Upgrade to 3.13.0 (#2293512)

* Tue May 28 2024 Robert Scheck <robert@fedoraproject.org> 3.12.1-1
- Upgrade to 3.12.1 (#2283595)

* Mon May 20 2024 Robert Scheck <robert@fedoraproject.org> 3.12.0-1
- Upgrade to 3.12.0

* Thu Apr 11 2024 Robert Scheck <robert@fedoraproject.org> 3.11.0-1
- Upgrade to 3.11.0 (#2274242)

* Tue Mar 12 2024 Robert Scheck <robert@fedoraproject.org> 3.10.1-1
- Upgrade to 3.10.1 (#2269261)

* Mon Mar 11 2024 Robert Scheck <robert@fedoraproject.org> 3.10.0-2
- Added upstream patch to fix mtx_unlock on discard in aureceiver

* Sun Mar 10 2024 Robert Scheck <robert@fedoraproject.org> 3.10.0-1
- Upgrade to 3.10.0 (#2268424)

* Wed Feb 07 2024 Pete Walter <pwalter@fedoraproject.org> - 3.9.0-2
- Rebuild for libvpx 1.14.x

* Thu Feb 01 2024 Robert Scheck <robert@fedoraproject.org> 3.9.0-1
- Upgrade to 3.9.0 (#2262187)

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 06 2024 Robert Scheck <robert@fedoraproject.org> 3.8.1-1
- Upgrade to 3.8.1 (#2256553)

* Thu Dec 28 2023 Robert Scheck <robert@fedoraproject.org> 3.8.0-1
- Upgrade to 3.8.0 (#2256050)

* Sun Nov 26 2023 Robert Scheck <robert@fedoraproject.org> 3.7.0-1
- Upgrade to 3.7.0 (#2251125)

* Sun Oct 29 2023 Robert Scheck <robert@fedoraproject.org> 3.6.0-1
- Upgrade to 3.6.0 (#2244802)

* Sun Sep 17 2023 Robert Scheck <robert@fedoraproject.org> 3.5.1-1
- Upgrade to 3.5.1 (#2238647)

* Sat Aug 12 2023 Robert Scheck <robert@fedoraproject.org> 3.4.0-1
- Upgrade to 3.4.0 (#2230766)

* Sat Aug 05 2023 Richard Shaw <hobbes1069@gmail.com> - 3.3.0-3
- Rebuild for codec2.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Robert Scheck <robert@fedoraproject.org> 3.3.0-1
- Upgrade to 3.3.0 (#2220879)

* Wed May 31 2023 Robert Scheck <robert@fedoraproject.org> 3.2.0-1
- Upgrade to 3.2.0 (#2211408)

* Thu Apr 27 2023 Robert Scheck <robert@fedoraproject.org> 3.1.0-1
- Upgrade to 3.1.0 (#2190310)

* Mon Mar 20 2023 Robert Scheck <robert@fedoraproject.org> 3.0.0-1
- Upgrade to 3.0.0 (#2180064)
- Added (hopefully future upstream) patch for PipeWire support

* Sat Feb 18 2023 Robert Scheck <robert@fedoraproject.org> 2.12.0-1
- Upgrade to 2.12.0 (#2170292)

* Wed Feb 15 2023 Tom Callaway <spot@fedoraproject.org> - 2.11.0-3
- rebuild for libvpx

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Robert Scheck <robert@fedoraproject.org> 2.11.0-1
- Upgrade to 2.11.0 (#2160564)

* Wed Dec 07 2022 Robert Scheck <robert@fedoraproject.org> 2.10.0-1
- Upgrade to 2.10.0 (#2151456)

* Thu Nov 17 2022 Robert Scheck <robert@fedoraproject.org> 2.9.0-4
- Added upstream patch to fix GTK+ dial history space error

* Tue Nov 08 2022 Robert Scheck <robert@fedoraproject.org> 2.9.0-3
- Added upstream patch to fix GTK+ dial segfault regression

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 2.9.0-2
- Rebuild for updated codec2.

* Tue Nov 01 2022 Robert Scheck <robert@fedoraproject.org> 2.9.0-1
- Upgrade to 2.9.0 (#2139174)

* Tue Oct 11 2022 Robert Scheck <robert@fedoraproject.org> 2.8.2-1
- Upgrade to 2.8.2 (#2133869)

* Sat Oct 01 2022 Robert Scheck <robert@fedoraproject.org> 2.8.1-1
- Upgrade to 2.8.1 (#2131453)

* Sat Oct 01 2022 Robert Scheck <robert@fedoraproject.org> 2.8.0-1
- Upgrade to 2.8.0

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
