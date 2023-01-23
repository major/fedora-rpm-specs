Name: ttf2pt1
Version: 3.4.4
Release: 36%{?dist}
Summary: TrueType to Adobe Type 1 font converter
Summary(sv): Konverterare från TrueType till Adobe Type 1

License: GPLv2+ and BSD with advertising
URL: http://%name.sourceforge.net
Source: http://download.sourceforge.net/%name/%name-%version.tgz
Patch0: ttf2pt1-destdir.patch
Patch1: ttf2pt1-freetype.patch
Patch2: ttf2pt1-sed.patch
Patch3: ttf2pt1-doc.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: freetype-devel >= 2.0.3
BuildRequires: perl-generators
BuildRequires: perl-podlators
BuildRequires: fakeroot
BuildRequires: t1lib-devel

Requires: t1utils

%description
Ttf2pt1 is a font converter from the True Type format (and some other formats
supported by the FreeType library as well) to the Adobe Type1 format.

%description -l sv
Ttf2pt1 är en konverterare för typsnitt från formatet True Type (och
några andra format som stödjs av biblioteket FreeType) till formatet
Adobe Type 1.


%prep
%setup -q
%patch0
%patch1
%patch2
%patch3


%build
make CFLAGS_SYS='%optflags -D_GNU_SOURCE' CFLAGS_FT="-DUSE_FREETYPE `pkg-config --cflags freetype2`" LIBS_FT="`pkg-config --libs freetype2`" VERSION=%version all
rm -rf __dist_other
mkdir -p __dist_other/other
cp -p other/bz* other/Makefile other/README* __dist_other/other
make -C other cmpf dmpf

%install
# The installation does explicit chown to root and chgrp to bin.
# Use fakeroot to avoid getting errors in the build.  RPM will
# make sure the ownership is correct in the final package.
fakeroot make DESTDIR=%buildroot INSTDIR=%_prefix TXTFILES= MANDIR=%_mandir VERSION=%version install
# Use the system t1asm from t1utils instead of a local version.
rm -r %buildroot/%_libexecdir
# Remove scripts only used during build
rm %buildroot%_datadir/%name/scripts/{convert,convert.cfg.sample,frommap,html2man,inst_dir,inst_file,mkrel,unhtml}
# Put tools in the standard path
mv %buildroot/%_datadir/%name/other/cmpf %buildroot/%_bindir/%{name}_cmpf
mv %buildroot/%_datadir/%name/other/dmpf %buildroot/%_bindir/%{name}_dmpf
cp other/cntstems.pl %buildroot/%_bindir/%{name}_cntstems
cp other/lst.pl %buildroot/%_bindir/%{name}_lst
cp other/showdf %buildroot/%_bindir/%{name}_showdf
cp other/showg %buildroot/%_bindir/%{name}_showg


%files
%doc CHANGES* README* FONTS FONTS.html COPYRIGHT app/TeX __dist_other/other
%doc scripts/convert.cfg.sample
%_bindir/%{name}*
%_datadir/%name
%exclude %_datadir/%name/app
%exclude %_datadir/%name/other
%_mandir/man1/*


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Göran Uddeborg <goeran@uddeborg.se> - 3.4.4-26
- Add an explicit build requirement on gcc.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.4.4-21
- Actually enable FreeType features (#1365659)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.4.4-15
- Perl 5.18 rebuild

* Mon Feb 18 2013 Göran Uddeborg <goeran@uddeborg.se> 3.4.2-14
- pod2man is now in the package perl-podlators.  Do buildrequire on
  that package rather than perl.
- Remove some obsolete sections like an explicit buildroot definition
  and clean section.
- Provide Swedish translation of the summary and description.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 18 2008 Göran Uddeborg <goeran@uddeborg.se> 3.4.4-7
- Don't build in parallel.  Two calls of scripts/html2man on
  FONTS.html could step on each other toes.

* Tue Oct 14 2008 Göran Uddeborg <goeran@uddeborg.se> 3.4.4-6
- Install cmpf and dmpf with a ttf2pt1 prefix.
- Install scripts from "other" directory in the standard path with a
  ttf2pt1_ prefix.
- Update documentation with the new names and paths of the scripts,
  and remove any references to obsolete code not included in the
  package.

* Tue Sep 30 2008 Göran Uddeborg <goeran@uddeborg.se> 3.4.4-5
- Several updates from review (BZ 462446 up to comment 11)

* Mon Sep 29 2008 Göran Uddeborg <goeran@uddeborg.se> 3.4.4-4
- Moved example code to /usr/share/doc. (review BZ 462446)
- Excluded unused patch code for old XFree86 versions.

* Tue Sep 16 2008 Göran Uddeborg <goeran@uddeborg.se> 3.4.4-3
- Removed Swedish translations for public package

* Tue Sep 16 2008 Göran Uddeborg <goeran@uddeborg.se> 3.4.4-2
- Repackaged according to Fedora packaging guidelines

* Sun Sep  5 2004 Göran Uddeborg <goeran@uddeborg.se> 3.4.4-1
- Upgraded to 3.4.4.

* Tue Oct  7 2003 Göran Uddeborg <goeran@uddeborg.se> 3.4.3-1
- Upgraded to 3.4.3.

* Tue Oct 15 2002 Göran Uddeborg <goeran@uddeborg.se> 3.4.2-1
- Upgraded to 3.4.2.

* Thu Dec 27 2001 Göran Uddeborg <goeran@uddeborg.se>
- Added build requirement on freetype-devel.

* Mon Nov 26 2001 Göran Uddeborg <goeran@uddeborg.se>
- First RPM packaging.
