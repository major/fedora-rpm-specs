# SPDX-License-Identifier: MIT

BuildArch: noarch
BuildRequires: bdftopcf fonttosfnt
BuildRequires: make

%global fontname bitmap
%global fontconf 66-%{fontname}

Version: 0.3
Release: 49%{?dist}
License: GPL-2.0-only AND MIT AND LicenseRef-Lucida

%global foundry           Bitmap

%global common_description %{expand:
The bitmap-fonts package provides a number of bitmap fonts selected\
from the xorg package designed for use locations such as\
terminals.
}

%global fontfamily1       Lucida Typewriter
%global fontsummary1      Selected CJK bitmap fonts for Anaconda
%global fontlicense1      LicenseRef-Lucida
%global fontlicenses1     LU_LEGALNOTICE
%global fontpkgheader1    %{expand:
Provides: %{name}-cjk = %{version}-%{release}
Conflicts: bitmap-lucida-typewriter-opentype-fonts
}
%global fonts1            lut*.pcf.gz
%global fontconfs1        %{SOURCE17}
%global fontdescription1  %{expand:
%{common_description}
}

%global fontfamily2       Lucida Typewriter OpenType
%global fontsummary2      Selected CJK bitmap fonts for Anaconda (OpenType version)
%global fontlicense2      LicenseRef-Lucida
%global fontlicenses2     LU_LEGALNOTICE
%global fontpkgheader2    %{expand:
Conflicts: bitmap-lucida-typewriter-fonts
}
%global fonts2            lut*.otb
%global fontconfs2        %{SOURCE18}
%global fontdescription2  %{expand:
%{common_description}
}

%global fontfamily3       Fangsongti
%global fontsummary3      Selected CJK bitmap fonts for Anaconda
%global fontlicense3      MIT
%global fontlicenses3     LICENSE
%global fontpkgheader3    %{expand:
Provides: %{name}-cjk = %{version}-%{release}
Conflicts: bitmap-fangsongti-opentype-fonts
}
%global fonts3            fangsongti*.pcf.gz
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}
}

%global fontfamily4       Fangsongti OpenType
%global fontsummary4      Selected CJK bitmap fonts for Anaconda (OpenType version)
%global fontlicense4      MIT
%global fontlicenses4     LICENSE
%global fontpkgheader4    %{expand:
Conflicts: bitmap-fangsongti-fonts
}
%global fonts4            fangsongti*.otb
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}
}

%global fontfamily5       Console
%global fontsummary5      Selected set of bitmap fonts
%global fontlicense5      GPL-2.0-only
%global fontlicenses5     COPYING
%global fontpkgheader5    %{expand:
Conflicts: bitmap-console-opentype-fonts
}
%global fonts5            fixfont-3.5/console8x16*.pcf.gz
%global fontconfs5        %{SOURCE11}
%global fontdescription5  %{expand:
%{common_description}
}

%global fontfamily6       Console OpenType
%global fontsummary6      Selected set of bitmap fonts (OpenType version)
%global fontlicense6      GPL-2.0-only
%global fontlicenses6     COPYING
%global fontpkgheader6    %{expand:
Conflicts: bitmap-console-fonts
}
%global fonts6            fixfont-3.5/console8x16*.otb
%global fontconfs6        %{SOURCE12}
%global fontdescription6  %{expand:
%{common_description}
}

%global fontfamily7       Fixed
%global fontsummary7      Selected set of bitmap fonts
%global fontlicense7      GPL-2.0-only
%global fontlicenses7     COPYING
%global fontpkgheader7    %{expand:
Conflicts: bitmap-fixed-opentype-fonts
}
%global fonts7            fixfont-3.5/console9*.pcf.gz
%global fontconfs7        %{SOURCE15}
%global fontdescription7  %{expand:
%{common_description}
}

%global fontfamily8       Fixed OpenType
%global fontsummary8      Selected set of bitmap fonts (OpenType version)
%global fontlicense8      GPL-2.0-only
%global fontlicenses8     COPYING
%global fontpkgheader8    %{expand:
Conflicts: bitmap-fixed-fonts
}
%global fonts8            fixfont-3.5/console9*.otb
%global fontconfs8        %{SOURCE16}
%global fontdescription8  %{expand:
%{common_description}
}


Source0:  bitmap-fonts-%{version}.tar.bz2
Source1:  fixfont-3.5.tar.bz2
Source2:  LICENSE
Source3:  COPYING
Source11: 66-bitmap-console.conf
Source12: 66-bitmap-console-opentype.conf
Source13: 66-bitmap-fangsongti.conf
Source14: 66-bitmap-fangsongti-opentype.conf
Source15: 66-bitmap-fixed.conf
Source16: 66-bitmap-fixed-opentype.conf
Source17: 66-bitmap-lucida-typewriter.conf
Source18: 66-bitmap-lucida-typewriter-opentype.conf

Name:     bitmap-fonts
Summary:  Selected set of bitmap fonts
%description
%wordwrap -v common_description

%package -n %{fontname}-fonts-all
Summary: Compatibility files of bitmap-font families
Provides: bitmap-fonts = %{version}-%{release}
Obsoletes: bitmap-fonts < %{version}-%{release}
Provides: bitmap-fonts-compat = %{version}-%{release}
Obsoletes: bitmap-fonts-compat < %{version}-%{release}
Requires: %{fontname}-lucida-typewriter-fonts = %{version}-%{release}
Requires: %{fontname}-fangsongti-fonts = %{version}-%{release}
Requires: %{fontname}-console-fonts = %{version}-%{release}
Requires: %{fontname}-fixed-fonts = %{version}-%{release}
Requires: ucs-miscfixed-fonts
Conflicts: %{fontname}-opentype-fonts-all

