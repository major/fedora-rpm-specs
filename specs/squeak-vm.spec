%global major   4
%global minor   10
%global patch   2
%global rev     2614
%global vmver   %{major}.%{minor}.%{patch}.%{rev}
%global vmver2   %{major}.%{minor}.%{patch}-%{rev}
%global source  Squeak-%{vmver}-src-no-mp3

Name:           squeak-vm
Version:        %{vmver}
Release:        36%{?dist}
Summary:        The Squeak virtual machine

License:        MIT
URL:            http://squeakvm.org/unix
Source0:        http://squeakvm.org/unix/release/%{source}.tar.gz
Source1:        inisqueak
Source2:        squeak-desktop-files.tar.gz
Patch0:         squeak-vm-dprintf.patch
Patch1:         alsa-fixes.patch
Patch2:         squeak-vm-4.10.2-fix-cmake.patch
Patch3:         squeak-vm-4.10.2-squeak-init-fix.patch
Patch4:         squeak-vm-4.10.2-format-security.patch
Patch5:         squeak-vm-4.10.2-gcc-14-fix.patch

# For clean upgrade path, could be probably dropped in F20 or later
Provides:       %{name}-nonXOplugins = %{version}-%{release}
Obsoletes:      %{name}-nonXOplugins < 4.10.2.2614-1

Requires:       xmessage

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libX11-devel libXt-devel libvorbis-devel libtheora-devel speex-devel
BuildRequires:  dbus-devel alsa-lib-devel pango-devel mesa-libGL-devel
BuildRequires:  libICE-devel libSM-devel libXext-devel libuuid-devel
BuildRequires:  libffi-devel nas-devel pulseaudio-libs-devel libxml2-devel glib2-devel
BuildRequires:  cairo-devel,  libv4l-devel

%description
Squeak is a full-featured implementation of the Smalltalk programming
language and environment based on (and largely compatible with) the original
Smalltalk-80 system.

This package contains just the Squeak virtual machine.

%prep
%setup -q -n %{source} -a 2

%patch -P0 -p1 -b .dprintf
%patch -P1 -p2 -b .alsa-fixes
%patch -P2 -p1 -b .fix-cmake
%patch -P3 -p1 -b .squeak-init-fix
%patch -P4 -p1 -b .format-security
%patch -P5 -p1 -b .gcc-14-fix

# Fix libdir
sed -i 's|libdir="${prefix}/lib/squeak"|libdir="%{_libdir}/squeak"|' unix/cmake/squeak.in

%build
%cmake ./unix -DCMAKE_VERBOSE_MAKEFILE=ON -DVM_HOST="%{_host}" -DVM_VERSION="%{vmver2}" -DPLATFORM_SOURCE_VERSION="%{rev}"
%cmake_build

%install
%cmake_install

# these files will be put in std RPM doc location
rm -rf %{buildroot}%{_prefix}/doc/squeak

# install the desktop stuff
install -D --mode=u=rw,go=r squeak.xml %{buildroot}%{_datadir}/mime/packages/squeak.xml
install -D --mode=u=rw,go=r squeak.png %{buildroot}%{_datadir}/pixmaps/squeak.png

%global icons_dir %{buildroot}%{_datadir}/icons/gnome
for size in 16 24 32 48 64 72 96
do
  mkdir -p %{icons_dir}/${size}x${size}/mimetypes
  install -m0644 squeak${size}.png %{icons_dir}/${size}x${size}/mimetypes/application-x-squeak-image.png
  install -m0644 squeaksource${size}.png %{icons_dir}/${size}x${size}/mimetypes/application-x-squeak-source.png
done

# Remove squeak.sh & mysqueak, obsoleted
rm -f %{buildroot}%{_bindir}/squeak.sh

# Install own version of inisqueak
install -m0755 %{SOURCE1} %{buildroot}%{_bindir}/inisqueak

