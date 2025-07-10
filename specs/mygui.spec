Name:           mygui
Version:        3.4.3
Release:        %autorelease
Summary:        Fast, simple and flexible GUI library for games and 3D applications.
License:        MIT
URL:            http://mygui.info/
Source0:        https://github.com/MyGUI/mygui/archive/MyGUI%{version}/mygui-MyGUI%{version}.tar.gz
# Demo and tools resources configuration
Source1:        resources.xml
# Script to run MyGui tools
Source2:        MyGUI-Tools
# Desktop files
Source3:        mygui-layouteditor.desktop
Source4:        mygui-imageeditor.desktop
Source5:        mygui-fonteditor.desktop
Source6:        mygui-skineditor.desktop

BuildRequires:  cmake
BuildRequires:  cmake(SDL2)
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  freetype-devel 
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  graphviz
BuildRequires:  libuuid-devel
BuildRequires:  libX11-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  ninja-build
BuildRequires:  ois-devel
BuildRequires:  SDL2_image-devel

Requires:       dejavu-sans-fonts

%description
MyGUI is a cross-platform library for creating graphical user interfaces (GUIs) for games and 3D applications.

%package        devel
Summary:        Development files for MyGUI
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mesa-libGL-devel
Requires:       ois-devel
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        devel-doc
Summary:        Development documentation for MyGUI
BuildArch:      noarch

%description    devel-doc
The %{name}-devel-doc package contains reference documentation for
developing applications that use %{name}.

%package tools
Summary:        MyGUI tools 
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains the MyGUI tools, installed in %{_bindir}. 
LayoutEditor is an application for designing UIs using MyGUI library,
FontEditor, ImageEditor and SkinEditor are also provided. They are
renamed to be prefixed with mygui (ie mygui-LayoutEditor)

%prep
%setup -qn %{name}-MyGUI%{version}


%build
%cmake -G Ninja \
   -DMYGUI_BUILD_DEMOS=FALSE \
   -DMYGUI_BUILD_DOCS=TRUE \
   -DMYGUI_BUILD_PLUGINS=OFF \
   -DMYGUI_BUILD_TOOLS=TRUE \
   -DMYGUI_DONT_USE_OBSOLETE=ON \
   -DMYGUI_INSTALL_DEMOS=FALSE \
   -DMYGUI_INSTALL_DOCS=TRUE \
   -DMYGUI_INSTALL_PDB=FALSE \
   -DMYGUI_INSTALL_TOOLS=TRUE \
   -DMYGUI_RENDERSYSTEM=4 \
   -DMYGUI_USE_SYSTEM_GLEW=TRUE
%cmake_build
cd %{_vpath_builddir}
pushd Docs
doxygen
popd

