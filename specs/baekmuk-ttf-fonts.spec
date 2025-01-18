# SPDX-License-Identifier: MIT

%global fontname    baekmuk-ttf
%global archivename %{fontname}-%{version}

BuildArch: noarch
BuildRequires: mkfontdir
BuildRequires: ttmkfdir >= 3.0.6

Version: 2.2
Release: 64%{?dist}
License: Baekmuk
URL:     http://kldp.net/projects/baekmuk/

%global foundry           Baekmuk
%global fontlicense       Baekmuk
%global fontlicenses      COPYRIGHT COPYRIGHT.ko
%global fontdocs          README

%global common_description %{expand:
This package provides the free Korean TrueType fonts.
}

%global fontfamily1       Baekmuk Batang
%global fontsummary1      Korean Baekmuk TrueType Batang typeface
%global fontpkgheader1    %{expand:
Obsoletes:      %{name}-batang < 2.2-13
Provides:       %{name}-batang = %{version}-%{release}
Obsoletes:      %{fontname}-batang-fonts < 2.2-60
Provides:       %{fontname}-batang-fonts = %{version}-%{release}
Obsoletes:      %{name}-common < 2.2-60
Provides:       %{name}-common = %{version}-%{release}
}
%global fonts1            ttf/batang.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

Batang is Korean TrueType font in Serif typeface.
}

%global fontfamily2       Baekmuk Dotum
%global fontsummary2      Korean Baekmuk TrueType Dotum typeface
%global fontpkgheader2    %{expand:
Obsoletes:      %{name}-dotum < 2.2-13
Provides:       %{name}-dotum = %{version}-%{release}
Obsoletes:      %{fontname}-dotum-fonts < 2.2-60
Provides:       %{fontname}-dotum-fonts = %{version}-%{release}
Obsoletes:      %{name}-common < 2.2-60
Provides:       %{name}-common = %{version}-%{release}
}
%global fonts2            ttf/dotum.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

Dotum is Korean TrueType font in San-serif typeface.
}

%global fontfamily3       Baekmuk Gulim
%global fontsummary3      Korean Baekmuk TrueType Gulim typeface
%global fontpkgheader3    %{expand:
Obsoletes:      %{name}-gulim < 2.2-13
Provides:       %{name}-gulim = %{version}-%{release}
Obsoletes:      %{fontname}-gulim-fonts < 2.2-60
Provides:       %{fontname}-gulim-fonts = %{version}-%{release}
Obsoletes:      %{name}-common < 2.2-60
Provides:       %{name}-common = %{version}-%{release}
}
%global fonts3            ttf/gulim.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

Gulim is Korean TrueType font in Monospace typeface.
}

%global fontfamily4       Baekmuk Headline
%global fontsummary4      Korean Baekmuk TrueType Headline typeface
%global fontpkgheader4    %{expand:
Obsoletes:      %{name}-hline < 2.2-13
Provides:       %{name}-hline = %{version}-%{release}
Obsoletes:      %{fontname}-hline-fonts < 2.2-60
Provides:       %{fontname}-hline-fonts = %{version}-%{release}
Obsoletes:      %{name}-common < 2.2-60
Provides:       %{name}-common = %{version}-%{release}
}
%global fonts4            ttf/hline.ttf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

Headline is Korean TrueType font in Black face.
}


Source0:  http://kldp.net/baekmuk/release/865-%{archivename}.tar.gz#/%{archivename}.tar.gz
Source11: 68-%{fontpkgname1}.conf
Source12: 68-%{fontpkgname2}.conf
Source13: 68-%{fontpkgname3}.conf
Source14: 68-%{fontpkgname4}.conf

Name:     %{fontname}-fonts
Summary:  Free Korean TrueType fonts
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg


%prep
%autosetup -n %{archivename}

# convert Korean copyright file to utf8
%{_bindir}/iconv -f EUC-KR -t UTF-8 COPYRIGHT.ks > COPYRIGHT.ko


%build
%fontbuild -a

%install
%fontinstall -a

for fontdir in `echo %{fontdir1} %{fontdir2} %{fontdir3} %{fontdir4}`; do
    %__install -d -m 0755 %{buildroot}$fontdir

    # fonts.{scale,dir}
    %{_bindir}/ttmkfdir -d %{buildroot}$fontdir \
      -o %{buildroot}$fontdir/fonts.scale
      %{_bindir}/mkfontdir %{buildroot}$fontdir
done

%check
%fontcheck -a

%fontfiles -z 1
%verify(not md5 size mtime) %{fontdir1}/fonts.dir
%verify(not md5 size mtime) %{fontdir1}/fonts.scale

%fontfiles -z 2
%verify(not md5 size mtime) %{fontdir2}/fonts.dir
%verify(not md5 size mtime) %{fontdir2}/fonts.scale

%fontfiles -z 3
%verify(not md5 size mtime) %{fontdir3}/fonts.dir
%verify(not md5 size mtime) %{fontdir3}/fonts.scale

