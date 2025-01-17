%{?mingw_package_header}
%bcond_without extras

%global         api_version     1.0

Name:           mingw-gstreamer1-plugins-bad-free
Version:        1.25.1
Release:        1%{?dist}
Summary:        Cross compiled GStreamer1 plug-ins "bad"

# The freeze and nfs plugins are LGPLv2 (only)
License:        LGPL-2.0-or-later AND LGPL-2.0-only
URL:            http://gstreamer.freedesktop.org/
# The source is:
# http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
# modified with gst1-p-bad-cleanup.sh from SOURCE1
Source0:        gst-plugins-bad-free-%{version}.tar.xz
Source1:        gst-p-bad-cleanup.sh
# Adapt for directxmath header location
Patch1:        gst-p-bad-directxmath.patch

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  orc-compiler

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-directxmath
BuildRequires:  mingw64-directxmath
BuildRequires:  mingw32-gstreamer1 >= %{version}
BuildRequires:  mingw64-gstreamer1 >= %{version}
BuildRequires:  mingw32-gstreamer1-plugins-base >= %{version}
BuildRequires:  mingw64-gstreamer1-plugins-base >= %{version}
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw32-curl
BuildRequires:  mingw64-curl
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw64-gnutls
BuildRequires:  mingw32-gsm
BuildRequires:  mingw64-gsm
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw32-jasper
BuildRequires:  mingw64-jasper
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw32-librsvg2
BuildRequires:  mingw64-librsvg2
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-nettle
BuildRequires:  mingw64-nettle
BuildRequires:  mingw32-openexr
BuildRequires:  mingw64-openexr
BuildRequires:  mingw32-openal-soft
BuildRequires:  mingw64-openal-soft
BuildRequires:  mingw32-openjpeg2
BuildRequires:  mingw64-openjpeg2
BuildRequires:  mingw32-opus
BuildRequires:  mingw64-opus
BuildRequires:  mingw32-orc
BuildRequires:  mingw64-orc
BuildRequires:  mingw32-openssl
BuildRequires:  mingw64-openssl
BuildRequires:  mingw32-wavpack
BuildRequires:  mingw64-wavpack

# For glib-genmarshal
BuildRequires:  glib2-devel


%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


# Mingw32
%package -n mingw32-gstreamer1-plugins-bad-free
Summary:        %{summary}
Requires:       mingw32-gstreamer1 >= %{version}
Obsoletes:      mingw32-gstreamer1-plugins-bad < 1.14.1-1
Provides:       mingw32-gstreamer1-plugins-bad = 1.14.1-1

%description -n mingw32-gstreamer1-plugins-bad-free
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


# Mingw64
%package -n mingw64-gstreamer1-plugins-bad-free
Summary:        %{summary}
Requires:       mingw64-gstreamer1 >= %{version}
Obsoletes:      mingw64-gstreamer1-plugins-bad < 1.14.1-1
Provides:       mingw64-gstreamer1-plugins-bad = 1.14.1-1

%description -n mingw64-gstreamer1-plugins-bad-free
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n gst-plugins-bad-%{version}


