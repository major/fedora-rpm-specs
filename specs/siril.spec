# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global forgeurl https://gitlab.com/free-astro/siril
%global commit 94c459464fcad5bdf773bf56ead9c9b62096ce11
%forgemeta

Name:           siril
Version:        1.3.6
Release:        %autorelease
Summary:        Astronomical image processing software

# Selected portions of the software derived from SLEEF
# are licensed under Boost license:
# - src/core/sleef.h
#
# 'GPL-2.0-or-later' used in:
# - src/io/kstars/binfile.h
# - src/io/kstars/byteorder.h
#
# 'Zlib' used in:
# - src/pixelMath/tinyexpr.c
# - src/pixelMath/tinyexpr.h
#
# https://gitlab.com/free-astro/siril/-/issues/1192
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND BSL-1.0 AND Zlib
URL:            https://siril.org
Source:         %{forgesource}

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg-free-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(healpix_cxx)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libxisf)
BuildRequires:  pkgconfig(rtprocess)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(yyjson)
BuildRequires:  pkgconfig(wcslib)

Recommends:     gvfs
Recommends:     python3dist(astropy-healpix)

Provides:       bundled(htmesh) = 1.0.0
Provides:       bundled(kplot) = 0.1.14

%description
Siril is an image processing tool specially tailored for noise reduction and
improving the signal/noise ratio of an image from multiple captures, as
required in astronomy. Siril can align automatically or manually, stack and
enhance pictures from various file formats, even images sequences (movies and
SER files)


%prep
%forgeautosetup -p1


%build
%meson \
    -Drelocatable-bundle=no

%meson_build


%install
%meson_install

rm -f %{buildroot}%{_pkgdocdir}/LICENSE.md
rm -f %{buildroot}%{_pkgdocdir}/GPL-2.0-or-later.txt
rm -f %{buildroot}%{_pkgdocdir}/LICENSE_sleef.txt
rm -f %{buildroot}%{_pkgdocdir}/LICENSE_zlib.txt

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.siril.Siril.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.siril.Siril.appdata.xml

%files -f %{name}.lang
%license LICENSE.md 3rdparty_licenses/GPL-2.0-or-later.txt 3rdparty_licenses/LICENSE_sleef.txt 3rdparty_licenses/LICENSE_zlib.txt
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}*
%{_datadir}/applications/org.siril.Siril.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/org.siril.Siril.appdata.xml
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*.1.gz


%changelog
%autochangelog
