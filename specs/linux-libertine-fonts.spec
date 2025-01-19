# Packaging template: multi-family fonts packaging.
#
# SPDX-License-Identifier: MIT
#
# This template documents spec declarations, used when packaging multiple font
# families, from a single dedicated source archive. The source rpm is named
# after the first (main) font family). Look up “fonts-3-sub” when the source
# rpm needs to be named some other way.
#
# It is part of the following set of packaging templates:
# “fonts-0-simple”: basic single-family fonts packaging
# “fonts-1-full”:   less common patterns for single-family fonts packaging
# “fonts-2-multi”:  multi-family fonts packaging
# “fonts-3-sub”:    packaging fonts, released as part of something else
#
%global posttag 2012_07_02

Version: 5.3.0
Release: 31.%{posttag}%{?dist}
URL:     http://linuxlibertine.sf.net
BuildRequires: fonts-rpm-macros >= 1:2.0.5-9


# The following declarations will be aliased to [variable]0 and reused for all
# generated *-fonts packages unless overriden by a specific [variable][number]
# declaration.
%global foundry           linux-libertine
%global fontlicense       GPL-2.0-or-later WITH Font-exception-2.0 OR OFL-1.1
%global fontlicenses      OFL-1.1.txt GPL.txt LICENCE.txt
%global fontdocs          ToDo.txt Readme-TEX.txt README ChangeLog.txt Bugs.txt
%global fontdocsex        %{fontlicenses}

# A text block that can be reused as part of the description of each generated
# subpackage.
%global common_description %{expand:
The Linux Libertine Open Fonts are a TrueType font family for practical use in documents.  They were created to provide a free alternative to proprietary standard fonts.
}

# Declaration for the subpackage containing the first font family. Also used as
# source rpm info. All the [variable]0 declarations are equivalent and aliased
# to [variable].

%global fontfamily0       Linux Libertine
%global fontsummary0      Linux Libertine Open Fonts
%global fontpkgheader0    %{expand:
Obsoletes: linux-libertine-fonts-common < 5.3.0-25
Provides: linux-libertine-fonts-common = %{version}-%{release}
}
%global fonts0            LinLibertine_RZ.otf LinLibertine_RZI.otf LinLibertine_R.otf LinLibertine_RI.otf LinLibertine_RB.otf LinLibertine_RBI.otf LinLibertine_DR.otf LinLibertine_I.otf
%global fontsex0          %{nil}
%global fontconfs0        %{SOURCE10} %{SOURCE13}
%global fontconfsex0      %{nil}
%global fontdescription0  %{expand:
%{common_description}
This package contains Serif fonts.
}

%global fontfamily1       Linux Biolinum
%global fontsummary1      Sans-serif fonts from Linux Libertine Open Fonts
%global fontpkgheader1    %{expand:
Obsoletes: linux-libertine-fonts-common < 5.3.0-25
Provides: linux-libertine-fonts-common = %{version}-%{release}
}
%global fonts1            LinBiolinum_R.otf LinBiolinum_RI.otf LinBiolinum_RB.otf LinBiolinum_K.otf
%global fontsex1          %{nil}
%global fontconfs1        %{SOURCE11}
%global fontconfsex1      %{nil}
%global fontdescription1  %{expand:
%{common_description}
This package contains Sans fonts.
}

%global fontfamily2       Linux Libertine Mono
%global fontsummary2      Monospace font from Linux Libertine Open Fonts
%global fontpkgheader2    %{expand:
Obsoletes: linux-libertine-fonts < 5.3.0-25
Obsoletes: linux-libertine-fonts-common < 5.3.0-25
Provides: linux-libertine-fonts-common = %{version}-%{release}
}
%global fonts2            LinLibertine_M.otf
%global fontsex2          %{nil}
%global fontconfs2        %{SOURCE12}
%global fontconfsex2      %{nil}
%global fontdescription2  %{expand:
%{common_description}
This package contains Monospace font.
}

Source0:  http://download.sourceforge.net/sourceforge/linuxlibertine/LinLibertineOTF_%{version}_%{posttag}.tgz
Source10: 60-linux-libertine-fonts.conf
Source11: 61-linux-libertine-biolinum-fonts.conf
Source12: 61-linux-libertine-mono-fonts.conf
Source13: 29-linux-libertine-fonts-metrics-alias.conf

# “fontpkg” will generate the font subpackage headers corresponding to the
# elements declared above.
# “fontpkg” accepts the following selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontpkg -a

# “fontmetapkg” will generate a font meta(sub)package header for all the font
# subpackages generated in this spec. Optional arguments:
# – “-n [name]”      use [name] as metapackage name
# – “-s [variable]”  use the content of [variable] as metapackage summary
# – “-d [variable]”  use the content of [variable] as metapackage description
# – “-z [numbers]”   restrict metapackaging to [numbers] comma-separated list
#                    of font package suffixes
%fontmetapkg

