Name:		meshlab
Summary:	A system for processing and editing unstructured 3D triangular meshes
Version:	2022.02
Release:	5%{?dist}
URL:		https://github.com/cnr-isti-vclab/meshlab
# Bundled e57 is Boost-licensed
License:	GPLv2+ and BSD and Public Domain and ASL 2.0 and Boost
Source0:	https://github.com/cnr-isti-vclab/meshlab/archive/MeshLab-%{version}/%{name}-%{version}.tar.gz
# Matches 2022.02:
%global vcglibver e4950d1
# Probably belongs in its own package, but nothing else seems to depend on it.
Source2:	https://github.com/cnr-isti-vclab/vcglib/archive/%{vcglibver}/vcglib-%{vcglibver}.tar.gz
# Notes for Fedora users (around issues with Wayland)
Source3:	README.Fedora
Provides:	bundled(vcglib) = %{vcglibver}

# Properly install u3d IDTFConverter library
# Patch0:         meshlab-2020.07-u3d-install-fix.patch
# Adjust MESHLAB_LIB_INSTALL_DIR to not have a meshlab/ subdir
# and adjust MESHLAB_PLUGIN_INSTALL_DIR to have it
Patch1:         meshlab-2021.07-MESHLAB_LIB_INSTALL_DIR-fix.patch
# Enable use of system levmar
Patch2:         meshlab-2021.07-system-levmar.patch
# Fix FTBFS with GCC 13+ by adding include <cstdint>
# Upstream already added that in https://github.com/asmaloney/libE57Format/pull/176
Patch3:         meshlab-2022.02-e57-gcc13.patch

# Bundled things
# This is a fork of a fork. Fun.
Provides:	bundled(u3d) = 1.4.5-meshlab
Provides:	bundled(e57) = 2.3.0

BuildRequires:	bzip2-devel
BuildRequires:	eigen3-devel
BuildRequires:	glew-devel
BuildRequires:  gmp-devel
BuildRequires:	levmar-devel
BuildRequires:	lib3ds-devel
BuildRequires:	muParser-devel
BuildRequires:	qhull-devel
BuildRequires:	qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtxmlpatterns-devel qt5-qtscript-devel
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
BuildRequires:	xerces-c-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:	%{ix86}
%endif

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

%description
MeshLab is an open source, portable, and extensible system for the
processing and editing of unstructured 3D triangular meshes.  The
system is aimed to help the processing of the typical not-so-small
unstructured models arising in 3D scanning, providing a set of tools
for editing, cleaning, healing, inspecting, rendering and converting
these kinds of meshes.

%prep
%setup -q -n meshlab-MeshLab-%{version} -a 2
# %%patch0 -p1 -b .installfix
%patch1 -p1 -b .libdirfix
%patch2 -p1 -b .system-levmar
%patch3 -p1 -b .e57-gcc13
cp %{SOURCE3} .
rmdir src/vcglib && mv vcglib-%{vcglibver}* src/vcglib

# remove some bundles
%if 0
rm -rf src/external/glew*
rm -rf src/external/qhull*
rm -rf src/external/levmar*
rm -rf src/external/lib3ds*
rm -rf src/external/muparser*
%endif

# plugin path
sed -i -e 's|"lib"|"%{_lib}"|g' src/common/globals.cpp
# sed -i -e 's|"lib"|"%{_lib}"|g' src/meshlab/plugindialog.cpp

# icon path, see https://github.com/cnr-isti-vclab/meshlab/pull/752
# sed -i -e 's|/icons/pixmaps|/pixmaps|g' src/CMakeLists.txt

%build
export CXXFLAGS=`echo %{optflags} -std=c++14 -fopenmp -DSYSTEM_QHULL -I/usr/include/libqhull`

