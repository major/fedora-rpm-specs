Summary: A predictive text input system
Name: dasher
Version: 5.0.0
Release: 0.25.beta%{?dist}
License: GPL-2.0-or-later
URL: http://www.inference.phy.cam.ac.uk/dasher/
Source0: https://github.com/ipomoena/dasher/archive/DASHER_5_0_0_beta.tar.gz

# https://github.com/ipomoena/dasher/pull/97
Patch0: dasher-5.0.0-sys-stat.patch

# https://github.com/dasher-project/dasher/pull/169
Patch1: gnome-doc-utils-depr.patch

# https://gitlab.gnome.org/GNOME/dasher/-/merge_requests/3
Patch2: 0001-Remove-extern-C-warpper-around-atspi-glib-headers-in.patch

BuildRequires: at-spi2-core-devel
BuildRequires: desktop-file-utils
BuildRequires: expat-devel
BuildRequires: gcc gcc-c++
BuildRequires: libXtst-devel
BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: yelp-tools

BuildRequires: gnome-common
BuildRequires: automake autoconf libtool
BuildRequires: make


%description
Dasher is an information-efficient text-entry interface, driven by natural
continuous pointing gestures. Dasher is a competitive text-entry system
wherever a full-size keyboard cannot be used, e.g. when operating a computer
one-handed, by joystick, touchscreen, trackball, or mouse, when operating
a computer without hands (i.e. by head-mouse or by eyetracker), or on
palmtops or wearable computers.

%prep
%setup -q -n dasher-DASHER_5_0_0_beta
%autopatch -p1
echo "5.0.0" > .tarball-version
rm  m4/glib-gettext.m4
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-japanese

make %{?_smp_mflags}

%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/dasher.desktop

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%doc AUTHORS README NEWS
%license COPYING
%{_bindir}/dasher
%{_datadir}/applications/dasher.desktop
%{_datadir}/dasher
%{_datadir}/icons/hicolor/*/apps/dasher.*

%{_mandir}/*/dasher.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.25.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.24.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.23.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.22.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.21.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.20.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.19.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.18.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.17.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.16.beta
- Pick a FTBFS fix for recent glib changes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.15.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.14.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.13.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Yanko Kaneti <yaneti@declera.com> - 5.0.0-0.12.beta
- Port from gnome-doc-utils to yelp-tools
- Remove unused libwnck dependency

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.11.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.10.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Yanko Kaneti <yaneti@declera.com> - 5.0.0-0.9.beta
- BR: gcc gcc-c++ - https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.8.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.7.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.0-0.6.beta
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 19 2016 Yanko Kaneti <yaneti@declera.com> - 5.0.0-0.1.beta
- Move to the 5.0.0 pre-releases on github.
- Drop gsettings patches and schemas because it no longer uses gsettings

* Tue Feb  9 2016 Yanko Kaneti <yaneti@declera.com> - 4.11.0-5.20150716git13371a4
- Add patch for build with recent gcc

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-5.20150716git13371a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Yanko Kaneti <yaneti@declera.com> - 4.11.0-4.20150716git13371a4
- Remove defattr. Use license.
- Remove deprecated glib gettext m4 macros.

* Fri Jul 31 2015 Yanko Kaneti <yaneti@declera.com> 4.11.0-3.20150716git13371a4
- Translate CamelCase settings names to valid gsettings names.

* Thu Jul 16 2015 Yanko Kaneti <yaneti@declera.com> 4.11.0-2.20150716git13371a4
- Add fix for crash on main window button close

* Thu Jul 16 2015 Yanko Kaneti <yaneti@declera.com> 4.11.0-1.20150716git13371a4
- Move to a recent git snapshot to avoid old gnome tech.
- Disable japanese for now.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.10.1-16
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

- Parallel build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Yanko Kaneti <yaneti@declera.com> 4.10.1-11
- Autoreconf for now for aarch64. #925229
- Fix blank canvas on startup. GNOME #607775
- Fix url in about bax at least. #538333

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Kalev Lember <kalevlember@gmail.com> - 4.10.1-9
- Drop deps on gnome-speech, it's retired from rawhide

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Jon Ciesla <limburgher@gmail.com> - 4.10.1-7
- Fixed whitespace, license tag and category per merge review, BZ 225674.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 4.10.1-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Matthias Clasen <mclasen@redhat.com> - 4.10.1-1
- Update to 4.10.1

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 4.10.0-1
- Update to 4.10.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 4.9.0-3
- Improve %%summary and %%description

* Thu Oct  9 2008 Matthias Clasen <mclasen@redhat.com> - 4.9.0-2
- Save some space

