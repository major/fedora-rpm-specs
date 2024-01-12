# codecs which cannot be shipped in Fedora proper
%bcond freeworld 0
%bcond faad2 %{with freeworld}
%bcond x264 %{with freeworld}
%bcond x265 %{with freeworld}

# not compatible with asdcplib-2.12
%bcond asdcp %[!(0%{?fedora} >= 38 || 0%{?rhel} >= 10)]
# not compatible with opencv 3.4 or 4.0
# https://code.videolan.org/videolan/vlc/-/issues/22016
%bcond opencv 0
# not compatible with libplacebo-6
# https://code.videolan.org/videolan/vlc/-/merge_requests/3950
%bcond placebo %[!(0%{?fedora} >= 39 || 0%{?rhel} >= 10)]
# disabled due to various issues
%bcond projectm 0

%ifnarch s390x
%bcond crystalhd %[0%{?fedora} || 0%{?rhel} < 9]
%bcond ieee1394 1
%endif

%ifarch x86_64
%bcond vpl 1
%endif

Name:		vlc
Epoch:		1
Version:	3.0.20
Release:	%autorelease -b 3
Summary:	The cross-platform open-source multimedia framework, player and server
License:	GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause
URL:		https://www.videolan.org
Source:		https://get.videolan.org/vlc/%{version}/vlc-%{version}.tar.xz
Source:         macros.vlc
# https://fedoraproject.org/wiki/Changes/CryptoPolicy
Patch:		0001-Use-SYSTEM-wide-ciphers-for-gnutls.patch
# Fix building with fdk-aac-2.0; backport for 3.0 from flathub
Patch:		fdk-aac2.patch
# separate avcodec-vaapi conditional from other vaapi modules
Patch:		vaapi-without-ffmepg4.patch
# port from intel-mediasdk to oneVPL
Patch:          oneVPL.patch

%{load:%{S:1}}
%global __provides_exclude_from ^%{vlc_plugindir}/.*$

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib

