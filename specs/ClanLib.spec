Summary:        Cross platform C++ game library
Name:           ClanLib
Version:        2.3.7
Release:        34%{?dist}
License:        zlib
URL:            http://www.clanlib.org/
Source0:        http://www.clanlib.org/download/releases-2.0/%{name}-%{version}.tgz
# This is http://clanlib.org/docs/clanlib-2.3/reference_doxygen.zip renamed
# to reflect the exact version for which it was downloaded
Source1:        ClanLib-%{version}-generated-docs.zip
Patch1:         ClanLib-2.3.4-gcc47.patch
Patch2:         ClanLib-2.3.4-non-x86.patch
Patch3:         ClanLib-2.3.7-no-wm_type-in-fs.patch
Patch4:         ClanLib-2.3.7-no-ldflags-for-conftest.patch
Patch5:         ClanLib-2.3.7-gcc7.patch
Patch6:         ClanLib-2.3.7-ftbfs.patch
Patch7:         ClanLib-2.3.7-link-pthread.patch
BuildRequires:  make gcc-c++
BuildRequires:  libX11-devel libXi-devel libXmu-devel libGLU-devel libICE-devel
BuildRequires:  libXext-devel libXxf86vm-devel libXt-devel xorg-x11-proto-devel
BuildRequires:  libvorbis-devel mikmod-devel alsa-lib-devel
BuildRequires:  libpng-devel libjpeg-devel fontconfig-devel
BuildRequires:  libXrender-devel sqlite-devel libtool
Provides:       clanlib = %{version}-%{release}

%description
ClanLib is a cross platform C++ game library.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libGLU-devel xorg-x11-proto-devel libXrender-devel
Requires:       fontconfig-devel libjpeg-devel libpng-devel libXxf86vm-devel
Requires:       mikmod-devel alsa-lib-devel sqlite-devel pcre-devel
Provides:       clanlib-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -a 1
./autogen.sh
mv reference_doxygen html


%build
%configure --disable-dependency-tracking --disable-static --disable-docs \
  --disable-clanRegExp   \
  --enable-clanDisplay   \
  --enable-clanGL        \
  --enable-clanGL1       \
  --enable-clanSound     \
  --enable-clanDatabase  \
  --enable-clanSqlite    \
  --enable-clanNetwork   \
  --enable-clanGUI       \
  --enable-clanCSSLayout \
  --enable-clanSWRender  \
  --enable-clanMikMod    \
  --enable-clanVorbis

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.la


%ldconfig_scriptlets


%files
%doc CREDITS
%license COPYING
%{_libdir}/libclan23*.so.*

