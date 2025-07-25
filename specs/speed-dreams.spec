Name:           speed-dreams
Version:        2.4.2
Release:        3%{?dist}
Epoch:          1
Summary:        3D Open Racing Simulation

# Speed Dreams source is under GPL-2.0-or-later by default
# https://speed-dreams.net/en/about
License: GPL-2.0-or-later AND LAL-1.3
# Media content: Graphics, sounds, and other artistic works are licensed under LAL-1.3

URL:            https://www.speed-dreams.net
# ------------------------------------------------------------------------------
# retrieve sources and create archive:
# 
# $ git clone --recursive https://forge.a-lec.org/speed-dreams/speed-dreams-code speed-dreams
# $ cd speed-dreams
# $ git checkout tags/v2.4.2
# $ git submodule update --init --recursive
# $ cd ..
# $ mv speed-dreams speed-dreams-2.4.2
# $ tar -cJf speed-dreams-2.4.2.tar.xz speed-dreams-2.4.2
# ------------------------------------------------------------------------------
Source0:        %{name}-%{version}.tar.xz

ExcludeArch:    s390x

Provides:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-robots-base = %{epoch}:%{version}
Requires:       opengl-games-utils
Requires:       bitstream-vera-sans-fonts
Requires:       dejavu-lgc-sans-fonts
BuildRequires:  bitstream-vera-sans-fonts
BuildRequires:  dejavu-lgc-sans-fonts
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  chrpath
BuildRequires:  libcurl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  enet-devel
BuildRequires:  expat-devel
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  FreeSOLID-devel >= 2.1.2
BuildRequires:  libGL-devel
BuildRequires:  libjpeg-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  plib-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  OpenSceneGraph-devel
BuildRequires:  cjson-devel
BuildRequires:  minizip-devel
BuildRequires:  rhash-devel

# Dont provide or require internal libs. Using new rpm builtin filtering,
# see https://docs.fedoraproject.org/en-US/packaging-guidelines/AutoProvidesAndRequiresFiltering/
%global __requires_exclude                       liblearning.so
%global __requires_exclude %{__requires_exclude}|libnetworking.so
%global __requires_exclude %{__requires_exclude}|libraceengine.so
%global __requires_exclude %{__requires_exclude}|librobottools.so
%global __requires_exclude %{__requires_exclude}|libtgf.so
%global __requires_exclude %{__requires_exclude}|libtgfclient.so
%global __requires_exclude %{__requires_exclude}|libtgfdata.so
%global __requires_exclude %{__requires_exclude}|libportability.so
%global __requires_exclude %{__requires_exclude}|libcsnetworking.so

%global __provides_exclude_from %{_libdir}/games/speed-dreams-2/.*\\.so

%description
Speed-Dreams is a 3D racing cars simulator using OpenGL. A Fork of TORCS.
The goal is to have programmed robots drivers racing against each others.
You can also drive yourself with either a wheel, keyboard or mouse.

%package robots-base
Summary:       The Open Racing Car Simulator additional dirt tracks
BuildArch:     noarch
Requires:      %{name} =  %{epoch}:%{version}-%{release}

%description robots-base
This package contains additional tracks for the game.

%package devel
Summary:       The Open Racing Car Simulator development files
Requires:      %{name}%{?_isa} =  %{epoch}:%{version}-%{release}
            
%description devel
This package contains the development files for the game.

%prep
%autosetup -p1 -n %{name}-%{version}

# delete unused header file on arm achitecture
sed -i -e 's|#include "OsgReferenced.h"||g' src/modules/graphic/osggraph/Sky/OsgDome.h

# remove obsolete encoding key from .desktop file
sed -i '/^Encoding=/d' speed-dreams.desktop.in
sed -i '/^Name=/c\Name=/Speed Dreams 2' speed-dreams.desktop.in
sed -i '/^Icon=/c\Icon=/usr/share/games/speed-dreams-2/data/icons/icon.png' speed-dreams.desktop.in

