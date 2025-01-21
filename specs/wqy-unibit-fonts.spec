# SPDX-License-Identifier: MIT

%global fontname wqy-unibit

BuildRequires:  make
BuildRequires:  bdftopcf
BuildRequires:  perl-interpreter

Version: 1.1.0
Release: 36%{?dist}
URL:     http://wenq.org/enindex.cgi

%global foundry           WQY
%global fontlicense       GPL-2.0-only WITH Font-exception-2.0
%global fontlicenses      COPYING
%global fontdocs          AUTHORS ChangeLog README

%global fontfamily        Unibit
%global fontsummary       WenQuanYi Unibit Bitmap Font
%global fonts             *.pcf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
The Wen Quan Yi Unibit is designed as a dual-width (16x16,16x8) 
bitmap font to provide the most complete international symbol 
coverage, serving as the system-wide fall-back font. This font 
has covered over 46000 Unicode code points in BMP.
It is intended to supersede the outdated GNU Unifont.
This font was created by merging the latest update of GNU 
Unifont [GPL] (by Roman Czyborra and David Starner et al., the 
font was last updated in 2004), WenQuanYi Bitmap Song [GPL] 
0.8.1 (by Qianqian Fang and WenQuanYi contributors) and 
Fixed-16x8 [public domain] bitmap fonts from X11 core fonts. 
The entire CJK Unified Ideographics (U4E00-U9FA5) and CJK Unified 
Ideographics Extension A(U3400-U4DB5) blocks were replaced by 
high-quality glyphs from China National Standard GB19966-2005 
(public domain). Near a thousand of non-CJK characters were improved by 
WenQuanYi contributors via their collaborative font editing website at
http://wenq.org/eindex.cgi?Unicode_Chart_EN

}

Source0:  http://downloads.sourceforge.net/wqy/wqy-unibit-bdf-%{version}-1.tar.gz
Patch0:   wqy-unibit-fixes-build.patch

%fontpkg

%prep
%autosetup -n %{fontname}


%build
make
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Peng Wu <pwu@redhat.com> - 1.1.0-32
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul  6 2015 Peng Wu <pwu@redhat.com> - 1.1.0-16
- Fixes rawhide build

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Peng Wu <pwu@redhat.com> - 1.1.0-11
- Fixes spec file

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Qianqian Fang <fangqq@gmail.com> 1.1.0-5
- use fontpackages macro

* Sun Sep 30 2007 Qianqian Fang <fangqq@gmail.com> 1.1.0-4
- more spec file clean up

* Thu Sep 27 2007 Qianqian Fang <fangqq@gmail.com> 1.1.0-3
- change install directory to /usr/share/fonts/wenquanyi-unibit/

* Tue Sep 25 2007 Qianqian Fang <fangqq@gmail.com> 1.1.0-2
- change install directory to /usr/share/fonts/wqy-unibit/

* Fri Sep 14 2007 Qianqian Fang <fangqq@gmail.com> 1.1.0-1
- add more than 80 new glyphs between 0xFF00-0xFFFD, totaling 46443 glyphs

* Tue Sep 11 2007 Qianqian Fang <fangqq@gmail.com> 1.0.0-3
- remove non-ascii character from README, update upstream tarball

* Tue Sep 11 2007 Qianqian Fang <fangqq@gmail.com> 1.0.0-2
- change package name from wqy-unibit to wqy-unibit-fonts
- follow the new guideline for F8, use font catalogue symlink (#252279)

* Sun Sep 9 2007 Qianqian Fang <fangqq@gmail.com> 1.0.0-1
- initial release of the font
- initial packaging for Fedora (#285561)