%files
%doc unix/ChangeLog unix/doc/{README*,LICENSE,*RELEASE_NOTES}
%{_bindir}/*
%dir %{_libdir}/squeak
%dir %{_libdir}/squeak/%{vmver2}
%if 0 == 0%{?nonXOplugins}
%{_libdir}/squeak/%{vmver2}/so.FileCopyPlugin
%{_libdir}/squeak/%{vmver2}/so.B3DAcceleratorPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.PseudoTTYPlugin
%{_libdir}/squeak/%{vmver2}/so.UnixOSProcessPlugin
%{_libdir}/squeak/%{vmver2}/so.XDisplayControlPlugin

%{_libdir}/squeak/%{vmver2}/so.AioPlugin
%{_libdir}/squeak/%{vmver2}/so.ClipboardExtendedPlugin
%{_libdir}/squeak/%{vmver2}/so.DBusPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.GStreamerPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.ImmX11Plugin
#%%{_libdir}/squeak/%%{vmver2}/so.KedamaPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.KedamaPlugin2
%{_libdir}/squeak/%{vmver2}/so.MIDIPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.OggPlugin
%{_libdir}/squeak/%{vmver2}/so.RomePlugin
%{_libdir}/squeak/%{vmver2}/so.Squeak3D
%{_libdir}/squeak/%{vmver2}/so.UUIDPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.VideoForLinuxPlugin
%{_libdir}/squeak/%{vmver2}/so.HostWindowPlugin

#%%{_libdir}/squeak/%%{vmver2}/npsqueak.so
#%%{_libdir}/squeak/%%{vmver2}/squeak
%{_libdir}/squeak/%{vmver2}/so.vm-display-X11
%{_libdir}/squeak/%{vmver2}/so.vm-display-fbdev
%{_libdir}/squeak/%{vmver2}/so.vm-display-null
%{_libdir}/squeak/%{vmver2}/so.vm-sound-ALSA
%{_libdir}/squeak/%{vmver2}/so.vm-sound-OSS
%{_libdir}/squeak/%{vmver2}/so.vm-sound-null

#%%{_libdir}/squeak/%%{vmver2}/so.Mpeg3Plugin
%{_libdir}/squeak/%{vmver2}/so.SqueakFFIPrims
%{_libdir}/squeak/%{vmver2}/so.vm-display-custom
%{_libdir}/squeak/%{vmver2}/so.vm-sound-NAS
%{_libdir}/squeak/%{vmver2}/so.vm-sound-custom
%{_libdir}/squeak/%{vmver2}/so.vm-sound-pulse
%{_libdir}/squeak/%{vmver2}/squeakvm

# 4.10 plugins
%{_libdir}/squeak/%{vmver2}/ckformat
%{_libdir}/squeak/%{vmver2}/so.CameraPlugin
%{_libdir}/squeak/%{vmver2}/so.ScratchPlugin
%{_libdir}/squeak/%{vmver2}/so.UnicodePlugin
%{_libdir}/squeak/%{vmver2}/so.WeDoPlugin

%endif
%{_mandir}/man*/*
#%%dir %%{_datadir}/squeak
#%%{_datadir}/squeak/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/gnome/*/mimetypes/*.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb  5 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.10.2.2614-34
- Fixed FTBFS with gcc-14
  Resolves: rhbz#2261712

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 4.10.2.2614-28
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb  6 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.10.2.2614-26
- Fixed FTBFS
  Resolves: rhbz#1923669

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 4.10.2.2614-24
- Require xmessage not xorg-x11-apps

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.10.2.2614-18
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2.2614-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2.2614-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 4.10.2.2614-12
- update icon/mime scriptlets

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2.2614-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2.2614-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec  6 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 4.10.2.2614-9
- Fixed compilation with -Werror=format-security
  Resolves: rhbz#1037336
- Fixed bogus dates in changelog (best effort)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2.2614-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Daniel Drake <dsd@laptop.org> - 4.10.2.2614-7
- Add upstream fixes for ALSA sound backend, needed for OLPC.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2.2614-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 4.10.2.2614-5
- Removed desktop file
  Resolves: rhbz#544256

* Mon Nov 26 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 4.10.2.2614-4
- Another upgrade path fix

* Sun Nov 25 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 4.10.2.2614-3
- Rebuilt with RPM_OPT_FLAGS and made build more verbose
  Resolves: rhbz#879974

* Fri Nov 23 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 4.10.2.2614-2
- Fixed upgrade path from older Fedoras

