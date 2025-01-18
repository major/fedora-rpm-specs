Summary:        Version 0.6 of this Cross platform C++ game library
Name:           ClanLib06
Version:        0.6.5
Release:        65%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://www.clanlib.org/
# No URL as this old version is no longer available on clanlib.org
Source0:        ClanLib-%{version}-1.tar.gz
# prebuild docs to avoid multilib conflicts. To regenerate untar and configure,
# cd Documentation, make, make install HTML_PREFIX=`pwd`/html, cd ..,
# tar cvfz ClanLib-%%{version}-generated-docs.tar.gz Documentation/html
Source1:        ClanLib-%{version}-generated-docs.tar.gz
Patch0:         ClanLib-0.6.5-debian.patch
Patch1:         ClanLib-0.6.5-suse.patch
Patch2:         ClanLib-0.6.5-tolua++.patch
Patch3:         ClanLib-0.6.5-smalljpg.patch
Patch4:         ClanLib-0.6.5-gcc4.3.patch
Patch5:         ClanLib-0.6.5-mikmod32.patch
Patch6:         ClanLib-0.6.5-alsa.patch
Patch7:         ClanLib-0.6.5-extra-keys.patch
Patch8:         ClanLib-0.6.5-xev-keycodes.patch
Patch9:         ClanLib-0.6.5-iterator-abuse.patch
Patch10:        ClanLib-0.6.5-gcc4.6.patch
Patch11:        ClanLib-0.6.5-gzopen-flags.patch
Patch12:        ClanLib-0.6.5-libpng15.patch
Patch13:        ClanLib-0.6.5-lua52.patch
Patch14:        ClanLib-0.6.5-gcc6.patch
Patch15:        ClanLib-0.6.5-xwayland-fixes.patch
Patch16:        ClanLib-0.6.5-resolution-sort-fix.patch
Patch17:        ClanLib-0.6.5-numpad-keys-fix.patch
Patch18:        ClanLib-0.6.5-compiler-warnings.patch
Patch19:        ClanLib-header.patch
Patch20:        ClanLib-0.6.5-joystick.patch
Patch21:        ClanLib-0.6.5-fix-ldflags-use.patch
Patch22:        ClanLib-0.6.5-use-pthread_mutexattr_settype.patch
BuildRequires:  make gcc gcc-c++
BuildRequires:  libX11-devel libXext-devel libXt-devel libGLU-devel
BuildRequires:  libICE-devel libXxf86vm-devel xorg-x11-proto-devel
BuildRequires:  libvorbis-devel libpng-devel libjpeg-devel mikmod-devel
BuildRequires:  alsa-lib-devel Hermes-devel freetype-devel autoconf
BuildRequires:  tolua++-devel >= 1.0.93-14
Provides:       clanlib06 = %{version}-%{release}

%description
Version 0.6 of this cross platform C++ game library, which is still used
by many games.


%package devel
Summary:        Development files for ClanLib 0.6
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libGLU-devel Hermes-devel mikmod-devel libpng-devel
Provides:       clanlib06-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use ClanLib 0.6.


%prep
%autosetup -p1 -a 1 -n ClanLib-%{version}
# mark asm files as NOT needing execstack
for i in `find Sources -name '*.s'`; do
  echo '.section .note.GNU-stack,"",@progbits' >> $i
done
autoconf


%build
export CXXFLAGS="$RPM_OPT_FLAGS -Wno-unused-result -Wno-write-strings -Wno-char-subscripts -Wno-deprecated-declarations"
%ifarch %{ix86}
ARCH_CONFIG_FLAGS=--enable-asm386
%endif
%configure --disable-debug --enable-dyn --disable-directfb $ARCH_CONFIG_FLAGS
tolua++ -o Sources/Lua/clanbindings.cpp Sources/Lua/clanbindings.pkg
# no smpflags, it somehow breaks the libs, causing a crash on exit like this:
#0  0x00007ffff7ecee98 in CL_Signal_v2<CL_InputDevice*, CL_Key const&>::~CL_Signal_v2() () from /lib64/libclanJPEG.so.2
#1  0x00007ffff786a48e in __cxa_finalize () from /lib64/libc.so.6
#2  0x00007ffff7e44367 in __do_global_dtors_aux () from /lib64/libclanPNG.so.2
#3  0x00007fffffffd1d0 in ?? ()
#4  0x00007ffff7fe213b in _dl_fini () from /lib64/ld-linux-x86-64.so.2
make


%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.a
chmod -x $RPM_BUILD_ROOT%{_mandir}/man1/clanlib-config.1*


%ldconfig_scriptlets


