# Force out of source build
%undefine __cmake_in_source_build

Name:           allegro
Version:        4.4.3.1
Release:        10%{?dist}

Summary:        A game programming library
Summary(es):    Una libreria de programacion de juegos
Summary(fr):    Une librairie de programmation de jeux
Summary(it):    Una libreria per la programmazione di videogiochi
Summary(cs):    Knihovna pro programování her

License:        Giftware
URL:            http://liballeg.org/
Source0:        https://github.com/liballeg/allegro5/releases/download/%{version}/allegro-%{version}.tar.gz
Patch1:         allegro-4.0.3-cfg.patch
Patch2:         allegro-4.0.3-libdir.patch
Patch5:         allegro-4.4.2-buildsys-fix.patch
Patch6:         allegro-4.4.2-doc-noversion.patch
# Replace racy recursive mutex implementation with proper recursive mutexes
Patch8:         allegro-4.4.2-mutex-fix.patch
# Calling Xsync from the bg thread causes deadlock issues
Patch9:         allegro-4.4.2-no-xsync-from-thread.patch
# gnome-shell starts apps while gnome-shell has the keyb grabbed...
Patch10:        allegro-4.4.2-keybgrab-fix.patch
# 4.4.3 has dropped the fadd/fsub etc aliases, but some apps need them
Patch11:        allegro-4.4.2-compat-fix-aliases.patch
# 4.4.3 accidentally broke the tools, fix them (rhbz1682921)
Patch12:        allegro-4.4.3-datafile-double-free.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1767827
# starting texinfo-6.7 the default encoding is UTF-8 and because allegro's
# source .texi file is encoded in ISO-8859-1, additional command is needed
Patch13:        allegro-4.4.3-texinfo-non-utf8-input-fix.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  texinfo cmake3
BuildRequires:  xorg-x11-proto-devel libX11-devel libXpm-devel libXcursor-devel
BuildRequires:  libXxf86vm-devel libXxf86dga-devel libGL-devel libGLU-devel
BuildRequires:  alsa-lib-devel jack-audio-connection-kit-devel
BuildRequires:  libjpeg-devel libpng-devel libvorbis-devel
Requires:       timidity++-patches

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia.

%description -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia.

%description -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale.

%description -l cs
Allegro je multiplatformní knihovna pro počítačové hry a jiné
typy multimediálního programování.


%package devel
Summary:        A game programming library
Summary(es):    Una libreria de programacion de juegos
Summary(fr):    Une librairie de programmation de jeux
Summary(it):    Una libreria per la programmazione di videogiochi
Summary(cs):    Knihovna pro programování her
Requires:       %{name}%{?_isa} = %{version}-%{release}, xorg-x11-proto-devel
Requires:       libX11-devel, libXcursor-devel

%description devel
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%description devel -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete es necesario para compilar los programas que usen Allegro.

%description devel -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia. Ce
package est nécessaire pour compiler les programmes utilisant Allegro.

%description devel -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto è necessario per compilare programmi scritti con Allegro.

%description devel -l cs
Allegro je multiplatformní knihovna pro počítačové hry a jiné
typy multimediálního programování. Tento balíček je je potřebný
k sestavení programů napsaných v Allegru.


%package tools
Summary:        Extra tools for the Allegro programming library
Summary(es):    Herramientas adicionales para la librería de programación Allegro
Summary(fr):    Outils supplémentaires pour la librairie de programmation Allegro
Summary(it):    Programmi di utilità aggiuntivi per la libreria Allegro
Summary(cs):    Přídavné nástroje pro programovou knihovnu Allegro
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description tools
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package contains extra
tools which are useful for developing Allegro programs.

%description tools -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete contiene herramientas adicionales que son útiles para
desarrollar programas que usen Allegro.

%description tools -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia. Ce
package contient des outils supplémentaires qui sont utiles pour le
développement de programmes avec Allegro.

%description tools -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto contiene programmi di utilità aggiuntivi utili allo sviluppo
di programmi con Allegro.

%description tools -l cs
Allegro je multiplatformní knihovna pro počítačové hry a jiné
typy multimediálního programování. Tento balíček obsahuje přídavné nástroje,
které jsou užitečné pro vývoj Allegro programů.

