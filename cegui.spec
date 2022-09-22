Name:           cegui
Version:        0.8.7
Release:        25%{?dist}
Summary:        Free library providing windowing and widgets for graphics APIs / engines
License:        MIT
URL:            http://www.cegui.org.uk
Source0:        http://downloads.sourceforge.net/crayzedsgui/cegui-%{version}.tar.bz2
Patch0:         cegui-0.8.4-lua53.patch

BuildRequires:  gcc-c++
BuildRequires:  DevIL-devel
BuildRequires:  freeimage-devel
BuildRequires:  expat-devel
BuildRequires:  freetype-devel > 2.0.0
BuildRequires:  libxml2-devel
BuildRequires:  libICE-devel
BuildRequires:  glm-devel
BuildRequires:  libGLU-devel
BuildRequires:  libtool
BuildRequires:  libSM-devel
BuildRequires:  lua-devel >= 0.5.2
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  SILLY-devel
BuildRequires:  tolua++-devel >= 1.0.93-14
BuildRequires:  tinyxml-devel
BuildRequires:  glew-devel
BuildRequires:  ogre-devel >= 1.7.0
BuildRequires:  ois-devel
BuildRequires:  irrlicht-devel >= 1.8
# We no longer build a python subpackage as the python bindings are
# broken when building with gcc6 / boost-1.60 and no-one uses them
Obsoletes:      %{name}-python < %{version}-%{release}
# Idem for the xerces-xmlparser (broken with recent xerces versions)
Obsoletes:      %{name}-xerces-xmlparser < %{version}-%{release}
# We no longer build the samples and devel-doc subpackages, because CEGUI is no
# longer maintained upstream and thus should not be used for new projects
Obsoletes:      %{name}-samples < %{version}-%{release}
Obsoletes:      %{name}-devel-doc < %{version}-%{release}

%description
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines where such functionality is not natively available, or
severely lacking. The library is object orientated, written in C++, and
targeted at games developers who should be spending their time creating great
games, not building GUI sub-systems!


%package devel
Summary:        Development files for cegui
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-DevIL-imagecodec = %{version}-%{release}
Requires:       %{name}-freeimage-imagecodec = %{version}-%{release}
Requires:       %{name}-irrlicht-renderer = %{version}-%{release}
Requires:       %{name}-ogre-renderer = %{version}-%{release}
Requires:       %{name}-null-renderer = %{version}-%{release}
Requires:       %{name}-libxml-xmlparser = %{version}-%{release}
Requires:       %{name}-tinyxml-xmlparser = %{version}-%{release}
Requires:       libGLU-devel

%description devel
Development files for cegui


%package DevIL-imagecodec
Summary:        Alternative imagecodec library for CEGUI using DevIL
Requires:       cegui = %{version}-%{release}

%description DevIL-imagecodec
Alternative imagecodec library for CEGUI using DevIL.


%package freeimage-imagecodec
Summary:        Alternative imagecodec library for CEGUI using freeimage
Requires:       cegui = %{version}-%{release}

%description freeimage-imagecodec
Alternative imagecodec library for CEGUI using freeimage.


%package irrlicht-renderer
Summary:        Irrlicht renderer for CEGUI
Requires:       cegui = %{version}-%{release}

%description irrlicht-renderer
Irrlicht renderer for CEGUI.


%package ogre-renderer
Summary:        OGRE renderer for CEGUI
Requires:       cegui = %{version}-%{release}

%description ogre-renderer
OGRE renderer for CEGUI.


%package null-renderer
Summary:        Null renderer for CEGUI
Requires:       cegui = %{version}-%{release}

%description null-renderer
Null renderer for CEGUI. Useful for headless deployments or unit testing.


%package libxml-xmlparser
Summary:        Alternative xml parsing library for CEGUI using libxml
Requires:       cegui = %{version}-%{release}

%description libxml-xmlparser
Alternative xml parsing library for CEGUI using libxml.


%package tinyxml-xmlparser
Summary:        Alternative xml parsing library for CEGUI using tinyxml
Requires:       cegui = %{version}-%{release}

%description tinyxml-xmlparser
Alternative xml parsing library for CEGUI using tinyxml.


%prep
%setup -q
%patch0 -p1
find -name "*.orig" -exec rm -f {} ';'


