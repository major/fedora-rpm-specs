# https://github.com/pioneerspacesim/pioneer/issues/3846
ExclusiveArch: %{ix86} x86_64

%global fontlicense       OFL-1.1
%global fontlicenses      licenses/SIL-1.1.txt
%global common_description %{expand:
This font is generated and used by Pioneer package}

%global fontfamily1       Inpionata
%global fontsummary1      Pioneer Inpionata font
%global fonts1            data/fonts/Inpionata.ttf
%global fontdescription1  %{expand:
%{common_description}.}
%global fontpkgheader1    %{expand:
Obsoletes: %{name}-inpionata-fonts < %{version}-%{release}
}

%global fontfamily2       Orbiteer Bold
%global fontsummary2      Pioneer Orbiteer Bold font
%global fonts2            data/fonts/Orbiteer-Bold.ttf
%global fontdescription2  %{expand:
%{common_description}.}
%global fontpkgheader2    %{expand:
Obsoletes: %{name}-orbiteer-bold-fonts < %{version}-%{release}
}

%global fontfamily3       PionilliumText22L Medium
%global fontsummary3      Pioneer PionilliumText22L Medium font
%global fonts3            data/fonts/PionilliumText22L-Medium.ttf
%global fontdescription3  %{expand:
%{common_description}.}
%global fontpkgheader3    %{expand:
Obsoletes: %{name}-pionilliumtext22l-medium-fonts < %{version}-%{release}
}

