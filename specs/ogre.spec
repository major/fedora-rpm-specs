%undefine __cmake_in_source_build

Name:           ogre
Version:        1.9.0
Release:        51%{?dist}
Epoch:          1
Summary:        Object-Oriented Graphics Rendering Engine
# MIT - main library
# CC-BY-SA-3.0 - devel docs
# MIT      - shaders for DeferredShadingMedia samples
# Public Domain - CMAKE file (ignored as they are not of build result)
#               - see https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/691 for list of files
# Zlib - Samples/Media/*/DualQuaternion*
#      - Tools/XMLConverter/src/tiny*
# BSL-1.0 - Many of the maths/spatial routines (OgreMain/include/OgreAny.h, OgreMain/include/OgrePlane.h ...)
# LicenseRef-Callaway-dante-treglia - OgreMain/include/OgreSingleton.h
#         - temporary id, see https://gitlab.com/fedora/legal/fedora-license-data/-/issues/595
# NCSA - OgreMain/include/OgreSmallVector.h
# BSD-3-Clause - OgreMain/include/OgreUTFString.h
# MIT-Khronos-old - RenderSystems/GL/include/GL/glew.h, RenderSystems/GL/include/GL/glxew.h, RenderSystems/GL/include/GL/wglew.h
# GPL-2.0-or-later WITH Bison-exception-1.24 - RenderSystems/GL/src/nvparse/*_parser.cpp
# SGI-B-2.0 - RenderSystems/GLES2/include/GLES2/gl2.h
# LGPL-2.1-only - Tools/Common/setup/License.rtf
# LGPL-2.1-or-later - files in Tools/BlenderExport/
# GPLv2-or-later - Tools/LightwaveConverter
# LicenseRef-Callaway-scintilla - Tools/MaterialEditor/wxscintilla_1.69.2/src/scintilla/License.txt
#             temporary id, see https://gitlab.com/fedora/legal/fedora-license-data/-/issues/597
# LGPL-2.0-or-later WITH WxWindows-exception-3.1 - Tools/MaterialEditor/wxscintilla_1.69.2/src/ScintillaWX.h
License:        MIT AND LicenseRef-Fedora-Public-Domain AND CC-BY-SA-3.0 AND Zlib AND BSL-1.0 AND LicenseRef-Callaway-dante-treglia AND NCSA AND BSD-3-Clause AND MIT-Khronos-old AND GPL-2.0-or-later WITH Bison-exception-1.24 AND SGI-B-2.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND GPLv2-or-later AND LicenseRef-Callaway-scintilla AND LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:            http://www.ogre3d.org/
# This is modified http://downloads.sourceforge.net/ogre/ogre-v%%(echo %%{version} | tr . -).tar.bz2
# with non-free files striped (see ogre-make-clean.sh):
# Update local glew copy
# - Non-free licensed headers under RenderSystems/GL/include/GL removed
# - Non-free chiropteraDM.pk3 under Samples/Media/packs removed
# - Non-free textures under Samples/Media/materials/textures/nvidia
Source0:        %{name}-%{version}-clean.tar.bz2
Patch0:         ogre-1.7.2-rpath.patch
Patch1:         ogre-1.9.0-glew.patch
Patch3:         ogre-1.7.2-fix-ppc-build.patch
Patch5:         ogre-1.9.0-build-rcapsdump.patch
Patch6:         ogre-thread.patch
Patch7:         ogre-1.9.0-dynlib-allow-no-so.patch
# FIXME: Patch is bogus on Fedora >= 24
Patch8:         ogre-1.9.0-cmake-freetype.patch
Patch9:         ogre-1.9.0-cmake_build-fix.patch
Patch10:        ogre-aarch64.patch
Patch11:        ogre-riscv64.patch
# Resolve link errors due to incorrect template creation
# https://bitbucket.org/sinbad/ogre/commits/a24ac4afbbb9dc5ff49a61634af50da11ba8fb97/
# https://bugzilla.redhat.com/show_bug.cgi?id=1223612
Patch12:        ogre-a24ac4afbbb9dc5ff49a61634af50da11ba8fb97.diff
# Remove unnecessary inclusion of <sys/sysctl.h>
# https://bugzilla.redhat.com/show_bug.cgi?id=1841324
Patch13:        ogre-1.9.0-sysctl.patch
Patch14:        %{name}-gcc11.patch
BuildRequires:  gcc-c++
BuildRequires:  zziplib-devel freetype-devel
BuildRequires:  libXaw-devel libXrandr-devel libXxf86vm-devel libGLU-devel
BuildRequires:  ois-devel freeimage-devel openexr-devel
BuildRequires:  glew-devel
BuildRequires:  boost-devel
# BuildRequires:  poco-devel
BuildRequires:  tinyxml-devel
BuildRequires:  cmake
BuildRequires:  libatomic
BuildRequires:  cppunit-devel
Provides:       bundled(wxScintilla) = 1.69.2

