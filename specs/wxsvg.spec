Name:          wxsvg
Version:       1.5.25
Release:       4%{?dist}
Summary:       C++ library to create, manipulate and render SVG files
License:       LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:           https://sourceforge.net/projects/wxsvg
Source0:       https://downloads.sourceforge.net/wxsvg/wxsvg-%{version}.tar.bz2

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: expat-devel
BuildRequires: libexif-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: wxGTK-devel

%description
wxSVG is C++ library to create, manipulate and render Scalable Vector Graphics
(SVG) files with the wxWidgets toolkit.

%package devel
Summary: Development files for the wxSVG library
Group: Development/Libraries

%description devel
wxSVG is C++ library to create, manipulate and render Scalable Vector Graphics
(SVG) files with the wxWidgets toolkit.

This package provides the files required to develop programs that use wxsvg.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static

%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_bindir}/svgview
%{_libdir}/libwxsvg.so.3{,.*}

%files devel
%{_includedir}/wxSVG/
%{_includedir}/wxSVGXML/
%{_libdir}/libwxsvg.so
%{_libdir}/pkgconfig/libwxsvg.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 22 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.5.25-3
- rebuilt for FFmpeg 7

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.5.25-1
- Update to 1.5.25

* Wed May 08 2024 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.24-7
- Minor fix to FFmpeg 7.0 compatibility patch

* Mon May 06 2024 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.24-6
- Add patch for FFMPEG 7 compatibility

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 30 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.5.24-4
- spec cleanup for Fedora inclusion
- use upstream patches with fixes for autoconf-2.71 and gcc-13
- use SPDX License expression
- use pkgconfig-style build dependencies for FFmpeg, cairo and pangocairo
- drop unused build dependencies

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.5.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 13 2023 Leigh Scott <leigh123linux@gmail.com> - 1.5.24-2
- rebuilt

* Wed Aug 31 2022 Sérgio Basto <sergio@serjux.com> - 1.5.24-1
- Update wxsvg to 1.5.24, this release fixes the build with ffmpeg 5.x

* Sun Aug 07 2022 Leigh Scott <leigh123linux@gmail.com> - 1.5.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon Feb 28 2022 Sérgio Basto <sergio@serjux.com> - 1.5.23-4
- Switch to compat-ffmpeg4

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.5.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 04 2021 Sérgio Basto <sergio@serjux.com> - 1.5.23-2
- Rebuild with wxGTK-3.1.x
- Some cleanups

* Wed Dec 01 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.5.23-1
- Update to 1.5.23

* Fri Nov 12 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.22-7
- Rebuilt for new ffmpeg snapshot

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.5.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.5.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.22-4
- Rebuilt for new ffmpeg snapshot

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.5.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.5.22-2
- Rebuild for ffmpeg-4.3 git

* Sat Feb 08 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.5.22-1
- Update to 1.5.22

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.5.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.5.21-1
- Update to 1.5.21

* Mon Aug 26 2019 Sérgio Basto <sergio@serjux.com> - 1.5.20-1
- Update wxsvg to 1.5.20

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 1.5.19-2
- Rebuild for new ffmpeg version

* Thu Jul 04 2019 Sérgio Basto <sergio@serjux.com> - 1.5.19-1
- Update wxsvg to 1.5.19

* Fri Jun 14 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.5.18-1
- Update to 1.5.18

* Mon May 27 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.5.17-1
- Update to 1.5.17

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.5.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.5.16-1
- Update to 1.5.16

* Tue Dec 25 2018 Sérgio Basto <sergio@serjux.com> - 1.5.15-1
- Update to 1.5.15
- Move to wxGTK3 as request in rfbz#5068

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.5.12-7
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.5.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.5.12-5
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.5.12-3
- Rebuilt for ffmpeg-3.5 git

* Tue Oct 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.5.12-2
- Rebuild for ffmpeg update

* Fri Oct 06 2017 Sérgio Basto <sergio@serjux.com> - 1.5.12-1
- Update wxsvg to 1.5.12

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.5.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 30 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.5.11-3
- Rebuild for ffmpeg update

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Sérgio Basto <sergio@serjux.com> - 1.5.11-1
- Update wxsvg to 1.5.11

* Mon Oct 24 2016 Sérgio Basto <sergio@serjux.com> - 1.5.10-1
- Update to 1.5.10, added support of EXIF metadata.

* Tue Sep 27 2016 Sérgio Basto <sergio@serjux.com> - 1.5.9-4
- Let try compat-wxGTK3-gtk2, rfbz#4267

* Tue Aug 16 2016 Sérgio Basto <sergio@serjux.com> - 1.5.9-3
- Remove Requires old wxGTK-devel in wxsvg-devel, also don't need Requires wxsvg

* Mon Aug 15 2016 Sérgio Basto <sergio@serjux.com> - 1.5.9-2
- Upstream suggested to use wxGTK 3.x.

* Tue Aug 09 2016 Sérgio Basto <sergio@serjux.com> - 1.5.9-1
- Update to 1.5.9
- Remove patch0, patch is already in source.

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.5.8-4
- Rebuilt for ffmpeg-3.1.1

* Sat Jul 30 2016 Sérgio Basto <sergio@serjux.com> - 1.5.8-3
- Try fix rfbz#4137 , with upstream fixes.

* Fri Jul 08 2016 Sérgio Basto <sergio@serjux.com> - 1.5.8-2
- Cleanup spec and add License tag

* Wed Jun 22 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.5.8-1
- Update to 1.5.8

* Tue Oct 27 2015 Sérgio Basto <sergio@serjux.com> - 1.5.5-1
- Update to 1.5.5.
- Use autoreconf -i instead autogen.sh