BuildRequires:	a52dec-devel
BuildRequires:	aalib-devel
%if %{with faad2}
BuildRequires:	faad2-devel
%endif
BuildRequires:	hostname
BuildRequires:	kernel-headers
%if %{with crystalhd}
BuildRequires:	libcrystalhd-devel
%endif
BuildRequires:	libgcrypt-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libpng-devel
BuildRequires:	lirc-devel
BuildRequires:	live555-devel
BuildRequires:	lua-devel
BuildRequires:	pkgconfig(alsa) >= 1.0.24
BuildRequires:	pkgconfig(aom)
#BuildRequires:	pkgconfig(aribb24)
#BuildRequires:	pkgconfig(aribb25)
%if %{with asdcp}
BuildRequires:	pkgconfig(asdcplib)
%endif
BuildRequires:	pkgconfig(avahi-client) >= 0.6
#BuildRequires:	pkgconfig(breakpad-client)
BuildRequires:	pkgconfig(caca) >= 0.99.beta14
BuildRequires:	pkgconfig(daaladec)
BuildRequires:	pkgconfig(daalaenc)
BuildRequires:	pkgconfig(dav1d)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dvdnav) > 4.9.0
BuildRequires:	pkgconfig(dvdread) > 4.9.0
BuildRequires:	pkgconfig(egl)
#BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(fdk-aac)
BuildRequires:	pkgconfig(flac)
#BuildRequires:	pkgconfig(fluidlite)
BuildRequires:	pkgconfig(fluidsynth) >= 1.1.2
BuildRequires:	pkgconfig(fontconfig) >= 2.11
#BuildRequires:	pkgconfig(freerdp)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(gnutls) >= 3.3.6
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(gstreamer-video-1.0)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(jack) >= 1.9.7
BuildRequires:	pkgconfig(kate) >= 0.3.0
BuildRequires:	pkgconfig(libarchive) >= 3.1.0
BuildRequires:	pkgconfig(libass) >= 0.9.8
BuildRequires:	pkgconfig(libavcodec) >= 57.37.100
BuildRequires:	pkgconfig(libavformat) >= 53.21.0
BuildRequires:	pkgconfig(libavutil) >= 52.0.0
BuildRequires:	pkgconfig(libbluray) >= 0.6.2
BuildRequires:	pkgconfig(libcddb) >= 0.9.5
BuildRequires:	pkgconfig(libchromaprint)
%if %{with ieee1394}
BuildRequires:	pkgconfig(libdc1394-2) >= 2.1.0
%endif
BuildRequires:	pkgconfig(libdca) >= 0.0.5
#BuildRequires:	pkgconfig(libdsm) >= 0.2.0
BuildRequires:	pkgconfig(libdvbpsi)
BuildRequires:	pkgconfig(libebml) >= 1.3.6
BuildRequires:	pkgconfig(libgme)
#BuildRequires:	pkgconfig(libgoom2)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(libmatroska)
BuildRequires:	pkgconfig(libmodplug) >= 0.8.9.0
BuildRequires:	pkgconfig(libmpeg2) >= 0.3.2
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libmtp) >= 1.0.0
BuildRequires:	pkgconfig(libnfs) >= 1.10.0
BuildRequires:	pkgconfig(libnotify) pkgconfig(gtk+-3.0)
%if %{with placebo}
BuildRequires:	pkgconfig(libplacebo) >= 0.2.1
%endif
BuildRequires:	pkgconfig(libpostproc)
%if %{with projectm}
BuildRequires:	pkgconfig(libprojectM)
%endif
BuildRequires:	pkgconfig(libpulse) >= 1.0
%if %{with ieee1394}
BuildRequires:	pkgconfig(libraw1394) >= 2.0.1 pkgconfig(libavc1394) >= 0.5.3
%endif
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.9.0
BuildRequires:	pkgconfig(libsecret-1) >= 0.18
#BuildRequires:	pkgconfig(libsidplay2)
#BuildRequires:	pkgconfig(libsmb2) >= 3.0.0
BuildRequires:	pkgconfig(libssh2)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libudev) >= 142
BuildRequires:	pkgconfig(libupnp)
BuildRequires:	pkgconfig(libva) >= 0.38
BuildRequires:	pkgconfig(libva-drm)
BuildRequires:	pkgconfig(libva-wayland)
BuildRequires:	pkgconfig(libva-x11)
BuildRequires:	pkgconfig(libvncclient) >= 0.9.9
#BuildRequires:	pkgconfig(libvsxu)
BuildRequires:	pkgconfig(libxml-2.0) >= 2.5
BuildRequires:	pkgconfig(microdns) >= 0.1.2
BuildRequires:	pkgconfig(minizip)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(ogg) >= 1.0
%if %{with opencv}
BuildRequires:	pkgconfig(opencv)
%endif
BuildRequires:	pkgconfig(opus) >= 1.0.3
BuildRequires:	pkgconfig(protobuf-lite) >= 2.5
BuildRequires:	pkgconfig(Qt5Core) >= 5.5
BuildRequires:	pkgconfig(Qt5Gui) >= 5.5
BuildRequires:	pkgconfig(Qt5Svg) >= 5.5
BuildRequires:	pkgconfig(Qt5Widgets) >= 5.5
BuildRequires:	pkgconfig(Qt5X11Extras) >= 5.5
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(schroedinger-1.0) >= 1.0.10
BuildRequires:	pkgconfig(SDL_image) >= 1.2.10
#BuildRequires:	pkgconfig(shine) >= 3.0.0
BuildRequires:	pkgconfig(shout) >= 2.1
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(soxr) >= 0.1.2
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(spatialaudio)
BuildRequires:	pkgconfig(speex) >= 1.0.5
BuildRequires:	pkgconfig(speexdsp)
BuildRequires:	pkgconfig(srt) >= 1.3.0
BuildRequires:	pkgconfig(taglib) >= 1.9
BuildRequires:	pkgconfig(theoradec)
BuildRequires:	pkgconfig(theoraenc)
BuildRequires:	pkgconfig(tiger) >= 0.3.1
BuildRequires:	pkgconfig(twolame)
BuildRequires:	pkgconfig(vdpau) >= 0.6
BuildRequires:	pkgconfig(vorbis) >= 1.1
BuildRequires:	pkgconfig(vorbisenc) >= 1.1
%if %{with vpl}
BuildRequires:	pkgconfig(vpl)
%endif
BuildRequires:	pkgconfig(vpx) >= 1.5.0
BuildRequires:	pkgconfig(wayland-client) >= 1.5.91
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-protocols)
#BuildRequires:	pkgconfig(x262)
%if %{with x264}
BuildRequires:	pkgconfig(x264) >= 0.153
%endif
%if %{with x265}
BuildRequires:	pkgconfig(x265)
%endif
BuildRequires:	pkgconfig(xcb) >= 1.6
BuildRequires:	pkgconfig(xcb-composite)
BuildRequires:	pkgconfig(xcb-keysyms) >= 0.3.4
BuildRequires:	pkgconfig(xcb-randr) >= 1.3
BuildRequires:	pkgconfig(xcb-shm)
BuildRequires:	pkgconfig(xcb-xv) >= 1.1.90.1
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(zvbi-0.2) >= 0.2.28
BuildRequires:	qt5-qtbase-private-devel
BuildRequires:	zlib-devel

