%global __cmake_in_source_build 1

%global commit 570ba7a8adc7973327ae612a3d535fd8621c41dd
%global date 20180321
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# For building documentation, it needed Python2
%global with_doc 0


Name:           openclonk
Summary:        Multiplayer action, tactics and skill game
Version:        8.1
Release:        18.%{date}git%{shortcommit}%{?dist}
URL:            http://www.openclonk.org/
Source0:        https://github.com/openclonk/openclonk/archive/%{commit}/%{name}-%{commit}.tar.gz
License:        ISC and CC-BY-SA

Source1:        %{name}-html.desktop
Source2:        %{name}-docs.png
Patch0:         %{name}-gcc11.patch

BuildRequires: make
BuildRequires:  boost-devel
BuildRequires:  cmake, gcc, gcc-c++
BuildRequires:  python3-devel
BuildRequires:  gtest-devel
BuildRequires:  libjpeg-devel
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libpng12)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(xml2po)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  readline-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libxslt
BuildRequires:  gettext
BuildRequires:  libxml2-devel
BuildRequires:  gtk3-devel

Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme
Provides:       bundled(timsort)

Obsoletes:   %{name}-devel-docs < 0:8.1-9
Obsoletes:   %{name}-doc < 0:8.1-10

%description
Clonk is a multiplayer-action-tactics-skill game.
It is often referred to as a mixture of The Settlers and Worms.
In a simple 2D antfarm-style landscape, the player controls
his crew of Clonks, small but robust humanoid beings.
The game encourages free play but the normal goal is to
either exploit valuable resources from the earth
by building a mine or fight each other on an arena-like map.

%package     data
Summary:     %{summary}
Requires:    %{name} = %{version}-%{release}
BuildArch:   noarch

%description data
This package contains the data files for openclonk.

%if 0%{?with_doc}
%package     doc
Summary:     Documentation for developing programs that will use %{name}
BuildArch:   noarch
Requires:    xdg-utils
Obsoletes:   %{name}-devel-docs < 0:8.1-9

%description doc
This package contains documentation needed for developing with %{name}.
%endif

%prep
%autosetup -p1 -n %{name}-%{commit}

# remove bundled tinyxml
rm -rf thirdparty/tinyxml
# remove bundled getopt
rm -rf thirdparty/getopt
# remove bundled natupnp
rm -rf thirdparty/natupnp
rm -rf planet/Tests.c4f
# change permission in src and docs folder
find src -type f | xargs chmod -v 644
find docs -type f | xargs chmod -v 644
find docs -type d | xargs chmod -v 755