%fontfiles -z 4
%verify(not md5 size mtime) %{fontdir4}/fonts.dir
%verify(not md5 size mtime) %{fontdir4}/fonts.scale

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Feb 24 2023 Peng Wu <pwu@redhat.com> - 2.2-60
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov  2 2022 Akira TAGOH <tagoh@redhat.com> - 2.2-58
- Drop old dependencies.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  2 2021 Peng Wu <pwu@redhat.com> - 2.2-54
- Resolves: rhbz#1933564 - Don't BuildRequires xorg-x11-font-utils

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun  3 2019 Akira TAGOH <tagoh@redhat.com> - 2.2-49
- Install metainfo files into %%{_metainfodir}.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Peng Wu <pwu@redhat.com> - 2.2-47
- Update Source URL

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jan 30 2018 Akira TAGOH <tagoh@redhat.com> - 2.2-45
- Update the priority to change the default font to Noto.

* Mon Jan 22 2018 Peng Wu <pwu@redhat.com> - 2.2-44
- Drop baekmuk-ttf-fonts-ghostscript subpackage

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Daiki Ueno <dueno@redhat.com> - 2.2-40
- replace %%define uses with %%global

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.2-38
- Add metainfo file to show this font in gnome-software
- Remove buildroot which is optional now
- Remove group tag

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 2.2-33
- fix <test> usage in fontconfig files (Closes: #837526)

* Mon Feb  6 2012 Daiki Ueno <dueno@redhat.com> - 2.2-32
- Update the priority.
  nhn-nanum-fonts -> 65-0, un-core-fonts -> 65-1, baekmuk-ttf-fonts -> 65-2
- Drop buildroot cleanup.
- Drop %%defattr(0644,root,root,0755) from %%files.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 26 2010 Akira TAGOH <tagoh@redhat.com> - 2.2-29
- Improve the fontconfig config file to match ko-kr as well. (#586306)
- sync NVR and fixes from RHEL-6.
- Update the priority.

* Wed Apr 21 2010 Caius 'kaio' Chance <k at kaio.me> - 2.2-25
- Resolves: rhbz#578017 (Remove binding="same" from conf files.)

* Wed Jan 13 2010 Caius 'kaio' Chance <k at kaio.me> - 2.2-24.el6
- Fixed rpmlint errors.
- Synchronized version number with another tree.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 08 2009 Caius 'kaio' Chance <cchance@redhat.com> - 2.2-21.fc11
- Resolves: rhbz#483327 (Fixed unowned directories.)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Caius Chance <cchance@redhat.com> - 2.2-19.fc11
- Resolves: rhbz#483327
- Reowned font directory by subpackage -common.
- Splited ghostscript files to subpackage -ghostscript.
- Updated paths in ghostscript files.

* Mon Feb 02 2009 Caius Chance <cchance@redhat.com> - 2.2-18.fc11
- Updated fontconfig .conf files based on fontpackages templates.

* Tue Jan 27 2009 Caius Chance <cchance@redhat.com> - 2.2-17.fc11
- Resolves: rhbz#477332
- Fixed obsoletion of baekmuk-ttf-common-fonts.

* Thu Jan 22 2009 Caius Chance <cchance@redhat.com> - 2.2-16.fc11
- Resolves: rhbz#477332
- Refined dependencies.

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 2.2-15.fc11
- Fix busted inter-subpackage dependencies

* Tue Jan 20 2009 Caius Chance <cchance@redhat.com> - 2.2-14.fc11
- Resolves: rhbz#477332
- Refined according to Mailhot's comments (477410) on liberaton fonts.

* Mon Jan 19 2009 Caius Chance <cchance@redhat.com> - 2.2-13.fc11
- Resolves: rhbz#477332
- Package renaming for post-1.13 fontpackages.

* Fri Jan 16 2009 Caius Chance <cchance@redhat.com> - 2.2-12.fc11
- Resolves: rhbz#477332 (Repatched buildsys error.)

* Fri Jan 16 2009 Caius Chance <cchance@redhat.com> - 2.2-11.fc11
- Resolves: rhbz#477332 (Included macro _font_pkg and created fontconfig .conf files.)

* Fri Jan 09 2009 Caius Chance <cchance@redhat.com> - 2.2-10.fc11
- Resolves: rhbz#477332 (Converted to new font packaging guidelines.)

* Mon Jun 30 2008 Caius Chance <cchance@redhat.com> - 2.2-9.fc10
- Refine obsoletes tag version-release specific.

* Mon Jun 30 2008 Caius Chance <cchance@redhat.com> - 2.2-8.fc10
- Resolves: rhbz#453080 (fonts-korean is deprecated and should be removed.)

* Wed Nov 14 2007 Jens Petersen <petersen@redhat.com> - 2.2-7
- better url
- use fontname and fontdir macros

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 2.2-6
- convert Korean copyright file to utf8 (Mamoru Tasaka, #300651)

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 2.2-5
- more fixes from Mamoru Tasaka, #300651:
- make common subpackage own ghostscript conf.d
- conflict with previous fonts-korean
- update CID font maps

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 2.2-4
- preserve timestamps of installed files (Mamoru Tasaka, #300651)
- add a common subpackage for shared files (Mamoru Tasaka, #300651)

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 2.2-3
- do not provide ttfonts-ko in subpackages (Mamoru Tasaka, #300651)

* Sat Sep 22 2007 Jens Petersen <petersen@redhat.com> - 2.2-2
- license is now designated Baekmuk

* Sat Sep 22 2007 Jens Petersen <petersen@redhat.com> - 2.2-1
- new package separated from fonts-korean (#253155)