Provides:	%{name}-xorg%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-gui-qt%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:	%{name}-gui-skins2%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:	%{name}-plugin-ffmpeg%{?_isa} = %{epoch}:%{version}-%{release}

Requires:       hicolor-icon-theme
%if %{undefined flatpak}
Requires:       kf5-filesystem
%endif
# For xdg-screensaver (libxdg_screensaver_plugin)
Recommends:	xdg-utils


%description
VLC media player is a highly portable multimedia player and multimedia framework
capable of reading most audio and video formats as well as DVDs, Audio CDs VCDs,
and various streaming protocols.
It can also be used as a media converter or a server to stream in uni-cast or
multi-cast in IPv4 or IPv6 on networks.

%package libs
Summary:	VLC media player runtime libraries
Recommends:	libproxy-bin%{?_isa}
Conflicts:	%{name}-core < %{epoch}:%{version}-%{release}
%description libs
VLC media player runtime libraries

%package cli
Summary:	VLC media player command line interface
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:	%{name}-plugin-lua%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-core < %{epoch}:%{version}-%{release}
Provides:	%{name}-core = %{epoch}:%{version}-%{release}
Provides:	%{name}-nox = %{epoch}:%{version}-%{release}
%description cli
VLC media player command line interfaces

%package gui-ncurses
Summary:	VLC media player TUI
Requires:	%{name}-cli%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description gui-ncurses
VLC media player ncurses-based terminal interface

%package gui-qt
Summary:	VLC media player Qt GUI
Requires:	%{name}-cli%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-video-out%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugin-lua%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	(qt5-qtwayland%{?_isa} if libwayland-client%{?_isa})
Recommends:	%{name}-plugin-ffmpeg%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:	%{name}-plugin-visualization%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:	(%{name}-plugin-gnome%{?_isa} = %{epoch}:%{version}-%{release} if gnome-keyring)
Recommends:	(%{name}-plugin-kde%{?_isa} = %{epoch}:%{version}-%{release} if kf5-kwallet)
Recommends:	(%{name}-plugin-notify%{?_isa} = %{epoch}:%{version}-%{release} if gtk3)
Recommends:	(%{name}-plugin-pulseaudio%{?_isa} = %{epoch}:%{version}-%{release} or vlc-plugin-pipewire%{?_isa})
%description gui-qt
VLC media player Qt graphical interface

%package gui-skins2
Summary:	VLC media player Skins2 GUI
Requires:	%{name}-cli%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-gui-qt%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnu-free-sans-fonts
%description gui-skins2
VLC media player skinnable graphical interface

%package plugins-base
Summary:	VLC media player core
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 10
Requires:	google-noto-sans-mono-fonts
Requires:	google-noto-serif-fonts
%else
Requires:	google-noto-sans-mono-vf-fonts
Requires:	google-noto-serif-vf-fonts
%endif
Recommends:	libv4l%{?_isa}
Conflicts:	%{name}-core < %{epoch}:%{version}-%{release}
%description plugins-base
VLC media player core components