# Filter private libraries
%global __provides_exclude ^(%%(find %{buildroot}%{_libdir}/%{name} -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/%{name} -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
#

%global use_autotools 0
%global use_intermediate 0

%if 0%{?use_intermediate}
%global commit cd91559f6e6ab1bf42a6270c0826e4ea5f2d3f29
%global date .20230301git
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%else
%global commit %{nil}
%global date %{nil}
%global shortcommit %{nil}
%endif

## This package uses an own miniz.h file.
## Upstream: taken from http://miniz.googlecode.com/svn/trunk/miniz.c. I've cut this into
## header and implementation files and disabled (via define) some interfaces that
## we don't need:
# - MINIZ_NO_ARCHIVE_WRITING_APIS
# - MINIZ_NO_ZLIB_COMPATIBLE_NAMES

Name: pioneer
Summary: A game of lonely space adventure
Version: 20250203
Release: %autorelease

## Main license: GPLv3
## Dejavu font license: Bitstream Vera and Public Domain
## The file scripts/ShipPlanner015.py: GPLv2+
## contrib/lz4: BSD 2-Clause
License: GPL-3.0-only AND GPL-2.0-or-later AND Bitstream-Vera AND LicenseRef-Fedora-Public-Domain AND BSD-2-Clause
URL: http://pioneerspacesim.net/
#Source0: https://github.com/pioneerspacesim/%%{name}/archive/%%{commit}/%%{name}-%%{version}.tar.gz
Source0: https://github.com/pioneerspacesim/%{name}/archive/%{version}/%{name}-%{version}.tar.gz


BuildRequires: make
%if 0%{?use_autotools}
BuildRequires: autoconf
BuildRequires: automake
%else
BuildRequires: cmake
%endif
BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: fontpackages-devel
BuildRequires: gcc, gcc-c++
BuildRequires: graphviz
BuildRequires: ImageMagick
BuildRequires: pkgconfig
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(libpng)
BuildRequires: assimp-devel >= 3.2
BuildRequires: mesa-libGLU-devel
BuildRequires: NaturalDocs
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: %{name}-data = %{version}-%{release}
Requires: hicolor-icon-theme
Requires: graphviz%{?_isa}

Obsoletes: %{name}-doc < 0:20191117-3
Provides: bundled(fmt) = 6.2.1

# I prefer to install binary files manually
Patch0: %{name}-use_manual_installation.patch

Patch1: %{name}-gcc14.patch
Patch2: %{name}-fix_GCC15.patch

%fontpkg -a


%description
A space adventure game set in the Milky Way galaxy at the turn of
the 31st century.

The game is open-ended, and you are free to explore the millions of star
systems in the game. You can land on planets, slingshot past gas giants, and
burn yourself to a crisp flying between binary star systems. You can try your
hand at piracy, make your fortune trading between systems, or do missions for
the various factions fighting for power, freedom or self-determination.

####################
%package data
Summary: Data files of %{name}
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: dejavu-sans-fonts
BuildRequires: dejavu-sans-mono-fonts
Requires: wqy-microhei-fonts
Requires: dejavu-sans-fonts
Requires: dejavu-sans-mono-fonts

%description data
Data files of %{name}.

%prep
%autosetup -n %{name}-%{version} -N
%patch -P 0 -p1 -b .backup
%patch -P 1 -p1 -b .backup
%patch -P 2 -p1 -b .backup

%build
%if 0%{?use_autotools}
./bootstrap
%configure --disable-silent-rules --with-ccache --without-strip \
 --with-version --with-extra-version --without-extra-warnings \
 --without-thirdparty --without-external-liblua --with-no-optimise \
 PIONEER_DATA_DIR=%{_datadir}/%{name}/data
%make_build V=1 OPTIMISE=""
%else
mkdir -p build
%cmake -B build -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
       -DPROJECT_VERSION_INFO:STRING=%{version} \
       -DUSE_SYSTEM_LIBLUA:BOOL=OFF \
       -DUSE_SYSTEM_LIBGLEW:BOOL=OFF \
       -DPIONEER_DATA_DIR:PATH=%{_datadir}/%{name}/data -DFMT_INSTALL:BOOL=ON \
       -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}/%{name}
%make_build -C build all build-data
%endif

## Build documentation
#pushd doxygen
#doxygen
#popd


%fontbuild -a

%install
%if 0%{?use_autotools}
%make_install
%else
%make_install -C build
%endif

# Install binary files manually
mkdir -p %{buildroot}%{_bindir}
install -pm 755 build/pioneer %{buildroot}%{_bindir}/
install -pm 755 build/modelcompiler %{buildroot}%{_bindir}/
install -pm 755 build/savegamedump %{buildroot}%{_bindir}/

## Use rpaths versus private libraries
chrpath -r %{_libdir}/%{name} %{buildroot}%{_bindir}/*

# Remove unused development files
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/pioneer/cmake
rm -rf %{buildroot}%{_libdir}/pioneer/pkgconfig

## Install icons
mkdir -p %{buildroot}%{_datadir}/icons/%{name}
install -pm 644 application-icon/*.ico %{buildroot}%{_datadir}/icons/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -pm 644 application-icon/badge-* %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/22x22/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/40x40/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -Dpm 644 application-icon/pngs/%{name}-16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
install -Dpm 644 application-icon/pngs/%{name}-22x22.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps
install -Dpm 644 application-icon/pngs/%{name}-24x24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
install -Dpm 644 application-icon/pngs/%{name}-32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -Dpm 644 application-icon/pngs/%{name}-40x40.png %{buildroot}%{_datadir}/icons/hicolor/40x40/apps
install -Dpm 644 application-icon/pngs/%{name}-48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -Dpm 644 application-icon/pngs/%{name}-64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -Dpm 644 application-icon/pngs/%{name}-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -Dpm 644 application-icon/pngs/%{name}-256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

## Modifing of desktop file
# Converting to utf-8
for file in %{buildroot}%{_datadir}/applications/net.pioneerspacesim.Pioneer.desktop ; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

# Renaming and editing
mv %{buildroot}%{_datadir}/applications/net.pioneerspacesim.Pioneer.desktop %{buildroot}%{_datadir}/applications/pioneer.desktop
desktop-file-edit \
 --set-icon=%{_datadir}/icons/hicolor/64x64/apps/%{name}-64x64.png \
 --set-key=Exec --set-value="env force_s3tc_enable=true SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0 pioneer" \
 --set-key=StartupNotify --set-value=false \
 %{buildroot}%{_datadir}/applications/pioneer.desktop

## Change and edit of appdata file
mv %{buildroot}%{_metainfodir}/net.pioneerspacesim.Pioneer.metainfo.xml %{buildroot}%{_metainfodir}/pioneer.metainfo.xml
sed -i 's|net.pioneerspacesim.Pioneer.desktop|pioneer.desktop|' %{buildroot}%{_metainfodir}/pioneer.metainfo.xml
sed -i 's|<id>net.pioneerspacesim.Pioneer</id>|<id type="desktop">pioneer.desktop</id>|' %{buildroot}%{_metainfodir}/pioneer.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/pioneer.metainfo.xml

## Remove empty directories
find %{buildroot} -name '.gitignore' -exec rm -rf {} ';'

## Unbundle DejaVuSans.ttf, DejaVuSansMono.ttf and wqy-microhei.ttc
ln -sf $(fc-match -f "%{file}" "wenquanyimicrohei") %{buildroot}%{_datadir}/%{name}/data/fonts/wqy-microhei.ttc
ln -sf $(fc-match -f "%{file}" "dejavusansmono") %{buildroot}%{_datadir}/%{name}/data/fonts/DejaVuSansMono.ttf
ln -sf $(fc-match -f "%{file}" "dejavusans") %{buildroot}%{_datadir}/%{name}/data/fonts/DejaVuSans.ttf

# Install Pioneer fonts and link to to the Fedora Fonts Packaging paths
%fontinstall -a
ln -sf %{_datadir}/fonts/inpionata-fonts/Inpionata.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/Inpionata.ttf
ln -sf %{_datadir}/fonts/orbiteer-fonts/Orbiteer-Bold.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/Orbiteer-Bold.ttf
ln -sf %{_datadir}/fonts/pionilliumtext22l-fonts/PionilliumText22L-Medium.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/PionilliumText22L-Medium.ttf


%check	
%fontcheck

%fontfiles -a


%files
%{_bindir}/%{name}
#%%{_libdir}/%%{name}/
%{_bindir}/modelcompiler
%{_bindir}/savegamedump
%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/icons/hicolor/22x22/apps/*.png
%{_datadir}/icons/hicolor/24x24/apps/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png
## Following directories are not owned by hicolor-icon-theme
%dir %{_datadir}/icons/hicolor/40x40
%dir %{_datadir}/icons/hicolor/40x40/apps
##
%{_datadir}/icons/hicolor/40x40/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/64x64/apps/*.png
%{_datadir}/icons/hicolor/128x128/apps/*.png
%{_datadir}/icons/hicolor/256x256/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/%{name}/
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.metainfo.xml

%files data
%license licenses/*.txt
# Image Use Policy - NASA Spitzer Space Telescope
%doc AUTHORS.txt Changelog.txt Quickstart.txt README.md
%{_datadir}/%{name}/


%changelog
%autochangelog
