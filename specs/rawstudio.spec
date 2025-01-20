# https://github.com/rawstudio/rawstudio/commit/c140a5eb64901e07db5190db20f9884e86e5dcae
%global commit1 c140a5eb64901e07db5190db20f9884e86e5dcae
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

# https://github.com/klauspost/rawspeed/commit/5f73d8b84273c02c3e675c4963c94299be4ccc91
%global commit2 5f73d8b84273c02c3e675c4963c94299be4ccc91
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})

# https://github.com/darktable-org/rawspeed/commit/c753388b096e31f276730ee9b21a9389ca291c7b
%global forgeurl3 https://github.com/darktable-org/rawspeed
%global commit3 c753388b096e31f276730ee9b21a9389ca291c7b

%forgemeta -a

%global build_type_safety_c 0

Name:           rawstudio
Version:        2.1
Release:        0.40.20210527.git%{shortcommit1}%{?dist}
Summary:        Read, manipulate and convert digital camera raw images

# GPL-2.0-or-later: main program
# (Apache-2.0 OR MIT): rawspeed/src/external/gopro/vc5/table17.inc
# BSD-3-Clause: rawspeed/include/libjpeg/turbojpeg.h
# CC-BY-ND-2.5: pixmaps/artwork.license
# CC-BY-SA-3.0:
# - rawspeed/data/
# - profiles/
# (GPL-2.0-or-later AND LicenseRef-Fedora-public-domain): src/rs-store.c
# (GPL-2.0-or-later AND MIT):
# - plugins/colorspace-transform/colorspace_transform_avx.c
# - plugins/colorspace-transform/colorspace_transform_sse2.c
# GPL-3.0-or-later: rawspeed/src/utilities/identify/rawspeed-identify.cpp
# IJG:
# - rawspeed/include/libjpeg/jerror.h
# - rawspeed/include/libjpeg/jmorecfg.h
# - rawspeed/include/libjpeg/jpeglib.h
# LGPL-2.0-or-later: rawspeed/
# (LGPL-2.0-or-later AND BSD-3-Clause):
#  - rawspeed/RawSpeed/X3fParser.cpp
# (LGPL-2.0-or-later AND MIT):
# - rawspeed/src/librawspeed/decompressors/DeflateDecompressor.cpp
# (LGPL-2.0-or-later AND MIT-Modern-Variant):
# - RawSpeed/LJpegDecompressor.cpp
# - src/librawspeed/codes/PrefixCodeLookupDecoder.h
# - src/librawspeed/codes/PrefixCodeLUTDecoder.h
# LGPL-2.1-or-later:
# - rawspeed/src/librawspeed/decompressors/FujiDecompressor.cpp
# - rawspeed/src/librawspeed/decompressors/FujiDecompressor.h
# - rawspeed/src/librawspeed/decompressors/PanasonicV6Decompressor.cpp
# - rawspeed/src/librawspeed/decompressors/PanasonicV6Decompressor.h
# - rawspeed/src/librawspeed/decompressors/PanasonicV7Decompressor.cpp
# - rawspeed/src/librawspeed/decompressors/PanasonicV7Decompressor.h
# LicenseRef-Fedora-Public-Domain:profiles/compatibleWithAdobeRGB1998*.icc
# MIT:
# - rawspeed/RawSpeed/pugiconfig.hpp
# - rawspeed/RawSpeed/pugixml-readme.txt
# - rawspeed/RawSpeed/pugixml.cpp
# - rawspeed/RawSpeed/pugixml.hpp
# - rawspeed/RawSpeed/TiffTag.h
# - rawspeed/src/librawspeed/tiff/TiffTag.h
# - rawspeed/src/utilities/rstest/md5.cpp
# - rawspeed/src/utilities/rstest/md5.h
# - rawspeed/src/utilities/rstest/MD5Test.cpp
# - plugins/dcp/adobe-camera-raw-tone.*
# - plugins/dcp/pow-sse2.h
# Zlib: profiles/compatibleWithAdobeRGB1998*
License:        GPL-2.0-or-later AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND CC-BY-ND-2.5 AND CC-BY-SA-3.0 AND (GPL-2.0-or-later AND LicenseRef-Fedora-public-domain) AND (GPL-2.0-or-later AND MIT) AND GPL-3.0-or-later AND IJG AND LGPL-2.0-or-later AND (LGPL-2.0-or-later AND BSD-3-Clause) AND (LGPL-2.0-or-later AND MIT) AND (LGPL-2.0-or-later AND MIT-Modern-Variant) AND LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain AND MIT AND Zlib
URL:            http://rawstudio.org

