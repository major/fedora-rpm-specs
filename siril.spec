Name:           siril
Version:        1.2.0
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
Source0:        https://free-astro.org/download/%{name}-%{version}.tar.bz2

Patch1:         siril-1.0.2-opencv_flann.patch

# Notes on dependencies:
# No ffms and heif support 

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
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(rtprocess)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(wcslib)

Recommends:     gvfs

Provides:       bundled(kplot) = 0.1.14

%description
Siril is an image processing tool specially tailored for noise reduction and
improving the signal/noise ratio of an image from multiple captures, as
required in astronomy. Siril can align automatically or manually, stack and
enhance pictures from various file formats, even images sequences (movies and
SER files)


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%meson \
    -Drelocatable-bundle=no \
    -Dopenmp=true \
    -Dlibheif=false \
    -Dffms2=false \
    -Denable-libcurl=yes

%meson_build


%install
%meson_install

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    platform-specific/linux/org.free_astro.siril.desktop

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.free_astro.siril.appdata.xml

%files -f %{name}.lang
%license LICENSE.md LICENSE_sleef.txt
%doc AUTHORS ChangeLog NEWS README.md
%{_bindir}/%{name}*
%{_datadir}/applications/org.free_astro.siril.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/org.free_astro.siril.appdata.xml
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*.1.gz
# licenses are packaged with %%license
%exclude %{_pkgdocdir}/LICENSE.md
%exclude %{_pkgdocdir}/LICENSE_sleef.txt


%changelog
%autochangelog