%global _vpath_srcdir src
%cmake \
	-DCMAKE_SKIP_RPATH=ON \
	-DCMAKE_VERBOSE_MAKEFILE=OFF \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DALLOW_BUNDLED_EIGEN=OFF \
	-DALLOW_BUNDLED_GLEW=OFF \
	-DALLOW_BUNDLED_LEVMAR=ON \
	-DALLOW_BUNDLED_LIB3DS=OFF \
	-DALLOW_BUNDLED_MUPARSER=OFF \
	-DALLOW_BUNDLED_NEWUOA=ON \
	-DALLOW_BUNDLED_OPENCTM=ON \
	-DALLOW_BUNDLED_QHULL=OFF \
	-DALLOW_BUNDLED_SSYNTH=ON \
	-DALLOW_BUNDLED_XERCES=OFF \
	-DALLOW_SYSTEM_EIGEN=ON \
	-DALLOW_SYSTEM_GLEW=ON \
	-DALLOW_SYSTEM_GMP=ON \
	-DALLOW_SYSTEM_LIB3DS=ON \
	-DALLOW_SYSTEM_MUPARSER=ON \
	-DALLOW_SYSTEM_OPENCTM=ON \
	-DALLOW_SYSTEM_QHULL=ON \
	-DALLOW_SYSTEM_XERCES=ON \
	-DEigen3_DIR=usr/include/eigen3 \
	-DGlew_DIR=/usr/include/GL \
	-DQhull_DIR=/usr/include/libqhull

%cmake_build

# create desktop file
cat <<EOF >meshlab.desktop
[Desktop Entry]
Name=meshlab
GenericName=MeshLab 3D triangular mesh processing and editing
Exec=env QT_QPA_PLATFORM=xcb meshlab
Icon=meshlab
Terminal=false
Type=Application
Categories=Graphics;
EOF

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -a meshlab.png %{buildroot}%{_datadir}/pixmaps/

# add desktop link
install -d -m 755 %{buildroot}%{_datadir}/applications
install -p -m 644 meshlab.desktop %{buildroot}%{_datadir}/applications
desktop-file-validate %{buildroot}%{_datadir}/applications/meshlab.desktop

