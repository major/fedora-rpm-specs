Name:           koverartist
Version:        0.7.6
Release:        32%{?dist}
Summary:        Create CD/DVD covers
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.kde-apps.org/content/show.php?content=38195
Source0:        http://kde-apps.org/CONTENT/content-files/38195-%{name}_%{version}.orig.tar.bz2
Patch0:         koverartist-0.7.6-gcc47.patch
BuildRequires:  kdelibs4-devel gettext desktop-file-utils cmake

# Required by configure
BuildRequires:  /usr/bin/perl perl(Getopt::Long)
BuildRequires: make

%description
KoverArtist is a program for the fast creation of covers for
cd/dvd cases and boxes. The main idea behind it is to be able
to create decent looking covers with some mouseclicks.

%prep
%setup -q
%patch -P0 -p1 -b .gcc47

%build
%configure --disable-rpath
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/kde4/%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/koverartist
%{_datadir}/icons/hicolor/*/apps/koverartist.png
%{_datadir}/applications/kde4/koverartist.desktop
%{_datadir}/kde4/apps/%{name}/
%{_datadir}/mime/packages/mime-types/x-koa*.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.6-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.6-15
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.7.6-12
- Add BR: /usr/bin/perl, perl(Getopt::Long)
  (Fix F26FTBFS, RHBZ#1423821).
- Add %%license.
- Fix bogus %%changelog dates.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.6-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 0.7.6-7
- update scriptlets, BR: kdelibs4-devel

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Tom Callaway <spot@fedoraproject.org> 0.7.6-1
- update to 0.7.6

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-16
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Sebastian Vahl <fedora@deadbabylon.de> 0.5-11
- added patch to compile with gcc-4.3

* Sat Feb 09 2008 Sebastian Vahl <fedora@deadbabylon.de> 0.5-10
- rebuild for new gcc-4.3

* Sun Dec 02 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-9
- BR: kdelibs3-devel (instead of kdelibs-devel)
- make sure qt-devel would be found

* Thu Aug 16 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-8
- Change License to GPLv2+

* Thu Apr 12 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-7
- changed vendor and use /usr/share/applications/kde

* Wed Apr 11 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-6
- run gtk-update-icon-cache on post and postun
- run update-desktop-database on post and postun
- added BR: desktop-file-utils

* Thu Jan 18 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-5
- some cleanup in description
- dropped X-Fedora in desktop-file-install

* Wed Jan 17 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-4
- Use find_lang macro

* Wed Jan 17 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-3
- use desktop-file-install
- BR: desktop-file-utils
- changed rpm-group to Applications/Publishing

* Fri Dec 01 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-2
- BR: gettext

* Wed Nov 01 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-1
- New upstream version: 0.5

* Wed Oct 25 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.4.3-2
- Rebuild for FC6

* Wed Jul 26 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.4.3-1
- New upstream version: 0.4.3

* Fri Jun 16 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.4-1
- New upstream version: 0.4

* Wed May 03 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.3.6-1
- New upstream version: 0.3.3

* Fri Apr 28 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.3.3-1
- New upstream version: 0.3.3

* Thu Apr 27 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.3.2-1
- New upstream version: 0.3.2

* Mon Apr 24 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.3.1-1
- Initial RPM Release