* Fri Nov 23 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 4.10.2.2614-1
- New version
  Resolves: rhbz#861633, rhbz#861970, rhbz#856016
- Fixed desktop file
  Resolves: rhbz#544256
- Merged nonXOplugins to main package
- Replaced defines by globals
- Added own version of inisqueak
- Fixed squeak startup script (by squeak-init-fix patch)
- Removed squeak.sh and mysqueak
- Removed sources symlinks
- Dropped alsa-scratchy-sound patch (upstreamed)
- Dropped imgdir, rpath patches (not needed)
- Defuzzification of patches
- Added xmessage requirement (xorg-x11-apps)
- Fixed bogus dates in changelog

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar  7 2012 Daniel Drake <dsd@laptop.org> - 3.10.5-8
- Fix build, by temporarily excluding V4L plugin (for now).
- A V4L2 port is in progress.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 21 2010 Daniel Drake <dsd@laptop.org> - 3.10.5-5
- Add upstream patch to fix sound loss during suspend/resume

* Mon Dec 28 2009 Daniel Drake <dsd@laptop.org> - 3.10.5-4
- forgot to add patch to cvs; retag

* Mon Dec 28 2009 Daniel Drake <dsd@laptop.org> - 3.10.5-3
- Add (already upstream) patch to fix crackly sound output

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Gavin Romig-Koch <gavin@redhat.com> - 3.10.5-1
  - upgrade to new upstream
  - work around dprintf problem
  - UUID lib now in libuuid-devel (moved from e2fsprogs-devel) 
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Gavin Romig-Koch <gavin@redhat.com> - 3.10.4-3
   - SqueakFFIPrims only works on ix86 and ppc
   - add a missing dir macro
   - correct the requires on -nonXOplugins
   - correct handling of no nonXOplugins
* Mon Jan 19 2009 Gavin Romig-Koch <gavin@redhat.com> - 3.10.4-3
   - add missing build dependancy for UUIDPlugin
   - add missing defattr macro
   - corrections needed by rpmlint
* Sat Jan 17 2009 Gavin Romig-Koch <gavin@redhat.com> - 3.10.3-4
   - upgrade to upstream 3.10.3-4
   - switch from svn to tarball as upstream source
* Wed Jan 07 2009 Gavin Romig-Koch <gavin@redhat.com> - 3.10.3-3
  - split out nonXOplugins
  - corrected script requirements
* Tue Nov 25 2008 Gavin Romig-Koch <gavin@redhat.com> - 3.10.3-2
  - Fix rpmlint problems
    - mode of squeak-vm-tarball-from-svn.sh
    - squeak.desktop: Icon, MimeType, Encoding
    - move the _libdir .source links into this, non-noarch, rpm
    - remove x mode of a number of .c and .h source files from upstream
    - use explicit --mode when installing files
    - replace tabs with spaces
    - shbang for mysqueak
* Tue Jul 29 2008 Gavin Romig-Koch <gavin@redhat.com> - 3.10.3-1
  - incorporated slightly modified Desktop related changes from 
    Gerard Milmeister <gemi@bluewin.ch> 
  - update .spec to Fedora Guidelines
  - add mysqueak
  - olpc macro to distinguish olpc builds 
  - distinguish between squeak image icons, and squeak source icons
* Mon Jul 07 2008 Bert Freudenberg <bert@freudenbergs.de>
  - 3.10-3olpc5; SVN r. 1899
  - re-enable new (IPv6) socket primitives (bf)
  - RomePlugin pango fixes (yo)
* Mon Jun 23 2008 Bert Freudenberg <bert@freudenbergs.de>
  - 3.10-3olpc4; SVN r. 1895
  - RomePlugin pango fixes (yo)
  - X11 drag-and-drop fixes (tak)
* Tue Jun 03 2008 Bert Freudenberg <bert@freudenbergs.de>
  - 3.10-3olpc3; SVN r.1889
  - prefer 24 and 16 bpp over 32 to fix alpha issue in compositing desktops (bf)
* Mon May 19 2008 Bert Freudenberg <bert@freudenbergs.de>
  - 3.10-3olpc2; SVN r.1879
  - re-add big cursor support (bf)