* Fri Apr 25 2008 Matthias Clasen <mclasen@redhat.com> - 4.9.0-1
- Update to 4.9.0
- Build with --enable-japanese and --enable-chinese (#444131)

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 4.7.3-1
- Update to 4.7.3

* Tue Feb 19 2008 Matthias Clasen <mclasen@redhat.com> - 4.7.0-3
- Fix build with gcc 4.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.7.0-2
- Autorebuild for GCC 4.3

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 4.7.0-1
- Update to 4.7.0

* Mon Oct 15 2007 Matthias Clasen <mclasen@redhat.com> - 4.6.1-1
- Update to 4.6.1 (bug fixes)

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 4.6.0-1
- Update to 4.6.0

* Mon Aug  6 2007 Matthias Clasen <mclasen@redhat.com> - 4.5.2-2
- Update license field

* Mon Jul  9 2007 Matthias Clasen <mclasen@redhat.com> - 4.5.2-1
- Update to 4.5.2

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 4.5.1-1
- Update to 4.5.1

* Sun May 20 2007 Matthias Clasen <mclasen@redhat.com> - 4.5.0-1
- Update to 4.5.0

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 4.4.0-1
- Update to 4.4.0

* Wed Feb 28 2007 Matthias Clasen <mclasen@redhat.com> - 4.3.5-1
- Update to 4.3.5

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> - 4.3.4-1
- Update to 4.3.4

* Wed Dec 20 2006 Matthias Clasen <mclasen@redhat.com> - 4.3.3-1
- Update to 4.3.3

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 4.3.2-1
- Update to 4.3.2

* Tue Nov  7 2006 Matthias Clasen <mclasen@redhat.com> - 4.3.1-1
- Update to 4.3.1

* Sat Nov  4 2006 Matthias Clasen <mclasen@redhat.com> - 4.2.1-1
- Update to 4.2.1

* Sun Sep  3 2006 Matthias Clasen <mclasen@redhat.com> - 4.2.0-1.fc6
- Update to 4.2.0

* Sat Aug 26 2006 Karsten Hopp <karsten@redhat.com> - 4.1.10-2.fc6
- buildrequire intltool which was previously pulled in by scrollkeeper but
  dropped this requirement because of bz #203606

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 4.1.10-1.fc6
- Update to 4.1.10

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 4.1.9-1.fc6
- Update to 4.1.9

* Thu Aug  3 2006 Matthias Clasen <mclasen@redhat.com> - 4.1.8-1.fc6
- Update to 4.1.8

* Wed Jul 26 2006 John (J5) Palmieri <johnp@redhat.com> - 4.1.7-3.fc6
- Add dist tag and rebuild

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 4.1.7-2
- Rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4.1.7-1.1
- rebuild

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 4.1.7-1
- Update t0 4.1.7

* Mon Jun 12 2006 Matthias Clasen <mclasen@redhat.com> - 4.1.4-2
- Update to 4.1.4

* Thu Jun  8 2006 Matthias Clasen <mclasen@redhat.com> - 4.1.0-2
- Add missing BuildRequires

* Wed May 17 2006 Matthias Clasen <mclasen@redhat.com> - 4.1.0-1
- Update to 4.1.0

* Mon May 15 2006 John (J5) Palmieri <johnp@redhat.com> - 4.0.2-2.1
- bump and rebuild

* Tue Apr  4 2006 Matthias Clasen <mclasen@redhat.com> - 4.0.2-2
- Update to 4.0.2

* Mon Mar 13 2006 Ray Strode <rstrode@redhat.com> - 4.0.0-1
- Update to 4.0.0

* Sun Feb 26 2006 Matthias Clasen <mclasen@redhat.com> - 3.99.5-1
- Update to 3.99.5

* Fri Feb 24 2006 Matthias Clasen <mclasen@redhat.com> 3.99.4-3
- Prereq: scrollkeeper

* Mon Feb 20 2006 Karsten Hopp <karsten@redhat.de> 3.99.4-2
- BuildRequires: libXtst-devel

* Sun Feb 12 2006 Matthias Clasen <mclasen@redhat.com> - 3.99.4-1
- Update to 3.99.4

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.99.2-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.99.2-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Ray Strode <rstrode@redhat.com> 3.99.2-2
- make compile

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com>
- Update to 3.99.2

* Mon Jan 16 2006 Matthias Clasen <mclasen@redhat.com>
- Update to 3.99.1

* Sun Dec 11 2005 Matthias Clasen <mclasen@redhat.com>
- Add -Wl,--export-dynamic,
- Make compile with gcc 4.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 18 2005 Bill Nottingham <notting@redhat.com>
- fix references to /usr/X11R6

* Wed Sep  7 2005 Matthias Clasen <mclasen@redhat.com> 
- Update to 3.2.18

* Tue Aug 16 2005 Matthias Clasen <mclasen@redhat.com> 
- Rebuilt

* Wed Aug 10 2005 <mclasen@redhat.com> 3.2.15-3
- Rebuild

* Tue Jul 12 2005 <mclasen@redhat.com> 3.2.15-2
- Rebuild

* Mon Mar 14 2005 <mclasen@redhat.com> 3.2.15-1
- Update to 3.2.15
- Require a new enough libwnck

* Wed Mar  2 2005 <mclasen@redhat.com> 3.2.13-2
- Rebuilt with gcc4

* Fri Feb  4 2005 <mclasen@redhat.com> 3.2.13-1
- Update to 3.2.13

* Fri Jan 28 2005 <mclasen@redhat.com> 3.2.12-1
- Update to 3.2.12

* Wed Nov  3 2004  <jrb@redhat.com> - 3.2.11-5
- add BuildRequires, #134956

* Mon Oct  4 2004 GNOME <jrb@redhat.com> - 3.2.11-4
- install schemas file by hand

* Wed Sep 22 2004 Bill Nottingham <notting@redhat.com>
- fix typo (#133058)

* Tue Sep 14 2004 GNOME <jrb@redhat.com> - 3.2.11-3
- fix schemas file and crasher.

* Tue Aug 31 2004 Jonathan Blandford <jrb@redhat.com> 3.2.11-2
- add lib64 to search libs.

* Mon Aug 30 2004 Jonathan Blandford <jrb@redhat.com> 
- Initial build.


