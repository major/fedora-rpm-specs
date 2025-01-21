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
%global srcver 20040629
%global catalogue %{_sysconfdir}/X11/fontpath.d

Name: sazanami-fonts
Version: 0.%{srcver}
Release: 48%{?dist}
URL:     http://efont.sourceforge.jp/
BuildRequires: fonts-rpm-macros >= 1:2.0.5-9
BuildRequires: fonttools
BuildRequires: ttmkfdir >= 3.0.6
BuildRequires: mkfontdir xorg-x11-fonts-misc >= 7.5-11


# The following declarations will be aliased to [variable]0 and reused for all
# generated *-fonts packages unless overriden by a specific [variable][number]
# declaration.
%global foundry           Sazanami
%global fontlicense       BSD-3-Clause
%global fontlicenses      LICENSE.shinonome LICENSE_J.mplus
%global fontdocs          README.sazanami README.kappa README.ayu doc/misaki/misakib8.txt README.oradano
%global fontdocsex        %{fontlicenses}

# A text block that can be reused as part of the description of each generated
# subpackage.
%global common_description %{expand:The Sazanami type faces are automatically generated from Wadalab font kit.
They also contains some embedded Japanese bitmap fonts.
}

# Declaration for the subpackage containing the first font family. Also used as
# source rpm info. All the [variable]0 declarations are equivalent and aliased
# to [variable].

%global fontfamily0       Sazanami Gothic
%global fontsummary0      Sazanami Gothic Japanese TrueType font
%global fontpkgheader0    %{expand:
Obsoletes: sazanami-fonts-common < %{version}-%{release}
Provides: sazanami-fonts-common = %{version}-%{release}
}
%global fonts0            sazanami-gothic.ttf
%global fontsex0          %{nil}
%global fontconfs0        %{SOURCE10}
%global fontconfsex0      %{nil}
%global fontdescription0  %{expand:
%{common_description}
This package contains Japanese TrueType font for Gothic type face.
}

%global fontfamily1       Sazanami Mincho
%global fontsummary1      Sazanami Mincho Japanese TrueType font
%global fontpkgheader1    %{expand:
Obsoletes: sazanami-fonts-common < %{version}-%{release}
Provides: sazanami-fonts-common = %{version}-%{release}
}
%global fonts1            sazanami-mincho.ttf
%global fontsex1          %{nil}
%global fontconfs1        %{SOURCE11}
%global fontconfsex1      %{nil}
%global fontdescription1  %{expand:
%{common_description}
This package contains Japanese TrueType font for Mincho type face.
}


Source0:  http://globalbase.dl.sourceforge.jp/efont/10087/sazanami-%{srcver}.tar.bz2
Source1:  fonts.alias.sazanami-gothic
Source2:  fonts.alias.sazanami-mincho
Source10: 70-%{fontpkgname0}.conf
Source11: 70-%{fontpkgname1}.conf
Patch0:   uni7E6B-gothic.patch
Patch1:   uni7E6B-mincho.patch
Patch2:   uni8449-mincho.patch


Summary: Sazanami Japanese TrueType fonts
License: BSD-3-Clause
BuildArch: noarch

%description
%{common_description}

# “fontpkg” will generate the font subpackage headers corresponding to the
# elements declared above.
# “fontpkg” accepts the following selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontpkg -z 0 -s

%fontpkg -z 1

# “fontmetapkg” will generate a font meta(sub)package header for all the font
# subpackages generated in this spec. Optional arguments:
# – “-n [name]”      use [name] as metapackage name
# – “-s [variable]”  use the content of [variable] as metapackage summary
# – “-d [variable]”  use the content of [variable] as metapackage description
# – “-z [numbers]”   restrict metapackaging to [numbers] comma-separated list
#                    of font package suffixes
%fontmetapkg

%prep
%setup -q -n sazanami-%{srcver}

%build
# “fontbuild” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontbuild -a

#rhbz#196433: modify the ttfs to change the glyph for 0x7E6B
ttx -i -a -e sazanami-gothic.ttf
patch -b -z .uni7E6B sazanami-gothic.ttx %{PATCH0}
touch -r sazanami-gothic.ttf sazanami-gothic.ttx
rm sazanami-gothic.ttf
ttx -b sazanami-gothic.ttx
touch -r sazanami-gothic.ttx sazanami-gothic.ttf

ttx -i -a -e sazanami-mincho.ttf
patch -b -z .uni7E6B sazanami-mincho.ttx %{PATCH1}
patch -b -z .uni8449 sazanami-mincho.ttx %{PATCH2}
touch -r sazanami-mincho.ttf sazanami-mincho.ttx
rm sazanami-mincho.ttf
ttx -b sazanami-mincho.ttx
touch -r sazanami-mincho.ttx sazanami-mincho.ttf