Source0:        https://github.com/rawstudio/%{name}/archive/%{commit1}/%{name}-%{shortcommit1}.tar.gz
# cd plugins/load-rawspeed/rawspeed
Source1:        https://github.com/klauspost/rawspeed/archive/%{commit2}/rawspeed-%{shortcommit2}.tar.gz
Source2:        %{forgesource3}
Patch0:         https://github.com/sergiomb2/rawstudio/compare/master...load-dcraw_9.28.diff
Patch2:         0001-Use-ConvertUTF16toUTF8-from-V8-project.patch
Patch3:         0001-Fix-build-with-exiv2-0.28.0.patch
# from https://github.com/rawstudio/rawstudio/pull/81.patch
Patch4:         81.patch
Patch5:         Fix-Rw2Decoder.patch
Patch6:         rawstudio-libxml2.patch
Patch7:         rawstudio-c99.patch
Patch8:         GDateTime.patch


BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gphoto2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
# rawstudio disabled support for osm-gps-map
# BuildRequires:  pkgconnfig(osmgpsmap-1.0)

Provides:       bundled(ufraw) = 0.23

Requires:       librawstudio%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Rawstudio is a highly specialized application for processing RAW images
from digital cameras. It is not a fully featured image editing application.

The RAW format is often recommended to get the best quality out of digital
camera images.  The format is specific to cameras and cannot be read by most
image editing applications.

Rawstudio makes it possible to read and manipulate RAW images, experiment
with the controls to see how they affect the image, and finally export into
JPEG, PNG or TIF format images from most digital cameras.


%package -n     librawstudio-devel
Summary:        librawstudio development files
Requires:       librawstudio%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n librawstudio-devel
Development files for rawstudio backend library


%package -n     librawstudio
Summary: Rawstudio backend library

%description -n librawstudio
Rawstudio backend library


%prep
%setup -q -n %{name}-%{commit1} -a1 -a2
rmdir plugins/load-rawspeed/rawspeed
mv rawspeed-%{commit2} plugins/load-rawspeed/rawspeed
rm -rfv plugins/load-rawspeed/rawspeed/data
mv rawspeed-%{commit3}/data plugins/load-rawspeed/rawspeed/data
%autopatch -p1


%build
# autogen requires sources from git and works with git submodules
#./autogen.sh --no-configure
autoreconf -i

%configure --disable-static --enable-experimental --enable-maintainer-mode
%make_build


%install
%make_install
%find_lang %{name}

desktop-file-install \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        --remove-category Application                           \
        --delete-original                                       \
        ${RPM_BUILD_ROOT}%{_datadir}/applications/rawstudio.desktop

