%global link_tcmalloc 1
%global development 0

%if 0%{?development}
%global commit 4059ae5bcad8e18443bf8f37bcff84de1dcc0d03
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

Name:           rawtherapee
%if 0%{?development}
Version:        5.9~20221002git%{shortcommit}
%else
Version:        5.12~rc1
%endif
Release:        %autorelease
Summary:        Raw image processing software

License:        GPL-3.0-or-later and AGPL-3.0-or-later and MIT-open-group and IJG and BSL-1.0 and Apache-2.0
URL:            http://www.rawtherapee.com/

%if 0%{?development}
Source0:        https://github.com/Beep6581/RawTherapee/archive/%{commit}/RawTherapee-%{commit}.tar.gz
# File created with ./create_ReleaseInfo.sh 5.9 4059ae5 2022-10-02
Source1:        create_ReleaseInfo.sh
Source2:        ReleaseInfo.cmake
%else
#Source0:        https://rawtherapee.com/shared/source/%%{name}-%%{version}.tar.xz
Source0:        https://github.com/Beep6581/RawTherapee/releases/download/5.12-rc1/rawtherapee-5.12-rc1.tar.xz
%endif

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  klt-devel
BuildRequires:  libappstream-glib
BuildRequires:  libatomic

BuildRequires:  pkgconfig(exiv2) >= 0.24
BuildRequires:  pkgconfig(expat) >= 2.1
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.48
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.3
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(lensfun) >= 0.2
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libiptcdata)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.52
%if 0%{?link_tcmalloc}
BuildRequires:  pkgconfig(libtcmalloc)
%endif
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(zlib)

Requires:       hicolor-icon-theme

# https://fedorahosted.org/fpc/ticket/530
# to find: `grep DCRAW_VERSION: rawtherapee-*/rtengine/dcraw.c`
Provides:       bundled(dcraw) = 9.27


%description
Rawtherapee is a RAW image processing software. It gives full control over
many parameters to enhance the raw picture before finally exporting it
to some common image format.

%prep
%if 0%{?development}
%autosetup -p1 -n RawTherapee-%{commit}
cp -p %SOURCE2 .
%else
%autosetup -p1 -n %{name}-5.12-rc1
%endif

# remove bundled KLT, so we're sure to use system provided KLT
rm -rf rtengine/klt/

# remove bundled libraw, so we're sure to use system provided libraw
rm -rf rtengine/libraw/

%build
# do not build shared libs
# https://github.com/Beep6581/RawTherapee/pull/5479
%{cmake} \
        -DCMAKE_BUILD_TYPE=release \
        -DLIBDIR=%{_libdir} \
        -DBUILD_SHARED_LIBS:BOOL=OFF \
%if 0%{?link_tcmalloc}
        -DENABLE_TCMALLOC=ON \
%endif
        -DWITH_SYSTEM_KLT=ON \
        -DWITH_SYSTEM_LIBRAW="ON" \
        -DWITH_JXL="ON"

%cmake_build


%install
%cmake_install


# These file are taken from the root already
rm -rf %{buildroot}/%{_datadir}/doc 


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/com.%{name}.RawTherapee.appdata.xml


%files
%doc AUTHORS.txt RELEASE_NOTES.txt
%license LICENSE licenses/DroidSansMonoDotted.txt licenses/sleef_LICENSE.txt licenses/jdatasrc
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/com.%{name}.RawTherapee.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
%autochangelog