%package jack-plugin
Summary:        Allegro JACK (Jack Audio Connection Kit) plugin
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description jack-plugin
This package contains a plugin for Allegro which enables Allegro to playback
sound through JACK (Jack Audio Connection Kit).


%package -n alleggl
Summary:        OpenGL support library for Allegro
License:        zlib or GPL+
URL:            http://allegrogl.sourceforge.net/
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n alleggl
AllegroGL is an Allegro add-on that allows you to use OpenGL alongside Allegro.
You use OpenGL for your rendering to the screen, and Allegro for miscellaneous
tasks like gathering input, doing timers, getting cross-platform portability,
loading data, and drawing your textures. So this library fills the same hole
that things like glut do.

%package -n alleggl-devel
Summary:        Development files for alleggl
License:        zlib or GPL+
Requires:       alleggl%{?_isa} = %{version}-%{release}

%description -n alleggl-devel
The alleggl-devel package contains libraries and header files for
developing applications that use alleggl.


%package -n jpgalleg
Summary:        JPEG library for the Allegro game library
License:        zlib
URL:            http://www.ecplusplus.com/index.php?page=projects&pid=1
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n jpgalleg
jpgalleg is a JPEG library for use with the Allegro game library. It allows
using JPEG's as Allegro bitmaps.

%package -n jpgalleg-devel
Summary:        Development files for jpgalleg
License:        zlib
Requires:       jpgalleg%{?_isa} = %{version}-%{release}

%description -n jpgalleg-devel
The jpgalleg-devel package contains libraries and header files for
developing applications that use jpgalleg.


%package loadpng
Summary:        OGG/Vorbis library for the Allegro game library
License:        Public Domain
URL:            http://wiki.allegro.cc/index.php?title=LoadPNG
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description loadpng
loadpng is some glue that makes it easy to use libpng to load and
save bitmaps from Allegro programs.

%package loadpng-devel
Summary:        Development files for loadpng
License:        Public Domain
Requires:       %{name}-loadpng%{?_isa} = %{version}-%{release}

%description loadpng-devel
The loadpng-devel package contains libraries and header files for
developing applications that use loadpng.


%package logg
Summary:        OGG/Vorbis library for the Allegro game library
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description logg
LOGG is an Allegro add-on library for playing OGG/Vorbis audio files.

%package logg-devel
Summary:        Development files for logg
License:        MIT
Requires:       %{name}-logg%{?_isa} = %{version}-%{release}

%description logg-devel
The logg-devel package contains libraries and header files for
developing applications that use logg.


%prep
%autosetup -p1

%build
%cmake3 -DOpenGL_GL_PREFERENCE:STRING=LEGACY -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DDOCDIR:STRING=%{_pkgdocdir} -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE
%cmake3_build

