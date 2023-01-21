Name:           oggvideotools
Version:        0.9.1
Release:        9%{?dist}
Summary:        Toolbox for manipulating Ogg video files

License:        GPLv2+
URL:            https://dev.streamnik.de/oggvideotools.html
Source0:        https://downloads.sourceforge.net/project/oggvideotools/oggvideotools/%{name}-%{version}/%{name}-%{version}.tar.gz

Patch0001:      0001-scripts-install-mkSlideshow-as-well.patch
Patch0002:      0002-scripts-install-to-bin-not-sbin.patch
Patch0003:      0003-docs-install-to-share-man.patch
Patch0004:      0004-make-all-internal-libs-STATIC.patch
Patch0005:      0005-unbundle-libresample.patch
Patch0006:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/mayhem-crash-oggjoin.patch
Patch0007:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/manual-typos.patch
Patch0008:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/oggThumb-zero-getopt-long.patch
Patch0009:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/init-for-valgrind.patch
Patch0010:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/import-cstring.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(theoradec)
BuildRequires:  pkgconfig(theoraenc)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(libresample)
BuildRequires:  boost-devel
BuildRequires:  gd-devel

%description
A toolbox for manipulating Ogg video files, which usually consist of a
video stream (Theora) and an audio stream (Vorbis). It includes a
number of handy command line tools for manipulating these video files,
such as for splitting the different streams.

%prep
%autosetup -p1
chmod 644 docs/DocuOggVideoTools.pdf

# Remove bundled libresample
rm -rf src/libresample/

%build
%cmake
%cmake_build

%install
%cmake_install

chmod +x %buildroot%{_bindir}/mkThumbs
chmod +x %buildroot%{_bindir}/mkSlideshow

%global ogg_tool() \
%{_bindir}/ogg%{1}\
%{_mandir}/man1/ogg%{1}.1*

%files
%doc README ChangeLog docs/DocuOggVideoTools.pdf
%license COPYING
%ogg_tool Cat
%ogg_tool Cut
%ogg_tool Dump
%ogg_tool Join
%ogg_tool Length
%ogg_tool Silence
%ogg_tool Slideshow
%ogg_tool Split
%ogg_tool Thumb
%ogg_tool Transcode
%{_bindir}/mkThumbs
%{_mandir}/man1/mkThumbs.1*
%{_bindir}/mkSlideshow

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.1-4
- Fix build and minor rpmlint permission issues

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.1-1
- Update to latest version (from 2016 though ;)).

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.9-7
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.9-2
- Unbundle libresample
- Fix broken dependencies by building static libraries

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.9-1
- Update to 0.9

* Wed Mar 09 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.8-22
- Add oggvideotools-0.8-gcc6.patch (F24FTBFS, RHBZ#1307813)
- Add %%license.
- Don't run autoreconf.
- Fix bogus %%changelog entries.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  1 2015 Tom Callaway <spot@fedoraproject.org> - 0.8-20
- rebuild for libvpx 1.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8-18
- Rebuilt for GCC 5 C++11 ABI change

* Mon Apr  6 2015 Tom Callaway <spot@fedoraproject.org> - 0.8-17
- rebuild against libvpx 1.4.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 0.8-13
- rebuild for new GD 2.1.0

* Mon May 13 2013 Adam Miller <maxamillion@fedoraproject.org> - 0.8-12
- BZ 926266 - add aarch64 support

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.8-10
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.8-9
- rebuild against new libjpeg

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.8-7
- Fix FTBFS

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.8-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 24 2010 Adam Miller <maxamillion@fedoraproject.org> - 0.8-2
- Added man pages

* Mon May 24 2010 Adam Miller <maxmaillion@fedoraproject.org> - 0.8-1
- Upgrade to latest upstream (0.8)

* Mon Aug 10 2009 Adam Miller <maxamillion [AT] gmail.com> - 0.7b-3
- Fixed source0 as per https://www.redhat.com/archives/fedora-devel-list/2009-August/msg00591.html

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 29 2009 Adam Miller <maxamillion [AT] gmail.com> - 0.7b-1
- New release upstream, previous patches are included and no longer needed

* Mon May 18 2009 Adam Miller <maxamillion [AT] gmail.com> - 0.7a-4
- Patch from upstream applied for segfault in oggStream due to big packets

* Fri May 15 2009 Adam Miller <maxamillion [AT] gmail.com> - 0.7a-3
- Patched a bug in oggSlideshow no showing help menu if no args passed

* Fri May 15 2009 Adam Miller <maxamillion [AT] gmail.com> - 0.7a-2
- Added gd-devel to requires as there was an issue with dependencies of:
        oggSlideshow, oggResize, and oggThumb

* Wed Apr 15 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.7a-1
- update to 0.7a
  dropped upstreamed cstring patch
  added oggResize
  bugfix for wrong size in oggThumb, which causes a green border
  minor bugfixes:
  - random number generator is always initialized with a random seed
  - command line options harmonized (e.g. -s is always size)
  handling for corrupt End-Of-Stream markers
  added sample scripts for easy creation of thumbnails and slideshows with sound
  dokumentation update

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan  9 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.6-1
- update to 0.6
  added oggSlideshow, oggThumb
  handling for huge files > 4GB implemented
  packet order with oggCut has been fixed and cleaned up
  ogg type in BOS packet is completely analysed
  added support for kate-streams (done by ogg.k.ogg.k)

* Tue Aug 12 2008 Matt Domsch <mdomsch@fedoraproject.org> - 0.5-1
- Fedora patches applied upstream
- improved documentation

* Thu Jul 24 2008 Matt Domsch <mdomsch@fedoraproject.org> - 0.4-1
- initial build