mv doc/shinonome/LICENSE LICENSE.shinonome
mv doc/mplus/LICENSE_J LICENSE_J.mplus
mv README README.sazanami
mv doc/kappa/README README.kappa
mv doc/ayu/README.txt README.ayu
mv doc/oradano/README.txt README.oradano

%install
install -dm 0755 $RPM_BUILD_ROOT%{catalogue}

%fontinstall -z 0
install -pm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname0}/fonts.alias
ttmkfdir -d $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname0} -o $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname0}/fonts.scale
mkfontdir $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname0}
ln -sf $(realpath --relative-to=$RPM_BUILD_ROOT%{catalogue} $RPM_BUILD_ROOT%{_fontbasedir})/%{fontpkgname0} $RPM_BUILD_ROOT%{catalogue}/%{fontpkgname0}

%fontinstall -z 1
install -pm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname1}/fonts.alias
ttmkfdir -d $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname1} -o $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname1}/fonts.scale
mkfontdir $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname1}
ln -sf $(realpath --relative-to=$RPM_BUILD_ROOT%{catalogue} $RPM_BUILD_ROOT%{_fontbasedir})/%{fontpkgname1} $RPM_BUILD_ROOT%{catalogue}/%{fontpkgname1}

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
%fontfiles -z 0
%{catalogue}/%{fontpkgname0}
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname0}/fonts.dir
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname0}/fonts.scale
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname0}/fonts.alias

%fontfiles -z 1
%{catalogue}/%{fontpkgname1}
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname1}/fonts.dir
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname1}/fonts.scale
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname1}/fonts.alias

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Akira TAGOH <tagoh@redhat.com> - 0.20040629-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 17 2023 Akira TAGOH <tagoh@redhat.com> - 0.20040629-44
- Revise the spec file for new packaging guidelines.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec  5 2022 Akira TAGOH <tagoh@redhat.com> - 0.20040629-42
- Convert License tag to SPDX.

* Wed Nov  2 2022 Akira TAGOH <tagoh@redhat.com> - 0.20040629-41
- Drop old dependencies.
- Fix validation error in fontconfig config files.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Kalev Lember <klember@redhat.com> - 0.20040629-33
- Avoid hardcoding ttmkfdir and mkfontdir prefix

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Akira TAGOH <tagoh@redhat.com> - 0.20040629-29
- Update the priority to change the default font to Noto.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 07 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.20040629-26
- Build against new fonttools-3.0-4 build

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov  4 2014 Akira TAGOH <tagoh@redhat.com> - 0.20040629-23
- Rebuilt to get the proper fonts.scale with fixed xorg-x11-fonts-misc. (#1007493)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Akira TAGOH <tagoh@redhat.com> - 0.20040629-18
- Correct fontconfig config file. (#837532)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Akira TAGOH <tagoh@redhat.com> - 0.20040629-16
- Add xorg-x11-fonts-misc to BR. (#733106)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 23 2010 Akira TAGOH <tagoh@redhat.com> - 0.20040629-14
- Fix the broken outline path of U+8449 in sazanami-mincho. (#606876)

* Tue May 25 2010 Akira TAGOH <tagoh@redhat.com> - 0.20040629-13
- Improve the fontconfig config file to match ja as well.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 0.20040629-12
- Get rid of compare="contains".

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 0.20040629-11
- Get rid of binding="same" from the fontconfig config file. (#578045)

* Tue Oct  6 2009 Akira TAGOH <tagoh@redhat.com> - 0.20040629-9
- keeps the original timestamps for TTFs.

* Mon Oct 05 2009 Caolán McNamara <caolanm@redhat.com>
- use ttx and rebuild the font by merging the original .ttfs with the
  custom replacement uni7E6B glyphs

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-8.20061016
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-7.20061016
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Akira TAGOH <tagoh@redhat.com> - 0.20040629-6.20061016
- Rename the package name again.

* Thu Dec 25 2008 Akira TAGOH <tagoh@redhat.com> - 0.20040629-5.20061016
- Update the spec file to fit into new guideline. (#477453)

* Tue Aug 28 2007 Jens Petersen <petersen@redhat.com> - 0.20040629-4.20061016
- use the standard font scriptlets (#259041)

* Thu Aug 23 2007 Akira TAGOH <tagoh@redhat.com> - 0.20040629-3.20061016
- Update %%description.
- Separate package for gothic and mincho.

* Fri Aug 17 2007 Akira TAGOH <tagoh@redhat.com> - 0.20040629-1.20061016
- Split sazanami*ttf up from fonts-japanese.