# libcrystalhd requires crystalhd-firmware, is for specific hardware
%if %{with crystalhd}
%package plugin-crystalhd
Summary:	VLC media player Crystal HD plugin
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-extras < %{epoch}:%{version}-%{release}
Provides:	%{name}-extras = %{epoch}:%{version}-%{release}
%description plugin-crystalhd
Crystal HD plugin for VLC media player
%endif

# libavcodec/libavformat etc. have many dependencies
%package plugin-ffmpeg
Summary:	VLC media player FFmpeg plugins
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-ffmpeg
FFmpeg support plugins for VLC media player

# for MIDI playback, requires a soundfont (usually quite large)
%package plugin-fluidsynth
Summary:	VLC media player MIDI playback plugin
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:     fluid-soundfont-gm
%description plugin-fluidsynth
MIDI playback support plugin for VLC media player

# requires libsecret, for gnome-keyring secrets storage on GNOME
%package plugin-gnome
Summary:	VLC media player Gnome Keyring plugin
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-gnome
Gnome Keyring integration for VLC media player

# alternative codecs for specific formats, requires many of its own plugins
%package plugin-gstreamer
Summary:	VLC media player GStreamer codec plugin
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	gstreamer1-plugins-good%{?_isa}
Requires:	gstreamer1-plugins-bad-free%{?_isa}
Recommends:	gstreamer1-plugin-libav%{?_isa}
Recommends:	gstreamer1-plugin-openh264%{?_isa}
%description plugin-gstreamer
GStreamer decoder plugins for VLC media player

# requires libdc1394/libavc1394/libraw1394, is for specific hardware
%if %{with ieee1394}
%package plugin-ieee1394
Summary:	VLC media player IEEE 1394 plugins
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-ieee1394
IEEE 1394 (FireWire) plugins for VLC media player
%endif

# depends on j-a-c-k or pipewire-j-a-c-k, for low-latency audio
%package plugin-jack
Summary:	VLC media player JACK plugins
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Suggests:       pipewire-jack-audio-connection-kit
%description plugin-jack
PulseAudio plugins for VLC media player

# for KWallet secrets storage on KDE Plasma
%package plugin-kde
Summary:	VLC media player KWallet plugin
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-kde
KDE KWallet integration for VLC media player

# requires lua, used by CLI and GUI
%package plugin-lua
Summary:	VLC media player lua scripting plugins
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%{?lua_version:Requires: lua(abi) = %{lua_version}}
%description plugin-lua
Lua scripting support for VLC media player

# requires gtk3 to render the notification icon
%package plugin-notify
Summary:	VLC media player notification plugin
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-notify
Desktop notification plugin for VLC media player

# opencv has many dependencies
%if %{with opencv}
%package plugin-opencv
Summary:	VLC media player OpenCV plugins
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-opencv
OpenCV plugins for VLC media player
%endif

# uses libpulse to connect to pipewire-pulseaudio
# vlc-plugin-pipewire plugin is an alternative
%package plugin-pulseaudio
Summary:	VLC media player PulseAudio plugins
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-pulseaudio
PulseAudio plugins for VLC media player

# requires libsmbclient, for SMB protocol support
%package plugin-samba
Summary:	VLC media player SMB plugin
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-samba
Samba access plugin for VLC media player

# requires librsvg2, for SVG decoding and screen overlay
%package plugin-svg
Summary:	VLC media player SVG plugins
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-svg
SVG plugins for VLC media player

# requires libv4l, libva, OpenGL, X11/xcb, etc.
%package plugins-video-out
Summary:	VLC media player vout plugins
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugins-video-out
Video output plugins for VLC media player

%package plugin-visualization
Summary:	VLC media player visualization plugins
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-visualization
Visualization plugins for VLC media player

%package plugin-vnc
Summary:	VLC media player VNC plugin
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description plugin-vnc
VNC access plugin for VLC media player

%package devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications and plugins that use %{name}.


%prep
%autosetup -p1