%build
#   chromaprint was enabled in the !mingw package in 6eadf04
#   openal, openjpeg, ofa, webp were enabled in the !mingw package in c609b28
#   there are mingw-openjpeg and mingw-webp packages available
#   uvch264 was enabled in the !mingw package in fcee991
#   curl and winks are disabled only in the mingw package
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_meson \
    -Dpackage-name="Fedora Mingw GStreamer-plugins-bad package" \
    -Dpackage-origin="http://download.fedoraproject.org" \
    %{!?with_extras:-D fbdev=disabled -D decklink=disabled } \
    %{!?with_extras:-D assrender=disabled -D bs2b=disabled } \
    %{!?with_extras:-D chromaprint=disabled -D d3dvideosink=disabled } \
    %{!?with_extras:-D directsound=disabled -D dts=disabled } \
    %{!?with_extras:-D fluidsynth=disabled -D openexr=disabled } \
    %{!?with_extras:-D curl=disabled -D curl-ssh2=disabled } \
    %{!?with_extras:-D ttml=disabled -D kate=disabled } \
    %{!?with_extras:-D modplug=disabled -D ofa=disabled } \
    %{!?with_extras:-D vdpau=disabled -D openal=disabled } \
    %{!?with_extras:-D opencv=disabled -D openjpeg=disabled } \
    %{!?with_extras:-D wildmidi=disabled -D zbar=disabled } \
    %{!?with_extras:-D gme=disabled -D lv2=disabled } \
    -D doc=disabled -D magicleap=disabled -D msdk=disabled \
    -D dts=disabled -D faac=disabled -D faad=disabled \
    -D mpeg2enc=disabled -D mplex=disabled \
    -D neon=disabled -D rtmp=disabled -D rtmp2=disabled \
    -D flite=disabled -D sbc=disabled -D opencv=disabled \
    %{!?with_extras:-D spandsp=disabled -D va=disabled } \
    -D voamrwbenc=disabled -D x265=disabled \
    -D dvbsuboverlay=disabled -D dvdspu=disabled -D siren=disabled \
    -D opensles=disabled -D tinyalsa=disabled \
    -D wasapi=enabled -D wasapi2=disabled -D avtp=disabled \
    -D dc1394=disabled -D directfb=disabled -D iqa=disabled \
    -D libde265=disabled -D musepack=disabled -D openni2=disabled \
    -D sctp=disabled -D svthevcenc=disabled -D voaacenc=disabled \
    -D zxing=disabled -D wpe=disabled -D x11=disabled \
    -D openh264=disabled \
    -D examples=disabled -D tests=disabled
#    -D d3d11=disabled \


%mingw_ninja


%install
%mingw_ninja_install

