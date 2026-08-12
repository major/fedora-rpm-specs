# Disable X11 for RHEL 10+
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]

Name:           mpv
Version:        0.41.0
Release:        %autorelease

# overall license is GPL-2.0-or-later and LGPL-2.1-or-later
# BSD-2-Clause
#   osdep/android/strnlen.c
#   osdep/android/strnlen.h
# BSD-3-Clause
#   audio/filter/af_scaletempo2_internals.h
# ISC
#   audio/out/ao_sndio.c
#   include/mpv/client.h
#   include/mpv/render.h
#   include/mpv/render_gl.h
#   include/mpv/stream_cb.h
#   misc/thread_pool.c
#   misc/thread_tools.c
#   osdep/win32-console-wrapper.c
#   player/client.c
#   player/lua/console.lua
#   ta/ta.c
#   ta/ta.h
#   ta/ta_talloc.c
#   ta/ta_talloc.h
#   ta/ta_utils.c
# MIT
#   misc/codepoint_width.c
#   osdep/dirent-win.h
#   osdep/timer-darwin.c
#   player/lua/fzy.lua
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
Summary:        Movie player playing most video formats and DVDs
URL:            https://%{name}.io/
Source0:        https://github.com/%{name}-player/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Switch to runtime loading of libvsscript with VapourSynth R74+
# https://github.com/mpv-player/mpv/commit/75b2ccfeb1ce4ed5a40ac9860fa74f3d1265e13f
Patch1:         mpv-vapoursynth-r74.patch
# Fix build with VapourSynth < R74
# https://github.com/mpv-player/mpv/commit/44a9b03f244f24e0ea443370cf2cfae0da5767f9
Patch2:         mpv-vapoursynth-rtld-global.patch
# Load versioned libvsscript.so
Patch3:         mpv-vapoursynth-soname.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  libatomic
BuildRequires:  meson
BuildRequires:  python3-docutils

BuildRequires:  perl(Encode)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigRat)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(ffnvcodec)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libarchive) >= 3.4.0
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec) >= 60.31.102
BuildRequires:  pkgconfig(libavdevice) >= 60.3.100
BuildRequires:  pkgconfig(libavfilter) >= 9.12.100
BuildRequires:  pkgconfig(libavformat) >= 60.16.100
BuildRequires:  pkgconfig(libavutil) >= 58.29.100
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.57
BuildRequires:  pkgconfig(libplacebo) >= 6.338.2
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample) >= 4.12.100
BuildRequires:  pkgconfig(libswscale) >= 7.5.100
BuildRequires:  pkgconfig(libva)
# https://github.com/mpv-player/mpv/wiki/FAQ#user-content-Why_does_mpv_not_support_Lua_53_or_newer
BuildRequires:  pkgconfig(lua-5.1)
BuildRequires:  pkgconfig(mujs)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(uchardet)
# Only the headers are used; the library itself is loaded at runtime. The
# vapoursynth-script module this used to need as well is gone since R79.
BuildRequires:  pkgconfig(vapoursynth) >= 56
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zimg) >= 2.9
BuildRequires:  pkgconfig(zlib)
%if %{with x11}
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(xpresent)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xv)
%endif

Requires:       hicolor-icon-theme
# Loading VapourSynth at runtime leaves no linkage for RPM to pick up on.
Requires:       vapoursynth-libs%{?_isa}
Provides:       mplayer-backend
Recommends:     (yt-dlp or youtube-dl)
Suggests:       yt-dlp

%description
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

Mpv has an OpenGL, Vulkan, and D3D11 based video output that is capable of many
features loved by videophiles, such as video scaling with popular high quality
algorithms, color management, frame timing, interpolation, HDR, and more.

While mpv strives for minimalism and provides no real GUI, it has a small
controller on top of the video for basic control.

Mpv can leverage most hardware decoding APIs on all platforms. Hardware
decoding can be enabled at runtime on demand.

Powerful scripting capabilities can make the player do almost anything. There
is a large selection of user scripts on the wiki.

A straightforward C API was designed from the ground up to make mpv usable as
a library and facilitate easy integration into other applications.

%package libs
Summary: Dynamic library for Mpv frontends
# Loading VapourSynth at runtime leaves no linkage for RPM to pick up on.
Requires: vapoursynth-libs%{?_isa}
Recommends: (yt-dlp or youtube-dl)
Suggests: yt-dlp

%description libs
This package contains the dynamic library libmpv, which provides access to Mpv.

%package devel
Summary: Development package for libmpv
Provides: %{name}-libs-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-libs-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains development header files and libraries for Mpv.

%prep
%autosetup -p1
sed -e "s|/usr/local/etc|%{_sysconfdir}/%{name}|" -i etc/%{name}.conf

%build
%meson --auto-features=auto \
    -Dalsa=enabled \
    -Dbuild-date=false \
    -Dcaca=enabled \
    -Dcdda=enabled \
    -Dcplayer=true \
    -Dcplugins=enabled \
    -Dcuda-hwaccel=enabled \
    -Dcuda-interop=enabled \
    -Ddmabuf-wayland=enabled \
    -Ddrm=enabled \
    -Ddvbin=enabled \
    -Ddvdnav=enabled \
    -Degl-drm=enabled \
    -Degl-wayland=enabled \
%if %{with x11}
    -Degl-x11=enabled \
    -Dgl-x11=enabled \
    -Dvaapi-x11=enabled \
    -Dvdpau-gl-x11=enabled \
    -Dvdpau=enabled \
    -Dx11=enabled \
    -Dxv=enabled \
%endif
    -Degl=enabled \
    -Dgbm=enabled \
    -Dgl=enabled \
    -Dhtml-build=enabled \
    -Diconv=enabled \
    -Djack=enabled \
    -Djavascript=enabled \
    -Djpeg=enabled \
    -Dlcms2=enabled \
    -Dlibarchive=enabled \
    -Dlibavdevice=enabled \
    -Dlibbluray=enabled \
    -Dlibmpv=true \
    -Dlua=enabled \
    -Dmanpage-build=enabled \
    -Dopenal=enabled \
    -Dopensles=disabled \
    -Doss-audio=disabled \
    -Dpipewire=enabled \
    -Dplain-gl=enabled \
    -Dpulse=enabled \
    -Drubberband=enabled \
    -Dsdl2-audio=enabled \
    -Dsdl2-gamepad=enabled \
    -Dsdl2-video=enabled \
    -Dshaderc=disabled \
    -Dsndio=disabled \
    -Dspirv-cross=disabled \
    -Duchardet=enabled \
    -Dvaapi-drm=enabled \
    -Dvaapi-wayland=enabled \
    -Dvaapi=enabled \
    -Dvapoursynth=enabled \
    -Dvector=enabled \
    -Dvulkan=enabled \
    -Dwayland=enabled \
    -Dwerror=false \
    -Dzimg=enabled \
    -Dzlib=enabled
%meson_build

%install
%meson_install
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%docdir %{_docdir}/%{name}/
%license LICENSE.GPL LICENSE.LGPL Copyright
%{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{bash_completions_dir}/%{name}
%{zsh_completions_dir}/_%{name}
%{fish_completions_dir}/%{name}.fish
%{_mandir}/man1/%{name}.*
%{_metainfodir}/%{name}.metainfo.xml
%dir %{_sysconfdir}/%{name}/

%files libs
%license LICENSE.GPL LICENSE.LGPL Copyright
%{_libdir}/lib%{name}.so.2{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