rm -f aclocal.m4 m4/lib*.m4 m4/lt*.m4
./bootstrap

# switch "Allow automatic icon change" to opt-in
sed -i -e 's|\("qt-icon-change",\) true|\1 false|' modules/gui/qt/qt.cpp

# sync appstream app-id with Flathub
sed -i -e 's|org\.videolan\.vlc|org.videolan.VLC|' share/vlc.appdata.xml.in.in

%if 0%{?flatpak}
# icons are renamed in order to be exported
sed -i -e '/icon_theme_load/s|"vlc"|"org.videolan.VLC"|' modules/notify/notify.c
sed -i -e '/fromTheme/s|"vlc"|"org.videolan.VLC"|' \
	modules/gui/qt/main_interface.cpp modules/gui/qt/qt.cpp
%endif

touch src/revision.txt


%build
export LIVE555_PREFIX=%{_prefix}
%configure 							\
	--disable-silent-rules					\
	--disable-dependency-tracking				\
	--with-binary-version=%{version}			\
	--disable-static					\
	--with-pic						\
	--disable-rpath						\
	--enable-dbus						\
	--disable-optimizations					\
	--enable-lua						\
								\
	--enable-archive					\
	--enable-live555					\
	--enable-dc1394%{!?with_ieee1394:=no}			\
	--enable-dv1394%{!?with_ieee1394:=no}			\
	--enable-linsys						\
	--enable-dvdread					\
	--enable-dvdnav						\
	--enable-bluray						\
	--enable-opencv%{!?with_opencv:=no}			\
	--enable-smbclient					\
	--disable-dsm						\
	--enable-sftp						\
	--enable-nfs						\
	--disable-smb2						\
	--enable-v4l2						\
	--disable-decklink					\
	--enable-vcd						\
	--enable-libcddb					\
	--enable-screen						\
	--enable-vnc						\
	--disable-freerdp					\
	--enable-realrtsp					\
	--enable-asdcp%{!?with_asdcp:=no}			\
								\
	--enable-dvbpsi						\
	--enable-gme						\
	--disable-sid						\
	--enable-ogg						\
	--enable-shout						\
	--enable-matroska					\
	--enable-mod						\
	--enable-mpc						\
								\
	--disable-shine						\
	--disable-omxil						\
	--enable-crystalhd%{!?with_crystalhd:=no}		\
	--enable-mad						\
	--enable-mpg123						\
	--enable-gst-decode					\
	--enable-avcodec					\
	--enable-libva						\
	--enable-avformat					\
	--enable-swscale					\
	--enable-postproc					\
	--enable-faad%{!?with_faad2:=no}			\
	--enable-aom						\
	--enable-dav1d						\
	--enable-vpx						\
	--enable-twolame					\
	--enable-fdkaac						\
	--enable-a52						\
	--enable-dca						\
	--enable-flac						\
	--enable-libmpeg2					\
	--enable-vorbis						\
	--enable-tremor						\
	--enable-speex						\
	--enable-opus						\
	--enable-spatialaudio					\
	--enable-theora						\
	--enable-oggspots					\
	--enable-daala						\
	--enable-schroedinger					\
	--enable-png						\
	--enable-jpeg						\
	--disable-bpg						\
	--disable-x262						\
	--enable-x265%{!?with_x265:=no}				\
	--enable-x264%{!?with_x264:=no}				\
	--enable-x26410b%{!?with_x264:=no}			\
	--enable-vpl%{!?with_vpl:=no}				\
	--enable-fluidsynth					\
	--disable-fluidlite					\
	--enable-zvbi						\
	--disable-telx						\
	--enable-libass						\
	--disable-aribsub					\
	--disable-aribb25					\
	--enable-kate						\
	--enable-tiger						\
	--enable-css						\
								\
	--enable-gles2						\
	--enable-xcb						\
	--enable-xvideo						\
	--enable-vdpau						\
	--enable-wayland					\
	--enable-sdl-image					\
	--enable-freetype					\
	--enable-fribidi					\
	--enable-harfbuzz					\
	--enable-fontconfig					\
	--with-default-font-family=NotoSerif			\
	--with-default-monospace-font-family=NotoSansMono	\
	--enable-svg						\
	--enable-svgdec						\
	--enable-aa						\
	--enable-caca						\
	--disable-mmal						\
	--disable-evas						\
								\
	--enable-pulse						\
	--enable-alsa						\
	--enable-jack						\
	--enable-samplerate					\
	--enable-soxr						\
	--enable-chromaprint					\
	--enable-chromecast					\
								\
	--enable-qt						\
	--enable-skins2						\
	--disable-libtar					\
	--enable-lirc						\
	--enable-srt						\
								\
	--disable-goom						\
	--enable-projectm%{!?with_projectm:=no}			\
	--disable-vsxu						\
								\
	--enable-avahi						\
	--enable-udev						\
	--enable-mtp						\
	--enable-upnp						\
	--enable-microdns					\
								\
	--enable-libxml2					\
	--enable-libgcrypt					\
	--enable-gnutls						\
	--enable-taglib						\
	--enable-secret						\
	--enable-kwallet					\
	--disable-update-check					\
	--enable-notify						\
	--enable-libplacebo%{!?with_placebo:=no}		\
	--with-kde-solid=%{_datadir}/solid/actions		\
	%{nil}

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build


