#global extra_version -2

Name:           cdogs-sdl
Version:        0.7.3
Release:        14%{?dist}
Summary:        C-Dogs is an arcade shoot-em-up
# The game-engine is GPLv2+
# The game art is CC
# Automatically converted from old format: GPLv2+ and CC-BY and CC-BY-SA and CC0 - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-CC-BY-SA AND CC0-1.0
URL:            http://cxong.github.io/cdogs-sdl/
Source0:        https://github.com/cxong/cdogs-sdl/archive/%{version}%{?extra_version}.tar.gz#/%{name}-%{version}%{?extra_version}.tar.gz
Patch0:         cdogs-sdl-0.5.8-cmake.patch
Patch1:         cdogs-sdl-0.7.3-fcommon-fix.patch
BuildRequires:  gcc
BuildRequires:  cmake SDL2_mixer-devel SDL2_image-devel libGL-devel
BuildRequires:  ncurses-devel physfs-devel enet-devel
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme
Obsoletes:      cdogs-data < 0.5
Provides:       cdogs-data = %{version}-%{release}

%description
C-Dogs SDL is a port of the old DOS arcade game C-Dogs to modern operating
systems utilizing the SDL Media Libraries. C-Dogs is an arcade shoot-em-up
which lets players work alone and cooperatively during missions or fight
against each other in the “dogfight” death-match mode. The DOS version of
C-Dogs came with several built in missions and dogfight maps. This version
does too. The author of the DOS version of C-Dogs was Ronny Wester. We would
like to thank Ronny for releasing the C-Dogs sources to the public.


%prep
%autosetup -p1 -n %{name}-%{version}%{?extra_version}
# We use the system enet
rm -r src/cdogs/enet
# Misc. cleanups
sed -i 's/\r//' doc/original_readme.txt
find graphics sounds -name "*.sh" -delete


%build
%cmake -DCDOGS_DATA_DIR=/usr/share/cdogs-sdl/ -DUSE_SHARED_ENET=1
%cmake_build


%install
%cmake_install


%check
desktop-file-validate \
  $RPM_BUILD_ROOT%{_datadir}/applications/io.github.cxong.%{name}.desktop
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/io.github.cxong.%{name}.appdata.xml


%files
%doc doc/AUTHORS doc/CREDITS doc/original_readme.txt doc/README_DATA.md
%license doc/COPYING.BSD doc/COPYING.GPL doc/COPYING.MJSON.txt doc/COPYING.xgetopt.txt doc/COPYING.yajl.txt doc/LICENSE.nanopb.txt doc/license.rlutil.txt
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/appdata/io.github.cxong.%{name}.appdata.xml
%{_datadir}/applications/io.github.cxong.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.cxong.%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.3-13
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Hans de Goede <hdegoede@redhat.com> - 0.7.3-1
- New upstream release 0.7.3 (rhbz#1692052)
- Fix FTBFS (rhbz#1799213)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.5-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May  1 2017 Hans de Goede <hdegoede@redhat.com> - 0.6.5-1
- New upstream release 0.6.5

* Mon Mar 13 2017 Hans de Goede <hdegoede@redhat.com> - 0.6.4-1
- New upstream release 0.6.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Hans de Goede <hdegoede@redhat.com> - 0.6.3-1
- New upstream release 0.6.3 (rhbz#1403457)

* Fri Aug 12 2016 Hans de Goede <hdegoede@redhat.com> - 0.6.2-1
- New upstream release 0.6.2
- The "Redistributable, no modification permitted" assets have been
  relicensed under CC-BY

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Hans de Goede <hdegoede@redhat.com> - 0.5.8-3
- Fix crash due to missing /usr/share/cdogs-sdl/cdogs_icon.bmp (rhbz#1296890)

* Fri Jun 19 2015 Hans de Goede <hdegoede@redhat.com> - 0.5.8-2
- Add Keywords field to .desktop file

* Thu Jun 18 2015 Hans de Goede <hdegoede@redhat.com> - 0.5.8-1
- New upstream and new upstream release 0.5.8
- Fix FTBFS
- Add an appdata file
- cdogs-data is now part of the main cdogs-sdl package

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.4-11
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-3
- Rebuild for buildId

* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-2
- Update License tag for new Licensing Guidelines compliance
- Fix building with new glibc open() argument checking

* Mon Jul 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-1
- Initial Fedora Extras package