%description
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier and more
intuitive for developers to produce applications utilizing
hardware-accelerated 3D graphics. The class library abstracts all the
details of using the underlying system libraries like Direct3D and
OpenGL and provides an interface based on world objects and other
intuitive classes.

%package paging
Summary:        OGRE component for terrain paging
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description paging
Provides paging functionality. In essence it allows worlds to be rendered
and loaded at the same time.

%package property
Summary:        OGRE component for property introspection
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description property
OGRE's property system allows you to associate values of arbitrary type with
names, and have those values exposed via a self-describing interface.

%package rtss
Summary:        OGRE RT Shader System component
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description rtss
The Real Time Shader System, or RTSS for short, is a component of Ogre. This
component is used to generate shaders on the fly based on object material
properties, scene setup and other user definitions.

%package terrain
Summary:        OGRE component for terrain rendering
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description terrain
OGRE's terrain component provides rendering of terrain represented by
heightmaps.

%package overlay
Summary:        OGRE overlay component
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description overlay
Overlays allow you to render 2D and 3D elements on top of the normal scene
contents to create effects like heads-up displays (HUDs), menu systems,
status panels etc.

%package volume
Summary:        OGRE component for volume rendering
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description volume
This component used to render volumes. It can handle any volume data but
featurewise has a tedency towards terrains.

%package utils
Summary:        OGRE production pipeline utilities
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description utils
Contains OgreXMLConverter, it can take .mesh.xml files and convert them into
their binary variant.
Also provides OgreMeshUpgrader that can load old Ogre .mesh files and upgrade
them to the latest version.

%package devel
Summary:        Ogre header files and documentation
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-paging%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-property%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-rtss%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-terrain%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-overlay%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-volume%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:       pkgconfig
# Requires:       poco-devel
Requires:       boost-devel
Requires:       glew-devel
Requires:       cmake
Obsoletes:      %{name}-devel-doc <= %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the header files for Ogre.
Install this package if you want to develop programs that use Ogre.