%install
%make_install CPPROG="cp -p"

# RPM macros for other vlc-plugin-* packages
install -D -m0644 %{S:1} %{buildroot}%{_rpmmacrodir}/macros.vlc

# Ghost the plugins cache
touch %{buildroot}%{vlc_plugindir}/plugins.dat

# Use installed fonts for skins2; gnu-free is part of flatpak runtime
rm -f %{buildroot}%{_datadir}/vlc/skins2/fonts/FreeSans{,Bold}.ttf
ln -s %{_usr}/share/fonts/gnu-free/FreeSans{,Bold}.ttf %{buildroot}%{_datadir}/vlc/skins2/fonts/

# Remove libtool libraries (for RHEL 9 and older)
find %{buildroot}%{_libdir} -name '*.la' -delete

# unpackaged static library
rm -f %{buildroot}%{_libdir}/vlc/libcompat.*

# GNOME 2 script, not compatible with GNOME 3+
rm -f %{buildroot}%{_datadir}/vlc/utils/gnome-vlc-default.sh

# The default PNG icons are used for desktop menu, notifications, and SNI;
# all other icons are compiled in as resources
find %{buildroot}%{_datadir}/icons/hicolor -type f ! -name 'vlc.png' -delete
rm -f %{buildroot}%{_datadir}/vlc/vlc.ico

# docs will be installed in %%files
rm -rf %{buildroot}%{_docdir}/vlc

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/vlc.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/vlc.appdata.xml

# chroma_copy_test fails on s390x (big endian?)
%ifnarch s390x
make check
%endif


%transfiletriggerin libs -- %{vlc_plugindir}
%{_libdir}/vlc/vlc-cache-gen %{vlc_plugindir} &>/dev/null || :

%transfiletriggerpostun libs -- %{vlc_plugindir}
%{_libdir}/vlc/vlc-cache-gen %{vlc_plugindir} &>/dev/null || :


%files
%doc AUTHORS NEWS README THANKS
%license COPYING COPYING.LIB
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/solid/actions/%{name}-*.desktop
%{_datadir}/vlc/utils/
%{_metainfodir}/%{name}.appdata.xml

%files libs -f %{name}.lang
%license COPYING.LIB
# client library, used by e.g. kaffeine, phonon-backend-vlc, etc.
%{_libdir}/libvlc.so.5{,.*}
# plugin API, used by vlc-plugin(s)-*
%{_libdir}/libvlccore.so.9{,.*}
%dir %{_libdir}/vlc/
%{_libdir}/vlc/vlc-cache-gen
%dir %{vlc_plugindir}
%ghost %{vlc_plugindir}/plugins.dat

%files cli
%{_bindir}/vlc
%{_bindir}/cvlc
%{_bindir}/rvlc
%{_bindir}/vlc-wrapper
%{_mandir}/man1/vlc*.1*