* Thu Apr 09 2015 Sérgio Basto <sergio@serjux.com> - 1.5.4-1
- Update to 1.5.4.

* Fri Jan 23 2015 Sérgio Basto <sergio@serjux.com> - 1.5.3-1
- Update to 1.5.3.

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 1.5-3
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.5-2
- Rebuilt for FFmpeg 2.4.x

* Sun Aug 10 2014 Sérgio Basto <sergio@serjux.com> - 1.5-1
- Update to 1.5

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 1.3-2
- Rebuilt for ffmpeg-2.3

* Sat May 10 2014 Sérgio Basto <sergio@serjux.com> - 1.3-1
- New upstream release .

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 1.2.1-2
- Rebuilt for ffmpeg-2.2

* Thu Oct 17 2013 Sérgio Basto <sergio@serjux.com> - 1.2.1-1
- Update to 1.2.1

* Mon Oct 07 2013 Sérgio Basto <sergio@serjux.com> - 1.2-1
- Update to 1.2

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.15-3
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.15-2
- Rebuilt for x264/FFmpeg

* Sat May 11 2013 Sérgio Basto <sergio@serjux.com> - 1.1.15-1
- Update to 1.1.15

* Mon Apr 08 2013 Sérgio Basto <sergio@serjux.com> - 1.1.14-1
- Update to 1.1.14

* Wed Feb 20 2013 Sérgio Basto <sergio@serjux.com> - 1.1.13-1
- Update to 1.1.13

* Wed Jan 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.12-2
- Rebuilt for ffmpeg

* Mon Jan 21 2013 Sérgio Basto <sergio@serjux.com> - 1.1.12-1
- Update to 1.1.12
- re-use ./autogen.sh
- minor clean ups 

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.9-2
- Rebuilt for FFmpeg 1.0

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.9-1
- Update to 1.1.9
- Use SF URL

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.8-2
- Rebuilt for FFmpeg

* Thu May 03 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.8-1
- Update to 1.1.8

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.2-3
- Rebuilt for x264/FFmpeg

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 28 2011 Stewart Adam <s.adam at diffingo.com> - 1.1.2-1
- Update to 1.1.2

* Mon Sep 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.8-2
- Update to FFmpeg-0.8

* Mon May 2 2011 Stewart Adam <s.adam at diffingo.com> - 1.0.8-1
- Update to 1.0.8

* Mon Jan 18 2010 Stewart Adam <s.adam at diffingo.com> - 1.0.2_1-1
- Update to 1.0.2_1 release

* Wed Oct 21 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.0-8
- rebuild for new ffmpeg

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.0-7
- rebuild for new F11 features

* Wed Jan 21 2009 Stewart Adam <s.adam at diffingo.com> - 1.0-6
- Add libtool and ffmpeg-devel BR
- Package headers & binaries again

* Tue Jan 20 2009 Stewart Adam <s.adam at diffingo.com> - 1.0-5
- Bump for correct upgrade path from Fedora

* Tue Jan 20 2009 Stewart Adam <s.adam at diffingo.com> - 1.0-4
- Rename wxsvg-freeworld to wxsvg and remove soname patch
- Update description

* Thu Dec 11 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-3
- Change soname to wxsvg_freeworld
- Update expat patch, rm -rf internal expat sources
- BR: expat should be BR: expat-devel

* Thu Nov 13 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-2
- Split off a devel package

* Thu Nov 13 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-1
- Update to 1.0 final
- Remove requires on /etc/ld.so.conf.d
- Patch out the internal expat build
- Remove requires on wxsvg
- Own %%{_libdir}/wxsvg-freeworld

* Fri Oct 17 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-0.11.b11
- Remove useless -devel subpackage

* Thu Oct 16 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-0.10.b11
- Remove binaries and include files; these are the same as the originals
- Remove ffmpeg-devel requirement on -devel package
- Get rid of %%configure hack (CFLAGS/CXXFLAGS)
- Require wxsvg and wxsvg-devel so the proper binaries and headers are
  pulled in
- Add patch to use LIBAVFORMAT_{CFLAGS,LDFLAGS} in Makefile.am

* Wed Oct 15 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-0.9.b11
- Make devel package require ffmpeg-devel
- Edit #include statements to append -freeworld
- Add README.Fedora

* Sat Sep 27 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-0.8.b11
- New package based from Fedora's spec
- Update to 1.0b11, enable ffmpeg
- Use ld.so.conf.d to override non-ffmpeg enabled libraries

* Wed Mar  5 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.8.b10
- Update to 1.0b10.
- Build with dependency tracking disabled.

* Sun Feb 24 2008 Matthias Saou <http://freshrpms.net/> 1.0-0.8.b7_3
- Downgrade to 1.0b7_3 since 1.0b8_1 requires ffmpeg and disabling it doesn't
  seem to work properly and it has never avtually been built.
- Update URL field.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 Matthias Saou <http://freshrpms.net/> 1.0-0.6.b8_1
- Update to 1.0b8_1.
- Replace shipping our own ltmain.sh with running libtoolize.
- Disable new ffmpeg option (which is enabled by default).
- Still needs work (doesn't compile!), since ffmpeg seems to be mandatory now.

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.5.b7_3
- Rebuild for new BuildID feature.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.4.b7_3
- Update License field.

* Wed Jun  6 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.3.b7_3
- Update to 1.0b7_3.
- Pass -p to install.
- Remove no longer needed freetype patch, but...
- ...include our own ltmain.sh because it's missing...
- ...run ./autogen.sh since Makefile.in files are missing too.

* Wed May  9 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.2.b7
- Remove rpath on 64bit.
- Update sf.net download URL.
- Add missing wxGTK-devel requirement to the devel package.

* Fri Jan 19 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.1.b7
- Initial RPM release.