* Wed May 14 2008 Bert Freudenberg <bert@freudenbergs.de>
  - 3.10-3olpc1; SVN r. 1878
  - updated DBus plugin (incompatible w/ previous versions)
  - add plugins: GStreamer, ImmX11, Aio
  - fixed international keyboard input
  - merged with trunk
* Fri Jan 04 2008 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-12olpc5; SVN r. 1811
  - remove Mpeg3Plugin
  - fix KedamaPlugin2 (exports where not listed) 
  - fix show-source key
  - fix SEGFAULT in OggPlugin
  - add RomePlugin w/ Pango support
  - fix drag-n-drop
* Mon Dec 03 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-12olpc4: SVN r. 1795
  - fix dbus plugin not zero-terminating some strings (bf)
* Wed Oct 31 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-12olpc3: SVN r. 1787
  - fixed errors about state checking in drag and drop (tak)
  - make cursor keys work with utf32 char code (yo)
  - add SetSwitch, GetSwitch, and SetDevice mixer functions (yo)
* Tue Oct 23 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-12olpc2: SVN r. 1779
  - use CPPFLAGS not CFLAGS for -DSUGAR
  - handle view-source key (bf)
* Mon Oct 15 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-12olpc1: SVN r. 1776
  - merged with trunk (bf)
  - signed oop fixes (dave)
  - unicode key events (ian)
  - fix dbus plugin (bf)
* Thu Aug 30 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-11olpc5: SVN r. 1761
  - set _NET_WM_PID to our process id (danw)
  - generate WindowEventClose on delete window message (ian)
* Tue Jul 17 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-11olpc4: SVN r. 1747
  - added LocalePlugin (ian)
  - FileCopyPlugin is external now
  - follow symlinks in npsqueakregister (bf)
  - explicitely link against libXt (bf)
* Thu Jul 12 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-11olpc3: SVN r. 1740
  - fix spec file clean, add _smp_mflags as requested by fedora (bf)
  - XdndFinished is sent properly in drag-in with multiple types (tak)
  - Show cursor forced when drag-out (tak)
  - Fixed a bug about type index for clipboard (tak)
* Mon Jul 02 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-11olpc2: SVN r. 1735
  - clipboard/dns fixes (tak)
  - update spec to satisfy rpmlint
* Tue Jun 26 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-11olpc1: SVN r. 1728
  - IPv6 support (ian)
  - updated DBus plugin (impara, bf)
  - better drag-and-drop support, extended clipboard support (tak)
* Fri Jun 22 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-10olpc7: SVN r.1723
  - move build env to Fedora 7
  - require libdbus-1.so.3
  - configure without OpenGL (rather than hiding GL libs)
* Thu May 17 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-10olpc6: SVN r.1687
  - add ClipboardExtendedPlugin (tak)
  - add DBusPlugin (impara, bf)
  - support keypad keys (bf)
* Thu Apr 19 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-10olpc5: SVN r.1658
  - enabled Kedama plugin
* Wed Apr 04 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-10olpc4: SVN r.1652 (moved to OLPC branch)
  - added ogg plugin (tak)
* Fri Mar 23 2007 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-10olpc3: SVN r.1613 + olpc.patch
  - big cursor support (bf)
  - faster camera input (dgd)
* Thu Nov 09 2006 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-10olpc1: SVN r.1591
  - work around ALSA SIGIO issue (bf)
  - added dgd's camera support (V4L plugin)
* Thu Nov 09 2006 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-9olpc4: SVN r.1571
  - compile without GL
* Wed Oct 18 2006 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-9olpc3: SVN r.1571
  - relicensed to MIT
* Tue Oct 17 2006 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-9olpc2: SVN r.1566
  - yet another ALSA fix
* Thu Oct 12 2006 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-9olpc1: SVN r.1563
  - fix ALSA prim failed
  - add warpblt optimization
  - add Kedama2 plugin
  - exclude unneeded plugins
* Wed Oct 11 2006 Bert Freudenberg <bert@freudenbergs.de>
  - 3.9-8olpc2: SVN r.1557 adds access to ALSA mixer
* Fri Oct 06 2006 Bert Freudenberg <bert@freudenbergs.de>
  - initial RPM for OLPC (3.9-8olpc1)
