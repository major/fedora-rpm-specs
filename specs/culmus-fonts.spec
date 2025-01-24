BuildArch: noarch
BuildRequires: /usr/bin/makeotfexe
BuildRequires: fontforge

Version:   0.133
Release:   13%{?dist}
License:   GPL-2.0-only
URL:       http://culmus.sourceforge.net

%global common_description %{expand:
The culmus-fonts package contains fonts for the display of
Hebrew from the Culmus project.}

%global foundry           CLM
%global fontlicenses      LICENSE GNU-GPL LICENSE LICENSE-BITSTREAM
%global fontdocs          CHANGES
%global fontdocsex        %{fontlicenses}

%global fontfamily1       Aharoni CLM
%global fontsummary1      Aharoni CLM, a sans-serif font family
%global fontpkgheader1    %{expand:
Obsoletes: culmus-aharoni-clm-fonts < 0.133-1
Provides:  culmus-aharoni-clm-fonts = %{version}-%{release}
}
%global fonts1            AharoniCLM-*.otf
%global fontconfs1        %{SOURCE1}
%global fontdescription1  %{expand:
%{common_description}

This package provides Aharoni CLM, a sans-serif font family.
}

%global fontfamily2       Caladings CLM
%global fontsummary2      Caladings CLM, a fantasy font family
%global fontpkgheader2    %{expand:
Obsoletes: culmus-caladings-clm-fonts < 0.133-1
Provides:  culmus-caladings-clm-fonts = %{version}-%{release}
}
%global fonts2            CaladingsCLM.otf
%global fontconfs2        %{SOURCE2}
%global fontdescription2  %{expand:
%{common_description}

This package provides Caladings CLM, a fantasy font family.
}

%global fontfamily3       David CLM
%global fontsummary3      David CLM, a serif font family
%global fontpkgheader3    %{expand:
Obsoletes: culmus-david-clm-fonts < 0.133-1
Provides:  culmus-david-clm-fonts = %{version}-%{release}
}
%global fonts3            DavidCLM-*.otf
%global fontconfs3        %{SOURCE3}
%global fontdescription3  %{expand:
%{common_description}

This package provides David CLM, a serif font family.
}

%global fontfamily4       Drugulin CLM
%global fontsummary4      Drugulin CLM, a serif font family
%global fontpkgheader4    %{expand:
Obsoletes: culmus-drugulin-clm-fonts < 0.133-1
Provides:  culmus-drugulin-clm-fonts = %{version}-%{release}

}
%global fonts4            DrugulinCLM-*.otf
%global fontconfs4        %{SOURCE4}
%global fontdescription4  %{expand:
%{common_description}

This package provides Drugulin CLM, a serif font family.
}

%global fontfamily5       Ellinia CLM
%global fontsummary5      Ellinia CLM, a sans-serif font family
%global fontpkgheader5    %{expand:
Obsoletes: culmus-ellinia-clm-fonts < 0.133-1
Provides:  culmus-ellinia-clm-fonts = %{version}-%{release}

}
%global fonts5            ElliniaCLM-*.otf
%global fontconfs5        %{SOURCE5}
%global fontdescription5  %{expand:
%{common_description}

This package provides Ellinia CLM, a sans-serif font family.
}

%global fontfamily6       Frank Ruehl CLM
%global fontsummary6      Frank Ruehl CLM, a serif font family
%global fontpkgheader6    %{expand:
Obsoletes: culmus-frank-ruehl-clm-fonts < 0.133-1
Provides:  culmus-frank-ruehl-clm-fonts = %{version}-%{release}
}
%global fonts6            FrankRuehlCLM-*.ttf
%global fontconfs6        %{SOURCE6}
%global fontdescription6  %{expand:
%{common_description}

This package provides Frank Ruehl CLM, a serif font family.
}

%global fontfamily7       Hadasim CLM
%global fontsummary7      Hadasim CLM, a serif font family
%global fontpkgheader7    %{expand:
Obsoletes: culmus-hadasim-clm-fonts < 0.133-1
Provides:  culmus-hadasim-clm-fonts = %{version}-%{release}
}
%global fonts7            HadasimCLM-*.ttf
%global fontconfs7        %{SOURCE7}
%global fontdescription7  %{expand:
%{common_description}

This package provides Hadasim CLM, a serif font family.
}

%global fontfamily8       Keter YG
%global fontsummary8      Keter YG, a sans-serif font family
%global fontpkgheader8    %{expand:
Obsoletes: culmus-keteryg-fonts < 0.133-1
Provides:  culmus-keteryg-fonts = %{version}-%{release}
}
%global fonts8            KeterYG-*.ttf
%global fontconfs8        %{SOURCE8}
%global fontdescription8  %{expand:
%{common_description}

This package provides Keter YG, a sans-serif font family.
}

%global fontfamily9       Miriam CLM
%global fontsummary9      Miriam CLM, a sans-serif font family
%global fontpkgheader9    %{expand:
Obsoletes: culmus-miriam-clm-fonts < 0.133-1
Provides:  culmus-miriam-clm-fonts = %{version}-%{release}
}
%global fonts9            MiriamCLM-*.ttf
%global fontconfs9        %{SOURCE9}
%global fontdescription9  %{expand:
%{common_description}

This package provides Miriam CLM, a sans-serif font family.
}