%description -n %{fontname}-fonts-all
%common_desc
Meta-package for installing all font families of bitmap.

%files -n %{fontname}-fonts-all

%package -n %{fontname}-opentype-fonts-all
Summary:  Compatibility files of bitmap-font families (opentype version)
Provides: bitmap-opentype-fonts-compat = %{version}-%{release}
Obsoletes: bitmap-opentype-fonts-compat < %{version}-%{release}
Requires: %{fontname}-lucida-typewriter-opentype-fonts = %{version}-%{release}
Requires: %{fontname}-fangsongti-opentype-fonts = %{version}-%{release}
Requires: %{fontname}-console-opentype-fonts = %{version}-%{release}
Requires: %{fontname}-fixed-opentype-fonts = %{version}-%{release}
Requires: ucs-miscfixed-opentype-fonts
Conflicts: %{fontname}-fonts-all

%description -n %{fontname}-opentype-fonts-all
%common_desc
Meta-package for installing all font families of opentype bitmap.

%files -n %{fontname}-opentype-fonts-all


%fontpkg -a

%prep
%setup -q -a 1
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .


%build
make all

make -C fixfont-3.5 all

# Convert to OpenType Bitmap Font
# rm [0-9]*.bdf fixfont-3.5/[0-9]*.bdf

for bdf in `ls *.bdf`;
do fonttosfnt -b -c -g 2 -m 2 -o ${bdf%%bdf}otb  $bdf;
done

pushd fixfont-3.5
for bdf in `ls *.bdf`;
do fonttosfnt -b -c -g 2 -m 2 -o ${bdf%%bdf}otb  $bdf;
done
# For console9x15.otb
fonttosfnt -b -c -g 2 -m 2 -o console9x15.otb console9x15.pcf
popd

gzip *.pcf fixfont-3.5/*.pcf

%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 13 2023 Peng Wu <pwu@redhat.com> - 0.3-45
- Rename bitmap-fonts-compat and bitmap-opentype-fonts-compat metapkgs
- Resolves: RHBZ#2254164

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 24 2023 Peng Wu <pwu@redhat.com> - 0.3-43
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Parag Nemade <pnemade AT redhat DOT com> - 0.3-38
- Resolves: rhbz#1933563 - Don't BuildRequires xorg-x11-font-utils

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Peng Wu <pwu@redhat.com> - 0.3-36
- Rebuilt with fonttosfnt 1.2.1

* Fri Sep  4 2020 Peng Wu <pwu@redhat.com> - 0.3-35
- Use BDF fonts for OpenType conversion

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb  6 2020 Peng Wu <pwu@redhat.com> - 0.3-33
- Provide OpenType Bitmap fonts
- Use bitmapfonts2otb.py to combine bitmap fonts
- Add bitmap-*-opentype-fonts sub packages

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3-28
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 03 2010 Pravin Satpute <psatpute@redhat.com> - 0.3-16
- fixed lucida license
- added compat package for smooth upgradation

* Tue Mar 02 2010 Pravin Satpute <psatpute@redhat.com> - 0.3-15
- updated as per merge review comments
- bug 225617

* Wed Nov 18 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-14
- removed console8x8.pcf from console sub-package

* Fri Oct 09 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-13
- added lucida-typewriter and fixed subpackage
- removed common subpackage
- added conf file for each subpackage

* Fri Oct 09 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-12
- updates license for each subpackage

* Thu Sep 17 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-11
- second update as per merge review comment, bug 225617

* Thu Sep 17 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-10
- updating as per merge review comment

* Thu Sep 17 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-9
- updating as per new packaging guidelines

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3-6
- fix license tag

* Tue Feb 12 2008 Rahul Bhalerao <rbhalera@redhat.com> - 0.3-5.2
- Rebuild for gcc4.3.

* Tue Feb 27 2007 Mayank Jain <majain@redhat.com> - 0.3-5.1.2
- Changed BuildRoot to %%{_tmppath}/%%{name}-%%{version}-%%{release}-root-%%(%%{__id_u} -n)
- Changed Prereq tag to Requires(pre)
- In the "cjk" subpackage summary, CJK is now spelt with capital letters.
- Added %%{?dist} to the Release tag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3-5.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 09 2004 Caolan McNamara <caolanm@redhat.com> - 0.3-5
- build fixfont .pcfs from source .bdfs

* Wed Sep 22 2004 Owen Taylor <otaylor@redhat.com> - 0.3-4
- Update BuildRequires to xorg-x11-font-utils (#118428, Mike Harris)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Owen Taylor <otaylor@redhat.com>
- Version 0.3 adding misc-fixed fonts from ucs-fonts
- Adjust %%post, %%postun

* Mon Jan 13 2003 Owen Taylor <otaylor@redhat.com>
- Patch from Anthony Fok, to fix problem where fangsongti16.bdf
  wasn't considered to cover english because it didn't have
  e-diaresis. (Causing bad font choice in Anaconda)

* Wed Dec 18 2002 Than Ngo <than@redhat.com> 0.2-4
- add some bitmap fonts

* Thu Oct 31 2002 Owen Taylor <otaylor@redhat.com> 0.2-3
- Own the bitmap-fonts directory (Enrico Scholz, #73940)
- Add %%post, %%postun for cjk subpackage

* Fri Aug 30 2002 Alexander Larsson <alexl@redhat.com> 0.2-2
- Call fc-cache from post

* Wed Aug 28 2002 Owen Taylor <otaylor@redhat.com>
- Augment fangsongti fonts with characters from 8x16, 12x24

* Tue Jul 31 2002 Yu Shao <yshao@redhat.com>
- add fangsong*.bdf converted from gb16fs.bdf and gb24st.bdf

* Mon Nov 13 2000 Owen Taylor <otaylor@redhat.com>
- Initial package