%files devel
%doc README html
%{_libdir}/libclan23*.so
%{_includedir}/%{name}-2.3
%{_libdir}/pkgconfig/clan*-2.3.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct  5 2022 Hans de Goede <hdegoede@redhat.com> - 2.3.7-27
- Stop building clanRegExp lib, pcre1 is no longer maintained (rhbz#2128277)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug  2 2021 Hans de Goede <hdegoede@redhat.com> - 2.3.7-24
- Stop using the obsolete pthread_mutexattr_setkind_np function
  (really fix FTBFS and runtime issues in dependend packages)

* Mon Aug  2 2021 Hans de Goede <hdegoede@redhat.com> - 2.3.7-23
- Fix libclan23Core not being linked against libpthread which is causing
  FTBFS issues in other packages

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Hans de Goede <hdegoede@redhat.com> - 2.3.7-17
- Fix FTBFS (rhbz#1674574)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Hans de Goede <hdegoede@redhat.com> - 2.3.7-11
- Fix FTBFS (rhbz#1423261)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.7-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Apr  2 2015 Hans de Goede <hdegoede@redhat.com> - 2.3.7-6
- Fix building with _hardened_build 1 (rhbz#1207404)

* Mon Mar 30 2015 Xavier Bachelot <xavier@bachelot.org> - 2.3.7-5
- Don't rely on autodetection to select which modules to build.

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.7-4
- Rebuilt for GCC 5 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug  1 2013 Hans de Goede <hdegoede@redhat.com> - 2.3.7-1
- New upstream release 2.3.7 (rhbz#973934)
- Ignore apps requesting no-decorations in fullscreen mode

* Tue May 14 2013 Hans de Goede <hdegoede@redhat.com> - 2.3.6-11
- Rebuild to re-enable the graphics parts, which were disabled by
  configure in the last build because of a freetype issue (rhbz#961855)

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 2.3.6-10
- Remove no longer needed autoreconf call, %%configure from redhat-rpm-config
  >= 9.1.0-42 updates config.guess and config.sub for new architecture support

* Mon Mar 25 2013 Hans de Goede <hdegoede@redhat.com> - 2.3.6-9
- Run autoreconf for aarch64 support (rhbz#925149)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.3.6-7
- rebuild due to "jpeg8-ABI" feature drop

* Tue Jan 08 2013 Dan Horák <dan[at]danny.cz> - 2.3.6-6
- fix build on non-x86 arches

* Mon Jan 07 2013 Adam Tkac <atkac redhat com> - 2.3.6-5
- fix building against new mesa (upstream change r8912)

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.3.6-4
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 2.3.6-2
- Fix build on ARM

* Tue Mar 27 2012 Hans de Goede <hdegoede@redhat.com> - 2.3.6-1
- New upstream release 2.3.6 (rhbz#807218)

* Fri Feb 24 2012 Hans de Goede <hdegoede@redhat.com> - 2.3.5-1
- New upstream release 2.3.5 (rhbz#797132)

* Thu Jan 12 2012 Hans de Goede <hdegoede@redhat.com> - 2.3.4-4
- Fix building with gcc-4.7

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Hans de Goede <hdegoede@redhat.com> - 2.3.4-2
- Fixup BuildRequires and -devel Requires for new requirements of 2.3.4

* Sun Dec 11 2011 Hans de Goede <hdegoede@redhat.com> - 2.3.4-1
- New upstream release 2.3.4

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.1.2-3
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Hans de Goede <hdegoede@redhat.com> 2.1.2-1
- New upstream release 2.1.2
- Drop all patches (all upstreamed)

* Sat May 29 2010 Hans de Goede <hdegoede@redhat.com> 2.1.1-1
- New upstream release 2.1.1
- Fix clanSound clanMikMod and clanVorbis modules missing on ppc (#595934)

* Wed Nov 11 2009 Hans de Goede <hdegoede@redhat.com> 2.1.0-3
- Fix -devel Requires to require fontconfig-devel not just fontconfig

* Wed Nov 11 2009 Hans de Goede <hdegoede@redhat.com> 2.1.0-2
- Add Requires to -devel package to make sure all libs needed by
  "pkg-config --libs clanDisplay-2.1" are present

* Wed Nov  4 2009 Hans de Goede <hdegoede@redhat.com> 2.1.0-1
- Major new upstream release 2.1.0 (#532078)
- The old 1.0 version is now available in the ClanLib1 package for
  packages which need it

* Thu Sep 10 2009 Hans de Goede <hdegoede@redhat.com> 1.0.0-3
- Fix (workaround) viewport issues in fullscreen mode (#522116)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Hans de Goede <hdegoede@redhat.com> 1.0.0-1
- New upstream release 1.0.0, note: API compatible but changes soname

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Hans de Goede <hdegoede@redhat.com> 0.8.1-2
- Fix build with gcc 4.4  

* Wed Mar 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.1-1
- New upstream release
- Drop all patches (all upstreamed)
- Add patch to keep libclanDisplay-0.8 abi compatible with 0.8.0
- Warning, this release changes the ABI of the GUIStyleSilver input_box widget
- Warning, some small API changes, CL_KEY_ADD -> CL_KEY_NUMPAD_ADD, etc.

* Sat Mar  8 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-11
- Add a patch from Dave Jones fixing various wrong invocations of memset

* Sun Mar  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-10
- Add support for audio output through alsa (original ClanLib only supports
  OSS??), this also adds support for using pulseaudio through alsa

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.0-9
- Autorebuild for GCC 4.3

* Fri Jan  4 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-8
- Fix building with gcc 4.3

* Sun Oct 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-7
- Fix multilib conflicts in generated Reference documentation (bz 340851)

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-6
- Update License tag for new Licensing Guidelines compliance

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 0.8.0-5
- Rebuild against SDL_gfx 2.0.16.

* Sat Mar 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-4
- Fix some stupidness in the OpenGL surface code, which triggers an obscure
  bug in mesa-6.5.2, as a bonus the OpenGL surface's should be somewhat faster
  now. Details: https://bugs.freedesktop.org/show_bug.cgi?id=10491

* Sun Oct  8 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-3
- Rewrote ClanLib fullscreen handling to fix an issue where a part of the
  window decoration show in fullscreen mode on certain videocards

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-2
- FE6 Rebuild

* Sun Aug 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-1
- 0.8.0 final, warning ABI changed without soname change!
- Drop both our patches (both upstreamed)

* Wed Jul 26 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-0.6.RC2
- Add missing Requires: pkgconfig to -devel package

* Tue Jul 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-0.5.RC2
- Add libXt-devel BR to fix X detection on FC-5, sorry about all these
  missing BRs and Requires.

* Tue Jul 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-0.4.RC2
- Add libGLU-devel to the BuildRequires to fix build on FC-5
- Add missing Requires: libGLU-devel xorg-x11-proto-devel to -devel package

* Tue Jul 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-0.3.RC2
- Add libXi-devel to the BuildRequires so that clanGL gets build

* Fri Jul 21 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-0.2.RC2
- Change License: to "zlib License" as 0.8 is under the zlib License not the
  LGPL (0.6 is LGPL).
- Add a patch from pingus contrib dir which adds support for the grave key
- Add libXmu-devel to the BuildRequires

* Wed Jul 19 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-0.1.RC2
- Initial FE version based on the newrpms SRPM by Che.