# change permission due rpmlint W: spurious-executable-perm
chmod a-x README Credits.txt thirdparty/timsort/sort.h \
          COPYING TRADEMARK licenses/*

# Set directory for datafiles
sed -e 's|share/games/openclonk|share/openclonk|g' -i CMakeLists.txt

cp -p planet/COPYING COPYING-planet

# Force Python3
%if 0%{?with_doc}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}" docs/build_hhp.py docs/xml2po.py docs/build_contents.py
sed -i 's|@python2|@python3|' docs/Makefile
%endif

%build
mkdir -p build && cd build

# -Werror=format-security/ flag prevents compilation
# https://github.com/openclonk/openclonk/issues/64
export LDFLAGS="$RPM_LD_FLAGS"
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
%cmake -Wno-cpp -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_CXX_FLAGS:STRING="$SETOPT_FLAGS" \
 -DCMAKE_EXE_LINKER_FLAGS:STRING="$RPM_LD_FLAGS" \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_SKIP_RPATH:BOOL=NO -DWITH_AUTOMATIC_UPDATE:BOOL=OFF \
 -DUSE_X11:BOOL=ON -DUSE_GTK:BOOL=ON -DBUILD_SHARED_LIBS:BOOL=OFF \
 -DUSE_STATIC_BOOST=OFF -DUSE_SYSTEM_TINYXML=ON \
 -DUSE_GCC_STYLE_LTCG:BOOL=OFF ..
%make_build

# build the English HTML-documentation from the English \
# XML-source files and the translation file
%if 0%{?with_doc}
pushd ../docs
%make_build chm/en/Developer.chm
popd
%endif

%install
%make_install -C build
install -pm 755 $RPM_BUILD_ROOT%{_prefix}/games/openclonk $RPM_BUILD_ROOT%{_bindir}/
rm -rf $RPM_BUILD_ROOT%{_prefix}/games

# Move upstream appdata file to metainfo/ directory
mkdir -p $RPM_BUILD_ROOT%{_datadir}/metainfo
install -pm 644 $RPM_BUILD_ROOT%{_datadir}/appdata/*.appdata.xml $RPM_BUILD_ROOT%{_datadir}/metainfo/
rm -rf $RPM_BUILD_ROOT%{_datadir}/appdata

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/*.appdata.xml

%if 0%{?with_doc}
# W: wrong-file-end-of-line-encoding
sed -i 's/\r$//' docs/chm/en/Output.hhp

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}-docs.png

# HTML desktop files
install -pm 0644  %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/
%endif

# Set main desktop file (bz#1454638)
desktop-file-edit --remove-key=Comment[de] \
%if 0%{?fedora} && 0%{?fedora} < 31
 --set-key=Exec --set-value="env WAYLAND_DISPLAY= openclonk" \
%else
 --set-key=Exec --set-value=openclonk \
%endif
$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files
%doc Version.txt README TRADEMARK Credits.txt
%license COPYING COPYING-planet
%{_bindir}/openclonk
%{_bindir}/c4group
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/*.appdata.xml

%files data
%{_datadir}/%{name}/

%if 0%{?with_doc}
%files doc
%license COPYING COPYING-planet
%doc docs/chm/en
%{_datadir}/applications/%{name}-html.desktop
%{_datadir}/pixmaps/%{name}-docs.png
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-18.20180321git570ba7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 8.1-17.20180321git570ba7a
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-16.20180321git570ba7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-15.20180321git570ba7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-14.20180321git570ba7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 8.1-13.20180321git570ba7a
- Fix missing #include for gcc-11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-12.20180321git570ba7a
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-11.20180321git570ba7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 8.1-10.20180321git570ba7a
- Use python3 but disable documentation building

* Wed Jan 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 8.1-9.20180321git570ba7a
- Obsoletes devel-docs sub-package
- Add python2-devel BR

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-8.20180321git570ba7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-7.20180321git570ba7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-6.20180321git570ba7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 8.1-5.20180321git570ba7a
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-4.20180321git570ba7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Antonio Trande <sagitter@fedoraproject.org> - 8.1-3.20180321git570ba7a
- Update to commit #570ba7a (blake2 no-SSE reloaded) for upstream bug #69

* Sun Mar 18 2018 Antonio Trande <sagitter@fedoraproject.org> - 8.1-2
- ExclusiveArch for upstream bug #69

* Sat Mar 17 2018 Martin Gansser <martinkg@fedoraproject.org> - 8.1-1
- Update to 8.1 (bz#1557656)
- Add BR gcc

* Fri Feb 09 2018 Antonio Trande <sagitter@fedoraproject.org> - 8.0-2
- Set USE_GCC_STYLE_LTCG CMake option

* Fri Feb 09 2018 Martin Gansser <martinkg@fedoraproject.org> - 8.0-1
- Update to version 8.0
- Disable Werror=format-security flag (https://github.com/openclonk/openclonk/issues/64)
- Use appdata file from upstream

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0-10
- Remove obsolete scriptlets

* Fri Dec 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 7.0-9
- Appdata file moved into metainfo data directory

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 24 2017 Antonio Trande <sagitter@fedoraproject.org> - 7.0-6
- Set main desktop file (bz#1454638)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 7.0-4
- Rebuild for glew 2.0.0

* Tue May 10 2016 Antonio Trande <sagitter@fedoraproject.org> - 7.0-3
- Made sub-package for documentation

* Sun May 08 2016 Antonio Trande <sagitter@fedoraproject.org> - 7.0-2
- Unbundle getopt
- Strip all .png files
- Make an appdata file

* Sat May 07 2016 Antonio Trande <sagitter@fedoraproject.org> - 7.0-1
- First package