%prep
%setup -q -c

%build
# “fontbuild” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontbuild -a

%install
# “fontinstall” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontinstall -a

%check
# “fontcheck” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontcheck -a

# “fontfiles” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block
%fontfiles -a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-31.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-30.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Akira TAGOH <tagoh@redhat.com> - 5.3.0-29.2012_07_02
- Correct package replacement of linux-libertine-fonts-common.
  Resolves: rhbz#2282595

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-28.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-27.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-26.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 13 2023 Akira TAGOH <tagoh@redhat.com> - 5.3.0-24.2012_07_02
- Revise the spec file for new packaging guidelines.
- Add linux-libertine-mono-fonts sub-package.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-24.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec  2 2022 Akira TAGOH <tagoh@redhat.com> - 5.3.0-23.2012_07_02
- Convert License tag to SPDX.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-22.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-21.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-20.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-19.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-18.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-17.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-16.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 5.3.0-15.2012_07_02
- Install metainfo files under %%{_metainfodir}.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-14.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-13.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Akira TAGOH <tagoh@redhat.com> - 5.3.0-12.2012_07_02
- Modernize the spec file.
- Fix bogus date in the spec file.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-11.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-10.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-9.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-8.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-7.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Richard Hughes <richard@hughsie.com> - 5.3.0-6.2012_07_02
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-5.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-4.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-3.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Akira TAGOH <tagoh@redhat.com> - 5.3.0-2.2012_07_02
- Use OTF version of fonts.

* Tue Jul 24 2012 Akira TAGOH <tagoh@redhat.com> - 5.3.0-1.2012_07_02
- New upstream release.
- Giving up to build fonts from the source due to lacking of the build script.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.3-3.2011_06_21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Akira TAGOH <tagoh@redhat.com> - 5.1.3-2.2011_06_21
- Fix the order for substitute of Times New Roman. (#830849)

* Thu Apr 19 2012 Akira TAGOH <tagoh@redhat.com> - 5.1.3-1.2011_06_21
- New upstream release. (#813730)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.5-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Feb 17 2011 Akira TAGOH <tagoh@redhat.com> - 4.7.5-1.2
- Improve the spec file to meet the packaging guidelines. (#477418)
- Updates to 4.7.5-2 (#628540)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Kevin Fenzi <kevin@tummy.com> - 4.4.1-1
- Upgrade to 4.4.1
- Fix to match current font guidelines

* Sun Mar 15 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net> - 4.1.8-3
— Make sure F11 font packages have been built with F11 fontforge

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Frank Arnold <frank@scirocco-5v-turbo.de> 4.1.8-1
- Updated to 4.1.8
- Modified build procedure according to GENERATING.txt

* Wed Sep 3 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
-  2.7.9-2
⚙ Rebuild with pre-F10-freeze fontforge

* Sun Feb 03 2008 Frank Arnold <frank@scirocco-5v-turbo.de> 2.7.9-1
- Updated to 2.7.9
- Drop generated PDF files to save space

* Sun Sep 16 2007 Kevin Fenzi <kevin@tummy.com> - 2.6.9-1
- Updated to 2.6.9
- Update License tag

* Sat Mar 17 2007 Frank Arnold <frank@scirocco-5v-turbo.de> 2.4.9-1
- Updated to 2.4.9
- Reenabled generation of PDF files

* Sun Oct 01 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.2.0-1
- Updated to 2.2.0
- Removed ghosted cache file as it's no longer stored in tree
- Disabled generation of PDF files because fontforge will segfault
- Added OFL to License field

* Tue Sep 19 2006 Kevin Fenzi <kevin@tummy.com> 2.1.9-2
- Upload proper 2.1.9 sources and rebuild

* Tue Sep 19 2006 Kevin Fenzi <kevin@tummy.com> 2.1.9-1
- Update to 2.1.9

* Tue Aug 29 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.1.0-1
- Updated to 2.1.0

* Tue Feb 28 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.0.4-2
- Named back to linux-libertine-fonts

* Mon Feb 13 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.0.4-1
- Updated to 2.0.4
- Removed handling of fonts.cache-2

* Wed Feb 01 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.0.1-3
- Nuked separate fontforge build script, now in %%build section

* Tue Jan 31 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.0.1-2
- Fixed the following issues addressed by Ignacio Vazquez-Abrams
- Package renaming to font-linux-libertine
- Generate fonts from sources
- Sample sheets for each font in PDF format

* Mon Jan 30 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.0.1-1
- Initial RPM release
- Spec derived from other font packages