%install
%cmake_install
install -d %{buildroot}%{_datadir}/doc/mygui-devel-doc/html
install -d %{buildroot}%{_datadir}/MYGUI/Tools
install -D %{_vpath_builddir}/Docs/html/* %{buildroot}%{_datadir}/doc/mygui-devel-doc/html

# Install desktop entry for LayoutEditor
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE4}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE5}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE6}

# Replace resources.xml with our version of it
rm -f %{buildroot}%{_bindir}/resources.xml
install %{SOURCE1} %{buildroot}%{_datadir}/MYGUI/Tools/resources.xml

# Move tools out of bin and into datadir/tools
mv %{buildroot}%{_bindir}/ImageEditor %{buildroot}%{_datadir}/MYGUI/Tools/ImageEditor
mv %{buildroot}%{_bindir}/FontEditor %{buildroot}%{_datadir}/MYGUI/Tools/FontEditor
mv %{buildroot}%{_bindir}/LayoutEditor %{buildroot}%{_datadir}/MYGUI/Tools/LayoutEditor
mv %{buildroot}%{_bindir}/SkinEditor %{buildroot}%{_datadir}/MYGUI/Tools/SkinEditor

# Install our handy tools script
install -Dpm755 %{SOURCE2} %{buildroot}%{_bindir}/MyGUI-Tools

# Strip away unittests media 
rm -rf %{buildroot}%{_datadir}/MYGUI/Media/UnitTests

# Remove CMake stuff from Media
rm -f %{buildroot}%{_datadir}/MYGUI/Media/CMakeLists.txt

# Link fonts from dejavu package
ln -fs %{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans.ttf \
  %{buildroot}%{_datadir}/MYGUI/Media/MyGUI_Media/DejaVuSans.ttf
ln -fs %{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans-ExtraLight.ttf \
  %{buildroot}%{_datadir}/MYGUI/Media/MyGUI_Media/DejaVuSans-ExtraLight.ttf

# Move icons to appropriate directory
for size in 16 24 32 48 96 256 ; do
  install -Dpm644 Media/Common/Sources/Icons/MyGUI_Icon_FE_${size}x${size}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/mygui_fe.png
  install -Dpm644 Media/Common/Sources/Icons/MyGUI_Icon_IE_${size}x${size}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/mygui_ie.png
  install -Dpm644 Media/Common/Sources/Icons/MyGUI_Icon_SE_${size}x${size}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/mygui_se.png
done

# Layout Editor is missing 32x32 icons, so we're doing them seperately. 
for size in 16 24 48 96 256 ; do
    install -Dpm644 Media/Common/Sources/Icons/MyGUI_Icon_LE_${size}x${size}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/mygui_le.png
done

%check
%ctest

%files
%license COPYING.MIT
%doc README.md
%{_libdir}/libMyGUICommon.so.%{version}
%{_libdir}/libMyGUIEngine.so.%{version}
%dir %{_datadir}/MYGUI
%dir %{_datadir}/MYGUI/Media
%{_datadir}/MYGUI/Media/Common
%{_datadir}/MYGUI/Media/MyGUI_Media
%{_datadir}/MYGUI/Media/Wrapper

%files devel
%{_includedir}/MYGUI
%{_libdir}/libEditorFramework.so
%{_libdir}/libMyGUI.OpenGLPlatform.so
%{_libdir}/libMyGUICommon.so
%{_libdir}/libMyGUIEngine.so
%{_libdir}/pkgconfig/MYGUI.pc

%files devel-doc
%doc Docs/html

%files tools
%doc Tools/Readme.txt Tools/LayoutEditor/Readme.txt
%{_bindir}/MyGUI-Tools
%{_datadir}/MYGUI/Tools/resources.xml
%{_datadir}/MYGUI/Tools/LayoutEditor
%{_datadir}/MYGUI/Tools/ImageEditor
%{_datadir}/MYGUI/Tools/FontEditor
%{_datadir}/MYGUI/Tools/SkinEditor
%{_datadir}/MYGUI/Media/Tools
%{_datadir}/MYGUI/Media/Demos
%{_iconsdir}/hicolor/*/apps/mygui_*.png
%{_datadir}/applications/mygui-layouteditor.desktop
%{_datadir}/applications/mygui-skineditor.desktop
%{_datadir}/applications/mygui-fonteditor.desktop
%{_datadir}/applications/mygui-imageeditor.desktop


%changelog
%autochangelog
* Tue Jun 25 2025 Claire Robsahm <inquiries@chapien.net> - 3.4.3-4
- Made libraries and icons explicit rather than wildcard.
- Removed unnecessary dependencies and sorted them alphabetically.

* Mon Jun 09 2025 Claire Robsahm <inquiries@chapien.net> - 3.4.3-1
- Updated to 3.4.3. Build using OpenGL instead of OGRE.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 3.2.2-10
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 3.2.2-7
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 3.2.2-4
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 3.2.2-2
- Rebuilt for Boost 1.63

* Sat Mar 05 2016 Bruno Wolff III <bruno@wolff.to> - 3.2.2-1
- mygui 3.2.2
- Release notes: https://github.com/MyGUI/mygui/releases/tag/MyGUI3.2.2

* Thu Feb 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.1-9
- Reflect freetype header location having changed (F24FTBFS).
- Remove %%defattr.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.2.1-7
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 3.2.1-6
- Rebuilt for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Bruno Wolff III <bruno@wolff.to> - 3.2.1-4
- Make sure FTBFS issue is fixed

* Mon Feb 09 2015 Bruno Wolff III <bruno@wolff.to> - 3.2.1-3
- Rebuild for boost update

* Tue Dec 30 2014 Bruno Wolff III <bruno@wolff.to> - 3.2.1-2
- Don't use removed find -perm option (+) in MyGUI-Demos and MyGUI-Tools

