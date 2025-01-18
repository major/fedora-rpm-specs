Name:           fgrun
Summary:        Graphical front-end for launching FlightGear flight simulator
Version:        2016.3.1
Release:        62%{?dist}
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://sourceforge.net/projects/fgrun
# git clone http://git.code.sf.net/p/flightgear/fgrun
# cd fgrun
# git archive --format=tar.bz2 -o fgrun-2016.3.1.tar.bz2 --prefix=fgrun-2016.3.1/ version/2016.3.1
Source0:        fgrun-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        README.Fedora
# The icon is licensed under the CC Attribution-Share Alike 3.0 license
# http://commons.wikimedia.org/wiki/File:Bt_plane.svg
Source10:       http://upload.wikimedia.org/wikipedia/commons/9/9c/Bt_plane.svg
Source11:       Bt_plane-16.png
Source12:       Bt_plane-32.png
Source13:       Bt_plane-48.png
Source14:       Bt_plane-64.png
Source15:       Bt_plane-128.png
Patch1:         0001-Build-fgrun-with-static-ui-libs.patch
Patch2:         0002-Fix-a-crash-when-setting-defaults.patch
Patch3:         0003-Default-settings-for-Fedora.patch
Patch4:         0004-Fix-reloadPath-logic.patch
Requires:       FlightGear, opengl-games-utils, hicolor-icon-theme
BuildRequires:  gcc-c++
BuildRequires:  SimGear-devel >= 2.6.0
BuildRequires:  fltk-devel fltk-fluid plib-devel 
BuildRequires:  sg3_utils-devel OpenSceneGraph-devel mesa-libEGL-devel
BuildRequires:  gettext boost-devel desktop-file-utils
BuildRequires:  cmake

%description 
FlightGear Launch Control is a graphical front-end for launching
FlightGear flight simulator

%prep 
%autosetup -p1
cp -a %{SOURCE2} .

%build 
CXXFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64"
%cmake \
    -DSIMGEAR_SHARED=ON

%cmake_build

%install 
%cmake_install
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/fgrun-wrapper
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/fltk/flightgear.org
install -m 0644 fgrun.prefs \
        $RPM_BUILD_ROOT%{_sysconfdir}/fltk/flightgear.org/fgrun.prefs
%find_lang %{name}

desktop-file-install                                    \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications   \
        %{SOURCE1}

# install icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