%build
%cmake \
-D CMAKE_INSTALL_DOCDIR=%{_pkgdocdir} \
-D CEGUI_BUILD_IMAGECODEC_SDL2=false \
-D CEGUI_BUILD_IMAGECODEC_STB=false \
-D CEGUI_BUILD_IMAGECODEC_TGA=false \
-D CEGUI_BUILD_PYTHON_MODULES=false \
-D CEGUI_BUILD_RENDERER_DIRECTFB=false \
-D CEGUI_BUILD_XMLPARSER_XERCES=false \
-D CEGUI_OPTION_DEFAULT_XMLPARSER=ExpatParser \
-D CEGUI_OPTION_DEFAULT_IMAGECODEC=SILLYImageCodec \
-D CEGUI_BUILD_RENDERER_NULL=true \
-D CEGUI_BUILD_TESTS=false \
-D CEGUI_SAMPLES_ENABLED=false

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%ldconfig_scriptlets irrlicht-renderer

%ldconfig_scriptlets ogre-renderer

%ldconfig_scriptlets null-renderer


%files
%doc README.md
%license COPYING
%{_libdir}/libCEGUIBase-0.so.*
%{_libdir}/libCEGUICommonDialogs-0.so.*
%{_libdir}/libCEGUILuaScriptModule-0.so.*
%{_libdir}/libCEGUIOpenGLRenderer-0.so.*
%{_libdir}/cegui-0.8/libCEGUICoreWindowRendererSet.so
# this is the default parser, that's why it's not split off into a subpackage
%{_libdir}/cegui-0.8/libCEGUIExpatParser.so
# same with silly image codec
%{_libdir}/cegui-0.8/libCEGUISILLYImageCodec.so

%files devel
%{_bindir}/toluappcegui-0.8
%{_libdir}/libCEGUI*-0.so
%{_libdir}/pkgconfig/CEGUI-0.pc
%{_libdir}/pkgconfig/CEGUI-0-OPENGL.pc
%{_libdir}/pkgconfig/CEGUI-0-OPENGL3.pc
%{_libdir}/pkgconfig/CEGUI-0-OGRE.pc
%{_libdir}/pkgconfig/CEGUI-0-NULL.pc
%{_libdir}/pkgconfig/CEGUI-0-LUA.pc
%{_libdir}/pkgconfig/CEGUI-0-IRRLICHT.pc
%{_includedir}/cegui-0
%{_datadir}/cegui-0

%files irrlicht-renderer
%{_libdir}/libCEGUIIrrlichtRenderer-0.so.*

%files ogre-renderer
%{_libdir}/libCEGUIOgreRenderer-0.so.*

%files null-renderer
%{_libdir}/libCEGUINullRenderer-0.so.*

%files DevIL-imagecodec
%{_libdir}/cegui-0.8/libCEGUIDevILImageCodec.so

%files freeimage-imagecodec
%{_libdir}/cegui-0.8/libCEGUIFreeImageImageCodec.so

%files libxml-xmlparser
%{_libdir}/cegui-0.8/libCEGUILibXMLParser.so