# unbundle freesolid
rm -rf freesolid
rm -rf src/tools/trackeditor

# fixes spurious-executable-perm
# https://sourceforge.net/p/speed-dreams/tickets/605/
find . -name '*.c' -o -name '*.h' -o -name '*.cpp' -o -name '*.hpp' | \
    xargs chmod 644

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo       \
       -DCMAKE_SKIP_RPATH:BOOL=OFF                    \
       -DOPTION_DEBUG:STRING=ON                       \
       -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"  \
       -DSD_BINDIR:PATH=bin                           \
       -DOPTION_3RDPARTY_SOLID:BOOL=ON                \
       -DOPTION_TRACKEDITOR:BOOL=OFF                  \
       -DOPTION_OFFICIAL_ONLY:BOOL=ON                 \
       -DCMAKE_C_FLAGS="%{optflags}"                  \
       -DCMAKE_CXX_FLAGS="%{optflags}"
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name "*.cmake" -delete

install -Dm 0644 packaging/appdata/speed-dreams-2.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

pushd %{buildroot}%{_libdir}/games/%{name}-2
    # Change rpath to refer only private lib dir.
    for lib in $(find . -type f -name \*.so ); do
        # Bug: cmake should make so-files 755 on Fedora by default.
        chmod 755 $lib
        chrpath --replace %{_libdir}/games/%{name}-2/lib $lib
    done

    # Check that %%{buildroot}%%{_libdir}/games/%%{name}-2/lib doesn't 
    # contain unfiltered libs.
    excluded=$( echo '%{__requires_exclude}' | tr '|' ':' )
    for lib in *.so; do
        if [ "${excluded/${lib}/}" = "$excluded" ]; then
            echo "ERROR: $lib not filtered in __requires_exclude" >&2
            exit 2
        fi
    done
popd

# ERROR   0001: file '/usr/bin/speed-dreams-2' contains a standard runpath '/usr/lib64' in [/usr/lib64/games/speed-dreams-2/lib:/usr/lib64]
# ERROR   0001: file '/usr/bin/sd2-accc' contains a standard runpath '/usr/lib64' in [/usr/lib64/games/speed-dreams-2/lib:/usr/lib64]
# ERROR   0001: file '/usr/bin/sd2-nfs2ac' contains a standard runpath '/usr/lib64' in [/usr/lib64/games/speed-dreams-2/lib:/usr/lib64]
# ERROR   0001: file '/usr/bin/sd2-nfsperf' contains a standard runpath '/usr/lib64' in [/usr/lib64/games/speed-dreams-2/lib:/usr/lib64]
# ERROR   0001: file '/usr/bin/sd2-trackgen' contains a standard runpath '/usr/lib64' in [/usr/lib64/games/speed-dreams-2/lib:/usr/lib64]
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/speed-dreams-2
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-accc
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-nfs2ac
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-nfsperf
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-trackgen

# Remove obsolete or unnecessary files from the installation directory
rm -f %{buildroot}%{_includedir}/3D/Makefile.am
rm -f %{buildroot}%{_includedir}/SOLID/Makefile.am

# Replace bundled fonts with symlink to system fonts
ln -sf /usr/share/fonts/dejavu/DejaVuSans.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/DejaVuLGCSans.ttf
ln -sf /usr/share/fonts/bitstream-vera/Vera.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/Vera.ttf
ln -sf /usr/share/fonts/bitstream-vera/VeraBd.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/VeraBd.ttf
ln -sf /usr/share/fonts/bitstream-vera/VeraBI.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/VeraBI.ttf
ln -sf /usr/share/fonts/bitstream-vera/VeraMono.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/VeraMono.ttf
ln -sf ../Vera.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/vera/Vera.ttf

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

# remove zero length files
find %{buildroot} -size 0 -delete

