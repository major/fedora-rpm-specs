%global ISONAME KOI8-R
%global catalogue %{_sysconfdir}/X11/fontpath.d

Name:          fonts-%{ISONAME}
Version:       1.0
Release:       36%{?dist}
Summary:       Russian and Ukrainian language fonts for the X Window System
License:       MIT
#URL:          <none yet>
Source:        http://www.inp.nsk.su/~bolkhov/files/fonts/cyr-rfx/srctgz/cyr-rfx-koi8-ub-1.1.bdfs.tar.bz2
Source1:       Makefile.cyrfonts
Source2:       ftp://ftp.ksi-linux.com/pub/patches/ksi-XFree86-cyrillic-fonts.tar.bz2
Patch:         koi8-ub-bcl.patch
BuildRequires: mkfontdir, bdftopcf
BuildRequires: make
BuildArch:     noarch
Provides:      XFree86-KOI8-R
 
%description
If you use the X Window System and you want to display Russian and
Ukrainian fonts, you should install this package.

This package contains a full set of Russian and Ukrainian fonts, in
compliance with the KOI8-R standard. The fonts included in
this package are distributed free of charge and can be used
freely, subject to the accompanying license.


%package 75dpi
Summary: A set of 75 dpi Russian and Ukrainian language fonts for X
Provides:      XFree86-KOI8-R-75dpi-fonts

%description 75dpi
This package contains a set of Russian and Ukrainian language fonts
at 75 dpi resolution for the X Window System.

If you are installing the X Window System and you need to display
Russian and Ukrainian language characters in 75 dpi resolution, you should
install this package.

%package 100dpi
Summary: KOI8-R fonts in 100 dpi resolution for the X Window System
Provides:      XFree86-KOI8-R-100dpi-fonts

%description 100dpi
This package contains a set of Russian and Ukrainian language fonts
at 100 dpi resolution for the X Window System.

If you are installing the X Window System and you need to display
Russian and Ukrainian language characters in 100 dpi resolution, you should
install this package.

%prep
%setup -q -n koi8-ub -a 2
cp -a Cyrillic/100dpi ./
cp %{SOURCE1} ./Makefile
%patch -p1

pushd doc
iconv -f iso8859-1 -t utf-8 INSTALL.ru.txt > INSTALL.ru.txt.conv \
&& mv INSTALL.ru.txt.conv INSTALL.ru.txt

chmod 644 *.pl
popd

%build
make all

%install
DSTFONT=$RPM_BUILD_ROOT%{_datadir}/fonts/%{ISONAME}
make install PREFIX=$RPM_BUILD_ROOT \
 FONTDIR=$DSTFONT
mkdir -p $RPM_BUILD_ROOT%{catalogue}
ln -sf %{_datadir}/fonts/%{ISONAME}/misc $RPM_BUILD_ROOT%{catalogue}/%{ISONAME}-misc
ln -sf %{_datadir}/fonts/%{ISONAME}/75dpi $RPM_BUILD_ROOT%{catalogue}/%{ISONAME}-75dpi
ln -sf %{_datadir}/fonts/%{ISONAME}/100dpi $RPM_BUILD_ROOT%{catalogue}/%{ISONAME}-100dpi

%files
%doc doc  Cyrillic/COPYRIGHT
%dir %{_datadir}/fonts/%{ISONAME}
%{catalogue}/%{ISONAME}-misc
%{_datadir}/fonts/%{ISONAME}/misc

%files 75dpi
%{catalogue}/%{ISONAME}-75dpi
%{_datadir}/fonts/%{ISONAME}/75dpi

%files 100dpi
%{catalogue}/%{ISONAME}-100dpi
%{_datadir}/fonts/%{ISONAME}/100dpi

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0-21
- Fix rpmlint warnings file-not-utf8 and doc-file-depdendency
- Re-align the spec file lines
- Fix rpmlint warning of self-obsoletion
- Fix summary
- Use rpm macros
- remove %%clean and buildroot removal from %%install, optional now
- defattr, Group tag, buildroot tag are optional now

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0-18
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Jens Petersen <petersen@redhat.com> - 1.0-13
- rebuild for fonts.dir listing missing .bdf files (#466029)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 21 2007 Karsten Hopp <karsten@redhat.com> 1.0-10
- remove chkfontpath dependency (#252271)
- fix URL, fix buildroot

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0-9.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 07 2005 Caolan McNamara <caolanm@redhat.com> 1.0-9

* Thu Jul 07 2005 Karsten Hopp <karsten@redhat.de> 1.0-8
- BuildRequires xorg-x11-font-utils for bdftopcf and mkfontdir

* Tue Sep 21 2004 Than Ngo <than@redhat.com> 1.0-7
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.0-4
- rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Feb 26 2002 Mike A. Harris <mharris@redhat.com> 1.0-1
- Renamed package from XFree86-KOI8-R to fonts-KOI8-R since this is not part
  of XFree86, nor released by XFree86.org, and should not be named as such,
  as it causes confusion.
- Updated package descriptions to be fitting for the times.
- Removed bogus dependancy on XFree86 as X shouldn't be required just to
  install fonts.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 28 2001 Than Ngo <than@redhat.com>
- fixed incorect LANG (Bug #33250)

* Mon Dec 11 2000 Than Ngo <than@redhat.com>
- rebuilt with the fixed fileutils

* Thu Nov 16 2000 Than Ngo <than@redhat.com>
- add missing Prereq on /usr/sbin/chkfontpath

* Sun Sep  3 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- fix several typos with wrong directories in scripts

* Thu Jul 20 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix %%defattr in the wrong place in the files list

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- adopted for Winston. 