%global fontfamily10       Miriam Mono CLM
%global fontsummary10      Miriam Mono CLM, a monospace font family
%global fontpkgheader10    %{expand:
Obsoletes: culmus-miriam-mono-clm-fonts < 0.133-1
Provides:  culmus-miriam-mono-clm-fonts = %{version}-%{release}
}
%global fonts10            MiriamMonoCLM-*.ttf
%global fontconfs10        %{SOURCE10}
%global fontdescription10  %{expand:
%{common_description}

This package provides Miriam Mono CLM, a monospace font family.
}

%global fontfamily11       Nachlieli CLM
%global fontsummary11      Nachlieli CLM, a sans-serif font family
%global fontpkgheader11    %{expand:
Obsoletes: culmus-nachlieli-clm-fonts < 0.133-1
Provides:  culmus-nachlieli-clm-fonts = %{version}-%{release}
}
%global fonts11            NachlieliCLM-*.otf
%global fontconfs11        %{SOURCE11}
%global fontdescription11  %{expand:
%{common_description}

This package provides Nachlieli CLM, a sans-serif font family.
}

%global fontfamily12       Shofar
%global fontsummary12      Shofar, a serif font family
%global fontpkgheader12    %{expand:
Obsoletes: culmus-shofar-clm-fonts < 0.133-1
Provides:  culmus-shofar-clm-fonts = %{version}-%{release}
}
%global fonts12            Shofar*.ttf
%global fontconfs12        %{SOURCE12}
%global fontdescription12  %{expand:
%{common_description}

This package provides Shofar, a serif font family.
}

%global fontfamily13       Simple CLM
%global fontsummary13      Simple CLM, a sans-serif font family
%global fontpkgheader13    %{expand:
Obsoletes: culmus-simple-clm-fonts < 0.133-1
Provides:  culmus-simple-clm-fonts = %{version}-%{release}
}
%global fonts13            SimpleCLM-*.ttf
%global fontconfs13        %{SOURCE13}
%global fontdescription13  %{expand:
%{common_description}

This package provides Simple CLM, a sans-serif font family.
}

%global fontfamily14       Stam Ashkenaz CLM
%global fontsummary14      Stam Ashkenaz CLM, a serif font family
%global fontpkgheader14    %{expand:
Obsoletes: culmus-stamashkenaz-clm-fonts < 0.133-1
Provides:  culmus-stamashkenaz-clm-fonts = %{version}-%{release}
}
%global fonts14            StamAshkenazCLM.ttf
%global fontconfs14        %{SOURCE14}
%global fontdescription14  %{expand:
%{common_description}

This package provides Stam Ashkenaz CLM, a serif font family.
}

%global fontfamily15       Stam Sefarad CLM
%global fontsummary15      Stam Sefarad CLM, a serif font family
%global fontpkgheader15    %{expand:
Obsoletes: culmus-stamsefarad-clm-fonts < 0.133-1
Provides:  culmus-stamsefarad-clm-fonts = %{version}-%{release}
}
%global fonts15            StamSefaradCLM.ttf
%global fontconfs15        %{SOURCE15}
%global fontdescription15  %{expand:
%{common_description}

This package provides Stam Sefarad CLM, a serif font family.
}

%global fontfamily16       Yehuda CLM
%global fontsummary16      Yehuda CLM, a sans-serif font family
%global fontpkgheader16    %{expand:
Obsoletes: culmus-yehuda-clm-fonts < 0.133-1
Provides:  culmus-yehuda-clm-fonts = %{version}-%{release}
}
%global fonts16            YehudaCLM-*.otf
%global fontconfs16        %{SOURCE16}
%global fontdescription16  %{expand:
%{common_description}

This package provides Yehuda CLM, a sans-serif font family.
}
Source0:   http://downloads.sourceforge.net/culmus/culmus-%{version}.tar.gz
Source1:   66-%{fontpkgname1}.conf
Source2:   66-%{fontpkgname2}.conf
Source3:   65-%{fontpkgname3}.conf
Source4:   66-%{fontpkgname4}.conf
Source5:   66-%{fontpkgname5}.conf
Source6:   66-%{fontpkgname6}.conf
Source7:   66-%{fontpkgname7}.conf
Source8:   66-%{fontpkgname8}.conf
Source9:   66-%{fontpkgname9}.conf
Source10:  66-%{fontpkgname10}.conf
Source11:  66-%{fontpkgname11}.conf
Source12:  66-%{fontpkgname12}.conf
Source13:  66-%{fontpkgname13}.conf
Source14:  66-%{fontpkgname14}.conf
Source15:  66-%{fontpkgname15}.conf
Source16:  66-%{fontpkgname16}.conf
Source17:  modify-font-metadata.pe

Name:      culmus-fonts
Summary:   Fonts for Hebrew from Culmus project
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
%setup -q -n culmus-%{version}
cp -p %{SOURCE17} .