%files tinyxml-xmlparser
%{_libdir}/cegui-0.8/libCEGUITinyXMLParser.so

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.8.7-24
- Rebuild for glew 2.2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 14 2020 Hans de Goede <hdegoede@redhat.com> - 0.8.7-18
- Obsolete the dropped -devel-doc and -samples sub-packages (rhbz#1810754)

* Fri Feb 21 2020 Hans de Goede <hdegoede@redhat.com> - 0.8.7-17
- CEGUI is no longer maintained upstream and should not be used for new
  projects, drop the -devel-doc and -samples sub-packages
- Fix FTBFS (rhbz#1799217)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 0.8.7-13
- Rebuilt for Boost 1.69

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.8.7-12
- Rebuilt for glew 2.1.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Hans de Goede <hdegoede@redhat.com> - 0.8.7-10
- Fix FTBFS by disabling the xerces-xmlparser, it is broken with the latest
  xerces-c version and no-one uses it

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.8.7-8
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.8.7-5
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 0.8.7-3
- Rebuilt for Boost 1.63

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.8.7-2
- Rebuild for glew 2.0.0

* Thu Apr 28 2016 Martin Preisler <mpreisle@redhat.com> - 0.8.7-1
- Updated to new upstream release
- soname was accidentaly changed in CEGUI 0.8.6, 0.8.7 fixes that

* Mon Apr 25 2016 Bruno Wolff III <bruno@wolff.to> - 0.8.6-1
- New upstream with important bugfix new to 0.8.5
- A few other minor changes

* Mon Mar 14 2016 Martin Preisler <mpreisle@redhat.com> - 0.8.5-1
- Updated to new upstream release
- Commented out the check section, I have some path related issues with it

* Wed Feb 03 2016 Hans de Goede <hdegoede@redhat.com> - 0.8.4-17
- Fix a bunch of rpmlint issues
- Make devel-doc sub-pkg noarch

* Tue Feb 02 2016 Hans de Goede <hdegoede@redhat.com> - 0.8.4-16
- Fix FTBFS by disabling the python bindings, they are broken when building
  with gcc6 / boost-1.60 and no-one uses them
- Link against liblua-5.3.so instead of liblua-5.2.so

* Mon Feb 01 2016 Tim Niemueller <tim@niemueller.de> - 0.8.4-15
- rebuild for updated tolua++

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.8.4-14
- Rebuild for glew 1.13

* Wed Sep 02 2015 Jonathan Wakely <jwakely@redhat.com> 0.8.4-13
- Rebuilt for Boost 1.59 (again).

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.8.4-12
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.8.4-10
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Bruno Wolff III <bruno@wolff.to> 0.8.4-8
- Make sure FTBFS issue is fixed

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.8.4-7
- Rebuild for boost 1.57.0

* Wed Dec 17 2014 Hans de Goede <hdegoede@redhat.com> - 0.8.4-6
- Rebuilt against new lua-5.2 based tolua++

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Martin Preisler <mpreisle@redhat.com> - 0.8.4-4
- Build null renderer and run tests in the check phase

* Tue Jul 08 2014 Martin Preisler <mpreisle@redhat.com> - 0.8.4-3
- Added a patch that makes the samples build even when glfw is not available
- Added the OIS dependency for Ogre samples

* Mon Jul 07 2014 Martin Preisler <mpreisle@redhat.com> - 0.8.4-2
- Fixed doc file locations for COPYING and README.md

* Mon Jul 07 2014 Martin Preisler <mpreisle@redhat.com> - 0.8.4-1
- Updated to new upstream release

* Tue Jun 10 2014 Hans de Goede <hdegoede@redhat.com> - 0.8.3-4
- Fix wrong include path in CEGUI-0.pc

* Sun Jun 08 2014 Hans de Goede <hdegoede@redhat.com> - 0.8.3-3
- Rebuild for ogre 1.9.0
- Fix cegui building without freetype support
- Cegui uses tolua++ which only works with 5.1, not 5.2, switch to compat-lua
- Drop the bogus cegui-*-renderer from cegui-samples (the main cegui package
  which -samples requires provides the standard opengl renderer)

* Fri Jun 06 2014 Martin Preisler <mpreisle@redhat.com> - 0.8.3-2
- Added glm-devel to BuildRequires
- Upstream patch regarding PyCEGUI install location
- Upstream cmake patch to avoid build issues with newer cmake
- Spec cleanup

* Tue Jun 03 2014 Martin Preisler <mpreisle@redhat.com> - 0.8.3-1
- Updated to new upstream release

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.7.9-8
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.7.9-7
- rebuild for boost 1.55.0

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.7.9-6
- rebuilt for GLEW 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 0.7.9-4
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.7.9-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.7.9-2
- Rebuild for Boost-1.53.0

* Tue Jan 22 2013 Martin Preisler <mpreisle@redhat.com> - 0.7.9-1
- Updated to 0.7.9

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.7.7-4
- Rebuild for glew 1.9.0

* Wed Dec 05 2012 Martin Preisler <mpreisle@redhat.com> - 0.7.7-3
- rebuilt for Ogre 1.8.1

* Thu Nov 15 2012 Tom Callaway <spot@fedoraproject.org> - 0.7.7-2
- drop incorrect BR

* Tue Nov 13 2012 Tom Callaway <spot@fedoraproject.org> - 0.7.7-1
- update to 0.7.7

* Sat Aug 11 2012 Bruno Wolff III <bruno@wolff.to> 0.7.6-7
- Rebuild for boost 1.50

* Thu Jul 26 2012 Hans de Goede <hdegoede@redhat.com> - 0.7.5-7
- Rebuilt for new GLEW

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Bruno Wolff III <bruno@wolff.to> 0.7.6-5
- Rebuild for irrlicht soname bump

* Sun Apr 01 2012 Bruno Wolff III <bruno@wolff.to> 0.7.6-4
- Rebuild for ogre 1.7.4

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.7.6-3
- Rebuild against PCRE 8.30

* Tue Jan 24 2012 Martin Preisler <mpreisle@redhat.com> 0.7.6-2
- Added a patch to avoid using locate for python detection

* Mon Jan 23 2012 Martin Preisler <mpreisle@redhat.com> 0.7.6-1
- New upstream release
- Added python to build requirements
- Added graphviz to build requirements

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Bruno Wolff III <bruno@wolff.to> 0.7.5-10
- Rebuild for boost soname bump

* Wed Sep 21 2011 Martin Preisler <mpreisle@redhat.com> 0.7.5-9
- Added the python subpackage (PyCEGUI)

* Tue Jun 21 2011 Bruno Wolff III <bruno@wolff.to> 0.7.5-8
- Rebuild for glew soname bump

* Sun May 15 2011 Bruno Wolff III <bruno@wolff.to> 0.7.5-7
- Rebuild for ogre 1.7.3

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 0.7.5-6
- Rebuilt with xerces-c 3.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  7 2011 Tom Callaway <spot@fedoraproject.org> 0.7.5-4
- rebuild against ogre without poco

* Mon Jan 03 2011 Hans de Goede <hdegoede@redhat.com> 0.7.5-3
- Put the OGRE and Irrlicht renderers in their own subpackages to reduce the
  number of deps of the main cegui package

* Mon Jan 03 2011 Bruno Wolff III <bruno@wolff.to> 0.7.5-2
- Fix typo in ogre dependency

* Tue Dec 21 2010 Tom Callaway <spot@fedoraproject.org> 0.7.5-1
- New upstream release 0.7.5
- Enable support for ogre, irrlicht

* Fri Nov  5 2010 Hans de Goede <hdegoede@redhat.com> 0.7.4-1
- New upstream release 0.7.4
- Also build the freeimage image codec
- Put the non default image codecs (DevIL, freeimage) and xml parsers (libxml,
  tinyxml and xerces) into their own sub-packages to reduce the number of deps
  of the main cegui package

* Mon Jun 21 2010 Hans de Goede <hdegoede@redhat.com> 0.6.2-6
- Fix building with latest tinyxml (#599850)

* Sun Feb 07 2010 Bruno Wolff III <bruno@wolff.to> - 0.6.2-5
- Rebuild for xerces update.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Hans de Goede <hdegoede@redhat.com> 0.6.2-2
- Fix building with latest DevIL

* Wed Dec  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.2-1
- New upstream release 0.6.2

* Fri Jul 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.1-1
- New upstream release 0.6.1
- Drop upstreamed patches

* Sun May 18 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.0-1
- New upstream release 0.6.0
- No ABI stability, use full versioned (libtool -release) sonames
- Use system tolua++, change license tag to match
- Use system tinyxml

* Wed Feb 13 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-7
- Added patch for new xerces-c. Courtesy of Hans de Goede
- Converted some documentation to UTF8
- Minor spec cleanups

* Wed Aug 29 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-6
- Yet another release bump, for building against expat2.

* Tue Aug 21 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-5
- Release bump for F8 mass rebuild
- License change due to new guidelines

* Sat Jun 30 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-4
- Release bump

* Sun Jun 17 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-3
- rpath fixes for x86_64

* Sun Jun 10 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-2
- Added patch to fix undefined-non-weak-symbol warnings

* Wed May 30 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-1
- Upgrade to 0.5.0b
- Added patch from Gentoo to compile with lua 5.1
- Updated the patch to use versioned .so for dlopen()
- Dropped several patches as they are no longer needed
- Dropped useless provides. Nothing used them anyway
- Added support for the SILLY image codec
- Added support for xerces-c

* Mon Aug 28 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-11
- Release bump for FC6 mass rebuild

* Sat Aug 05 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-10
- Header fix for g++ v4.1+

* Tue Jul 18 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-9
- Use versioned .so for dlopen()

* Sun Jun 11 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-8
- Updated --rpath fixes again
- Package devel-docs renamed to devel-doc as per 'new' guidelines

* Sat Jun 10 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-7.iss
- Updated --rpath fixes

* Fri Jun 09 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-6.iss
- Added patch courtesy of Hans de Goede fixing TinyXML usage
- Added patch courtest of Hans de Goede fixing 64bit issues
- Updated --rpath fixes
- Trivial correction for pkgconfig BR, should be >= really and not >

* Wed Jun 07 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-5.iss
- Removed IrrlichtRender headers as we don't support it (yet - anyway)
- Removed usage of --rpath during build process
- libtool dropped as a BR (no longer needed due to --rpath fix)
- Moved rebuilding of C++ bindings to %%build section

* Mon Jun 05 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-4.iss
- Added a tentative patch for building with the system tolua++/lua
- Added tolua++-devel as a buildrequire
- Rebuild the C++ bindings using the system tolua++

* Sun May 28 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-3.iss
- Added patch courtesy of Hans de Goede to force compilation against the system
  pcre libs instead of the bundled pcre.
- Added pcre-devel to buildrequires
- Replace xorg-x11-devel with libGLU-devel
- Removed PCRE-LICENSE from doc as it's now compiled against system pcre
- Specified version for pkgconfig buildrequires
- Replaced source URL with primary sf site, rather than a mirror
- Don't use bootstrap
- Added cegui_mk2 provides
- Removed superfluous documentation from devel package

* Sat May 27 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-2.iss
- Use %%{?dist} for most recent changelog entry - avoids incoherent changelog
  versions if %%{?dist} macro is missing or different.
- Added %%{version}-%%{release} to provides field
- Replaced %%{__sed} with sed

* Sun May 21 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-1.iss
- Initial Release