pushd %{_vpath_builddir}
# Converting text documentation to UTF-8 encoding.
for file in docs/AUTHORS docs/CHANGES docs/THANKS \
        docs/info/*.info docs/txt/*.txt docs/man/get_camera_matrix.3 \
        ../addons/allegrogl/changelog; do
  iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
  touch -r $file $file.new && \
  mv $file.new $file
done
popd

%install
%cmake3_install

pushd %{_vpath_builddir}
# installation of these is broken, because they use a cmake GLOB, but
# that gets "resolved" when runnning cmake, and at that time the files
# to install aren't generated yet ...
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/html
install -p -m 644 docs/man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install -p -m 644 docs/html/*.{html,css} \
    $RPM_BUILD_ROOT%{_pkgdocdir}/html/
install -m 755 docs/makedoc $RPM_BUILD_ROOT%{_bindir}/allegro-makedoc
popd

# Install some extra files
install -Dpm 644 allegro.cfg $RPM_BUILD_ROOT%{_sysconfdir}/allegrorc
install -pm 755 tools/x11/xfixicon.sh $RPM_BUILD_ROOT%{_bindir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/allegro
install -pm 644 keyboard.dat language.dat $RPM_BUILD_ROOT%{_datadir}/allegro
install -Dpm 644 misc/allegro.m4 $RPM_BUILD_ROOT%{_datadir}/aclocal/allegro.m4

mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/allegrogl
install -pm 644 addons/allegrogl/changelog addons/allegrogl/faq.txt \
 addons/allegrogl/readme.txt addons/allegrogl/bugs.txt \
 addons/allegrogl/extensions.txt addons/allegrogl/howto.txt addons/allegrogl/quickstart.txt \
 addons/allegrogl/todo.txt $RPM_BUILD_ROOT%{_pkgdocdir}/allegrogl/

mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/loadpng
install -pm 644 addons/loadpng/CHANGES.txt addons/loadpng/README.txt addons/loadpng/THANKS.txt \
 $RPM_BUILD_ROOT%{_pkgdocdir}/loadpng/

mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/jpgalleg
install -pm 644 addons/jpgalleg/readme.txt \
 $RPM_BUILD_ROOT%{_pkgdocdir}/jpgalleg/


%ldconfig_scriptlets 
%ldconfig_scriptlets -n alleggl 

%ldconfig_scriptlets -n jpgalleg

%ldconfig_scriptlets loadpng

%ldconfig_scriptlets logg


%files
%{_pkgdocdir}/
%exclude %{_pkgdocdir}/dat*.txt
%exclude %{_pkgdocdir}/grabber.txt
%exclude %{_pkgdocdir}/allegrogl
%exclude %{_pkgdocdir}/jpgalleg
%exclude %{_pkgdocdir}/loadpng
%exclude %{_pkgdocdir}/loadpng
%license %{_pkgdocdir}/license.txt
%config(noreplace) %{_sysconfdir}/allegrorc
%{_libdir}/liballeg.so.4*
%{_datadir}/allegro
# We cannot use exclude for alleg-jack.so because then the build-id for it
# still ends up in the main allegro package, e.g. rpmlint says:
# allegro.x86_64: W: dangling-relative-symlink /usr/lib/.build-id/48/024a0ddad02d9c6f4b956fb18f20d4a0bfde41 ../../../../usr/lib64/allegro/4.4.3/alleg-jack.so
%dir %{_libdir}/allegro
%dir %{_libdir}/allegro/4.4.3
%{_libdir}/allegro/4.4.3/alleg-alsa*.so
%{_libdir}/allegro/4.4.3/alleg-dga2.so
%{_libdir}/allegro/4.4.3/modules.lst

%files devel
%{_bindir}/allegro-config
%{_bindir}/allegro-makedoc
%{_libdir}/liballeg.so
%{_libdir}/pkgconfig/allegro.pc
%{_includedir}/allegro
%{_includedir}/allegro.h
%{_includedir}/xalleg.h
%{_datadir}/aclocal/allegro.m4
%{_infodir}/allegro.info*
%{_mandir}/man3/*

%files tools
%{_pkgdocdir}/dat*.txt
%{_pkgdocdir}/grabber.txt
%{_bindir}/colormap
%{_bindir}/dat
%{_bindir}/dat2s
%{_bindir}/dat2c
%{_bindir}/exedat
%{_bindir}/grabber
%{_bindir}/pack
%{_bindir}/pat2dat
%{_bindir}/rgbmap
%{_bindir}/textconv
%{_bindir}/xfixicon.sh

%files jack-plugin
%{_libdir}/allegro/4.4.3/alleg-jack.so

%files -n alleggl
%license addons/allegrogl/gpl.txt
%license addons/allegrogl/zlib.txt
%{_libdir}/liballeggl.so.4*

%files -n alleggl-devel
%{_pkgdocdir}/allegrogl/
%{_libdir}/liballeggl.so
%{_libdir}/pkgconfig/allegrogl.pc
%{_includedir}/alleggl.h
%{_includedir}/allegrogl

%files -n jpgalleg
%license addons/jpgalleg/license.txt
%{_libdir}/libjpgalleg.so.4*

%files -n jpgalleg-devel
%{_pkgdocdir}/jpgalleg/
%{_libdir}/libjpgalleg.so
%{_libdir}/pkgconfig/jpgalleg.pc
%{_includedir}/jpgalleg.h

%files loadpng
%license addons/loadpng/LICENSE.txt
%{_pkgdocdir}/loadpng/
%{_libdir}/libloadpng.so.4*

%files loadpng-devel
%{_libdir}/libloadpng.so
%{_libdir}/pkgconfig/loadpng.pc
%{_includedir}/loadpng.h

%files logg
%license addons/logg/LICENSE.txt
%{_libdir}/liblogg.so.4*

%files logg-devel
%{_libdir}/liblogg.so
%{_libdir}/pkgconfig/logg.pc
%{_includedir}/logg.h


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.4.3.1-1
- Release 4.4.3.1
- Use %%_pkgdocdir
- Use CMake3 on epel
- Use dedicated CMake 'build' directory
- Patched for texinfo-6.7 (rhbz#1767827)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Hans de Goede <hdegoede@redhat.com> - 4.4.3-2
- The 4.4.3 update broke the dat and grabber tools, fix them (rhbz#1682921)

* Mon Feb 18 2019 Hans de Goede <hdegoede@redhat.com> - 4.4.3-1
- New upstream release 4.4.3

* Sat Feb 16 2019 Hans de Goede <hdegoede@redhat.com> - 4.4.2-23
- Fix FTBFS (rhbz#1674575)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Hans de Goede <hdegoede@redhat.com> - 4.4.2-20
- Fix PPC allegro app builds failing due to alcompat.h defining aliases for
  fadd / fdiv / fmull which conflict with system headers (#1582916, #1582917)
- Modernize spec-file a bit

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Hans de Goede <hdegoede@redhat.com> - 4.4.2-16
- Fix FBTFS

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Hans de Goede <hdegoede@redhat.com> - 4.4.2-13
- Fix allegro apps which start fullscreen failing to start from gnome-shell
  with a "Can not grab keyboard" error message

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 29 2014 Hans de Goede <hdegoede@redhat.com> - 4.4.2-11
- Replace racy recursive mutex implementation with proper recursive mutexes
- Use XPending instead of XSync + XeventsQueued to avoid a deadlock

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 15 2013 Hans de Goede <hdegoede@redhat.com> - 4.4.2-8
- Fix docdir for unversioned docdir F-20 change (rhbz#993664)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Hans de Goede <hdegoede@redhat.com> - 4.4.2-6
- Add /usr/share/aclocal/allegro.m4 to -devel package

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 15 2011 Peter Robinson <pbrobinson@fedoraproject.org> 4.4.2-2
- Make pre/post dependencies for all non i686 arches sane

* Tue Jul 12 2011 Hans de Goede <hdegoede@redhat.com> 4.4.2-1
- New upstream release
- Partially based on spec file update by Brandon McCaig <bamccaig@gmail.com>
- Drop a number of no longer relevant patches
- Now comes with alleggl, jpgalleg, loadpng and logg bundled

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  7 2011 Hans de Goede <hdegoede@redhat.com> 4.2.3-4
- Fix a format string bug in the pack utility reported on bugtraq
  (but without security implications)

* Thu Sep  9 2010 Hans de Goede <hdegoede@redhat.com> 4.2.3-3
- Fix FTBFS (#631099)

* Mon Jun 21 2010 Hans de Goede <hdegoede@redhat.com> 4.2.3-2
- Fix multilib conflict in -devel (#603836)

* Mon Oct  5 2009 Jindrich Novy <jnovy@redhat.com> 4.2.3-1
- update to 4.2.3

* Thu Sep 10 2009 Hans de Goede <hdegoede@redhat.com> 4.2.2-14
- Fix (workaround) viewport issues in fullscreen mode (#522116)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-11
- Fix wrong file path in semanage call in scriptlets (#481407)

* Mon May  5 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-10
- Look for /etc/timidity.cfg instead of /usr/share/timidity/timidity.cfg,
  as the latter is no longer available now that Fedora has switched from
  timidity++-patches to PersonalCopy-Lite-patches

* Tue Apr  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-9
- Fix i386 asm code compilation with latest binutils
- Remove -fomit-frame-pointer from the compile flags of the default build, so
  that we get a usefull debuginfo even for the normal (non debug/profile) lib

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.2.2-8
- Autorebuild for GCC 4.3

* Mon Jan 21 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-7
- Add makedoc utility to allegro-devel as allegro-makedoc (bz 429450)
- Fix sound when using pulseaudio
- Fix compilation of inline asm with gcc 4.3

* Sun Oct 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-6
- Require timidity++-patches instead of timidity++ itself so that we don't
  drag in arts and through arts, qt and boost
- Add BuildRequires: glib2-devel to workaround RH bug 331841

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-5
- Update to pristine upstream sources instead of using allegro.cc pre-release

* Tue Aug 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-4
- Rebuild for buildId

* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-3
- Enable building of JACK (Jack Audio Connection Kit) sound output plugin
- Put non default sound output plugins in their own subpackage to avoid
  dragging in unwanted deps (allegro-esound-plugin, allegro-arts-plugin,
  allegro-jack-plugin) (bz 250736)
- Make man pages and info file UTF-8

* Tue Jul 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-2
- sync .libdir patch to 4.2.2 and use it again for multilib devel goodness
  (make allegro-devel i386 and x86_64 parallel installable again)

* Mon Jul 23 2007 Jindrich Novy <jnovy@redhat.com> 4.2.2-1
- update to 4.2.2
- drop .libdir patch
- sync .multilib patch

* Fri Jul  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.1-3
- Silence output of chcon command in %%post, because otherwise users get this:
  "chcon: can't apply partial context to unlabeled file" when installing with
  selinux disabled (bz 246820)

* Fri Dec 22 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.1-2
- Restore multilib devel goodness patch (make allegro-devel i386 and x86_64
  parallel installable)
- Restore execstack patch so that binaries linked against allegro do not
  require an execstack and thus work under selinux (without this
  liballeg_unshareable.a contains object files which require an executable
  stack which will end up in any app linked against allegro)
- Make alleg-dga2.so plugin 100% PIC so it can load with selinux enabled
- Mark alleg-vga.so plugin as textrel_shlib_t as it isn't 100% PIC and cannot
  be fixed (easily) to be 100% PIC

* Tue Nov 28 2006 Jindrich Novy <jnovy@redhat.com> 4.2.1-1
- update to 4.2.1

* Sun Oct 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-18
- Multilib devel goodness (make allegro-devel i386 and x86_64 parallel
  installable)

* Sat Sep  2 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-17
- FE6 Rebuild

* Fri Jul 14 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-16
- Don't package the main allegro lib in -devel as its already in the main
  package, iow only put the debug and profile versions -devel.

* Thu Jul  6 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-15
- Stop allegro from making applications linked against it claim that they
  need an executable stack (Patch11). Unfortunatly this requires a rebuild of
  all applications linked against allegro.

* Mon Jun 26 2006 Jindrich Novy <jnovy@redhat.com> 4.2.0-14
- compile alld and allp debuging/profiling libraries (#196616)
- fix typo in release caused by recent changes

* Sat Jun 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-13
- Add autoconf BR for missing autoheader with the new mock config.

* Tue Mar 21 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-12
- Sleep in xwindows vsync emulation, instead of busy waiting.
- Add %%{dist} to Release

* Mon Mar 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-11
- really, _really_ fix asm stretch code on i386 with NX processors, long
  story see bugzilla bug 185214 .

* Sat Mar 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-10
- really fix asm stretch code on i386 with NX processors, on OpenBSD mprotects
  first argument does not need to be page-aligned, but on Linux it does.
  Note that for this to work you may also need to disable selinux (rh 185214)

* Wed Mar  8 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-9
- fix fullscreen <-> window switching bug (bz 183645)
- fix asm stretch code on i386 with NX processors, thanks to openBSD.

* Mon Feb 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-8
- fix sound not working on PPC (bz 183112)
- fix allegro not finding and loading plugins/modules on x86_64 (bz 183113)

* Wed Feb  8 2006 Jindrich Novy <jnovy@redhat.com> 4.2.0-7
- set timidity++ as Requires instead of BuildRequires

* Tue Feb  7 2006 Jindrich Novy <jnovy@redhat.com> 4.2.0-6
- fix digmid loading of timidity midi patches (#180154)

* Wed Jan 25 2006 Jindrich Novy <jnovy@redhat.com> 4.2.0-5
- update default allegro configuration to use sound successfully,
  thanks to Hans de Goede (#178383)
- add timidity++ dependency

* Mon Jan 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-4
- add allegro-4.2.0-nostrip.patch, so that the main .so file
  doesn't get stripped and we actually get debuginfo for it in
  allegro-debuginfo

* Fri Jan 20 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-3
- update / fix BuildRequires for modular X (bz 178245)

* Fri Dec 16 2005 Jindrich Novy <jnovy@redhat.com> 4.2.0-2
- update dependencies for the new modular X
- disable _smp_mflags to workaround build failure caused
  by bad dependencies

* Wed May 25 2005 Jindrich Novy <jnovy@redhat.com> 4.2.0-1
- update to 4.2.0
- package dat2c, allegro.m4
- replace XFree86-devel Buildrequires with xorg-x11-devel
- drop mmaptest, novga, gcc4 patches

* Wed May 25 2005 Jindrich Novy <jnovy@redhat.com> 4.0.3-13
- fix compilation on x86_64 (#158648)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 4.0.3-12
- rebuild on all arches

* Mon May  2 2005 Jindrich Novy <jnovy@redhat.com> 0:4.0.3-11
- fix build failures with gcc4 (#156224)
- don't use %%{name} in patch names
- add Czech translation to package description/summary

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Mar  4 2005 Ville Skyttä <ville.skytta at iki.fi>
- Split context marked dependency syntax to work around #118773.

* Sun Feb 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-9
- Disable vga and vbeaf on all non-%%{ix86}.
- Fix lib paths in allegro-config for 64-bit archs.
- Use *nix commands in allegrorc's [grabber] section.

* Sun Feb 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-8
- Build without vga and vbeaf on non-x86-like archs.
- Apply upstream patch to fix build without vga.

* Fri Nov 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-7
- Explicitly disable svgalib for now.
- Let rpm take care of all stripping.
- Build with whatever the compiler supports, MMX and friends are detected
  at runtime.
- Minor specfile style improvements.

* Wed Nov 10 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:4.0.3-6
- Fix build for FC3 via fixed mmap test in configure script.

* Mon Nov 10 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.5
- Use MMX/SSE where appropriate (bug 959).

* Mon May 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.4
- Include *.so.* symlink.
- Re-introduce ldconfigs.
- *grumble*

* Mon May 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.3
- -devel Requires XFree86-devel.

* Mon May 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.2
- Handle --excludedocs installs gracefully.
- BuildRequires arts-devel.
- Make *.so executable so RPM groks autodependencies.
- Update to accordance with current Fedora spec template.

* Sat Apr 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.1
- Update to 4.0.3.
- Make build honor optflags.
- Remove redundant ldconfigs.

* Sat Apr  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.0.1.rc3
- Update to 4.0.3RC3.

* Thu Mar 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.0.1.rc2
- Update to 4.0.3RC2, and to current Fedora guidelines.
- make -jX works again.
- Don't remove info files on -devel upgrade.

* Wed Feb 19 2003 Warren Togami <warren@togami.com> 4.0.3-0.beta2.fedora.2
- Disable smp make flags, Makefile needs fixing

* Wed Feb 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 4.0.3-0.beta2.fedora.1
- First Fedora release, based on upstream source RPM.

* Fri Dec 07 2001 Angelo Mottola <lillo@users.sourceforge.net>  4.0.0-1
- added italian translation

* Tue Oct 02 2001 Peter Wang <tjaden@users.sourceforge.net>  3.9.39-1
- icon courtesy of Johan Peitz

* Mon Sep 24 2001 Peter Wang <tjaden@users.sourceforge.net>
- remaining translations by Eric Botcazou and Grzegorz Adam Hankiewicz

* Sun Sep 23 2001 Peter Wang <tjaden@users.sourceforge.net>
- translations by Eric Botcazou and Javier González
- language.dat and keyboard.dat moved to main package
- devel split into devel and tools packages
- makedoc added to tools package

* Sun Sep 16 2001 Peter Wang <tjaden@users.sourceforge.net>
- merged Osvaldo's spec file with gfoot's spec and some other changes

* Wed Sep 27 2000 Osvaldo Santana Neto <osvaldo@conectiva.com>
- updated to 3.9.33