%build
# As per fonts packaging guidelines we cannot install non-opentype fonts
# hence lets use makeotf tool to convert them to otf type format
makeotfexe -f AharoniCLM-BoldOblique.pfa -b
makeotfexe -f AharoniCLM-Bold.pfa -b
makeotfexe -f AharoniCLM-BookOblique.pfa
makeotfexe -f AharoniCLM-Book.pfa
makeotfexe -f CaladingsCLM.pfa
makeotfexe -f DrugulinCLM-BoldItalic.pfa -bi
makeotfexe -f DrugulinCLM-Bold.pfa -b
makeotfexe -f ElliniaCLM-BoldItalic.pfa -bi
makeotfexe -f ElliniaCLM-Bold.pfa -b
makeotfexe -f ElliniaCLM-LightItalic.pfa -i
makeotfexe -f ElliniaCLM-Light.pfa
makeotfexe -f YehudaCLM-Bold.pfa -b
makeotfexe -f YehudaCLM-Light.pfa

fontforge ./modify-font-metadata.pe

%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Wed Jan 22 2025 Parag Nemade <pnemade AT redhat DOT com> - 0.133-13
- Fix FTBFS for F42

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.133-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.133-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.133-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.133-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.133-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.133-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Parag Nemade <pnemade AT redhat DOT com> - 0.133-6
- Update for SPDX license expression

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.133-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.133-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Parag Nemade <pnemade AT redhat DOT com> - 0.133-3
- Update the Obsoletes: version for smooth upgrade

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.133-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Parag Nemade <pnemade AT redhat DOT com> - 0.133-1
- Update to 0.133 release
- Convert to new fonts packaging guidelines
- Dropped *.afm font files
- Converted *.pfa font files to *.otf format using makeotfexe tool
- Drop Obsoletes: culmus-fonts

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 06 2016 Pravin Satpute <psatpute@redhat.com> - 0.130-9
- Resolved #1217066 : culmus-keteryg-fonts takes over Firefox?
- Update fontconf priority of all fonts from 65 to 66, except David

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.130-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 11 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.130-6
- Add metainfo file to show this font in gnome-software
- Remove owneship of %%{_fontdir} in -common
- Remove group tag

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.130-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 18 2013 Pravin Satpute <psatpute@redhat.com> - 0.130-4
- Resolved #1002085 :- Removed old obsoletes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.130-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Pravin Satpute <psatpute@redhat.com> - 0.130-2
- Resolved #975735 :- Typo in fontconfig file

* Wed Mar 20 2013 Pravin Satpute <psatpute@redhat.com> - 0.130-1
- Upstream release 0.130 new family Shofar
- Resolved #923153

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.121-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Pravin Satpute <psatpute@redhat.com> - 0.121-4
- Spec file cleanup #878538

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Pravin Satpute <psatpute@redhat.com> - 0.121-2
- Resolves bug 837533

* Mon Jan 30 2012 Pravin Satpute <psatpute@redhat.com> - 0.121-1
- Upstream new release 0.121 with Frank Ruehl OT

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Pravin Satpute <psatpute@redhat.com> - 0.120-1
- Upstream new release.
- Added new families Hadasim CLM, Keter YG, Simple CLM, Stam Ashkenaz CLM, Stam Sefarad CLM

* Fri Sep 03 2010 Pravin Satpute <psatpute@redhat.com> - 0.105-1
- Upstream new release.
- Miriam Mono family is now OpenType and has diacritics support developed by Yoram Gnat.

* Mon Apr 19 2010 Pravin Satpute <psatpute@redhat.com> - 0.104-3
- fixed bug 578018 .conf file

* Fri Feb 19 2010 Pravin Satpute <psatpute@redhat.com> - 0.104-2
- updated .conf file priorities
- fixed bug 565385

* Fri Feb 12 2010 Pravin Satpute <psatpute@redhat.com> - 0.104-1
- new upstream release

* Tue Jan 19 2010 Pravin Satpute <psatpute@redhat.com> - 0.103-5
- fixed compat package bug 484621

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Pravin Satpute <psatpute@redhat.com> - 0.103-3
- added DavidCLM afm and pfa
- bug 509694

* Wed Jul 08 2009 Pravin Satpute <psatpute@redhat.com> - 0.103-1
- upstream new release 0.103

* Tue Apr 14 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-6.fc11
- Rebuild for bug #491957.

* Thu Mar 19 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-5.fc11
- Corrected Obsoletes for compat.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-3.fc11
- Modified -compat.

* Mon Feb 09 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-2.fc11
- Created -compat for subpackage for smooth upgrade.

* Wed Feb 04 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-1.fc11
- Updated version.
- Following new font packaging guidelines.

* Wed Jul 23 2008 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-5.fc10
- Obsoleted dead package fonts-hebrew

* Mon Oct 15 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-4.fc8
- License change

* Thu Oct 11 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-3.fc8
- Updated according to the review

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-2.fc8
- Using common spec template for font packages

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-1.fc8
- Font directory and package name corrected and updated the version

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.100-1.fc8
- Split package from fonts-hebrew to reflect upstream project name