%files gui-ncurses
%{_bindir}/nvlc
%{vlc_plugindir}/gui/libncurses_plugin.so

%files gui-qt
%{_bindir}/qvlc
%{vlc_plugindir}/gui/libqt_plugin.so

%files gui-skins2
%{_bindir}/svlc
%{vlc_plugindir}/gui/libskins2_plugin.so
%{_datadir}/vlc/skins2/

%files plugins-base
%license COPYING COPYING.LIB
%exclude %{vlc_plugindir}/access/libaccess_jack_plugin.so
%exclude %{vlc_plugindir}/access/libavio_plugin.so
%if %{with ieee1394}
%exclude %{vlc_plugindir}/access/libdc1394_plugin.so
%exclude %{vlc_plugindir}/access/libdv1394_plugin.so
%endif
%exclude %{vlc_plugindir}/access/libpulsesrc_plugin.so
%exclude %{vlc_plugindir}/access/libsmb_plugin.so
%exclude %{vlc_plugindir}/access/libvnc_plugin.so
%{vlc_plugindir}/access/
%{vlc_plugindir}/access_output/
%{vlc_plugindir}/audio_filter/
%{vlc_plugindir}/audio_mixer/
%exclude %{vlc_plugindir}/audio_output/libjack_plugin.so
%exclude %{vlc_plugindir}/audio_output/libpulse_plugin.so
%{vlc_plugindir}/audio_output/
%exclude %{vlc_plugindir}/codec/libavcodec_plugin.so
%if %{with crystalhd}
%exclude %{vlc_plugindir}/codec/libcrystalhd_plugin.so
%endif
%exclude %{vlc_plugindir}/codec/libfluidsynth_plugin.so
%exclude %{vlc_plugindir}/codec/libgstdecode_plugin.so
%exclude %{vlc_plugindir}/codec/libsvgdec_plugin.so
%{vlc_plugindir}/codec/
%exclude %{vlc_plugindir}/control/libxcb_hotkeys_plugin.so
%{vlc_plugindir}/control/
%exclude %{vlc_plugindir}/demux/libavformat_plugin.so
%{vlc_plugindir}/demux/
%dir %{vlc_plugindir}/gui/
%exclude %{vlc_plugindir}/keystore/libkwallet_plugin.so
%exclude %{vlc_plugindir}/keystore/libsecret_plugin.so
%{vlc_plugindir}/keystore/
%{vlc_plugindir}/logger/
%{vlc_plugindir}/meta_engine/
%{vlc_plugindir}/misc/
%{vlc_plugindir}/mux/
%dir %{vlc_plugindir}/notify/
%exclude %{vlc_plugindir}/packetizer/libpacketizer_avparser_plugin.so
%{vlc_plugindir}/packetizer/
%exclude %{vlc_plugindir}/services_discovery/libpulselist_plugin.so
%exclude %{vlc_plugindir}/services_discovery/libxcb_apps_plugin.so
%{vlc_plugindir}/services_discovery/
%{vlc_plugindir}/spu/
%{vlc_plugindir}/stream_extractor/
%{vlc_plugindir}/stream_filter/
%exclude %{vlc_plugindir}/stream_out/libstream_out_chromaprint_plugin.so
%{vlc_plugindir}/stream_out/
%exclude %{vlc_plugindir}/text_renderer/libsvg_plugin.so
%{vlc_plugindir}/text_renderer/
%dir %{vlc_plugindir}/vaapi/
%dir %{vlc_plugindir}/vdpau/
%exclude %{vlc_plugindir}/video_chroma/libswscale_plugin.so
%{vlc_plugindir}/video_chroma/
%if %{with opencv}
%exclude %{vlc_plugindir}/video_filter/libopencv_*.so
%endif
%exclude %{vlc_plugindir}/video_filter/libpostproc_plugin.so
%{vlc_plugindir}/video_filter/
%dir %{vlc_plugindir}/video_output/
%{vlc_plugindir}/video_output/libfb_plugin.so
%{vlc_plugindir}/video_output/libvdummy_plugin.so
%{vlc_plugindir}/video_output/libvmem_plugin.so
%{vlc_plugindir}/video_output/libyuv_plugin.so
%dir %{vlc_plugindir}/video_splitter/
%dir %{vlc_plugindir}/visualization/
%dir %{_datadir}/vlc/