%files
%license LICENSE
%doc README.md
%{_mandir}/man6/*
%{_bindir}/%{name}-2
%{_bindir}/sd2-*
%{_libdir}/games/%{name}-2/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/games/%{name}-2/
%exclude %{_datadir}/games/%{name}-2/cars/
%exclude %{_datadir}/games/%{name}-2/config/
%exclude %{_datadir}/games/%{name}-2/data/
%exclude %{_datadir}/games/%{name}-2/drivers/
%exclude %{_datadir}/games/%{name}-2/tracks/

%files robots-base
%{_datadir}/games/%{name}-2/cars/
%{_datadir}/games/%{name}-2/config/
%{_datadir}/games/%{name}-2/data/
%{_datadir}/games/%{name}-2/drivers/
%{_datadir}/games/%{name}-2/tracks/

%files devel
%{_includedir}/%{name}-2/

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.2-2
- Switch on more debug information

* Fri May 30 2025 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.2-1
- Update to 2.4.2

* Tue May 27 2025 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.1-1
- Update to 2.4.1
- Add 9ae2b6cc83ce5cdaec58cb4d2aed2fb5ae60b7c8.patch to restore FindSOLID.cmake
  so that the FreeSOLID library can be found again

* Tue Jul 25 2023 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.0-1
- Update to 2.3.0
- Add BR SDL2_mixer-devel

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 11 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.3-4
- Rebuilt for rawhide

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Sandro Mani <manisandro@gmail.com> - 1:2.2.3-2
- Rebuild (OpenSceneGraph)

* Sat Aug 07 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.3-1
- Update to 2.2.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 10 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.2-13
- Rebuilt for rawhide

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Jeff Law <law@redhat.com> - 1:2.2.2-11
- Fix ordered comparison between pointer and NULL for gcc11

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.2-10
- Rebuilt for rawhide

* Fri Aug 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.2-9
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.2-6
- Rebuilt
- Add ExcludeArch s390x

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.2-4
- Rebuilt

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.2-1
- Update to 2.2.2

* Mon Aug 20 2018 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.2-0.4.20180820svn6542.rc2
- Update to 2.2.2-0.4.20180820svn6542.rc2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.2-0.3.20180309svn6528.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.2-0.2.20180309svn6528.rc2
- short dist name

* Tue Mar 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.2-0.1.20180309svn6528.rc2
- Update to 2.2.2-0.1.20180309svn6528.rc2
- Add BR: libcurl-devel

* Sun Mar 04 2018 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-8
- Rebuilt due Broken dependencies to FreeSOLID

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:2.2.1-6
- Rebuild for OpenSceneGraph-3.4.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-3
- Add %%{name}-params-conversion.patch

* Sat Apr 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-2
- Rebuilt due new qhull version

* Fri Apr 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-1
- Update to 2.2.1

* Mon Feb 29 2016 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.0-0.6.20160215svn6358.rc1
- Re-add epoch to allow update

* Wed Feb 17 2016 Martin Gansser <martinkg@fedoraproject.org> - 2.2.0-0.5.20160215svn6358.rc1
- Update to svn6358.rc1
- Fixed sed command
- Replaced $$RPM_BUILD_ROOT macro by %%{buildroot}
- Dropped speed-dreams-isnan-not-declared.patch

* Sun Jan 31 2016 Martin Gansser <martinkg@fedoraproject.org> - 2.2.0-0.4.20160131svn6353.beta1
- Update to svn6353.beta1
- Dropped t940-r6349.patch
- Added speed-dreams-isnan-not-declared.patch needed by F24
- Cleanup spec file
- Dropped %%cmake flag -DCMAKE_EXE_LINKER_FLAGS="-lexpat" no longer needed
- Dropped %%cmake flag -DSOLID_SOLID_INCLUDE_DIR:PATH="/usr/include/FreeSOLID" no longer needed

* Thu Jan 28 2016 Martin Gansser <martinkg@fedoraproject.org> - 2.2.0-0.3.20160111svn6344.beta1
- Update upstream ticket links
- Added patch t940-r6349.patch to fix #940 Race config screen corruption

* Mon Jan 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 2.2.0-0.2.20160111svn6344.beta1
- Changed %%cmake flag to -DSOLID_SOLID_INCLUDE_DIR
- Added danroid in for loop to create a link when library already exists

* Tue Jan 19 2016 Martin Gansser <martinkg@fedoraproject.org> - 2.2.0-0.1.20160111svn6344.beta1
- Update to Version 2.2.0 svn6344.beta1
- Dropped epoch
- Dropped BR SDL-devel
- Added BR SDL2-devel
- Added BR OpenSceneGraph-devel
- Added speed-dreams-arm.patch

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.0-0.24.20140627svn5799.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:2.1.0-0.23.20140627svn5799.rc2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1:2.1.0-0.22.20140627svn5799.rc2
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.0-0.21.20140627svn5799.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.1.0-0.20.20140627svn5799.rc2
- Update to svn5799.rc2
- added epoch to allow upgrade to pre-release
- added global svndate macro

* Thu Jun 26 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.1.0-19.trunk_r5796
- spec file cleanup
- rebuild for new svn version

* Wed Jun 25 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.1.0-18.trunk_r5781
- added BR libogg-devel
- added BR libvorbis-devel

* Tue Jun 24 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.1.0-17.trunk_r5781
- Update to rc1 svn5781
- added libportability.so to __requires_exclude
- remove zero length files

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-16.trunk_r4810.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.1.0-16.trunk_r4810.3
- Rebuild for enet soname change

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-15.trunk_r4810.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Bruno Wolff III <bruno@wolff.to> - 2.1.0-15.trunk_r4810.2
- Rebuild for enet soname change

* Sat Jun 15 2013 Bruno Wolff III <bruno@wolff.to> - 2.1.0-14.trunk_r4810.2
- Rebuild for enet 1.3.8 soname bump

* Sat Apr 27 2013 Bruno Wolff III <bruno@wolff.to> - 2.1.0-13.trunk_r4810.2
- Rebuild for enet 1.3.7 soname bump

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-12.trunk_r4810.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 2.1.0-12.trunk_r4810.1
- rebuild due to "jpeg8-ABI" feature drop

* Sun Dec 23 2012 Martin Gansser <martinkg@fedoraproject.org> 2.1.0-12.trunk_r4810
- rebuild against new libjpeg

* Wed Aug 22 2012 Martin Gansser <linux4martin@gmx.de> 2.1.0-11.trunk_r4810
- added requirement to the robots-base package

* Sun Aug 19 2012 Martin Gansser <linux4martin@gmx.de> 2.1.0-10.trunk_r4810
- removed %%_isa requirement on opengl-games-utils because its a noarch package

* Fri Aug 17 2012 Martin Gansser <linux4martin@gmx.de> 2.1.0-9.trunk_r4810
- added Provides to the main package
- reversed the changes to the robots-base sub-package

* Fri Aug 17 2012 Martin Gansser <linux4martin@gmx.de> 2.1.0-8.trunk_r4810
- changed isa tag requirement on the robots-base sub-package
- Add  %%_isa requirement to opengl-games-utils

* Thu Aug 16 2012 Martin Gansser <linux4martin@gmx.de> 2.1.0-7.trunk_r4810
- added BuildArch noarch to speed-dreams-robots-base 
- removed enet requirement due autorequires

* Wed Aug 15 2012 Martin Gansser <linux4martin@gmx.de> 2.1.0-6.trunk_r4810
- changed requirement to enet, libenet is wrong

* Wed Aug 15 2012 Martin Gansser <linux4martin@gmx.de> 2.1.0-5.trunk_r4810
- Add libenet build requirement (needed on x86_64).

* Wed Aug 15 2012 Martin Gansser <linux4martin@gmx.de> 2.1.0-4.trunk_r4810
- added libenet Requirement

* Tue Aug 14 2012 Martin Gansser <linux4martin@gmx.de>  2.1.0-3.trunk_r4810
- added url to userman upstream bug report #739

* Mon Aug 13 2012 Martin Gansser <linux4martin@gmx.de>  2.1.0-2.trunk_r4810
- removed extra docs folder because of file redundancy
- leave comment, why removed docs folder

* Thu Jul 26 2012 Alec Leamas <leamas@nowhere.net>  2.1.0-1.trunk_r4810
- Conditionalize spec on post-release or ordinary.
- Updating to latest git.
- Handle build system bugs (#728,#729,#731).
- Fix 'identical binaries copied, not linked' in drivers(#730).
- Simplified file list, use temporary docs dir, claim all dirs.
- Sorted deps.
- Fix Release: field.
- Fix non-working handling of spurious-executable-perm (#605)
- Added rpath for internal libraries.
- Filter out internal libs in requires/provides.
- Removed unneeded install fixes and macros.

* Thu Jun 14 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-1%{?dist}
- finale release 2.0.0
- rebuild for Fedora 17

* Sat Mar 3 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1_r4420.20%{?dist}
- fix bug with libsolid use CMAKE_SKIP_RPATH build option
- remove wrapper script

* Sun Feb 26 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1_r4420.19%{?dist}
- more SPEC file cleanups

* Fri Feb 24 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1_r4420.18%{?dist}
- build wrapper script for non-standard lib location

* Thu Feb 09 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1_r4420.17%{?dist}
- remove bindir.patch and use cmake option
- remove macro real_ver
- fix license type
- remove dopple libdir entry in file section

* Wed Feb 08 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1_r4420.16%{?dist}
- fix in prep section wrong-file-end-of-line-encoding
- new URLs for source packages
- delete macro pkg_name

* Tue Feb 07 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1_r4420.15%{?dist}
- fix incoherent-version-in-changelog
- fix file-not-utf8
- fix description-line-too-long
- fix non-conffile-in-etc

* Mon Feb 06 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1-r4420-14
- removed gobal macro debug_package

* Wed Feb 01 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1-r4420-13
- add correct license type

* Sun Jan 29 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1-r4420-12
- rpm macro cleanup

* Thu Jan 26 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1-r4420-11
- add bindir patch

* Wed Jan 25 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1-r4420-10
- more SPEC file cleanups

* Tue Jan 24 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1-r4420-9
- more SPEC file cleanups
- removing files from /usr/share/pixmap

* Mon Jan 23 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1-r4420-8
- more SPEC file cleanups

* Sat Jan 21 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1-r4420-7
- SPEC file optimization

* Fri Jan 20 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1-r4420-6
- add library path to ld.so.conf.d/speed-dreams-2.conf

* Mon Jan 16 2012 Martin Gansser <linux4martin@gmx.de> 2.0.0-0.1.rc1-r4420-5
- new release

* Mon Oct 31 2011 Martin Gansser <linux4martin@gmx.de> 2.0.0-b1-r3937-4
- add CMAKE options DOPTION_DEBUG and SKIP_RPATH

* Sun Oct 16 2011 Mario Blättermann <mariobl@fedoraproject.org> 2.0.0-b1-r3937-3
- Removed unneeded definitions of BuildRoot, clean section
- Corrected URL
- Moved the *.desktop file to a real file as second source
- Removed unneeded BuildRequires

* Fri Oct 14 2011 Martin Gansser <linux4martin@gmx.de> 2.0.0-b1-r3937-2
- copy libsolid.so to SD lib dir

* Tue Oct 4 2011 Martin Gansser <linux4martin@gmx.de> 2.0.0-b1-r3937-1
- new version for Fedora 15

* Thu Jun 24 2010 Martin Gansser <linux4martin@gmx.de> 1.4.0-r2307-2
- initial version for Fedora 13
