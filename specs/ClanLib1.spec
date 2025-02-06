%define realname ClanLib

Summary:        Cross platform C++ game library
Name:           ClanLib1
Version:        1.0.0
Release:        46%{?dist}
License:        Zlib
URL:            http://www.clanlib.org/
Source0:        http://www.clanlib.org/download/releases-1.0/%{realname}-%{version}.tgz
# Prebuild docs to avoid multilib conflicts. To regenerate, build and install
# ClanLib without passing --disable-docs (requires perl, libxslt) and then:
# mv $RPM_BUILD_ROOT%%{_datadir}/doc/clanlib html
# tar cvfz ClanLib-%%{version}-generated-docs.tar.gz html
Source1:        ClanLib-%{version}-generated-docs.tar.gz
Patch0:         ClanLib-0.8.0-gcc43.patch
Patch1:         ClanLib-1.0.0-fullscreen-viewport.patch
Patch2:         ClanLib-1.0.0-libpng15.patch
Patch3:         ClanLib-1.0.0-gcc6.patch
Patch4:         ClanLib-1.0.0-NULL-not-defined.patch
Patch5:         ClanLib-1.0.0-use-pthread_mutexattr_settype.patch
Patch6:         ClanLib-1.0.0-gcc15.patch
BuildRequires:  make gcc-c++
BuildRequires:  libX11-devel libXi-devel libXmu-devel libGLU-devel libICE-devel
BuildRequires:  libXext-devel libXxf86vm-devel libXt-devel xorg-x11-proto-devel
BuildRequires:  libvorbis-devel mikmod-devel SDL-devel SDL_gfx-devel
BuildRequires:  alsa-lib-devel libpng-devel libjpeg-devel

%description
ClanLib is a cross platform C++ game library.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libGLU-devel xorg-x11-proto-devel pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -a 1 -n %{realname}-%{version}
iconv -f iso8859-1 -t utf8 NEWS > NEWS.utf8
touch -r NEWS.utf8 NEWS
mv NEWS.utf8 NEWS
iconv -f iso8859-1 -t utf8 CREDITS > CREDITS.utf8
touch -r CREDITS.utf8 CREDITS
mv CREDITS.utf8 CREDITS
# fixup pc files
sed -i 's|libdir=${exec_prefix}/lib|libdir=@libdir@|' pkgconfig/clan*.pc.in
sed -i 's|Libs:   -L${libdir}|Libs:   -L${libdir}/%{realname}-1.0|' \
  pkgconfig/clan*.pc.in


%build
%configure --disable-dependency-tracking --disable-static --enable-dyn \
  --disable-docs
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
# put .so links in a subdir of %%{libdir} so they don't conflict with
# ClanLib06-devel .so links. The pkg-config files are patches to transparently
# handle this for applications using us.
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{realname}-1.0
mv $RPM_BUILD_ROOT%{_libdir}/*.so $RPM_BUILD_ROOT%{_libdir}/%{realname}-1.0
for i in $RPM_BUILD_ROOT%{_libdir}/%{realname}-1.0/*; do
  ln -sf ../`readlink $i` $i
done
# we're API compatible with 0.8, add 0.8 pkgconfig symlinks, so 0.8
# expecting sources can be build against us
for i in $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc; do
  ln -s `basename $i` `echo $i|sed 's/1\.0\.pc/0\.8\.pc/'`
done


%ldconfig_scriptlets


%files
%doc CREDITS NEWS TODO-RSN
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc README* html
%{_libdir}/%{realname}-1.0
%{_includedir}/%{realname}-1.0
%{_libdir}/pkgconfig/clan*.pc


%changelog
* Mon Feb  3 2025 Hans de Goede <hdegoede@redhat.com> - 1.0.0-46
- Fix FTBFS (rhbz#2336002, rhbz#2339440)
- Drop quite old "Obsoletes: ClanLib"
- Fix rpmlint warnings

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar  6 2022 Hans de Goede <hdegoede@redhat.com> - 1.0.0-37
- Stop using obsolete pthread_mutexattr_setkind_np, fixing FTBFS of dependend
  packages

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Hans de Goede <hdegoede@redhat.com> - 1.0.0-35
- Fix FTBFS (rhbz#1987352)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Hans de Goede <hdegoede@redhat.com> - 1.0.0-27
- Fix FTBFS (rhbz#1582760)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 02 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.0-22
- Fix FTBFS with gcc6

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-20
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 1.0.0-18
- Rebuild for new SDL_gfx

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.0.0-16
- Rebuild for new SDL_gfx

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.0.0-13
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.0.0-12
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 11 2011 Hans de Goede <hdegoede@redhat.com> - 1.0.0-8
- Fix building with new libpng

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0-7
- Rebuild for new libpng

* Fri Jul 15 2011 Hans de Goede <hdegoede@redhat.com> - 1.0.0-6
- Rebuild for new SDL_gfx

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  3 2009 Hans de Goede <hdegoede@redhat.com> 1.0.0-4
- Rename package from ClanLib to ClanLib1, so that the ClanLib package name
  can be used for the new 2.x series, without dropping ClanLib-1.x from
  the distro as most ClanLib packages still need 1.x to build / run

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