%if %{with crystalhd}
%files plugin-crystalhd
%{vlc_plugindir}/codec/libcrystalhd_plugin.so
%endif

%files plugin-ffmpeg
%{vlc_plugindir}/access/libavio_plugin.so
%{vlc_plugindir}/codec/libavcodec_plugin.so
%{vlc_plugindir}/demux/libavformat_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_avparser_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_chromaprint_plugin.so
%{vlc_plugindir}/vdpau/libvdpau_avcodec_plugin.so
%{vlc_plugindir}/video_chroma/libswscale_plugin.so
%{vlc_plugindir}/video_filter/libpostproc_plugin.so

%files plugin-fluidsynth
%{vlc_plugindir}/codec/libfluidsynth_plugin.so

%files plugin-gnome
%{vlc_plugindir}/keystore/libsecret_plugin.so

%files plugin-gstreamer
%{vlc_plugindir}/codec/libgstdecode_plugin.so

%if %{with ieee1394}
%files plugin-ieee1394
%{vlc_plugindir}/access/libdc1394_plugin.so
%{vlc_plugindir}/access/libdv1394_plugin.so
%endif

%files plugin-jack
%{vlc_plugindir}/access/libaccess_jack_plugin.so
%{vlc_plugindir}/audio_output/libjack_plugin.so

%files plugin-kde
%{vlc_plugindir}/keystore/libkwallet_plugin.so

%files plugin-lua
%{_libdir}/vlc/lua/
%{vlc_plugindir}/lua/
%{_datadir}/vlc/lua/

%files plugin-notify
%{vlc_plugindir}/notify/libnotify_plugin.so

%if %{with opencv}
%files plugin-opencv
%{vlc_plugindir}/video_filter/libopencv_example_plugin.so
%{vlc_plugindir}/video_filter/libopencv_wrapper_plugin.so
%endif

%files plugin-pulseaudio
%{_libdir}/vlc/libvlc_pulse.so*
%{vlc_plugindir}/access/libpulsesrc_plugin.so
%{vlc_plugindir}/audio_output/libpulse_plugin.so
%{vlc_plugindir}/services_discovery/libpulselist_plugin.so

%files plugin-samba
%{vlc_plugindir}/access/libsmb_plugin.so

%files plugin-svg
%{vlc_plugindir}/codec/libsvgdec_plugin.so
%{vlc_plugindir}/text_renderer/libsvg_plugin.so

%files plugins-video-out
%{_libdir}/vlc/libvlc_vdpau.so*
%{_libdir}/vlc/libvlc_xcb_events.so*
%{vlc_plugindir}/control/libxcb_hotkeys_plugin.so
%{vlc_plugindir}/services_discovery/libxcb_apps_plugin.so
%{vlc_plugindir}/vaapi/*.so
%exclude %{vlc_plugindir}/vdpau/libvdpau_avcodec_plugin.so
%{vlc_plugindir}/vdpau/*.so
%exclude %{vlc_plugindir}/video_output/libfb_plugin.so
%exclude %{vlc_plugindir}/video_output/libvdummy_plugin.so
%exclude %{vlc_plugindir}/video_output/libvmem_plugin.so
%exclude %{vlc_plugindir}/video_output/libyuv_plugin.so
%{vlc_plugindir}/video_output/*.so
%{vlc_plugindir}/video_splitter/*.so

%files plugin-visualization
%{vlc_plugindir}/visualization/*.so

%files plugin-vnc
%{vlc_plugindir}/access/libvnc_plugin.so

%files devel
%dir %{_includedir}/vlc
%{_includedir}/vlc/*.h
%{_includedir}/vlc/plugins/
%{_libdir}/libvlc.so
%{_libdir}/libvlccore.so
%{_libdir}/pkgconfig/libvlc.pc
%{_libdir}/pkgconfig/vlc-plugin.pc
%{_rpmmacrodir}/macros.vlc


%changelog
%autochangelog
