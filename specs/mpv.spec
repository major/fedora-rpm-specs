# Disable X11 for RHEL 10+
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]

Name:           mpv
Version:        0.40.0
Release:        3%{?dist}

License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:        Movie player playing most video formats and DVDs
URL:            https://%{name}.io/
Source0:        https://github.com/%{name}-player/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

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
BuildRequires:  pkgconfig(libavcodec) >= 59.27.100
BuildRequires:  pkgconfig(libavdevice) >= 58.13.100
BuildRequires:  pkgconfig(libavfilter) >= 7.110.100
BuildRequires:  pkgconfig(libavformat) >= 59.24.100
BuildRequires:  pkgconfig(libavutil) >= 57.24.100
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.19
BuildRequires:  pkgconfig(libplacebo) >= 5.264.1
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample) >= 3.9.100
BuildRequires:  pkgconfig(libswscale) >= 5.9.100
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(lua-5.1)
BuildRequires:  pkgconfig(mujs)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(uchardet) >= 0.0.5
BuildRequires:  pkgconfig(vapoursynth)
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
    -Dsdl2=enabled \
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
%config(noreplace) %{_sysconfdir}/%{name}/encoding-profiles.conf

%files libs
%license LICENSE.GPL LICENSE.LGPL Copyright
%{_libdir}/lib%{name}.so.2{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Jul 29 2025 Nicolas Chauvet <kwizart@gmail.com> - 0.40.0-3
- Rebuilt for libplacebo

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Mar 26 2025 Sérgio Basto <sergio@serjux.com> - 0.40.0-1
- Update mpv to 0.40.0
- filesystem package owns completions folders, no need to co-own
  these directories anymore

* Wed Feb 19 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 0.39.0-5
- mpv-libs should also depend on yt-dlp

* Wed Jan 29 2025 Simone Caronni <negativo17@gmail.com> - 0.39.0-4
- Rebuild for updated VapourSynth.

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.39.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Michel Lind <salimma@fedoraproject.org> - 0.39.0-2
- Rebuilt for rubberband 4

* Tue Sep 24 2024 Sérgio Basto <sergio@serjux.com> - 0.39.0-1
- Update mpv to 0.39.0

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 0.38.0-4
- Rebuild for ffmpeg 7

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Nicolas Chauvet <kwizart@gmail.com> - 0.38.0-2
- Rebuilt for libplacebo/vmaf

* Sun Jun 02 2024 Robert-André Mauchin <zebob.m@gmail.com> - 0.38.0-1
- Update to 0.38.0
- Disable shaderc as per https://github.com/mpv-player/mpv/issues/13940
- Close: rhbz#2275979

* Wed May 22 2024 Simone Caronni <negativo17@gmail.com> - 0.37.0-5
- Rebuild for updated VapourSynth.

* Sun Feb 04 2024 Fabio Valentini <decathorpe@gmail.com> - 0.37.0-4
- Rebuild against fixed mujs to address dynamic linking issues.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 24 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.37.0-1
- Update to 0.37.0

* Sun Nov 12 2023 Sérgio Basto <sergio@serjux.com> - 0.36.0-5
- Remove unused build requires (https://github.com/rpmfusion/mpv/pull/19)

* Fri Sep 29 2023 Nicolas Chauvet <nchauvet@linagora.com> - 0.36.0-4
- Rebuilt for libplacebo

* Fri Jul 28 2023 Nicolas Chauvet <kwizart@gmail.com> - 0.36.0-3
- Rebuilt for libplacebo-6

* Mon Jul 24 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.36.0-2
- Switched to meson by upstream request.

* Sun Jul 23 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.36.0-1
- Updated to version 0.36.0.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.35.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.35.1-5
- Rebuild against new vapoursynth

* Wed Mar 22 2023 Nicolas Chauvet <kwizart@gmail.com> - 0.35.1-4
- rebuilt

* Sun Mar 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.35.1-3
- Rebuild for ffmpeg 6.0

* Tue Mar 07 2023 Maxwell G <maxwell@gtmx.me> - 0.35.1-2
- Backport upstream patch to fix yt-dlp hook

* Mon Jan 30 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.35.1-1
- Updated to version 0.35.1.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.35.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 23 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.35.0-2
- Rebuilt for libplacebo

* Sat Nov 12 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.35.0-1
- Updated to version 0.35.0.
- Enabled Wayland backend.
- Enabled native PipeWire output support.

* Mon Sep 05 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.34.1-11
- Moved to Fedora.
- Added XDG metainfo manifest.

* Sun Sep 04 2022 Leigh Scott <leigh123linux@gmail.com> - 0.34.1-10
- Add requires ffmpeg-libs

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.34.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Fri Jul 22 2022 Leigh Scott <leigh123linux@gmail.com> - 0.34.1-8
- Rebuild for new ffmpeg

* Sat Jul 09 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.34.1-7
- Rebuilt due to libplacebo update.

* Fri Jun 17 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.34.1-6
- rebuilt

* Tue Apr 19 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.34.1-5
- Make sure we're using the full ffmpeg-libs version.
- Removed no longer required patch.

* Fri Mar 04 2022 Leigh Scott <leigh123linux@gmail.com> - 0.34.1-4
- Rebuild for new vapoursynth

* Fri Feb 04 2022 Leigh Scott <leigh123linux@gmail.com> - 0.34.1-3
- Rebuild for new libvpx

* Mon Jan 10 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.34.1-2
- Removed boolean dependencies.

* Mon Jan 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.34.1-1
- Updated to version 0.34.1.

* Fri Dec 24 2021 Leigh Scott <leigh123linux@gmail.com> - 0.34.0-3
- Boolean dependencies are only fedora

* Tue Nov 09 2021 Leigh Scott <leigh123linux@gmail.com> - 0.34.0-2
- Rebuilt for new ffmpeg snapshot

* Mon Nov 01 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.34.0-1
- Updated to version 0.34.0.

* Mon Sep 20 2021 Leigh Scott <leigh123linux@gmail.com> - 0.33.1-4
- rebuilt

* Thu Aug 19 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.33.1-3
- rebuilt

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 05 2021 Leigh Scott <leigh123linux@gmail.com> - 0.33.1-1
- Update to 0.33.1

* Fri Apr 02 2021 Leigh Scott <leigh123linux@gmail.com> - 0.33.0-6
- rebuilt

* Wed Mar 24 2021 Leigh Scott <leigh123linux@gmail.com> - 0.33.0-5
- rebuilt

* Thu Feb 11 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.33.0-4
- Rebuilt

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.33.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 0.33.0-2
- Rebuilt for new ffmpeg snapshot

* Sun Nov 22 2020 Leigh Scott <leigh123linux@gmail.com> - 0.33.0-1
- Update to 0.33.0

* Wed Oct 21 2020 Leigh Scott <leigh123linux@gmail.com> - 0.32.0-10
- Rebuild for new libdvdread

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.32.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Leigh Scott <leigh123linux@gmail.com> - 0.32.0-8
- Fix lua mistake

* Tue Jun 30 2020 Leigh Scott <leigh123linux@gmail.com> - 0.32.0-7
- Rebuilt for new libplacebo

* Wed Jun 24 2020 Leigh Scott <leigh123linux@gmail.com> - 0.32.0-6
- Enable vapoursynth (rfbz#5681)

* Fri Apr 10 2020 Leigh Scott <leigh123linux@gmail.com> - 0.32.0-5
- Rebuild for new libcdio version

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.32.0-4
- Rebuild for ffmpeg-4.3 git

* Sat Feb 08 2020 Leigh Scott <leigh123linux@gmail.com> - 0.32.0-3
- Rebuild for new libplacebo version

* Sun Jan 26 2020 Leigh Scott <leigh123linux@gmail.com> - 0.32.0-2
- Drop libarchive support for f30 and el8, supporting 0.31.0 for the
  next decade isn't an option

* Sun Jan 26 2020 Leigh Scott <leigh123linux@gmail.com> - 0.32.0-1
- Update to 0.32.0

* Sat Dec 28 2019 Leigh Scott <leigh123linux@gmail.com> - 0.31.0-1
- Update to 0.31.0

* Thu Dec 19 2019 Leigh Scott <leigh123linux@gmail.com> - 0.30.0-3
- Rebuild for new libplacebo version

* Mon Nov 18 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.30.0-2
- rebuild for libdvdread ABI bump

* Fri Oct 25 2019 Leigh Scott <leigh123linux@gmail.com> - 0.30.0-1
- Update to 0.30.0

* Fri Oct 25 2019 Leigh Scott <leigh123linux@gmail.com> - 0.29.1-19.20191025.gite67386e
- Update to 20191025 snapshot

* Sun Oct 13 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-18.20191011.gita85fa2d
- Enable html doc as it's easier to read than the man page

* Sat Oct 12 2019 Leigh Scott <leigh123linux@gmail.com> - 0.29.1-17.20191011.gita85fa2d
- Update to 20191011 snapshot

* Thu Oct 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-16.20191003.gitdefc8f3
- Update to 20191003 snapshot

* Mon Sep 23 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-15.20190922.gitb6def65
- Rebuild with newer zimg

* Sun Sep 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-14.20190922.gitb6def65
- Remove BuildRequires dvdread and libv4l2
- Add BuildRequires zimg and caca

* Sun Sep 22 2019 Leigh Scott <leigh123linux@gmail.com> - 0.29.1-13.20190922.gitb6def65
- Update to 20190922 snapshot
- Switch to waf-python3

* Tue Sep 10 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-12.20190814.gitcd7bcb9
- Adjust epel8 build requires

* Tue Aug 27 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-11.20190814.gitcd7bcb9
- Rebuild for switch to lua

* Tue Aug 20 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-10.20190814.gitcd7bcb9
- Update to 20190814 snapshot

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 0.29.1-9.20190616.gitc9e7473
- Rebuild for new ffmpeg version

* Tue Jul 02 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.29.1-8.20190616.gitc9e7473
- Update to 20190616 snapshot
- Add libplacebo
- Fix support for FFmpeg DRM PRIME

* Sun Jun 23 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-6
- Rebuild against sdk9 nv-codec-headers
- Spec file clean up

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.29.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-4
- Enable JavaScript support (rfbz#5151)

* Tue Dec 18 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.29.1-3
- Enable rpi support

* Tue Nov 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-2
- Rebuild for new ffmpeg

* Sat Oct 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.29.1-1
- Update to 0.29.1
- Drop old Obsoletes and Provides
- Use modern marcos

* Tue Oct 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.29.0-3
- Add BuildRequires: libshaderc-devel

* Thu Aug 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.29.0-2
- Add BuildRequires: gcc

* Wed Jul 25 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.29.0-1
- Update to 0.29.0

* Wed Jun 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.28.2-6
- Revert last commit

* Sat Jun 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.28.2-5
- Rebuild for new libass version
- vulkan is x86 only

* Fri Apr 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.28.2-4
- Rebuild for ffmpeg-4.0 release

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.28.2-3
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.28.2-1
- Update to 0.28.2

* Sun Feb 11 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.28.1-1
- Update to 0.28.1

* Thu Feb 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.28.0-3
- Fix missing build requires

* Sat Jan 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.28.0-2
- Rebuild for libcdio

* Wed Jan 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.28.0-1
- Update to 0.28.0
- Enable VA-API
- Enable vulkan support

* Tue Jan 16 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.27.0-4
- Disable VA-API until 0.28.0 lands

* Mon Jan 15 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.27.0-3
- Rebuilt for VA-API 1.0.0

* Mon Oct 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.27.0-2
- Rebuild for ffmpeg update

* Fri Sep 15 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.27.0-1
- Update to 0.27.0
- Enable libarchive support (play .zip, .iso and other formats)

* Fri Aug 11 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.26.0-3
- Enable Samba support  (rfbz#4624)
- Enable TV and DVB support

* Wed Aug 09 2017 Miro Hrončok <mhroncok@redhat.com> - 0.26.0-2
- Enable DVD and CDDA support  (rfbz#4622)

* Thu Jul 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.26.0-1
- Update to 0.26.0

* Wed May 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.25.0-2
- Rebuild for ffmpeg update

* Mon May 08 2017 Miro Hrončok <mhroncok@redhat.com> - 0.25.0-1
- Update to 0.25.0

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.24.0-2
- Rebuild for ffmpeg update

* Sun Apr 02 2017 Miro Hrončok <mhroncok@redhat.com> - 0.24.0-1
- Update to 0.24.0

* Thu Mar 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.23.0-4
- Try to fix ppc build

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-2
- Fix AVAudioResampleContext: Unable to set resampling compensation (rfbz#4408)

* Sat Dec 31 2016 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-1
- Update to 0.23.0

* Sat Dec 03 2016 leigh scott <leigh123linux@googlemail.com> - 0.22.0-2
- Add patch to relax ffmpeg version check

* Sat Nov 26 2016 leigh scott <leigh123linux@googlemail.com> - 0.22.0-1
- update to 0.22.0

* Thu Nov 17 2016 Adrian Reber <adrian@lisas.de> - 0.21.0-3
- Rebuilt for libcdio-0.94

* Sat Nov 05 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.21.0-2
- Rebuilt for new ffmpeg
- Add provides mplayer-backend (rfbz#4284)

* Thu Oct 20 2016 Evgeny Lensky <surfernsk@gmail.com> - 0.21.0-1
- update to 0.21.0

* Tue Aug 16 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.19.0-3
- Update to 0.19.0
- Add LDFLAGS so build is hardened
- Fix CFLAGS
- Make build verbose
- Remove Requires pkgconfig from devel sub-package
- Fix source tag

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.18.1-2
- Rebuilt for ffmpeg-3.1.1

* Tue Jul 26 2016 Miro Hrončok <mhroncok@redhat.com> - 0.18.1-1
- Update to 0.18.1
- Remove patch for Fedora < 22

* Sun Jul 03 2016 Sérgio Basto <sergio@serjux.com> - 0.18.0-3
- BRs in alphabetical order, rename of sub-packages libs and other improvements

* Thu Jun 30 2016 Sérgio Basto <sergio@serjux.com> - 0.18.0-2
- Add BR perl(Encode) to build on F24 (merge from Adrian Reber PR)

* Tue Jun 28 2016 Sérgio Basto <sergio@serjux.com> - 0.18.0-1
- Update to 0.18.0

* Mon Apr 11 2016 Evgeny Lensky <surfernsk@gmail.com> - 0.17.0-1
- update to 0.17.0

* Mon Feb 29 2016 Evgeny Lensky <surfernsk@gmail.com> - 0.16.0-1
- update to 0.16.0
- edit mpv-config.patch

* Sun Feb 14 2016 Sérgio Basto <sergio@serjux.com> - 0.15.0-2
- Drop BR lirc, because support for LIRC has been removed in mpv 0.9.0.
- Add license tag.
- libmpv-devel does not need have same doc and license files.

* Thu Jan 21 2016 Evgeny Lensky <surfernsk@gmail.com> - 0.15.0-1
- update to 0.15.0

* Sat Dec 12 2015 Evgeny Lensky <surfernsk@gmail.com> - 0.14.0-1
- update to 0.14.0

* Thu Nov 26 2015 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- Add mesa-libEGL-devel to BRs

* Thu Nov 26 2015 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-1
- Updated to 0.13.0

* Thu Jun 11 2015 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-2
- Removed --disable-debug flag

* Wed Jun 10 2015 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-1
- Updated to 0.9.2
- Also build the library

* Sat May 16 2015 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-1
- Update to 0.9.1
- BR compat-lua-devel because mpv does not work with lua 5.3
- Add BR lcms2-devel (#3643)
- Removed --enable-joystick and --enable-lirc (no longer used)

* Tue Apr 28 2015 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-3
- Conditionalize old waf patch

* Tue Apr 28 2015 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-2
- Rebuilt

* Mon Apr 13 2015 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-1
- Updated

* Wed Jan 28 2015 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-1
- Updated

* Mon Dec 22 2014 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Slightly change the waf patch

* Mon Dec 22 2014 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-2
- Add patch to allow waf 1.7

* Sat Dec 13 2014 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-1
- New version 0.7.1
- Rebuilt new lirc (#3450)

* Tue Nov 04 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-3
- Rebuilt for vaapi 0.36

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 0.6.0-2
- Rebuilt for FFmpeg 2.4.3

* Sun Oct 12 2014 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-1
- New version 0.6.0

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-2
- Rebuilt for FFmpeg 2.4.x

* Wed Sep 03 2014 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-1
- New version 0.5.1
- Add BR ncurses-devel (#3233)

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 0.4.0-2
- Rebuilt for ffmpeg-2.3

* Tue Jul 08 2014 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-1
- New version 0.4.0

* Tue Jun 24 2014 Miro Hrončok <mhroncok@redhat.com> - 0.3.11-1
- New version 0.3.11

* Tue Mar 25 2014 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-2
- Rebuilt for new libcdio and libass

* Thu Mar 20 2014 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-1
- New version 0.3.6

* Fri Feb 28 2014 Miro Hrončok <mhroncok@redhat.com> - 0.3.5-2
- Rebuilt for mistake

* Fri Feb 28 2014 Miro Hrončok <mhroncok@redhat.com> - 0.3.5-1
- New version 0.3.5

* Sat Jan 25 2014 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-1
- New version 0.3.3

* Wed Jan 01 2014 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Use upstream .desktop file

* Wed Jan 01 2014 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-1
- New version 0.3.0
- Switch to waf
- Add some tricks from openSUSE
- Removed already included patch

* Sun Dec 22 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-8
- Added patch for https://fedoraproject.org/wiki/Changes/FormatSecurity

* Sun Dec 22 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-7
- Support wayland

* Sun Dec 22 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-6
- Rebuilt

* Sun Dec 22 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-5
- Fixed wrong license tag (see upstream a5507312)

* Sun Dec 15 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-4
- Added libva (#3065)

* Sun Dec 15 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-3
- Added lua and libquvi (#3025)

* Sun Dec 15 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-2
- Rebuilt for mistakes

* Sun Dec 15 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-1
- New version 0.2.4

* Mon Nov 11 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-4
- There's no longer AUTHORS file in %%doc
- Install icons

* Mon Nov 11 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-3
- Rebased config patch

* Mon Nov 11 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-2
- Proper sources for all branches

* Mon Nov 11 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-1
- New upstream version

* Sat Oct 12 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-4
- Fixing cvs errors

* Sat Oct 12 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-3
- Add desktop file

* Sat Oct 12 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-2
- Do not use xv as default vo

* Sat Oct 12 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-1
- New upstream release

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.2-4
- Rebuilt

* Mon Sep 09 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-3
- Added BR ffmpeg-libs

* Tue Aug 27 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-2
- Reduced BRs a lot (removed support for various stuff)
- Make smbclient realized
- Changed the description to the text from manual page

* Mon Aug 19 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-1
- Initial spec
- Inspired a lot in mplayer.spec
