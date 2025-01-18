Name:           asc
Version:        2.8.0.2
Release:        26%{?dist}
Summary:        Advanced Strategic Command
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.asc-hq.org/
Source0:        http://terdon.asc-hq.org/asc/builds/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         asc-2.8.0.2-gcc-10.patch
Patch1:         asc-2.8.0.2-gcc-11.patch
BuildRequires:  SDL_image-devel SDL_mixer-devel SDL_sound-devel
BuildRequires:  bzip2-devel libjpeg-devel libsigc++20-devel physfs-devel
BuildRequires:  libvorbis-devel libpng-devel libtiff-devel boost-devel
BuildRequires:  freetype-devel expat-devel lua-devel wxGTK-devel libcurl-devel
BuildRequires:  make gcc gcc-c++ libtool desktop-file-utils zip
Requires:       hicolor-icon-theme

%description
ASC is a free, turn based strategy game.


%prep
#bug in upstream tarbal, contains 2.8.0.1 dir instead of 2.8.0.2
%autosetup -p1 -n asc-2.8.0.1
autoreconf -ivf
sed -i 's|$datadir/games/|$datadir/|g' configure
sed -i 's|$(datadir)/games/|$(datadir)/|g' `find -name Makefile.in`
chmod -x source/libs/paragui/include/paragui.h source/unitcostcalculator-pbp.cpp


%build
export CXXFLAGS="$RPM_OPT_FLAGS -std=c++11 -D__EXPORT__="
%configure --enable-genparse --disable-paraguitest
make %{?_smp_mflags}


%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 data/icons/program-icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps


%files
%doc README AUTHORS
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/appdata
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}*.6.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.8.0.2-25
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 2.8.0.2-21
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 2.8.0.2-18
- Rebuild with wxWidgets 3.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 2.8.0.2-15
- Rebuilt for Boost 1.76

* Thu Jul 29 2021 Hans de Goede <hdegoede@redhat.com> - 2.8.0.2-14
- Fix FTBFS (rhbz#1987374)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.8.0.2-11
- Rebuilt for Boost 1.75

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 2.8.0.2-9
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Hans de Goede <hdegoede@redhat.com> - 2.8.0.2-7
- Add patch from gcc team for compilation with the upcoming gcc-10 release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 2.8.0.2-4
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Scott Talbert <swt@techie.net> - 2.8.0.2-2
- Rebuild against wxWidgets 3.0

* Tue Feb 27 2018 Hans de Goede <hdegoede@redhat.com> - 2.8.0.2-1
- New upstream version 2.8.0.2 (rhbz#1543419)
  * Fixed crash on 32 bit system when more than 32 terrain bits
    were defined
  * Add safety checks for graphics allocation errors of big maps
  * Prevent duplicate objects from being shown on object
    construction/removal
  * New unit cost formula for PBP
  * New terrain type: Concrete
  * Fixed some crashes

* Wed Feb 07 2018 Hans de Goede <hdegoede@redhat.com> - 2.6.1.0-13
- Fix FTBFS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.1.0-11
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 2.6.1.0-8
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.6.1.0-7
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.6.1.0-5
- Rebuilt for Boost 1.63

* Mon May 16 2016 Jonathan Wakely <jwakely@redhat.com> - 2.6.1.0-4
- Rebuilt for linker errors in boost (#1331983)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 2.6.1.0-2
- Rebuilt for Boost 1.60

* Thu Dec 10 2015 Hans de Goede <hdegoede@redhat.com> - 2.6.1.0-1
- New upstream version 2.6.1.0 (rhbz#1288897)

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.6.0.0-12
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.6.0.0-10
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.6.0.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.6.0.0-7
- Rebuild for boost 1.57.0

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 2.6.0.0-6
- rebuild for new lua

* Mon Oct 27 2014 Hans de Goede <hdegoede@redhat.com> - 2.6.0.0-5
- Add a larger icon (rhbz#1157515)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.6.0.0-2
- Rebuild for boost 1.55.0

* Sat Mar 08 2014 Hans de Goede <hdegoede@redhat.com> - 2.6.0.0-1
- New upstream version 2.6.0.0 (rhbz#1047182)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 2.5.0.0-5
- Rebuild for boost 1.54.0

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 2.5.0.0-4
- fix for lua 5.2

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 2.5.0.0-3
- Cleanup .desktop file to match current standards

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 2.5.0.0-2
- Remove no longer needed autoreconf call, %%configure from redhat-rpm-config
  >= 9.1.0-42 updates config.guess and config.sub for new architecture support

* Sat Mar 23 2013 Hans de Goede <hdegoede@redhat.com> - 2.5.0.0-1
- New upstream version 2.5.0.0 (rhbz#827946)
- Run autoreconf for aarch64 support (rhbz#925030)

* Sun Feb 10 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.4.0.0-13
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2.4.0.0-12
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2.4.0.0-11
- Rebuild for Boost-1.53.0

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.4.0.0-10
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.4.0.0-9
- rebuild against new libjpeg

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 2.4.0.0-8
- Rebuild for new boost

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0.0-6
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Hans de Goede <hdegoede@redhat.com> - 2.4.0.0-5
- Fix building with gcc-4.7

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Tom Callaway <spot@fedoraproject.org> - 2.4.0.0-3
- rebuild for physfs2

* Sat Nov 26 2011 Hans de Goede <hdegoede@redhat.com> - 2.4.0.0-2
- Rebuild for new boost

* Sat Jul 23 2011 Hans de Goede <hdegoede@redhat.com> - 2.4.0.0-1
- New upstream version 2.4.0.0
- Rebuild for new boost

* Thu Apr 07 2011 Hans de Goede <hdegoede@redhat.com> - 2.2.0.0-11
- Rebuild for new boost

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 29 2010 Bill Nottingham <notting@redhat.com> - 2.2.0.0-9
- Rebuild for Boost soname bump

* Tue Jul 27 2010 Bill Nottingham <notting@redhat.com> - 2.2.0.0-8
- Rebuild for Boost soname bump

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 2.2.0.0-7
- Rebuild for Boost soname bump

* Thu Aug 20 2009 Warren Togami <wtogami@redhat.com> - 2.2.0.0-6
- rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Hans de Goede <hdegoede@redhat.com> 2.2.0.0-4
- Rebuild for new boost

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Petr Machata <pmachata@redhat.com> - 2.2.0.0-2
- Rebuild for new boost

* Mon Dec 15 2008 Hans de Goede <hdegoede@redhat.com> 2.2.0.0-1
- New upstream version 2.2.0.0

* Sun Aug 17 2008 Hans de Goede <jwrdegoede@fedoraproject.org> 2.1.0.0-2
- Rebuild for new boost

* Mon Apr 14 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.1.0.0-1
- New upstream version 2.1.0.0

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.1.0-3
- Autorebuild for GCC 4.3

* Sat Jan 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.1.0-2
- Fix compilation with gcc-4.3

* Sun Oct 28 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.1.0-1
- New upstream version 2.0.1.0
- Use included (patched/bugfixed) paragui copy
- Use included (patched/bugfixed) SDLmm copy

* Tue Aug 28 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.16.4.0-3
- Rebuild for new expat 2.0

* Sun Aug  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.16.4.0-2
- Update License tag for new Licensing Guidelines compliance

* Mon Mar 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.16.4.0-1
- Initial Fedora Extras package based on specfile by Che (newrpms)