# Clean out files that should not be part of the rpm.
rm -f %{buildroot}%{mingw32_libdir}/gstreamer-%{api_version}/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gstreamer-%{api_version}/*.dll.a

%mingw_find_lang gstreamer1-plugins-bad-free --all-name


# Mingw32
%files -n mingw32-gstreamer1-plugins-bad-free -f mingw32-gstreamer1-plugins-bad-free.lang
%license COPYING
%doc AUTHORS README.md REQUIREMENTS
%{mingw32_bindir}/gst-transcoder-1.0.exe
# libraries
%{mingw32_bindir}/libgstadaptivedemux-1.0-0.dll
%{mingw32_bindir}/libgstanalytics-1.0-0.dll
%{mingw32_bindir}/libgstbadaudio-1.0-0.dll
%{mingw32_bindir}/libgstbasecamerabinsrc-1.0-0.dll
%{mingw32_bindir}/libgstcodecs-1.0-0.dll
%{mingw32_bindir}/libgstcodecparsers-1.0-0.dll
%{mingw32_bindir}/libgstcuda-1.0-0.dll
%{mingw32_bindir}/libgstd3d11-1.0-0.dll
%{mingw32_bindir}/libgstd3dshader-1.0-0.dll
%{mingw32_bindir}/libgstdxva-1.0-0.dll
%{mingw32_bindir}/libgstinsertbin-1.0-0.dll
%{mingw32_bindir}/libgstisoff-1.0-0.dll
%{mingw32_bindir}/libgstmpegts-1.0-0.dll
%{mingw32_bindir}/libgstmse-1.0-0.dll
%{mingw32_bindir}/libgstphotography-1.0-0.dll
%{mingw32_bindir}/libgstplay-1.0-0.dll
%{mingw32_bindir}/libgstplayer-1.0-0.dll
%{mingw32_bindir}/libgstsctp-1.0-0.dll
%{mingw32_bindir}/libgsttranscoder-1.0-0.dll
%{mingw32_bindir}/libgsturidownloader-1.0-0.dll
%{mingw32_bindir}/libgstwebrtc-1.0-0.dll

# bad plugins
%dir %{mingw32_libdir}/gstreamer-%{api_version}
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaccurip.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstadpcmdec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstadpcmenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaes.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaiff.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstanalyticsoverlay.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstasfmux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstasio.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiobuffersplit.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiofxbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiolatency.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiomixmatrix.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiovisualizers.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstautoconvert.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstbayer.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstbz2.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcamerabin.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstclosedcaption.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcodecalpha.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcoloreffects.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcolormanagement.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcurl.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstd3d.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstd3d11.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdash.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdebugutilsbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdecklink.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdirectsoundsrc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdtls.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdwrite.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdvbsubenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfaceoverlay.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfestival.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfieldanalysis.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfreeverb.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfrei0r.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgaudieffects.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgdp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgeometrictransform.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgsm.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsthls.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstid3tag.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstinsertbin.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstinter.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstinterlace.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstipcpipeline.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstivfparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstivtc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstjp2kdecimator.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstjpegformat.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstlegacyrawparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmidi.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegpsdemux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegpsmux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegtsdemux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegtsmux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmxf.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstnetsim.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstnvcodec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstopenal.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstopenexr.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstopenjpeg.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstopusparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstpcapparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstpnm.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstproxy.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstremovesilence.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrfbsrc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrist.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrsvg.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtpmanagerbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtponvif.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsdpelem.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsegmentclip.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsmooth.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsmoothstreaming.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstspeed.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsubenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstswitchbin.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsttensordecoders.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsttimecode.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsttranscode.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstttmlsubs.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideofiltersbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideoframe_audiolevel.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideoparsersbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideosignal.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvmnc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwasapi.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwebp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwinks.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwinscreencap.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsty4mdec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstamfcodec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcodectimestamper.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstqsv.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwin32ipc.dll

# plugin helper library headers
%{mingw32_includedir}/gstreamer-%{api_version}/gst/analytics/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/audio/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/basecamerabinsrc/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/codecparsers/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/interfaces/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/insertbin/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/isoff/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/mse/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/mpegts/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/play/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/player/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/sctp/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/transcoder/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/uridownloader/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/webrtc/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/cuda/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/d3d11/

%{mingw32_libdir}/gstreamer-%{api_version}/include/
%{mingw32_libdir}/libgstadaptivedemux-%{api_version}.dll.a
%{mingw32_libdir}/libgstanalytics-%{api_version}.dll.a
%{mingw32_libdir}/libgstbadaudio-%{api_version}.dll.a
%{mingw32_libdir}/libgstbasecamerabinsrc-%{api_version}.dll.a
%{mingw32_libdir}/libgstcodecs-%{api_version}.dll.a
%{mingw32_libdir}/libgstcodecparsers-%{api_version}.dll.a
%{mingw32_libdir}/libgstd3d11-%{api_version}.dll.a
%{mingw32_libdir}/libgstd3dshader-1.0.dll.a
%{mingw32_libdir}/libgstdxva-%{api_version}.dll.a
%{mingw32_libdir}/libgstinsertbin-%{api_version}.dll.a
%{mingw32_libdir}/libgstisoff-%{api_version}.dll.a
%{mingw32_libdir}/libgstmpegts-%{api_version}.dll.a
%{mingw32_libdir}/libgstmse-%{api_version}.dll.a
%{mingw32_libdir}/libgstphotography-%{api_version}.dll.a
%{mingw32_libdir}/libgstplay-%{api_version}.dll.a
%{mingw32_libdir}/libgstplayer-%{api_version}.dll.a
%{mingw32_libdir}/libgstsctp-%{api_version}.dll.a
%{mingw32_libdir}/libgsttranscoder-%{api_version}.dll.a
%{mingw32_libdir}/libgsturidownloader-%{api_version}.dll.a
%{mingw32_libdir}/libgstwebrtc-%{api_version}.dll.a
%{mingw32_libdir}/libgstcuda-%{api_version}.dll.a

%{mingw32_libdir}/pkgconfig/gstreamer-analytics-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-bad-audio-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-codecparsers-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-insertbin-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-mpegts-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-mse-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-photography-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-play-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-player-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-plugins-bad-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-sctp-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-transcoder-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-webrtc-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-cuda-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-d3d11-%{api_version}.pc

%{mingw32_datadir}/gstreamer-%{api_version}/presets/
%{mingw32_datadir}/gstreamer-%{api_version}/encoding-profiles/


# Mingw64
%files -n mingw64-gstreamer1-plugins-bad-free -f mingw64-gstreamer1-plugins-bad-free.lang
%license COPYING
%doc AUTHORS README.md REQUIREMENTS
%{mingw64_bindir}/gst-transcoder-1.0.exe
# libraries
%{mingw64_bindir}/libgstadaptivedemux-1.0-0.dll
%{mingw64_bindir}/libgstanalytics-1.0-0.dll
%{mingw64_bindir}/libgstbadaudio-1.0-0.dll
%{mingw64_bindir}/libgstbasecamerabinsrc-1.0-0.dll
%{mingw64_bindir}/libgstcodecs-1.0-0.dll
%{mingw64_bindir}/libgstcodecparsers-1.0-0.dll
%{mingw64_bindir}/libgstcuda-1.0-0.dll
%{mingw64_bindir}/libgstd3d11-1.0-0.dll
%{mingw64_bindir}/libgstd3dshader-1.0-0.dll
%{mingw64_bindir}/libgstdxva-1.0-0.dll
%{mingw64_bindir}/libgstinsertbin-1.0-0.dll
%{mingw64_bindir}/libgstisoff-1.0-0.dll
%{mingw64_bindir}/libgstmpegts-1.0-0.dll
%{mingw64_bindir}/libgstmse-1.0-0.dll
%{mingw64_bindir}/libgstphotography-1.0-0.dll
%{mingw64_bindir}/libgstplay-1.0-0.dll
%{mingw64_bindir}/libgstplayer-1.0-0.dll
%{mingw64_bindir}/libgstsctp-1.0-0.dll
%{mingw64_bindir}/libgsttranscoder-1.0-0.dll
%{mingw64_bindir}/libgsturidownloader-1.0-0.dll
%{mingw64_bindir}/libgstwebrtc-1.0-0.dll

# bad plugins
%dir %{mingw64_libdir}/gstreamer-%{api_version}
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaccurip.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstadpcmdec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstadpcmenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaes.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaiff.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstanalyticsoverlay.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstasfmux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstasio.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiobuffersplit.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiofxbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiolatency.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiomixmatrix.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiovisualizers.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstautoconvert.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstbayer.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstbz2.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcamerabin.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstclosedcaption.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcodecalpha.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcoloreffects.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcolormanagement.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcurl.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstd3d.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstd3d11.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdash.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdebugutilsbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdecklink.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdirectsoundsrc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdtls.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdwrite.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdvbsubenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfaceoverlay.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfestival.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfieldanalysis.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfreeverb.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfrei0r.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgaudieffects.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgdp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgeometrictransform.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgsm.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsthls.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstid3tag.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstinsertbin.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstinter.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstinterlace.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstipcpipeline.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstivfparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstivtc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstjp2kdecimator.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstjpegformat.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstlegacyrawparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmidi.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegpsdemux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegpsmux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegtsdemux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegtsmux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmxf.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstnetsim.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstnvcodec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstopenal.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstopenexr.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstopenjpeg.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstopusparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstpcapparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstpnm.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstproxy.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstremovesilence.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrfbsrc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrist.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrsvg.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtpmanagerbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtponvif.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsdpelem.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsegmentclip.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsmooth.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsmoothstreaming.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstspeed.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsubenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstswitchbin.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsttensordecoders.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsttimecode.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsttranscode.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstttmlsubs.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideofiltersbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideoframe_audiolevel.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideoparsersbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideosignal.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvmnc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwasapi.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwebp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwinks.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwinscreencap.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsty4mdec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstamfcodec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcodectimestamper.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstqsv.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwin32ipc.dll

# plugin helper library headers
%{mingw64_includedir}/gstreamer-%{api_version}/gst/analytics/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/audio/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/basecamerabinsrc/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/codecparsers/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/interfaces/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/insertbin/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/isoff/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/mse/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/mpegts/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/play/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/player/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/sctp/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/transcoder/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/uridownloader/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/webrtc/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/cuda/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/d3d11/

%{mingw64_libdir}/gstreamer-%{api_version}/include/
%{mingw64_libdir}/libgstadaptivedemux-%{api_version}.dll.a
%{mingw64_libdir}/libgstanalytics-%{api_version}.dll.a
%{mingw64_libdir}/libgstbadaudio-%{api_version}.dll.a
%{mingw64_libdir}/libgstbasecamerabinsrc-%{api_version}.dll.a
%{mingw64_libdir}/libgstcodecs-%{api_version}.dll.a
%{mingw64_libdir}/libgstcodecparsers-%{api_version}.dll.a
%{mingw64_libdir}/libgstd3d11-%{api_version}.dll.a
%{mingw64_libdir}/libgstd3dshader-1.0.dll.a
%{mingw64_libdir}/libgstdxva-%{api_version}.dll.a
%{mingw64_libdir}/libgstinsertbin-%{api_version}.dll.a
%{mingw64_libdir}/libgstisoff-%{api_version}.dll.a
%{mingw64_libdir}/libgstmpegts-%{api_version}.dll.a
%{mingw64_libdir}/libgstmse-%{api_version}.dll.a
%{mingw64_libdir}/libgstphotography-%{api_version}.dll.a
%{mingw64_libdir}/libgstplay-%{api_version}.dll.a
%{mingw64_libdir}/libgstplayer-%{api_version}.dll.a
%{mingw64_libdir}/libgstsctp-%{api_version}.dll.a
%{mingw64_libdir}/libgsttranscoder-%{api_version}.dll.a
%{mingw64_libdir}/libgsturidownloader-%{api_version}.dll.a
%{mingw64_libdir}/libgstwebrtc-%{api_version}.dll.a
%{mingw64_libdir}/libgstcuda-%{api_version}.dll.a

%{mingw64_libdir}/pkgconfig/gstreamer-analytics-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-bad-audio-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-codecparsers-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-insertbin-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-mpegts-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-mse-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-photography-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-play-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-player-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-plugins-bad-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-sctp-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-transcoder-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-webrtc-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-cuda-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-d3d11-%{api_version}.pc

%{mingw64_datadir}/gstreamer-%{api_version}/presets/
%{mingw64_datadir}/gstreamer-%{api_version}/encoding-profiles/


%changelog
* Wed Jan 15 2025 Sandro Mani <manisandro@gmail.com> - 1.25.1-1
- Update to 1.25.1

* Mon Jan 13 2025 Sandro Mani <manisandro@gmail.com> - 1.24.11-1
- Update to 1.24.11

* Fri Dec 06 2024 Sandro Mani <manisandro@gmail.com> - 1.24.10-1
- Update to 1.24.10

* Wed Nov 27 2024 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.24.9-3
- Rebuild (openexr)

* Thu Nov 14 2024 Sandro Mani <manisandro@gmail.com> - 1.24.9-2
- Rebuild (openexr)

* Tue Nov 05 2024 Sandro Mani <manisandro@gmail.com> - 1.24.9-1
- Update to 1.24.9

* Mon Sep 23 2024 Sandro Mani <manisandro@gmail.com> - 1.24.8-1
- Update to 1.24.8

* Fri Aug 23 2024 Sandro Mani <manisandro@gmail.com> - 1.24.7-1
- Update to 1.24.7

* Tue Jul 30 2024 Sandro Mani <manisandro@gmail.com> - 1.24.6-1
- Update to 1.24.6

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 23 2024 Sandro Mani <manisandro@gmail.com> - 1.24.5-1
- Update to 1.24.5

* Tue Jun 11 2024 Sandro Mani <manisandro@gmail.com> - 1.24.4-2
- Rebuild (openexr)

* Thu Jun 06 2024 Sandro Mani <manisandro@gmail.com> - 1.24.4-1
- Update to 1.24.4

* Wed May 01 2024 Sandro Mani <manisandro@gmail.com> - 1.24.3-1
- Update to 1.24.3

* Thu Mar 07 2024 Sandro Mani <manisandro@gmail.com> - 1.24.0-1
- Update to 1.24.0

* Sat Jan 27 2024 Sandro Mani <manisandro@gmail.com> - 1.22.9-1
- Update to 1.22.9

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Sandro Mani <manisandro@gmail.com> - 1.22.8-1
- Update to 1.22.8

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 1.22.7-1
- Update to 1.22.7

* Thu Sep 21 2023 Sandro Mani <manisandro@gmail.com> - 1.22.6-1
- Update to 1.22.6

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 1.22.5-1
- Update to 1.22.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Sandro Mani <manisandro@gmail.com> - 1.22.4-1
- Update to 1.22.4

* Thu May 25 2023 Sandro Mani <manisandro@gmail.com> - 1.22.3-1
- Update to 1.22.3

* Sat Apr 15 2023 Sandro Mani <manisandro@gmail.com> - 1.22.2-1
- Update to 1.22.2

* Sun Mar 19 2023 Sandro Mani <manisandro@gmail.com> - 1.22.1-1
- Update to 1.22.1

* Sat Jan 28 2023 Sandro Mani <manisandro@gmail.com> - 1.22.0-1
- Update to 1.22.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 13 2022 Sandro Mani <manisandro@gmail.com> - 1.20.4-1
- Update to 1.20.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 21 2022 Sandro Mani <manisandro@gmail.com> - 1.20.3-1
- Update to 1.20.3

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-4
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-3
- Rebuild with mingw-gcc-12

* Thu Feb 17 2022 Sandro Mani <manisandro@gmail.com> - 1.19.3-3
- Rebuild (openssl)

* Sat Feb 05 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-1
- Update to 1.20.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Sandro Mani <manisandro@gmail.com> - 1.19.3-1
- Update to 1.19.3

* Sat Oct 02 2021 Sandro Mani <manisandro@gmail.com> - 1.19.2-1
- Update to 1.19.2

* Thu Aug 19 2021 Sandro Mani <manisandro@gmail.com> - 1.19.1-3
- Rebuild (openexr3)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Sandro Mani <manisandro@gmail.com> - 1.19.1-1
- Update to 1.19.1

* Wed Apr 14 2021 Michael Cronenworth <mike@cchtml.com> - 1.18.4-2
- Rebuild for Nettle 3.7.2

* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 1.18.4-1
- Update to 1.18.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Sandro Mani <manisandro@gmail.com> - 1.18.2-2
- Rebuild (openexr)

* Thu Dec 10 2020 Sandro Mani <manisandro@gmail.com> - 1.18.2-1
- Update to 1.18.2

* Mon Nov 02 2020 Sandro Mani <manisandro@gmail.com> - 1.18.1-1
- Update to 1.18.1

* Wed Aug 12 13:38:11 GMT 2020 Sandro Mani <manisandro@gmail.com> - 1.16.2-3
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.16.2-1
- Update to 1.16.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 1.14.2-7
- Rebuild (OpenEXR)

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.14.2-6
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Aug 20 2019 Michael Cronenworth <mike@cchtml.com> - 1.14.2-5
- Rebuild for Nettle 3.5.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Sandro Mani <manisandro@gmail.com> - 1.14.2-3
- Rebuild (OpenEXR)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.14.2-1
- Update to 1.14.2

* Fri Aug 24 2018 Richard W.M. Jones <rjones@redhat.com> - 1.14.1-2
- Rebuild for new mingw-openssl.

* Thu Jul 19 2018 Victor Toso <victortoso@redhat.com> - 1.14.1-1
- Update to 1.14.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Sandro Mani <manisandro@gmail.com> - 1.12.3-2
- Rebuild (OpenEXR)

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 1.12.3-1
- Update to 1.12.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 1.12.1-1
- Update to 1.12.1

* Wed Feb  8 2017 Victor Toso <victortoso@redhat.com> - 1.11.1-1
- Update to 1.11.1
- Add audiobuffersplit
- Dataurisrc was moved to core
- Add ttmlsubs plugin
- Fix CVE-2017-5843
- Fix CVE-2017-5848

* Sat Nov  5 2016 Victor Toso <victortoso@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Thu May 12 2016 Kalev Lember <klember@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Use license macro for COPYING
- Drop libtool .la files

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.4.4-3
- Add proper obsoletes/provides tags to provide working upgrade path
  This is needed as the binary packages were renamed in a recent commit

* Thu May 14 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.4-2
- Rebuilt for mingw-gnutls 3.4 ABI change

* Mon Dec  1 2014 Victor Toso <victortoso@redhat.com> - 1.4.4-1
- Initial packaging.
  Resolves: rhbz#1166852
