# https://github.com/pioneerspacesim/pioneer/issues/3846
ExclusiveArch: %{ix86} x86_64

# Filter private libraries
%global __provides_exclude ^(%%(find %{buildroot}%{_libdir}/pioneer -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/pioneer -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
#

%global use_autotools 0
%global use_intermediate 0

%if 0%{?use_intermediate}
%global commit e85a0cf4ca8e710d926f6c1581c3d9db242f361f
%global date .20190924git
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
Version: 20230203
Release: 1%{date}%{shortcommit}%{?dist}

## Main license: GPLv3
## Dejavu font license: Bitstream Vera and Public Domain
## Pioneer's art, music and other assets (including Lua model scripts): CC-BY-SA
License: GPLv3 and CC-BY-SA and Bitstream Vera and Public Domain
URL: http://pioneerspacesim.net/
Source0: https://github.com/pioneerspacesim/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Source2: %{name}.appdata.xml

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
#BuildRequires: pkgconfig(glew)
#BuildRequires: pkgconfig(lua)
#BuildRequires: pkgconfig(fmt)
#BuildRequires: pkgconfig(liblz4)
#BuildRequires: miniz-devel
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
Requires: wqy-microhei-fonts
Requires: %{name}-inpionata-fonts
Requires: %{name}-orbiteer-bold-fonts
Requires: %{name}-pionilliumtext22l-medium-fonts

%description data
Data files of %{name}.


%global fontsummary Fonts used by Pioneer
####################
%package inpionata-fonts
Summary: %{fontsummary}
BuildArch: noarch
License:   OFL
Requires:  fontpackages-filesystem

%description inpionata-fonts
%{fontsummary}.

####################
%package orbiteer-bold-fonts
Summary: %{fontsummary}
BuildArch: noarch
License:   OFL
Requires:  fontpackages-filesystem

%description orbiteer-bold-fonts
%{fontsummary}.

####################
%package pionilliumtext22l-medium-fonts
Summary: %{fontsummary}
BuildArch: noarch
License:   OFL
Requires:  fontpackages-filesystem

%description pionilliumtext22l-medium-fonts
%{fontsummary}

%prep
%autosetup -n %{name}-%{version} -N

%patch0 -p1 -b .manual

## Pioneer does not work with Lua 5.4.*
## We cannot unbundle internal Lua yet
## See https://github.com/pioneerspacesim/pioneer/issues/3712
## https://github.com/mpv-player/mpv/issues/5205
#rm -rf contrib/lua

#rm -rf contrib/fmt
#rm -rf contrib/glew
#rm -rf contrib/miniz
#rm -rf contrib/lz4

%build
%if 0%{?use_autotools}
./bootstrap
%configure --disable-silent-rules --with-ccache --without-strip \
 --with-version --with-extra-version --without-extra-warnings \
 --without-thirdparty --without-external-liblua --with-no-optimise \
 PIONEER_DATA_DIR=%{_datadir}/%{name}
%make_build V=1 OPTIMISE=""
%else
mkdir -p build
%cmake -B build -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
       -DUSE_SYSTEM_LIBLUA:BOOL=OFF \
       -DUSE_SYSTEM_LIBGLEW:BOOL=OFF \
       -DPIONEER_DATA_DIR:PATH=%{_datadir}/%{name} -DFMT_INSTALL:BOOL=ON \
       -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}/%{name}
%make_build -C build all build-data
%endif

## Build documentation
#make codedoc
pushd doxygen
doxygen

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

## Moving and editing of appdata file
mkdir -p %{buildroot}%{_metainfodir}
mv %{buildroot}%{_datadir}/appdata/net.pioneerspacesim.Pioneer.appdata.xml %{buildroot}%{_metainfodir}/pioneer.appdata.xml
rm -rf %{buildroot}%{_datadir}/appdata
sed -i 's|net.pioneerspacesim.Pioneer.desktop|pioneer.desktop|' %{buildroot}%{_metainfodir}/pioneer.appdata.xml
sed -i 's|<id>net.pioneerspacesim.Pioneer</id>|<id type="desktop">pioneer.desktop</id>|' %{buildroot}%{_metainfodir}/pioneer.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

## Remove empty directories
find %{buildroot} -name '.gitignore' -exec rm -rf {} ';'

## Unbundle DejaVuSans.ttf, DejaVuSansMono.ttf and wqy-microhei.ttc
mkdir -p %{buildroot}%{_fontdir}
mv %{buildroot}%{_datadir}/%{name}/fonts/Inpionata.ttf %{buildroot}%{_fontdir}
mv %{buildroot}%{_datadir}/%{name}/fonts/Orbiteer-Bold.ttf %{buildroot}%{_fontdir}
mv %{buildroot}%{_datadir}/%{name}/fonts/PionilliumText22L-Medium.ttf %{buildroot}%{_fontdir}

ln -sf %{_fontdir}/Inpionata.ttf %{buildroot}%{_datadir}/%{name}/fonts/Inpionata.ttf
ln -sf %{_fontdir}/Orbiteer-Bold.ttf %{buildroot}%{_datadir}/%{name}/fonts/Orbiteer-Bold.ttf
ln -sf %{_fontdir}/PionilliumText22L-Medium.ttf %{buildroot}%{_datadir}/%{name}/fonts/PionilliumText22L-Medium.ttf

ln -sf $(fc-match -f "%{file}" "wenquanyimicrohei") %{buildroot}%{_datadir}/%{name}/fonts/wqy-microhei.ttc
ln -sf $(fc-match -f "%{file}" "dejavusansmono") %{buildroot}%{_datadir}/%{name}/fonts/DejaVuSansMono.ttf
ln -sf $(fc-match -f "%{file}" "dejavusans") %{buildroot}%{_datadir}/%{name}/fonts/DejaVuSans.ttf

%files
%doc doxygen/html
%{_bindir}/%{name}
%{_libdir}/%{name}/
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
%{_metainfodir}/*.appdata.xml

%files data
%license licenses/GPL-3.txt licenses/CC-BY-SA-3.0.txt licenses/DejaVu-license.txt licenses/SIL-1.1.txt
# Image Use Policy - NASA Spitzer Space Telescope
%license licenses/*.html
%doc AUTHORS.txt Changelog.txt Quickstart.txt README.md
%{_datadir}/%{name}/

%_font_pkg -n %{name}-inpionata Inpionata.ttf
%_font_pkg -n %{name}-orbiteer-bold Orbiteer-Bold.ttf
%_font_pkg -n %{name}-pionilliumtext22l-medium PionilliumText22L-Medium.ttf

%changelog
* Fri Feb 03 2023 Antonio Trande <sagitter@fedoraproject.org> - 20230203-1
- Release 20230203

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220203-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220203-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 26 2022 Antonio Trande <sagitter@fedoraproject.org> - 20220203-3
- Rebuild
- Use bundled GLEW

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 20220203-2
- Rebuild for glew 2.2

* Sat Feb 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 20220203-1
- Release 20220203

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210723-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 10 2021 Antonio Trande <sagitter@fedoraproject.org> - 20210723-3
- Expand build options (rhbz#2002768, upstream bug #5138)

* Sun Aug 01 2021 Rich Mattes <richmattes@gmail.com> - 20210723-2
- Rebuild for assimp-5.0.1

* Fri Jul 23 2021 Antonio Trande <sagitter@fedoraproject.org> - 20210723-1
- Release 20210723

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210203-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 20210203-1
- Release 20210203

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201222-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 20201222-0.4.rc1
- Bundle fmt-6.2.1 (rhbz#1911071)

* Mon Dec 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 20201222-0.3.rc1
- Change filtering method (rhbz#1911071)

* Mon Dec 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 20201222-0.2.rc1
- Install bundled private libraries (rhbz#1911071)

* Tue Dec 22 2020 Antonio Trande <sagitter@fedoraproject.org> - 20201222-0.1.rc1
- Release 20201222-rc1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200203-4
- Second attempt - Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Enable cmake_in_source_build

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200203-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Antonio Trande <sagitter@fedoraproject.org> - 20200203-2
- Conform fonts symlinks to the new paths (rhbz#1835506)

* Mon Feb 03 2020 Antonio Trande <sagitter@fedoraproject.org> - 20200203-1
- Release 20200203

* Thu Jan 30 2020 Antonio Trande <sagitter@fedoraproject.org> - 20191117-3
- Move HTML documentation into main package

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Antonio Trande <sagitter@fedoraproject.org> - 20191117-1
- Release 20191117

* Thu Oct 10 2019 Antonio Trande <sagitter@fedoraproject.org> - 20191009-2
- Add SDL env variable to desktop's Exec command (rhbz#1759866)

* Wed Oct 09 2019 Antonio Trande <sagitter@fedoraproject.org> - 20191009-1
- Release 20191009

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190203-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Antonio Trande <sagitter@fedoraproject.org> - 20190203-3
- Bugfix (upstream #4566)

* Sat Mar 09 2019 Antonio Trande <sagitter@fedoraproject.org> - 20190203-2
- Bugfix (upstream #4555) + new features

* Sun Feb 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 20190203-1
- Release 20190203

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181223-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 20181223-4
- Fix desktop file again

* Fri Jan 04 2019 Antonio Trande <sagitter@fedoraproject.org> - 20181223-3
- Fix desktop file

* Fri Jan 04 2019 Antonio Trande <sagitter@fedoraproject.org> - 20181223-2
- Fix desktop file installation

* Fri Jan 04 2019 Antonio Trande <sagitter@fedoraproject.org> - 20181223-1
- Release 20181223
- Note about Image Use Policy from NASA Spitzer Space Telescope
- Use Upstream's metadata files

* Thu Oct 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 20181127-0.1.gitb8e2b81
- Pre-release 20181127

* Wed Sep 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 20180203-5
- Use %%_metainfodir
- Remove Group tag

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180203-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 20180203-3
- Add gcc gcc-c++ BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180203-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Gwyn Ciesla <limburgher@gmail.com> 20180203-1
- 20180203

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20171001-3
- Remove obsolete scriptlets

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 20171001-2
- Appdata file moved into metainfo data directory

* Sun Oct 01 2017 Antonio Trande <sagitter@fedoraproject.org>  20171001-1
- Update to 20171001

* Tue Aug 29 2017 Antonio Trande <sagitter@fedoraproject.org>  20170827-2
- Exclude stripping of PNG files (bz#1486399)

* Sun Aug 27 2017 Antonio Trande <sagitter@fedoraproject.org>  20170827-1
- Update to 20170827

* Mon Aug 14 2017 Jon Ciesla <limburgher@gmail.com> 20170813-1
- 20170813

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170415-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170415-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 Gwyn Ciesla <limburgher@gmail.com> 20170415-1
- 20170415

* Mon Mar 06 2017 Jon Ciesla <limburgher@gmail.com> 20170304-1
- 20170304

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161129-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Antonio Trande <sagitter@fedoraproject.org>  20161129-3
- Use icon with size 64x64

* Fri Jan 06 2017 Antonio Trande <sagitter@fedoraproject.org>  20161129-2
- Set desktop icon

* Fri Dec 02 2016 Jon Ciesla <limburgher@gmail.com> 20161129-1
- 20161129

* Thu Nov 10 2016 Antonio Trande <sagitter@fedoraproject.org>  20161110-1
- Update to the version 20161110

* Mon Oct 31 2016 Antonio Trande <sagitter@fedoraproject.org>  20161028-1
- Update to the version 20161028 (Bug fixes)

* Wed Oct 26 2016 Antonio Trande <sagitter@fedoraproject.org> 20161022-3
- Set ExclusiveArch

* Tue Oct 25 2016 Antonio Trande <sagitter@fedoraproject.org> 20161022-2
- 'sed' patch for AARCH64 builds

* Mon Oct 24 2016 Jon Ciesla <limburgher@gmail.com> 20161022-1
- 20161022

* Thu Oct 13 2016 Jon Ciesla <limburgher@gmail.com> 20160907-1
- 20160907

* Sun Aug 14 2016 Antonio Trande <sagitter@fedoraproject.org>  20160814-1
- Update to the version 20160814

* Tue Jul 19 2016 Ben Rosser <rosser.bjr@gmail.com> 20160710-1
- Update to latest release

* Sat Jul 09 2016 Antonio Trande <sagitter@fedoraproject.org>  20160701-2
- Fix typos in the appdata file

* Sat Jul 09 2016 Antonio Trande <sagitter@fedoraproject.org>  20160701-1
- Update to release 20160701

* Sun Jun 12 2016 Antonio Trande <sagitter@fedoraproject.org>  20160512-6
- Patched for EXTRA_CXXFLAGS

* Thu Jun 02 2016 Antonio Trande <sagitter@fedoraproject.org>  20160512-5
- Patched for aarch64 build

* Thu Jun 02 2016 Antonio Trande <sagitter@fedoraproject.org>  20160512-4
- hardened_builds flags enabled
- assimp libraries linked manually

* Sat May 28 2016 Antonio Trande <sagitter@fedoraproject.org>  20160512-3
- Unbundle DejaVuSans.ttf DejaVuSansMono.ttf wqy-microhei.ttc font files
- Made Inpionata Orbiteer-Bold PionilliumText22L-Medium fonts sub-packages

* Fri May 27 2016 Antonio Trande <sagitter@fedoraproject.org>  20160512-2
- Made /usr/share/icons/hicolor/40x40 owned
- Replace Summary
- Made a doc sub-package

* Fri May 20 2016 Antonio Trande <sagitter@fedoraproject.org>  20160512-1
- First package