%files -f %{name}.lang
%doc README.md NEWS AUTHORS
%license COPYING
%{_bindir}/rawstudio
%{_libdir}/rawstudio
%{_datadir}/rawstudio
%{_datadir}/rawspeed
%{_datadir}/pixmaps/rawstudio
%{_datadir}/applications/*rawstudio.desktop
%{_datadir}/icons/rawstudio.png
%{_datadir}/appdata/rawstudio.appdata.xml

%files -n librawstudio
%{_libdir}/librawstudio-%{version}.so

%files -n librawstudio-devel
%{_includedir}/rawstudio-%{version}
%{_libdir}/librawstudio.so
%{_libdir}/pkgconfig/rawstudio-%{version}.pc

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.40.20210527.gitc140a5e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.39.20210527.gitc140a5e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Robert-André Mauchin <zebob.m@gmail.com> - c753388b096e31f276730ee9b21a9389ca291c7b
- Rebuilt for exiv2 0.28.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.37.20210527.gitc140a5e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild
- Fix build with 3 patches and set build_type_safety_c 0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.36.20210527.gitc140a5e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 13 2023 Sérgio Basto <sergio@serjux.com> - 2.1-0.35.20210527.gitc140a5e
- Add https://github.com/rawstudio/rawstudio/pull/81 to fix bug No thumbnails in
  priorities https://github.com/rawstudio/rawstudio/issues/80

* Mon Nov 13 2023 Sérgio Basto <sergio@serjux.com> - 2.1-0.34.20210527.gitc140a5e
- grab latest camera sata
- use pkgconfig
- Convert to SPDX licensing, license reanalysis done with scancode-toolkit.
  We have non-free code under the form of LicenseRef-Unicode-legacy-source-code, which is disallowed in Fedora: https://gitlab.com/fedora/legal/fedora-license-data/-/blob/main/data/LicenseRef-Unicode-legacy-source-code.toml
  So we patch it out and replace it with an implementation from Google V8 under BSD-3-Clause.
- Fix build with >=exiv2-0.28.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.33.20210527.git58a8959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.32.20210527.git58a8959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.31.20210527.git58a8959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.30.20210527.git58a8959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.29.20210527.git58a8959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 28 2021 Sérgio Basto <sergio@serjux.com> - 2.1-0.28.20210527.git58a8959
- Update to rawstudio 20210527.git58a8959 more ufraw updates

* Sun Apr 25 2021 Sérgio Basto <sergio@serjux.com> - 2.1-0.27.20200525.g8c732f1_rawspeed.20161119.gfa23d1c
- rawstudio-2.1-0.26.20200525.g8c732f1 more ufraw updates

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.26.20200305.g6e16257_rawspeed.20161119.gfa23d1c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.25.20200305.g6e16257_rawspeed.20161119.gfa23d1c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Sérgio Basto <sergio@serjux.com> - 2.1-0.24.20200305.g6e16257_rawspeed.20161119.gfa23d1c
- Organize sources and update official git commit, but dont expect anything new.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.23.20170414.g003dd4f_rawspeed.20161119.gfa23d1c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.22.20170414.g003dd4f_rawspeed.20161119.gfa23d1c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Sérgio Basto <sergio@serjux.com> - 2.1-0.21.20170414.g003dd4f_rawspeed.20161119.gfa23d1c
- Update plugins/load-dcraw (ufraw) with dcraw_9.28 to fix FTBFS

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.1-0.20.20170414.g003dd4f_rawspeed.20161119.gfa23d1c
- rebuild (exiv2)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.19.20170414.g003dd4f_rawspeed.20161119.gfa23d1c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.18.20170414.g003dd4f_rawspeed.20161119.gfa23d1c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Sérgio Basto <sergio@serjux.com> - 2.1-0.17.20170414.g003dd4f_rawspeed.20161119.gfa23d1c
- Update rawstudio
- Drop already upstreamed patches
- Update rawspeed
- load-dcraw updated to ufraw-0.22 + patches from ufraw fedora package
- Use system theme as default

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.16.20160223git6643b14_rawspeed_5f78369
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.15.20160223git6643b14_rawspeed_5f78369
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1-0.14.20160223git_rawspeed_
- rebuild (exiv2)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.13.20160223git6643b14_rawspeed_5f78369
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 25 2016 Sérgio Basto <sergio@serjux.com> - 2.1-0.12.20160223gitb6bddc9_rawspeed_5f78369
- Update Rawstudio and Rawspeed to the latest commits upstream.
- Remove plugin load-dcraw, also fix FTBFS (#1307983).
- Add one patch that isn't already in upstream tree.
- Add license tag.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.11.20150511git75ef4c4_rawspeed_4ea46dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Rex Dieter <rdieter@fedoraproject.org> 2.1-0.10.20150511git75ef4c4_rawspeed_4ea46dd
- rebuild (lensfun)

* Mon Dec 07 2015 Sérgio Basto <sergio@serjux.com> - 2.1-0.9.20150511git75ef4c4_rawspeed_4ea46dd
- Update rawspeed to git head 4ea46dd.
- Update to git latest bugfix, fix (#1285632) and other 2 SIGSEGV.
- Rawstudio requires same version of librawstudio.

* Wed Nov 25 2015 Sérgio Basto <sergio@serjux.com> - 2.1-0.5.20150511git983bda1
- Autotooling well.
- Follow https://fedoraproject.org/wiki/Packaging:SourceURL
- Added bundled(dcraw).

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.1-0.4.20150511git983bda1
- rebuild (exiv2)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.3.20150511git983bda1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Nils Philippsen <nils@redhat.com> - 2.1-0.2.20150511git983bda1
- rebuild for lensfun-0.3.1

* Wed May 13 2015 Sérgio Basto <sergio@serjux.com> - 2.1-0.1.20150511git983bda1
- Rawstudio from github https://github.com/rawstudio/rawstudio/ .
- Drop all patches because they are upstreamed.
- https://fedoraproject.org/wiki/Packaging:SourceURL#Github
- Updated requirements.
- Use a parcial copy of autogen.sh to build this package.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0-19
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 22 2015 Kalev Lember <kalevlember@gmail.com> - 2.0-18
- Fix the build with lensfun 0.3 (#1184156)

* Tue Jan 20 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.0-17
- rebuild (libgphoto2)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.0-15
- Fix builds for new arches (aarch64/ppc64le)
- Modernise spec

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.0-13
- rebuild (exiv2)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 2.0-11
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.0-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.0-8
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Gianluca Sforna <giallu@gmail.com> - 2.0-6
- rebuild (flickcurl)
- add patch for newer lensfun headers location

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 2.0-5
- rebuild (exiv2)

* Tue Feb 28 2012 Gianluca Sforna <giallu@gmail.com> - 2.0-4
- Fix FTBS with in F17+ (patch from upstream)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 2.0-2
- rebuild (exiv2)

* Fri Apr  8 2011 Gianluca Sforna <giallu@gmail.com> - 2.0-1
- Update to final release
- remove upstreamed patch

* Sat Mar 26 2011 Gianluca Sforna <giallu@gmail.com> - 2.0-0.1.beta1
- Update to released beta
- Split librawstudio library in own package

* Mon Mar 14 2011 Gianluca Sforna <giallu@gmail.com> - 1.2-10
- update to newer snapshot, another fixed crash

* Mon Feb 21 2011 Gianluca Sforna <giallu@gmail.com> - 1.2-9
- update to newer snapshot, includes fixes for #635964 and #636919
- remove upstreamed patch, add new one to remove -Werror
- require gphoto2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8.20100907svn3521
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.2-7.20100907svn3521
- rebuild (exiv2)

* Wed Sep  8 2010 Gianluca Sforna <giallu gmail com>
- Fix BuildRequires
- Add updated patch for X11 link issue

* Tue Sep  7 2010 Gianluca Sforna <giallu gmail com>
- move to a snapshot
- drop upstreamed patches
- add find-lang
- remove .la files
- disable static library build

* Mon May 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.2-5
- rebuild (exiv2)

* Sat Feb 13 2010 Gianluca Sforna <giallu gmail com> - 1.2-4
- Add explicit link to libX11 (#564638)

* Mon Jan 04 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.2-3
- rebuild (exiv2)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 10 2009 Gianluca Sforna <giallu gmail com> - 1.2-1
- New upstream release

* Thu Feb 26 2009 Gianluca Sforna <giallu gmail com> - 1.1.1-4
- Fix build with newer glibc

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.1.1-2
- respin (eviv2)

* Mon Oct 13 2008 Gianluca Sforna <giallu gmail com> - 1.1.1-1
- new upstream release

* Tue Sep 16 2008 Gianluca Sforna <giallu gmail com> - 1.1-1
- new upstream release

* Thu May  1 2008 Gianluca Sforna <giallu gmail com> - 1.0-1
- new upstream release
- drop upstreamed patch
- slightly improved summary

* Tue Feb 26 2008 Gianluca Sforna <giallu gmail com> - 0.7-2
- rebuild with gcc 4.3

* Thu Jan 24 2008 Gianluca Sforna <giallu gmail com> - 0.7-1
- New upstream release
- Improved package description
- Add fix for PPC build

* Sun Aug 19 2007 Gianluca Sforna <giallu gmail com> 0.6-1
- New upstream release
- Updated License field
- Include new pixmaps directory

* Wed Feb 21 2007 Gianluca Sforna <giallu gmail com> 0.5.1-1
- New upstream release
- Fix desktop-file-install warnings

* Tue Feb 06 2007 Gianluca Sforna <giallu gmail com> 0.5-1
- new upstream version
- add libtiff-devel BR
- drop upstreamed patch
- drop dcraw runtime Require

* Wed Sep 27 2006 Gianluca Sforna <giallu gmail com> 0.4.1-1
- new upstream version
- Add DESTDIR patch (and BR: automake)
- New .desktop file and icon

* Fri Jul 28 2006 Gianluca Sforna <giallu gmail com> 0.3-1
- Initial package. Adapted from fedora-rpmdevtools template.