install -m 0644 %{SOURCE10} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -m 0644 %{SOURCE11} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 0644 %{SOURCE12} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 0644 %{SOURCE13} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m 0644 %{SOURCE14} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -m 0644 %{SOURCE15} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files  -f %{name}.lang
%doc NEWS AUTHORS README README.Fedora
%license COPYING
%dir %{_sysconfdir}/fltk
%dir %{_sysconfdir}/fltk/flightgear.org
%{_sysconfdir}/fltk/flightgear.org/fgrun.prefs
%{_bindir}/* 
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2016.3.1-61
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-57
- rebuild with newer SimGear

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 21 2023 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-55
- rebuild with newer SimGear

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-53
- rebuild with newer SimGear

* Wed Oct 26 2022 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-52
- rebuild with newer SimGear

* Mon Oct 03 2022 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-51
- rebuild with newer SimGear

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 31 2022 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-49
- rebuild with newer SimGear

* Fri Feb 04 2022 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-48
- rebuild with newer SimGear

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Sandro Mani <manisandro@gmail.com> - 2016.3.1-46
- Rebuild (OpenSceneGraph)

* Wed Sep 01 2021 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-45
- rebuild with newer SimGear

* Mon Jul 26 2021 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-44
- rebuild with newer SimGear

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-42
- rebuild with newer SimGear

* Tue Mar 30 2021 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-41
- rebuild with newer SimGear

* Mon Mar 22 2021 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-40
- rebuild with newer SimGear

* Tue Jan 26 2021 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-39
- rebuild with newer SimGear

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-37
- rebuild with newer SimGear

* Tue Dec 01 2020 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-36
- rebuild with newer SimGear

* Sun Nov 29 2020 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-35
- rebuild with newer SimGear

* Mon Nov 09 2020 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-34
- rebuild with newer SimGear

* Fri Oct 30 2020 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-33
- rebuild with newer SimGear

* Mon Jul 27 2020 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-32
- use latest cmake macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-30
- rebuild with newer SimGear

* Sat May 23 2020 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-29
- rebuild with newer SimGear

* Tue May 12 2020 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-28
- rebuild with newer SimGear

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 2019 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-26
- rebuild with newer SimGear

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-24
- rebuild with newer SimGear

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-22
- rebuild with newer SimGear

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-20
- rebuild with newer SimGear

* Thu May 24 2018 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-19
- rebuild with newer SimGear

* Sun Apr 08 2018 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-18
- rebuild with newer SimGear

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2016.3.1-16
- Remove obsolete scriptlets

* Thu Sep 21 2017 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-15
- rebuild with newer SimGear

* Thu Sep 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 2016.3.1-14
- Rebuild for OpenSceneGraph-3.4.1.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-11
- rebuild with newer SimGear

* Wed Apr 05 2017 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-10
- rebuild with newer SimGear

* Fri Mar 03 2017 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-9
- rebuild with newer SimGear

* Fri Feb 24 2017 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-8
- rebuild with newer SimGear

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 2016.3.1-6
- Rebuilt for Boost 1.63

* Fri Jan 06 2017 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-5
- rebuild with newer SimGear

* Tue Dec 06 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-4
- rebuild with newer SimGear

* Fri Nov 25 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-3
- rebuild with newer SimGear

* Mon Nov 21 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-2
- rebuild with newer SimGear

* Wed Sep 14 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-1
- new upstream release

* Thu May 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.2.1-1
- new upstream release

* Wed May 11 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.1.2-1
- new upstream release

* Fri Feb 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.1.1-1
- new upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3.gitc09f1f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 3.7.0-2.gitc09f1f7
- Rebuilt for Boost 1.60

* Sat Sep 12 2015 Fabrice Bellet <fabrice@bellet.info> - 3.7.0-1.gitc09f1f7
- update to 3.7.0

* Fri Sep 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-9
- Rebuild for OSG-3.4.0.

* Thu Sep 10 2015 Tom Callaway <spot@fedoraproject.org> - 3.4.0-8
- do it again for simgear 3.7.0

* Thu Sep 10 2015 Tom Callaway <spot@fedoraproject.org> - 3.4.0-7
- rebuild for simgear 3.6.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.4.0-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.4.0-4
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-2
- Rebuild for Gcc-5.0.1.
- Modernize spec.
- Add %%license.

* Sun Feb 22 2015 Fabrice Bellet <fabrice@bellet.info> - 3.4.0-1
- new upstream release

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 3.2.0-3
- rebuild (fltk)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.2.0-2
- Rebuild for boost 1.57.0

* Fri Oct 17 2014 Fabrice Bellet <fabrice@bellet.info> - 3.2.0-1
- new upstream release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.0-4
- Rebuilt for OSG-3.2.1.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 3.0.0-2
- Rebuild for boost 1.55.0

* Fri Feb 21 2014 Fabrice Bellet <fabrice@bellet.info> - 3.0.0-1
- new upstream release

* Wed Dec 11 2013 Fabrice Bellet <fabrice@bellet.info> - 1.7.0-2
- Prevent build failure with -Werror=format-security (bug #1037061).

* Sun Sep 22 2013 Fabrice Bellet <fabrice@bellet.info> - 1.7.0-1
- new upstream release

* Thu Aug 15 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.6.2-8
- Rebuilt for OSG-3.2.0.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.6.2-6
- Rebuild for boost 1.54.0

* Wed Mar 13 2013 Fabrice Bellet <fabrice@bellet.info> - 1.6.2-5
- libpthread link patch is no longer needed (rh#918003)

* Wed Mar 06 2013 Fabrice Bellet <fabrice@bellet.info> - 1.6.2-4
- add libpthread to link fgrun

* Mon Feb 18 2013 Fabrice Bellet <fabrice@bellet.info> - 1.6.2-3
- rebuilt with newer SimGear

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 11 2012 Fabrice Bellet <fabrice@bellet.info> 1.6.2-1
- new upstream release

* Tue Jul 24 2012 Fabrice Bellet <fabrice@bellet.info> 1.6.1-4
- upstream patch r665 implements system-wide settings

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Fabrice Bellet <fabrice@bellet.info> 1.6.1-2
- define default settings for Fedora
- fix a crash when resetting default values
- add a README.Fedora to quickly explain the initial setup
  with terrasync

* Tue Feb 28 2012 Fabrice Bellet <fabrice@bellet.info> 1.6.1-1
- new upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-0.2.svn20110905
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 05 2011 Fabrice Bellet <fabrice@bellet.info> 1.6.0-0.1
- new snapshot

* Tue Jun 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 1.5.2-8
- Rebuild against OSG-2.8.5.

* Fri May 27 2011 Fabrice Bellet <fabrice@bellet.info> 1.5.2-7
- rebuilt for newer fltk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Fabrice Bellet <fabrice@bellet.info> 1.5.2-5
- add a requires hicolor-icon-theme
- fix the icon cache scriptlets
- fix the .desktop file
- fix the %%defattr macro

* Sun Mar 14 2010 Fabrice Bellet <fabrice@bellet.info> 1.5.2-4
- rebuild with -D_FILE_OFFSET_BITS=64

* Fri Mar 12 2010 Fabrice Bellet <fabrice@bellet.info> 1.5.2-3
- add an icon

* Mon Mar 01 2010 Fabrice Bellet <fabrice@bellet.info> 1.5.2-2
- fix a BuildRequires for a recent version of SimGear

* Fri Feb 26 2010 Fabrice Bellet <fabrice@bellet.info> 1.5.2-1
- new upstream release
- use scandir() instead of fl_filename_list() to browse airports files

* Tue Jan 27 2009 Pankaj Pandey <pankaj86@gmail.com> 1.5.1-1
- Created this spec file