* Tue Dec 30 2014 Bruno Wolff III <bruno@wolff.to> - 3.2.1-1
- License changed from LGPLv3 to MIT
- Source location changed from sourceforge to github
- Change log: https://github.com/MyGUI/mygui/releases/tag/MyGUI3.2.1
- Adjust patches for changes to cmake files
- Fix unowned directory
- Remove obsolete ldconfig file
- The supplied tools changed
- libX11-devel is now required for building
- Obsolete BUILDROOT definition removed

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.0-10
- Check for freetype2/freetype.h on fedora > 20 (FTBFS, RHBZ #1106255).
- Remove BR: autoconf, automake, libtool (unused).
- Remove BR: e2fsprogs-devel (unused).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 3.2.0-8
- rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 3.2.0-6
- Rebuild for boost 1.54.0

* Thu Apr 25 2013 Tom Callaway <spot@fedoraproject.org> - 3.2.0-5
- rebuild to include libCommon

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.2.0-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.2.0-3
- Rebuild for Boost-1.53.0

* Wed Dec 26 2012 Kevin Fenzi <kevin@scrye.com> 3.2.0-2
- Rebuild for new libCommon

* Tue Dec 04 2012 Bruno Wolff III <bruno@wolff.to> - 3.2.0-1
- Update to upstream 3.2.0
- Changelog: http://redmine.mygui.info/repositories/entry/mygui/tags/MyGUI3.2/ChangeLog.txt

* Fri Aug 10 2012 Bruno Wolff III <bruno@wolff.to> - 3.0.1-16
- Rebuild for boost 1.50

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Bruno Wolff III <bruno@wolff.to> - 3.0.1-14
- Rebuild for ogre 1.7.4

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-13
- Rebuilt for c++ ABI breakage

* Tue Jan 17 2012 Bruno Wolff III <bruno@wolff.to> - 3.0.1-12
- Rebuild for ois 1.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Bruno Wolff III <bruno@wolff.to> - 3.0.1-10
- Rebuild for boost soname bump

* Fri Jul 22 2011 Bruno Wolff III <bruno@wolff.to> - 3.0.1-9
- Rebuild for boost 1.47

* Sun May 15 2011 Bruno Wolff III <bruno@wolff.to> - 3.0.1-8
- Rebuild for ogre 1.7.3

* Mon May 02 2011 Kevin Fenzi <kevin@scrye.com> - 3.0.1-7
- Fix pc file issues. Fixes bug #693352

* Wed Apr 06 2011 Bruno Wolff III <bruno@wolff.to> - 3.0.1-6
- Rebuild for boost soname bump to 1.46.1 in rawhide.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Thomas Spura <tomspur@fedoraproject.org> - 3.0.1-4
- rebuild for new boost

* Sat Jan 08 2011 Bruno Wolff III <bruno@wolff.to> - 3.0.1-3
- Clean up a few more rpmlint warnings

* Sat Jan 08 2011 Bruno Wolff III <bruno@wolff.to> - 3.0.1-2
- Try to fix rpath issue

* Fri Jan 07 2011 Bruno Wolff III <bruno@wolff.to> - 3.0.1-1
- Update to 3.0.1 release
- Rebuild for ogre update

* Fri Nov 27 2009 Guido Grazioli <guido.grazioli@gmail.com> - 3.0.0-0.4.2332svn
- Install OGRE platform headers

* Wed Nov 18 2009 Guido Grazioli <guido.grazioli@gmail.com> - 3.0.0-0.3.2332svn
- Fix macros usage
- Fix Release tag
- Add desktop entry for LayoutEditor
- Update patch to fix missing undefined non-weak symbols
- Improve summaries and descriptions
- Remove redundant VERBOSE flag
- Add graphviz BR to generate doxygen graphs

* Fri Oct 30 2009 Guido Grazioli <guido.grazioli@gmail.com> - 3.0.0-2.2332svn
- Fix includes dir
- Remove plugin

* Fri Oct 23 2009 Guido Grazioli <guido.grazioli@gmail.com> - 3.0.0-1.2332svn
- Upstream to svn revision 2332
- Patch cmake build scripts to support multilib
- Fix package summaries
- Fix changelog
- Fix %%doc
- Add Require: ogre-devel to -devel subpackage
- Add -devel-doc subpackage
- Revert source tarball from xz to bzip2

* Sat Oct 03 2009 Guido Grazioli <guido.grazioli@gmail.com> - 2.3.0-4.1861svn
- Add BR: rpm >= 4.6.1-2 needed for F-10 builds (BZ #514480)

* Thu Oct 01 2009 Guido Grazioli <guido.grazioli@gmail.com> - 2.3.0-3.1861svn
- Improve package summary
- Provide scripts to run MyGUI tools

* Wed Sep 30 2009 Guido Grazioli <guido.grazioli@gmail.com> - 2.3.0-2.1861svn
- Add BR: libuuid-devel instead of BR: e2fsprogs-devel for F12+
- Fix License

* Tue Sep 29 2009 Guido Grazioli <guido.grazioli@gmail.com> - 2.3.0-1.1861svn
- Rename from libmygui to mygui
- Symlink fonts in media dir to dejavu-sans-fonts ones
- Add doxygen generated docs to -devel
- Provide a generic script to setup and run demos 
- Fix rpmlint warnings

* Mon Sep 28 2009 Guido Grazioli <guido.grazioli@gmail.com> - 2.3.0-0.1861svn
- Initial packaging
