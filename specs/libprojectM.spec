%global reltag rc7
%global commit0 f2e0a32368e73a26746b0ac04a9182b23256825f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       libprojectM
Version:    3.1.12
Release:    12%{?dist}
Summary:    The libraries for the projectM music visualization plugin
License:    LGPLv2+
URL:        https://github.com/projectM-visualizer/projectm
Source0:    https://github.com/projectM-visualizer/projectm/archive/v%{version}/libprojectM-%{version}.tar.gz
#Source0:    https://github.com/projectM-visualizer/projectm/archive/v%%{version}-%%{reltag}/libprojectM-%%{version}-%%{reltag}.tar.gz
#Source0:    https://github.com/projectM-visualizer/projectm/archive/%%{commit0}/%%{name}-%%{shortcommit0}.tar.gz
Patch1:     0001-Build-projectM_qt-shared-lib-instead-static-lib.patch
Patch2:     0002-Generate-libproject-qt.pc.patch
Patch3:     0003-With-shared-lib-libprojectM-qt-we-don-t-need-this-an.patch
#Patch1:     projectM-disable_native_plugins.patch
#Patch3:     projectm-3.1.0-autotools.patch

BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libgomp
BuildRequires:  pkgconfig(glesv2)
#BuildRequires:  pkgconfig(glew)
#BuildRequires:  pkgconfig(glm)
BuildRequires:  glm-devel
BuildRequires:  pkgconfig(sdl2)
# libprojectM-qt
BuildRequires:  pkgconfig(Qt5Core)
#BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
#BuildRequires:  pkgconfig(Qt5Xml)
#BuildRequires:  cmake(Qt5LinguistTools)
#projectM-jack
BuildRequires:  jack-audio-connection-kit-devel
#projectM-libvisual
%if !0%{?rhel}
#BuildRequires:  libvisual-devel = 1:0.4.0
%endif
#projectM-pulseaudio
BuildRequires:  pkgconfig(libpulse)
#BuildRequires:  llvm-devel

BuildRequires:  bitstream-vera-sans-fonts
BuildRequires:  bitstream-vera-sans-mono-fonts
BuildRequires:  make

Requires:       bitstream-vera-sans-fonts
Requires:  bitstream-vera-sans-mono-fonts

Provides:  libprojectM-qt = %{version}-%{release}
Obsoletes: libprojectM-qt < %{version}-%{release}
Obsoletes: projectM-libvisual < %{version}-%{release}

%description
projectM is an awesome music visualizer. There is nothing better in the world
of Unix. projectM's greatness comes from the hard work of the community. Users
like you can create presets that connect music with incredible visuals.
projectM is an LGPL'ed reimplementation of Milkdrop under OpenGL. All projectM
requires is a video card with 3D acceleration and your favorite music.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package qt
Summary:    The Qt frontend to the projectM visualization plugin
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later

%description qt
projectM-qt is a GUI designed to enhance the projectM user and preset writer
experience.  It provides a way to browse, search, rate presets and setup
preset playlists for projectM-jack and projectM-pulseaudio.

%package qt-devel
Summary:    Development files for %{name}-qt
Requires:   %{name}-qt = %{version}-%{release}
Requires:   pkgconfig libprojectM-devel qt-devel

%description qt-devel
The %{name}-qt-devel package contains libraries and header files for
developing applications that use %{name}-qt.

%package -n projectM-jack
Summary:    The projectM visualization plugin for jack
License:    GPLv2+ and MIT

%description -n projectM-jack
This package allows the use of the projectM visualization plugin through any
JACK compatible applications.

%package -n projectM-pulseaudio
Summary:    The projectM visualization plugin for pulseaudio
License:    GPLv2+ and MIT

%description -n projectM-pulseaudio
This package allows the use of the projectM visualization plugin through any
pulseaudio compatible applications.

%package -n projectM-libvisual
Summary:    The projectM visualization plugin for libvisual
License:    GPLv2+ and LGPLv2+ and MIT

%description -n projectM-libvisual
This package allows the use of the projectM visualization plugin through any
libvisual compatible applications.

%package -n projectM-SDL
Summary:    The projectM visualization plugin for SDL
License:    GPLv2+ and LGPLv2+ and MIT

%description -n projectM-SDL
This package allows the use of the projectM visualization plugin through any
SDL2 compatible applications.

%prep
#setup -q -n projectm-%%{commit0}
#setup -q -n projectm-%%{version}-%{reltag}
%autosetup -p1 -n projectm-%{version}