%files
%doc CREDITS NEWS ascii-logo
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc README README.gui README.upgrade Documentation/html
%{_bindir}/clanlib-config
%{_libdir}/*.so
%{_includedir}/ClanLib
%{_mandir}/man1/clanlib-config.1.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.5-64
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar  6 2022 Hans de Goede <hdegoede@redhat.com> - 0.6.5-56
- Use Fedora's standard LDFLAGS when linking
- Stop using obsolete pthread_mutexattr_setkind_np (rhbz#2045209)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb  6 2021 Hans de Goede <hdegoede@redhat.com> - 0.6.5-53
- Fix joystick-support (rhbz#1860696)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Jeff Law <law@redhat.com> - 0.6.5-51
- Explicitly include <cstddef> for NULL as its not implicitly included
  by gcc-11's header files

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Hans de Goede <hdegoede@redhat.com> - 0.6.5-48
- Fix ClanLib-0.6 apps crashing on exit

* Tue Nov  5 2019 Hans de Goede <hdegoede@redhat.com> - 0.6.5-47
- Fix a number of numpad keys not working in ClanLib-0.6 based games

* Tue Nov  5 2019 Hans de Goede <hdegoede@redhat.com> - 0.6.5-46
- Fix fullscreen windows not receiving events under Xwayland
- Fix ClanLib sometimes selecting a non optimal resolution when going fullscreen

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 20 2016 Hans de Goede <hdegoede@redhat.com> - 0.6.5-38
- Fix patch backup files getting installed under /usr/include/ClanLib

* Tue Feb 02 2016 Hans de Goede <hdegoede@redhat.com> - 0.6.5-37
- Fix FTBFS with gcc6

* Mon Feb 01 2016 Tim Niemueller <tim@niemueller.de> - 0.6.5-36
- rebuild for updated tolua++

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.5-34
- Rebuilt for GCC 5 C++11 ABI change

* Wed Dec 17 2014 Hans de Goede <hdegoede@redhat.com> - 0.6.5-33
- Rebuilt against new lua-5.2 based tolua++

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 09 2013 Hans de Goede <hdegoede@redhat.com> - 0.6.5-30
- Build with compat-lua-devel-5.1, rather then with lua-5.2, as tolua++
  has not been ported to lua-5.2. Fixes FTBFS (rhbz#991931)

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 0.6.5-28
- rebuild for new lua

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.6.5-26
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.6.5-25
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-23
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 11 2011 Hans de Goede <hdegoede@redhat.com> - 0.6.5-21
- Fix building with new libpng

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.5-20
- Rebuild for new libpng

* Sun Apr 03 2011 Hans de Goede <hdegoede@redhat.com> - 0.6.5-19
- Fix creating of clanlib data archives (rhbz#688309)

* Tue Feb 08 2011 Hans de Goede <hdegoede@redhat.com> - 0.6.5-18
- Fix building with gcc 4.6

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 29 2009 Hans de Goede <hdegoede@redhat.com> 0.6.5-16
- ClanLib06 used a hardcoded keycode table (lame), these have changed for some
  keys with us moving over to evdev, breaking the usage of these keys. Fix this
  by switching over to dynamically querying the X-server for keycodes
- Add a number of missing defines for non alpha-numerical keys
- Fix some abuse of iterators
- Remove smpflags, as that results in somehow broken libs (apps using them
  crash on exit ?)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep  7 2008 Hans de Goede <hdegoede@redhat.com> 0.6.5-13
- Fix patch fuzz build failure

* Sun Mar  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-12
- Add support for audio output through alsa (original ClanLib only supports
  OSS??), this also adds support for using pulseaudio through alsa

* Sun Feb 17 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-11
- Rebuild for new libmikmod
- Rebuild with gcc 4.3

* Fri Jan  4 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-10
- Fix building with gcc 4.3

* Sun Oct 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-9
- Explictily disable directfb support, so that it doesn't accidentally get
  build on system which have directfb installed
- Fix multilib conflict in the Reference documentation (bz 340861)

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-8
- Update License tag for new Licensing Guidelines compliance

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-7
- FE6 Rebuild

* Mon Jul 31 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-6
- Add missing Requires: libpng-devel to the -devel package <sigh>.

* Tue Jul 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-5
- Add missing BRs: libGLU-devel freetype-devel libXt-devel. To Fix resp
  building of clanGL, clanTTF and X detection on FC-5.

* Tue Jul 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-4
- Add missing Requires: libGLU-devel Hermes-devel mikmod-devel lua-devel to
  the -devel package.

* Sun Jul 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-3
- Mark asm files as NOT needing execstack, making us OK with new default
  SELinux targeted policy settings.

* Sun Jul 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-2
- Add missing BRs: tolua++-devel, Hermes-devel and autoconf

* Wed Jul 19 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.5-1
- Initial FE version based on the newrpms SRPM by Che.
