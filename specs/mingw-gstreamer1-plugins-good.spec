%{?mingw_package_header}

%global         api_version     1.0

Name:           mingw-gstreamer1-plugins-good
Version:        1.25.1
Release:        1%{?dist}
Summary:        Cross compiled GStreamer1 plug-ins good

License:        LGPL-2.0-or-later
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-orc
BuildRequires:  mingw64-orc
BuildRequires:  pkgconfig

# For glib-genmarshal
BuildRequires:  glib2-devel

BuildRequires:  mingw32-gstreamer1 >= %{version}
BuildRequires:  mingw64-gstreamer1 >= %{version}
BuildRequires:  mingw32-gstreamer1-plugins-base  >= %{version}
BuildRequires:  mingw64-gstreamer1-plugins-base  >= %{version}
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  mingw32-libsoup
BuildRequires:  mingw64-libsoup
BuildRequires:  mingw32-wavpack
BuildRequires:  mingw64-wavpack
BuildRequires:  mingw32-speex
BuildRequires:  mingw64-speex
BuildRequires:  mingw32-taglib
BuildRequires:  mingw64-taglib


%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.


# Mingw32
%package -n mingw32-gstreamer1-plugins-good
Summary:        %{summary}
Requires:       mingw32-gstreamer1 >= %{version}
Requires:       mingw32-gstreamer1-plugins-base >= %{version}

%description -n mingw32-gstreamer1-plugins-good
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.


# Mingw64
%package -n mingw64-gstreamer1-plugins-good
Summary:        %{summary}
Requires:       mingw64-gstreamer1 >= %{version}
Requires:       mingw64-gstreamer1-plugins-base >= %{version}

%description -n mingw64-gstreamer1-plugins-good
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n gst-plugins-good-%{version}


%build
%mingw_meson \
    -Dpackage-name='Fedora Mingw gstreamer1-plugins-good package' \
    -Dpackage-origin='http://download.fedora.redhat.com/fedora' \
    -Dexamples=disabled \
    -Dmonoscope=disabled \
    -Daalib=disabled \
    -Dlibcaca=disabled \
    -Dshout2=disabled \
    -Dflac=disabled \
    -Djack=disabled

%mingw_ninja


%install
%mingw_ninja_install

# Drop import libs for plugins
rm -rf %{buildroot}%{mingw32_libdir}/gstreamer-%{api_version}/*.dll.a
rm -rf %{buildroot}%{mingw64_libdir}/gstreamer-%{api_version}/*.dll.a

%mingw_find_lang gstreamer1-plugins-good --all-name


# Mingw32
%files -n mingw32-gstreamer1-plugins-good -f mingw32-gstreamer1-plugins-good.lang
%license COPYING
%doc AUTHORS README.md REQUIREMENTS

# Equaliser presets
%{mingw32_datadir}/gstreamer-%{api_version}/presets/

# non-core plugins without external dependencies
%{mingw32_libdir}/gstreamer-%{api_version}/libgstalaw.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstalpha.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstalphacolor.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstapetag.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiofx.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudioparsers.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstauparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstautodetect.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstavi.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcutter.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdebug.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdeinterlace.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdtmf.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsteffectv.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstequalizer.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstflv.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstflxdec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgoom.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgoom2k1.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsticydemux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstid3demux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstimagefreeze.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstinterleave.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstisomp4.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstlevel.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmatroska.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmulaw.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmultifile.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmultipart.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstnavigationtest.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstreplaygain.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtpmanager.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtsp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstshapewipe.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsmpte.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstspectrum.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstspeex.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsttaglib.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstudp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideobox.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideocrop.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideofilter.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideomixer.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwaveform.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwavenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwavpack.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwavparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsty4menc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstadaptivedemux2.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstxingmux.dll

# gstreamer1-plugins with external dependencies but in the main package
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcairo.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdirectsound.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgdkpixbuf.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstjpeg.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstpng.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsoup.dll


# Mingw64
%files -n mingw64-gstreamer1-plugins-good -f mingw64-gstreamer1-plugins-good.lang
%license COPYING
%doc AUTHORS README.md REQUIREMENTS

# Equaliser presets
%{mingw64_datadir}/gstreamer-%{api_version}/presets/

# non-core plugins without external dependencies
%{mingw64_libdir}/gstreamer-%{api_version}/libgstalaw.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstalpha.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstalphacolor.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstapetag.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiofx.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudioparsers.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstauparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstautodetect.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstavi.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcutter.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdebug.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdeinterlace.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdtmf.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsteffectv.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstequalizer.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstflv.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstflxdec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgoom.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgoom2k1.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsticydemux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstid3demux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstimagefreeze.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstinterleave.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstisomp4.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstlevel.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmatroska.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmulaw.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmultifile.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmultipart.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstnavigationtest.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstreplaygain.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtpmanager.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtsp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstshapewipe.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsmpte.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstspectrum.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstspeex.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsttaglib.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstudp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideobox.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideocrop.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideofilter.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideomixer.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwaveform.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwavenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwavpack.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwavparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsty4menc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstadaptivedemux2.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstxingmux.dll

# gstreamer1-plugins with external dependencies but in the main package
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcairo.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdirectsound.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgdkpixbuf.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstjpeg.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstpng.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsoup.dll


%changelog
* Wed Jan 15 2025 Sandro Mani <manisandro@gmail.com> - 1.25.1-1
- Update to 1.25.1

* Sun Jan 12 2025 Sandro Mani <manisandro@gmail.com> - 1.24.11-1
- Update to 1.24.11

* Fri Dec 06 2024 Sandro Mani <manisandro@gmail.com> - 1.24.10-1
- Update to 1.24.10

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

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-2
- Rebuild with mingw-gcc-12

* Sat Feb 05 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-1
- Update to 1.20.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Sandro Mani <manisandro@gmail.com> - 1.19.3-1
- Update to 1.19.3

* Sat Oct 02 2021 Sandro Mani <manisandro@gmail.com> - 1.19.2-1
- Update to 1.19.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Sandro Mani <manisandro@gmail.coM> - 1.19.1-1
- Update to 1.19.1

* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 1.18.4-1
- Update to 1.18.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Sandro Mani <manisandro@gmail.com> - 1.18.2-1
- Update to 1.18.2

* Mon Nov 02 2020 Sandro Mani <manisandro@gmail.com> - 1.18.1-1
- Update to 1.18.1

* Sun Sep 13 2020 Sandro Mani <manisandro@gmail.com> - 1.18.0-1
- Update to 1.18.0

* Wed Aug 12 13:38:35 GMT 2020 Sandro Mani <manisandro@gmail.com> - 1.16.2-3
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.16.2-1
- Update to 1.16.2

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.14.1-6
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.14.1-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Victor Toso <victortoso@redhat.com> - 1.14.1-1
- Update to 1.14.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 1.12.3-1
- Update to 1.12.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 1.12.1-1
- Update to 1.12.1

* Tue Feb  7 2017 Victor Toso <victortoso@redhat.com> - 1.11.1-1
- Update to 1.11.1
- Fixes: CVE-2016-10198, CVE-2016-10199
- Fixes: CVE-2017-5840
- Fixes: CVE-2017-5841
- Fixes: CVE-2017-5845

* Sat Nov  5 2016 Victor Toso <victortoso@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Thu May 12 2016 Kalev Lember <klember@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
- Add gdk-pixbuf build requirement. Resolves: rhbz#1239681

* Mon Dec  8 2014 Victor Toso <victortoso@redhat.com> - 1.4.4-1
- Initial packaging.
  Resolves: rhbz#1166697
