
Summary:	Graphical client for Firebird
Name:		flamerobin
Version:	0.9.9
Release:	6%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
Source0:	https://github.com/mariuz/%{name}/archive/%{name}-%{version}.tar.gz
URL:		http://www.flamerobin.org/
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	firebird-devel >= 2.0.0.12748
BuildRequires:	wxGTK-devel >= 3.0
BuildRequires:	desktop-file-utils
BuildRequires:	boost-devel
BuildRequires:	libicns-utils
BuildRequires:	cmake

%description
FlameRobin is a database administration tool for Firebird DBMS based on wxgtk
toolkit.

%prep
%autosetup -p1

%build
# FIX A TRAILING SEMICOLON ISSUE FOR KEYWORDS TAG IN .desktop FILE
sed -i "s/^Keywords=firebird/Keywords=firebird;/" res/%{name}.desktop
%cmake
%cmake_build

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/%{name}/docs

# INSTALL HICOLOR ICONS EXTRACTED FROM ICNS FILE
pushd res
icns2png -x -d 32 flamerobin.icns
for sz in 16 32 48 128
do
  install -Dm0644 flamerobin_${sz}x${sz}x32.png %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/%{name}.png
done
popd
rm %{buildroot}%{_datadir}/pixmaps/*.png

%files
%doc docs/*
%{_mandir}/man1/flamerobin.1*
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.9-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 11 2023  Philippe Makowski <makowski@fedoraproject.org> 0.9.9-1
- New upstream (#2242257)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.9.3.1-25
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 0.9.3.1-23
- Rebuild with wxWidgets 3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.9.3.1-21
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 24 2021 Philippe Makowski <makowski@fedoraproject.org> - 0.9.3.1-19
- build under s390x (bz 1969393 and 1987475)

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.3.1-18
- Rebuilt for Boost 1.76

* Mon Aug 02 2021 Philippe Makowski <makowski@fedoraproject.org> - 0.9.3.1-17
- Firebird 4 have build issues under s390x (bz 1969393)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.3.1-15
- Rebuilt for Boost 1.75

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.9.3.1-13
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.9.3.1-9
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.9.3.1-6
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.3.1-3
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Apr 04 2017  Philippe Makowski <makowski@fedoraproject.org> 0.9.3.1-1
- New upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-18.20130401snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.3-17.20130401snap
- Rebuilt for Boost 1.63

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 0.9.3-16.20130401snap
- Rebuilt for linker errors in boost (#1331983)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-15.20130401snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.9.3-14.20130401snap
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.9.3-13.20130401snap
- Rebuilt for Boost 1.59

* Mon Jul 27 2015 Adam Williamson <awilliam@redhat.com> - 0.9.3-12.20130401snap
- rediff configure-gcc5.patch for Fedora, add comment linking to upstream bug

* Fri Jul 24 2015 Philippe Makowski <makowski@fedoraproject.org>
- patch build for Boost 1.58

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.9.3-11.20130401snap
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-10.20130401snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.9.3-9.20130401snap
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-8.20130401snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-7.20130401snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.9.3-6.20130401snap
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.9.3-5.20130401snap
- rebuild for boost 1.55.0

* Thu Aug 08 2013 Philippe Makowski <makowski@fedoraproject.org>  0.9.3-4.20130401snap
- Prune unnecessary content from tarball  (bug #981900)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3.20130401snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.9.3-2.20130401snap
- Rebuild for boost 1.54.0

* Mon Apr 01 2013  Philippe Makowski <makowski@fedoraproject.org> 0.9.3-1
- Fix failed build for aarch64
- New upstream

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 11 2011  Philippe Makowski <makowski@fedoraproject.org> 0.9.2-4
- Fix failed build for Fedora 15

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.9.2-2
- rebuilt against wxGTK-2.8.11-2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild


* Sun Apr 12 2009  Philippe Makowski <makowski at firebird-fr.eu.org> 0.9.2-0
- First Fedora build
- New upstream: 0.9.2

* Tue Mar 24 2009 Philippe Makowski <makowski@firebird-fr.eu.org> 0.9.0-1
- Update to 0.9.0
- First mipsel build

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8.3-3mdv2009.0
+ Revision: 245195
- rebuild

* Thu Jan 31 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.8.3-1mdv2008.1
+ Revision: 160873
- New upstream: 0.8.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 18 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.8.1-1mdv2008.1
+ Revision: 99959
- Fix configure permission.
- New upstream: 0.8.1
- New upstream: 0.8.0

* Tue May 15 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.6-3mdv2008.0
+ Revision: 26964
- Rebuilt against new wx stuff.


* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 0.7.6-2mdv2007.0
+ Revision: 100700
- rebuild

* Mon Nov 27 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.6-1mdv2007.1
+ Revision: 87367
- New upstream: 0.7.6
- Added menu icon.

* Thu Nov 16 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.5-5mdv2007.1
+ Revision: 84903
- Added BuildRequires for ImageMagick: due to convert usage.
- Rebuilt against firebird 2.0 final.

* Thu Sep 07 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.5-4mdv2007.0
+ Revision: 60258
- New upstream: 0.7.5

* Wed Sep 06 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.2-4mdv2007.0
+ Revision: 59989
- Removed old-style menu entry. The new one (.desktop) will be added later.
- Import flamerobin

* Sat Sep 02 2006 Marcelo Ricardo Leitner <mrl@mandriva.com>
- Fixed BuildRequires.
- Removed hardcoded buildrequires to libraries: they should be automatic.
- Enhanced package description.

* Thu Aug 24 2006 Philippe Makowski <makowski@firebird-fr.eu.org> 
- change Requires to libfirebird2

* Thu Aug 17 2006 Philippe Makowski <makowski@firebird-fr.eu.org> 
- initial release