#replace by symlink
rm -r fonts/*
ln -s %{_datadir}/fonts/bitstream-vera-sans-mono-fonts/VeraMono.ttf fonts/
ln -s %{_datadir}/fonts/bitstream-vera-sans-fonts/Vera.ttf fonts/

chmod -x LICENSE.txt
chmod -x presets/tests/README.md

find -name "*.?pp" -type f -exec chmod -x {} ';'
find -name "*.c" -exec chmod -x {} ';'
find -name "*.h" -exec chmod -x {} ';'
find -name "*inl" -exec chmod -x {} ';'

%build
#export CXXFLAGS="%{optflags} -Wl,--as-needed"
./autogen.sh
%configure --disable-static --disable-rpath --enable-sdl --enable-threading \
    --enable-gles --with-gnu-ld --with-x

#  --enable-emscripten     Build for web with emscripten
#  --enable-llvm           Support for JIT using LLVM
%make_build


%install
%make_install

find %{buildroot} -name '*.la' -delete
find %{buildroot} -name "*inl" -exec chmod -x {} ';'
find %{buildroot} -name "*milk" -exec chmod -x {} ';'
find %{buildroot} -name "*prjm" -exec chmod -x {} ';'

desktop-file-validate %{buildroot}%{_datadir}/applications/projectM-pulseaudio.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/projectM-jack.desktop

%files
%doc src/libprojectM/ChangeLog
%doc AUTHORS.txt README.md
%license src/libprojectM/COPYING
%{_libdir}/libprojectM.so.*
%{_datadir}/projectM/

%files devel
%{_bindir}/projectM-unittest
%{_includedir}/libprojectM
%{_libdir}/libprojectM.so
%{_libdir}/pkgconfig/libprojectM.pc

%files qt
%license src/projectM-qt/COPYING
%{_libdir}/libprojectM_qt*.so.*
%{_datadir}/icons/hicolor/scalable/apps/projectM.svg

%files qt-devel
%doc src/projectM-qt/ReadMe
#{_includedir}/%%{name}-qt
%{_libdir}/libprojectM_qt*.so
%{_libdir}/pkgconfig/libprojectM-qt*.pc

%files -n projectM-jack
%doc src/projectM-jack/ChangeLog
%license src/projectM-jack/COPYING
%{_bindir}/projectM-jack
%{_datadir}/applications/projectM-jack.desktop
%{_mandir}/man1/projectM-jack.1*

%files -n projectM-pulseaudio
%doc  src/projectM-pulseaudio/ChangeLog
%license src/projectM-pulseaudio/COPYING
%{_bindir}/projectM-pulseaudio
%{_datadir}/applications/projectM-pulseaudio.desktop
%{_mandir}/man1/projectM-pulseaudio.1*

%files -n projectM-SDL
%{_bindir}/projectMSDL

%if 0 && !0%{?rhel}
%files -n projectM-libvisual
%doc src/projectM-libvisual/AUTHORS src/projectM-libvisual/ChangeLog
%license src/projectM-libvisual/COPYING
%{_libdir}/libvisual-0.4/
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.12-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Sérgio Basto <sergio@serjux.com> - 3.1.12-3
- Build libprojectM_qt as shared lib instead static lib
- Readd subpackge qt (which will have the dependencies on Qt alone)
- Add subpackage SDL
- Use bitstream-vera-sans-fonts instead dejavu-sans-fonts

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 21 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.1.12-1
- Update to 3.1.12 (#1931164)

* Sun Feb 14 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.1.11-1
- Update to 3.1.11 (#1928290)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8 (#1911013)

* Wed Sep 23 2020 Sérgio Basto <sergio@serjux.com> - 3.1.7-1
- Update libprojectM to 3.1.7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Sérgio Basto <sergio@serjux.com> - 3.1.3-1
- New version 3.1.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-0.9.rc7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Sérgio Basto <sergio@serjux.com> - 3.1.1-0.8.rc7
- v3.1.1-rc7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-0.7.rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Sérgio Basto <sergio@serjux.com> - 3.1.1-0.6.rc4
- Update to rc4 final

* Wed Apr 24 2019 Sérgio Basto <sergio@serjux.com> - 3.1.1-0.5.rc3
- Desktop improvments more drop SDL

* Sun Mar 17 2019 Sérgio Basto <sergio@serjux.com> - 3.1.1-0.4.rc3
- Minor improvements and try to build on i686

* Thu Mar 14 2019 Sérgio Basto <sergio@serjux.com> - 3.1.1-0.3.rc3
- Add Provides/Obsoletes for libprojectM-qt and projectM-libvisual

* Wed Mar 13 2019 Sérgio Basto <sergio@serjux.com> - 3.1.1-0.2.rc3
- Can't workaround FTBFS on i686
- Minor fix in desktop file

* Wed Mar 13 2019 Sérgio Basto <sergio@serjux.com> - 3.1.1-0.1.rc3
- Update to 3.1.1-rc3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-9
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 2.1.0-3
- Rebuild for glew 2.0.0

* Sat Mar 19 2016 Sérgio Basto <sergio@serjux.com> - 2.1.0-2
- On epel (6 and 7) disable projectM-libvisual. 

* Wed Mar 16 2016 Sérgio Basto <sergio@serjux.com> - 2.1.0-1
- Update to 2.1.0 .
- deleted: 01-change-texture-size.patch, upstreamed.
- deleted: 04-change-preset-duration.patch, upstreamed.
- deleted: libprojectM-USE_THREADS.patch, configurable.
- deleted: libprojectM-soname.patch, configurable.
- deleted: libprojectM-fonts.patch, configurable.
- deleted: libprojectM-freetype25.patch, it is build well with freetype.
- Add patch to fix FTBFS with GCC6, courtesy of Ralf Corsepius.
- Add as sub packages: libprojectM-qt, libprojectM-qt-devel, projectM-jack,
  projectM-libvisual and projectM-pulseaudio.
- Also checked that remove_pulse_browser_h.patch, projectM-pulseaudio-stat.patch
  and projectM-libvisual-gcc46.patch are upstreamed.
- Add libprojectM-2.1.0-paths.patch and libprojectM-qt-2.1.0-paths.patch, to fix
  _libdir paths 
- Using fedora-review fixed: mix tabs and spaces,
  unused-direct-shlib-dependency, wrong-script-end-of-line-encoding and
  spurious-executable-perm.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 2.0.1-27
- Rebuild for glew 1.13

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.1-25
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.0.1-23
- Fix FTBFS with freetype-2.5 (#1106066)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 2.0.1-21
- rebuilt for GLEW 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 2.0.1-18
- Rebuild for glew 1.9.0

* Thu Jul 26 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-17
- rebuild (glew)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  1 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.1-15
- Enhancement of the patch in 2.0.1-11: also override invalid font paths
  passed in by applications as these lead to an immediate crash. (#664088)
- Make -devel base pkg dep arch-specific.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-14
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 ajax@redhat.com - 2.0.1-12
- Rebuild for new glew soname

* Sat May  7 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.1-11
- Also BuildRequires the desired font packages for the safety-checks.
- Drop obsolete README.fedora file since users need not modify their
  config file manually anymore to prevent projectM from crashing.
- Revise fonts patch: check that user's configured font files exist,
  fall back to our defaults, add safety-check in spec file, replace
  font paths in prep section. (#698404, #698381)

* Mon Apr 25 2011 Jameson Pugh <imntreal@gmail.com> - 2.0.1-10
- Fixed fonts patch

* Wed Mar 23 2011 Jameson Pugh <imntreal@gmail.com> - 2.0.1-9
- Correct typo in requirements

* Tue Mar 15 2011 Jameson Pugh <imntreal@gmail.com> - 2.0.1-8
- Replace obsolete bitstream-vera font requirements with dejavu

* Sat Jul 17 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-7
- Updated font patch with Orcan's changes

* Sat Jul 10 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-6
- Added patches so clementine can be built against it

* Fri May 21 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-5
- Don't create fonts directory
- Add a README.fedora for instructions on upgrading from -3

* Mon Apr 05 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-4
- Got rid of font symlinks

* Mon Feb 08 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-3
- Patch to remove the USE_THREADS option pending an update from upstream

* Sun Jan 10 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-2
- Made needed soname bump

* Sun Dec 13 2009 Jameson Pugh (imntreal@gmail.com) - 2.0.1-1
- New release

* Mon Oct 12 2009 Jameson Pugh (imntreal@gmail.com) - 1.2.0r1300-1
- SVN Release to prepare for v2

* Wed Feb 25 2009 Jameson Pugh (imntreal@gmail.com) - 1.2.0-9
- Aparently stdio.h didn't need to be included in BuiltinParams.cpp before, but is now

* Tue Feb 24 2009 Jameson Pugh (imntreal@gmail.com) - 1.2.0-8
- Font packages renamed

* Fri Jan 02 2009 Jameson Pugh (imntreal@gmail.com) - 1.2.0-7
- Per recommendation, switched font packages from bitstream to dejavu

* Mon Dec 22 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-6
- Updated font package names

* Tue Nov 04 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-5
- Moved sed command from prep to install
- Correct libprojectM.pc patch

* Thu Oct 30 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-4
- Removed patch for ChangeLog, and used sed command in the spec
- Added VERBOSE=1 to the make line
- Added patch to correct libprojectM.pc

* Wed Oct 29 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-3
- Added a patch to correct ChangeLog EOL encoding
- Cleaned up all Requires and BuildRequires
- Corrected ownership of include/libprojectM and data/projectM
- Removed unnecessary cmake arguments

* Wed Sep 24 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-2
- Removed fonts from package
- Added symlinks to the fonts due to hard coded programing

* Tue Sep 02 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-1
- New release
- 64-bit patch no longer needed

* Mon Mar 31 2008 Jameson Pugh (imntreal@gmail.com) - 1.1-1
- New release

* Wed Dec 05 2007 Jameson Pugh <imntreal@gmail.com> - 1.01-1
- Initial public release of the package