%files
%doc README.md README.Fedora
%doc docs/readme.txt
%doc docs/privacy.txt
%license LICENSE.txt
%license src/external/u3d/COPYING
%{_bindir}/meshlab
# unsupported in 2021
# %%{_bindir}/meshlabserver
%{_libdir}/*.so*
%{_libdir}/meshlab/
%{_datadir}/meshlab/
%{_datadir}/applications/meshlab.desktop
%{_datadir}/icons/hicolor/512x512/apps/meshlab.png
%{_datadir}/pixmaps/meshlab.png
%license distrib/shaders/3Dlabs-license.txt
%license distrib/shaders/LightworkDesign-license.txt
# %%license unsupported/plugins_experimental/filter_segmentation/license.txt
# %%license unsupported/plugins_unsupported/filter_poisson/license.txt

%changelog
* Mon Dec 18 2023 Miro Hrončok <mhroncok@redhat.com> - 2022.02-5
- Drop a redundant BuildRequires: qtsoap5-devel

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Miro Hrončok <mhroncok@redhat.com> - 2022.02-3
- Fix build failure with GCC 13
- Declare bundled e57 library by providing bundled(e57) and adding Boost to the list of licenses
- Fixes: rhbz#2162550

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  9 2023 Tom Callaway <spot@fedoraproject.org> - 2022.02-1
- update to 2022.02

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 2021.07-4
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2021.07-2
- Drop obsolete BuildRequires on mpir-devel

* Mon Sep 20 2021 Tom Callaway <spot@fedoraproject.org> - 2021.07-1
- update to 2021.07

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2020.07-5
- BR MPIR even on ppc64le, as a generic build without optimized assembly
  routines is now available on that platform

* Thu Jul 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.07-4
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Miro Hrončok <mhroncok@redhat.com> - 2020.07-2
- Install the icon to /usr/share/pixmaps

* Thu Jul  2 2020 Tom Callaway <spot@fedoraproject.org> - 2020.07-1
- update to 2020.07
- add README.Fedora for workaround instructions on Wayland

* Tue Jun 16 2020 Cristian Balint <cristian.balint@gmail.com> - 2020.06-1
- New upstream release 2020.06 (#1844772)

* Tue Feb 18 2020 Tom Callaway <spot@fedoraproject.org> - 2016.12-12
- rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 2016.12-8
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Miro Hrončok <mhroncok@redhat.com> - 2016.12-6
- Fix Screened Poisson Surface Reconstruction filter (RHBZ#1559137) (again)

* Thu Mar 22 2018 Miro Hrončok <mhroncok@redhat.com> - 2016.12-5
- Fix Screened Poisson Surface Reconstruction filter (RHBZ#1559137)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Tom Callaway <spot@fedoraproject.org> 2016.12-1
- update to 2016.12

* Tue Jul 18 2017 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-13
- Fix FTBFS (RHBZ#1423936, RHBZ#1439673), exclude ppc64 arches

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-11
- Rebuild for glew 2.0.0

* Fri Apr 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.2-10
- Compile with -std=gnu++98 to work around c++14 incompatibilities
  (F24FTBFS, RHBZ#1305224).
- Rebuild for qhull-2015.2-1.

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-9
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1.3.2-8
- Rebuild for glew 1.13

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 1.3.2-3
- rebuilt for GLEW 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 28 2013 Eric Smith <eric@brouhaha.com> - 1.3.2-1
- Update to upstream 1.3.2.
- Updated Patch0.
- Patch7 (argcref) no longer needed, fixed upstream.
- Patch8 (gcc47) no longer needed, mostly fixed upstream.
- Patch9 added, see Debian bug 667276, previously handled in patch8, but
  unclear whether it was correct.
- Patch10 by Miro Hrončok added to fix another incompatibility with GCC 4.7.
- Patch11 by Jon Ciesla to fix include paths to prevent debugedit complaints.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 1.3.1-8
- Rebuild for glew 1.9.0

* Wed Aug 01 2012 Adam Jackson <ajax@redhat.com> - 1.3.1-7
- -Rebuild for new glew

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Eric Smith <eric@brouhaha.com> - 1.3.1-5
- Add new patch to resolve incompatibility with GCC 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 31 2011 Eric Smith <eric@brouhaha.com> - 1.3.1-2
- Add new patch to avoid crash due to mishandling of argc

* Fri Oct 21 2011 Orion Poplawski <orion@cora.nwra.com> - 1.3.1-1
- Update to 1.3.1
- Rebase patches
- Add new patches to add needed includes and disable openctm support until
  openctm is packaged

* Wed Oct 05 2011 Eric Smith <eric@brouhaha.com> - 1.3.0a-2
- removed bundled qtsoap, use shared library from Fedora package
- fix rpath handling for internal-only library

* Wed Aug 03 2011 Eric Smith <eric@brouhaha.com> - 1.3.0a-1
- update to latest upstream release
- added patch from Teemu Ikonen to fix FTBFS
- added patch from Teemu Ikonen to fix reading of .ply files in comma
  separator locales

* Tue Oct 05 2010 jkeating - 1.2.2-5.1
- Rebuilt for gcc bug 634757

* Fri Sep 10 2010 Eric Smith <eric@brouhaha.com> - 1.2.2-5
- Remove direct invocation of constructor to make GCC 4.5 happy

* Mon May  3 2010 Eric Smith <eric@brouhaha.com> - 1.2.2-4
- in prep, remove bundled getopt library sources, to ensure
  that we're using the system library instead
- include doc tag for poisson filter license.txt
- add BSD to license tag
- correct typo in comment in spec

* Wed Apr  7 2010 Eric Smith <eric@brouhaha.com> - 1.2.2-3
- updates based on pre-review comments by Jussi Lehtola

* Tue Apr  6 2010 Eric Smith <eric@brouhaha.com> - 1.2.2-2
- updates based on pre-review comments by Martin Gieseking

* Tue Feb  2 2010 Eric Smith <eric@brouhaha.com> - 1.2.2-1
- initial version