%package samples
Summary:        Ogre samples executables and media
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description samples
This package contains the compiled (not the source) sample applications coming
with Ogre.  It also contains some media (meshes, textures,...) needed by these
samples. The samples are installed in %{_libdir}/Samples/*.so and can be run
using SampleBrowser.

%prep
%setup -q
mkdir build
%patch -P0 -p1 -b .rpath
%patch -P1 -p1 -b .glew
%patch -P3 -p1 -b .ppc
%patch -P5 -p1 -b .build-rcapsdump
%patch -P6 -p0 -b .thread
%patch -P7 -p1 -b .dynlib-allow-no-so
%if (0%{?fedora} > 20) && (0%{?fedora} < 24)
# freetype header chaos:
# Fedora <= 20    headers in /usr/include/freetype2/freetype
# Fedora 21,22,23 headers in /usr/include/freetype2
# Fedora >= 24    headers in /usr/include/freetype2/freetype
%patch -P8 -p1 -b .cmake-freetype
%endif
%patch -P9 -p1 -b .cmake_build-fix
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1

# remove execute bits from src-files for -debuginfo package
chmod -x `find RenderSystems/GL -type f` \
  `find Samples/DeferredShading -type f` Samples/DynTex/src/DynTex.cpp
#  Samples/Common/bin/resources.cfg
# Remove spurious execute bits from some Media files
chmod -x `find Samples/Media/DeferredShadingMedia -type f`
# Add mit.txt symlink for links in License.html
rm -r Docs/licenses/*
ln -s ../COPYING Docs/licenses/mit.txt
# remove included tinyxml headers to ensure use of system headers
rm Tools/XMLConverter/include/tiny*

%build
%cmake -DOGRE_FULL_RPATH=0 -DCMAKE_SKIP_RPATH=1 -DOGRE_LIB_DIRECTORY=%{_lib} -DOGRE_BUILD_RTSHADERSYSTEM_EXT_SHADERS=1 -DOGRE_BUILD_PLUGIN_CG=0
%cmake_build

%install
%cmake_install

# Create config for ldconfig
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/OGRE" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

# Install the samples
mkdir -p %{buildroot}%{_libdir}/OGRE/Samples
mkdir -p %{buildroot}%{_sysconfdir}/OGRE
for cfg in plugins.cfg quakemap.cfg resources.cfg samples.cfg; do
  mv %{buildroot}%{_datadir}/OGRE/$cfg %{buildroot}%{_sysconfdir}/OGRE/
done

# Swap out reference to non-free quake map that was removed
cat << EOF > %{buildroot}%{_sysconfdir}/OGRE/quakemap.cfg
Archive: /usr/share/OGRE/media/packs/ogretestmap.zip 
Map: ogretestmap.bsp
EOF

# Fixing bug with wrong case for media
mkdir -p %{buildroot}%{_datadir}/OGRE/
mv %{buildroot}%{_datadir}/OGRE/Media %{buildroot}%{_datadir}/OGRE/media
mv %{buildroot}%{_datadir}/OGRE/media/PCZAppMedia/ROOM_NY.mesh %{buildroot}%{_datadir}/OGRE/media/PCZAppMedia/room_ny.mesh
mv %{buildroot}%{_datadir}/OGRE/media/PCZAppMedia/ROOM_PY.mesh %{buildroot}%{_datadir}/OGRE/media/PCZAppMedia/room_py.mesh

rm -f %{buildroot}%{_datadir}/OGRE/docs/CMakeLists.txt

# cmake macros should be in the cmake directory, not an Ogre directory
mkdir -p %{buildroot}%{_datadir}/cmake/Modules
mv %{buildroot}%{_libdir}/OGRE/cmake/* %{buildroot}%{_datadir}/cmake/Modules

%files
%doc AUTHORS BUGS COPYING
%doc Docs/ChangeLog.html Docs/License.html Docs/licenses Docs/ReadMe.html Docs/style.css Docs/ogre-logo*.gif
%{_libdir}/libOgreMain.so.*
%{_libdir}/OGRE

%{_datadir}/OGRE
%dir %{_sysconfdir}/OGRE
%exclude %{_bindir}/SampleBrowser
%exclude %{_libdir}/OGRE/Samples
%exclude %{_libdir}/OGRE/cmake
%exclude %{_datadir}/OGRE/media
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/*

%files paging
%{_libdir}/libOgrePaging.so.*

%files property
%{_libdir}/libOgreProperty.so.*

%files rtss
%{_libdir}/libOgreRTShaderSystem.so.*

%files terrain
%{_libdir}/libOgreTerrain.so.*

%files overlay
%{_libdir}/libOgreOverlay.so.*

%files volume
%{_libdir}/libOgreVolume.so.*

%files utils
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter
%{_bindir}/rcapsdump

%files devel
%{_libdir}/lib*Ogre*.so
%{_datadir}/cmake/Modules/*
%{_includedir}/OGRE
%{_libdir}/pkgconfig/*.pc

%files samples
%{_bindir}/SampleBrowser
%{_libdir}/OGRE/Samples
%{_datadir}/OGRE/media
%{_sysconfdir}/OGRE/plugins.cfg
%{_sysconfdir}/OGRE/quakemap.cfg
%{_sysconfdir}/OGRE/resources.cfg
%{_sysconfdir}/OGRE/samples.cfg


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1:1.9.0-49
- Rebuilt for openexr 3.2.4

* Mon Feb 26 2024 Songsong Zhang <U2FsdGVkX1@gmail.com> - 1:1.9.0-48
- Add riscv64 support

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1:1.9.0-46
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1:1.9.0-44
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1:1.9.0-41
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1:1.9.0-39
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1:1.9.0-37
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1:1.9.0-35
- Rebuilt for Boost 1.75

* Fri Dec 04 2020 Jeff Law <law@redhat.com> - 1:1.9.0-34
- Make comparison object invocable as const for gcc-11

* Sat Dec 05 2020 Sérgio Basto <sergio@serjux.com> - 1:1.9.0-33
- Fix epoch

* Fri Dec 04 2020 Sérgio Basto <sergio@serjux.com> - 1:1.9.0-32
- Fix cmake build

* Mon Nov 23 2020 Sérgio Basto <sergio@serjux.com> - 1.12.9-1
- Update to 1.12.9

* Sun Nov 22 2020 Sérgio Basto <sergio@serjux.com> - 1.12.6-1
- Update to 1.12.6
- Fix cmake build
- Use upstream source and simply remove the GL headers in %prep.
- Add Bitwise.patch for build on s390x

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-31
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-29
- Rebuilt for Boost 1.73
- Patched for glibc 2.32 (#1841324)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-25
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-22
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-19
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-18
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-16
- Rebuilt for Boost 1.63

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.9.0-14
- Do not apply ogre-1.9.0-cmake-freetype.patch on fedora >= 24 (Fix FTBS).

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-13
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.9.0-11
- rebuild for Boost 1.58

* Tue Jul 07 2015 Bruno Wolff III <bruno@wolff.to> = 1.9.0-10
- ogre-devel requires glew-devel for headers

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Orion Poplawski <orion@cora.nra.com> - 1.9.0-8
- Add patch to resolve link errors due to incorrect template creation (fix FTBFS bug #1223612)

* Mon May 04 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.9.0-8
- Indicate that this package bundles wxScintilla 1.69.2.

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 1.9.0-7
- Rebuilt for GCC 5 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.9.0-6
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.9.0-4
- fixed AArch64 identification macro

* Sun Jun 08 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.9.0-3
- properly obsolete ogre-devel-doc

* Sun Jun 08 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.9.0-2
- obsolete ogre-devel-doc
- fix requiring base package

* Sat Jun 07 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.9.0-1
- 1.9.0 upstream release (RHBZ #1104309)
- cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.8.1-11
- Rebuild for boost 1.55.0
- Fix detection of libfreetype (ogre-1.8.1-cmake-freetype.patch)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 1.8.1-9
- Update ogre-thread.patch to exclude -mt suffix from Boost.Thread and
  Boost.System DSO's.

* Sat Jul 27 2013 Petr Machata <pmachata@redhat.com> - 1.8.1-8
- Rebuild for boost 1.54.0

* Sat Apr 20 2013 Bruno Wolff III <bruno@wolff.to> - 1.8.1-7
- cmake scripts need to be at the top level
- Fix MODULES/Modules oops

* Sat Apr 20 2013 Bruno Wolff III <bruno@wolff.to> - 1.8.1-6
- Avoid opening plugins twice

* Sat Apr 20 2013 Bruno Wolff III <bruno@wolff.to> - 1.8.1-5
- Allow for plugin names to not end in .so - bz 573672
- Put cmake files in cmake directory instead of an Ogre directory

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.8.1-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.8.1-3
- Rebuild for Boost-1.53.0

* Sun Dec 09 2012 Bruno Wolff III <bruno@wolff.to> - 1.8.1-2
- Consuming packages using threads need to link to boost_system-mt

* Fri Nov 30 2012 Martin Preisler <mpreisle@redhat.com> - 1.8.1-1
- Update to upstream 1.8.1

* Fri Nov 30 2012 Martin Preisler <mpreisle@redhat.com> - 1.8.0-1
- Update to upstream 1.8.0
- Split the components into a subpackages
- Split utils into a subpackage
- Put cmake modules into the -devel subpackage

* Tue Oct 02 2012 Jon Ciesla <limburgher@gmail.com> - 1.7.4-5
- Fix FTBFS on ARM, based on debian's patch.

* Fri Aug 10 2012 Bruno Wolff III <bruno@wolff.to> - 1.7.4-4
- Fix for boost 1.50

* Sat Jul 21 2012 Bruno Wolff III <bruno@wolff.to> - 1.7.4-3
- Fix issue with utilSSE hack breaking under gcc 4.7 (bug 842041)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 01 2012 Bruno Wolff III <bruno@wolff.to> - 1.7.4-1
- Update to upstream 1.7.4
- This is a minor bugfix update from 1.7.3

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-6
- Rebuilt for c++ ABI breakage

* Tue Jan 17 2012 Bruno Wolff III <bruno@wolff.to> - 1.7.3-5
- Rebuild for ois 1.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.3-3
- Rebuild for boost soname bump

* Fri Jul 22 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.3-2
- Rebuild for boost 1.47

* Sat May 14 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.3-1
- Upstream update to 1.7.3
- Changelog at http://www.ogre3d.org/2011/05/08/ogre-1-7-3-cthugha-released#more-1284

* Mon Apr 04 2011 Jon Ciesla <limb@jcomserv.net> - 1.7.2-14
- Re-rebuilding for boost 1.46.1, 2011-03-15 rebuild got 1.46.0.

* Tue Mar 15 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-13
- Rebuild for boost 1.46.1 update

* Sun Mar 06 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-12
- Fix broken pkgconfig files

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-10
- With ogre 1.7, cegui is no longer a build dependency.

* Sun Feb 06 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-9
- Rebuild for boost soname bump.

* Tue Jan 11 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-8
- Fix config for replacement for quake map.

* Mon Jan 10 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-7
- Exclude CMakeLists.txt from Media
- Install Samples media where Ogre expects it.
- Ogre expects the *.cfg files in /etc/OGRE

* Fri Jan 07 2011 Tom Callaway <spot@fedoraproject.org> - 1.7.2-6
- BuildRequires: boost-devel for threading, Remove poco-devel from BR

* Wed Jan 05 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-5
- Drop ttb requirement entirely.

* Wed Jan 05 2011 Dan Horák <dan[at]danny.cz> - 1.7.2-4
- tbb is available only on selected architectures

* Wed Jan 05 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-3
- Use SampleBrowser instead of out of date ogre-samples script

* Mon Jan 03 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-2
- ogre-devel requires poco-devel to make sure references to poco headers works.

* Tue Dec 21 2010 Tom Callaway <spot@fedoraproject.org> - 1.7.2-1
- move to 1.7.2

* Sat Nov 28 2009 Bruno Wolff III <bruno@wolff.to> - 1.6.4-5
- Get upstream fixes since 1.6.4 release. This includes a couple of crash bugs.

* Mon Nov 23 2009 Bruno Wolff III <bruno@wolff.to> - 1.6.4-4
- Allow CEGIUOgreRenderer to find needed libraries

* Sat Nov 21 2009 Bruno Wolff III <bruno@wolff.to> - 1.6.4-3
- Spec file cleanups

* Tue Nov 17 2009 Bruno Wolff III <bruno@wolff.to> - 1.6.4-2
- Rebuild for ois 1.2

* Mon Sep 28 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.6.4-1
- New upstream release 1.6.4

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 16 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.6.2-1
- New upstream release 1.6.2
- Exceptions added to License
- Reenabling OpenEXR plugin, as it fixed now

* Fri Mar 06 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.6.1-5
- Add licenses of samples to License tag

* Mon Mar 02 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.6.1-4
- Update Ogre-Samples to work properly without CgProgramManager plugin

* Fri Feb 27 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.6.1-3
- Fixing PPC build

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Alexey Torkhov <atorkhov@gmail.com> 1.6.1-1
- New upstream release 1.6.1

* Tue Jan 20 2009 Hans de Goede <hdegoede@redhat.com> 1.6.0-5
- Adjust font requires for font rename (rh 480465)

* Sat Jan 10 2009 Hans de Goede <hdegoede@redhat.com> 1.6.0-4
- use regular (full) instead of lgc dejavu fonts for the demos (rh 477434)

* Sat Dec 27 2008 Hans de Goede <hdegoede@redhat.com> 1.6.0-3
- Remove non-free fonts from samples subpackage (rh 477434)

* Wed Dec  3 2008 Hans de Goede <hdegoede@redhat.com> 1.6.0-2
- Rebuild for new cegui

* Thu Nov 06 2008 Alexey Torkhov <atorkhov@gmail.com> 1.6.0-1
- New upstream release 1.6.0
- Updated samples running script
- Removed non-free quake map from samples media
- Added docs license in License tag

* Sun Sep 21 2008 Alexey Torkhov <atorkhov@gmail.com> 1.6.0-0.1.rc1
- New upstream release 1.6.0rc1
- Disabling broken OpenEXR plugin, it is not updated for long time and doesn't
  compile. FreeImage now have EXR support
- Updated private GLEW sources to 1.5.0 due to license issues and compiling
  against it instead of system ones, as it is patched by upstream

* Fri Jul 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.9-2
- Rebuild for new cegui

* Wed Jul  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.9-1
- New upstream release 1.4.9

* Thu May 22 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.8-2
- Rebuild for new cegui
- Use system tinyxml (bz 447698)

* Tue May 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.8-1
- New upstream release 1.4.8
- Warning as always with a new upstream ogre release this breaks the ABI
  and changes the soname!

* Sun Mar 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.7-2
- Switch to freeimage as imagelibrary, as upstream is abandoning DevIL support
  (bz 435399)
- Enable the openexr plugin

* Sun Mar 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.7-1
- New upstream release 1.4.7
- Warning as always with a new upstream ogre release this breaks the ABI
  and changes the soname!

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.6-5
- Autorebuild for GCC 4.3

* Thu Jan 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-4
- Install 2 additional header files for ogre4j (bz 429965)

* Tue Jan 22 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-3
- Rebuild for new glew

* Sat Jan 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-2
- Oops I just found out that ogre contains private copies of GL and GLEW
  headers, which fall under the not 100% SGI Free Software B and GLX Public
  License licenses, remove these (even from the tarbal!) and use the system
  versions instead

* Sat Dec 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-1
- New upstream release 1.4.6
- Warning as always with a new upstream ogre release this breaks the ABI
  and changes the soname!

* Wed Nov 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.5-3
- Fix building of ogre with an older version of ogre-devel installed
  (bz 382311)

* Mon Nov 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.5-2
- Ogre-Samples now takes the name of which samples to run as arguments, if no
  arguments are provided, it will run all of them like it used too (bz 377011)
- Don't install a useless / broken plugins.cfg in the Samples folder,
  Ogre-Samples will generate a correct one when run (bz 377011)

* Mon Oct  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.5-1
- New upstream release 1.4.5

* Fri Sep 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.4-1
- New upstream release 1.4.4 (bz 291481)

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.2-2
- Update License tag for new Licensing Guidelines compliance

* Sat Jun 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.2-1
- New upstream release 1.4.2
- Warning as always with a new upstream ogre release this breaks the ABI
  and changes the soname!
- Warning this release also breaks the API!

* Thu May 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.5-2
- Fix building on ppc64

* Fri Feb 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.5-1
- New upstream release 1.2.5

* Fri Jan 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.3-2
- Rebuild for new cairomm
- Added a samples sub-package (suggested by Xavier Decoret)

* Fri Oct 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.3-1
- New upstream release 1.2.3
- Warning as always with a new upstream ogre release this breaks the ABI
  and changes the soname!

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.2-2.p1
- FE6 Rebuild

* Thu Jul 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.2-1.p1
- New upstream release 1.2.2p1
- Drop integrated char_height patch
- Drop ogre-1.2.1-visibility.patch since this is fixed with the latest gcc
  release, but keep it in CVS in case things break again.
- Add a patch that replaces -version-info libtool argument with -release,
  which results in hardcoding the version number into the soname. This is
  needed because upstream changes the ABI every release, without changing the
  CURRENT argument passed to -version-info .
- Also add -release when linking libCEGUIOgreRenderer.so as that was previously
  unversioned.

* Tue Jul 18 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.1-3
- Add ogre-1.2.1-visibility.patch to fix issues with the interesting new
  gcc visibility inheritance.

* Fri Jul  7 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.1-2
- Make -devel package Requires on the main package fully versioned.
- Move libOgrePlatform.so out of %%{_libdir} and into the OGRE plugins dirs as
  its not versioned and only used through dlopen, so its effectivly a plugin.  

* Thu Jun 15 2006 Hans de Goede 1.2.1-1
- Initial FE packaging attempt, loosely based on a specfile created by
  Xavier Decoret <Xavier.Decoret@imag.fr>
