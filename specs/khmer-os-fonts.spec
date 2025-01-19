BuildArch: noarch

%global archivename All_KhmerOS_%{version}

Version:        5.0
Release:        44%{?dist}
License:        LGPL-2.1-or-later
URL:            http://www.khmeros.info/en/fonts

%global common_description %{expand:
The Khmer OS fonts include Khmer and Latin alphabets, and they have equivalent
sizes for Khmer and English alphabets, so that when texts mix both it is not
necessary to have different point sizes for the text in each language.

They were created by Danh Hong of the Cambodian Open Institute.}

%global foundry           Khmer OS
%global fontlicenses      License.txt

Source0:        http://downloads.sourceforge.net/khmer/%{archivename}.zip
Source11:       License.txt

Name:      khmer-os-fonts
Summary:   Khmer font family set created by Danh Hong of the Cambodian Open Institute
%description
%wordwrap -v common_description


%global fontfamily1       Battambang
%global fontsummary1      Battambang font
%global fontpkgheader1    %{expand:
Obsoletes: khmeros-battambang-fonts < 5.0-31
Provides: khmeros-battambang-fonts = %{version}-%{release}
}
%global fonts1            KhmerOS_battambang.ttf
%global fontconfs1        %{SOURCE1}
%global fontdescription1  %{expand:
%{common_description}

This package provides Battambang fonts.
}

%global fontfamily2       Bokor
%global fontsummary2      Bokor font
%global fontpkgheader2    %{expand:
Obsoletes: khmeros-bokor-fonts < 5.0-31
Provides: khmeros-bokor-fonts = %{version}-%{release}
}
%global fonts2            KhmerOS_bokor.ttf
%global fontconfs2        %{SOURCE2}
%global fontdescription2  %{expand:
%{common_description}

This package provides Bokor font family.
}

%global fontfamily3       Content
%global fontsummary3      Content font family
%global fontpkgheader3    %{expand:
Obsoletes: khmeros-base-fonts < 5.0-31
Provides: khmeros-base-fonts = %{version}-%{release}
}
%global fonts3            KhmerOS_content.ttf
%global fontconfs3        %{SOURCE3}
%global fontdescription3  %{expand:
%{common_description}

This package provides Content font family.
}

%global fontfamily4       Fasthand
%global fontsummary4      Fasthand font family
%global fontpkgheader4    %{expand:
Obsoletes: khmeros-handwritten-fonts < 5.0-31
Provides: khmeros-handwritten-fonts = %{version}-%{release}
}
%global fonts4            KhmerOS_fasthand.ttf
%global fontconfs4        %{SOURCE4}
%global fontdescription4  %{expand:
%{common_description}

This package provides Fasthand, a handwritten font family.
}

%global fontfamily5       Freehand
%global fontsummary5      Freehand font family
%global fontpkgheader5    %{expand:
Obsoletes: khmeros-handwritten-fonts < 5.0-31
Provides: khmeros-handwritten-fonts = %{version}-%{release}
}
%global fonts5            KhmerOS_freehand.ttf
%global fontconfs5        %{SOURCE5}
%global fontdescription5  %{expand:
%{common_description}

This package provides Freehand, a handwritten font family.
}

%global fontfamily6       Metal Chrieng
%global fontsummary6      Metal Chrieng font
%global fontpkgheader6    %{expand:
Obsoletes: khmeros-metal-chrieng-fonts < 5.0-31
Provides: khmeros-metal-chrieng-fonts = %{version}-%{release}
}
%global fonts6            KhmerOS_metalchrieng.ttf
%global fontconfs6        %{SOURCE6}
%global fontdescription6  %{expand:
%{common_description}

This package provides Metal Chrieng font.
}

%global fontfamily7       Muol
%global fontsummary7      Muol normal and Muol Light font family
%global fontpkgheader7    %{expand:
Obsoletes: khmeros-muol-fonts < 5.0-31
Provides: khmeros-muol-fonts = %{version}-%{release}
}
%global fonts7            KhmerOS_muol.ttf KhmerOS_muollight.ttf
%global fontconfs7        %{SOURCE7}
%global fontdescription7  %{expand:
%{common_description}

This package provides Muol normal and Muol Light font family.
}

%global fontfamily8       Muol Pali
%global fontsummary8      Muol Pali font
%global fontpkgheader8    %{expand:
Obsoletes: khmeros-muol-fonts < 5.0-31
Provides: khmeros-muol-fonts = %{version}-%{release}
}
%global fonts8            KhmerOS_muolpali.ttf
%global fontconfs8        %{SOURCE8}
%global fontdescription8  %{expand:
%{common_description}

This package provides Muol Pali font.
}

%global fontfamily9       Siemreap
%global fontsummary9      Siemreap font
%global fontpkgheader9    %{expand:
Obsoletes: khmeros-siemreap-fonts < 5.0-31
Provides: khmeros-siemreap-fonts = %{version}-%{release}
}
%global fonts9            KhmerOS_siemreap.ttf
%global fontconfs9        %{SOURCE9}
%global fontdescription9  %{expand:
%{common_description}

This package provides Siemreap fonts.
}

%global fontfamily10       System
%global fontsummary10      System font
%global fontpkgheader10    %{expand:
Obsoletes: khmeros-base-fonts < 5.0-31
Provides: khmeros-base-fonts = %{version}-%{release}
}
%global fonts10            KhmerOS_sys.ttf
%global fontconfs10        %{SOURCE10}
%global fontdescription10  %{expand:
%{common_description}

This package provides System font family.
}

%fontpkg -a

Source1:        68-%{fontpkgname1}.conf
Source2:        68-%{fontpkgname2}.conf
Source3:        68-%{fontpkgname3}.conf
Source4:        68-%{fontpkgname4}.conf
Source5:        68-%{fontpkgname5}.conf
Source6:        68-%{fontpkgname6}.conf
Source7:        68-%{fontpkgname7}.conf
Source8:        68-%{fontpkgname8}.conf
Source9:        68-%{fontpkgname9}.conf
Source10:       68-%{fontpkgname10}.conf

%fontmetapkg -z 1,2,3,6,9,10

%global muolmetasummary All the Muol font family packages
%global muolmetadescription %{expand:
This meta-package installs all the Muol font family packages.
}

%global handwrittenmetasummary All the handwritten font family packages
%global handwrittenmetadescription %{expand:
This meta-package installs all the handwritten font family packages.
}
%fontmetapkg -n khmer-os-muol-fonts-all -s muolmetasummary -d muolmetadescription -z 7,8

%fontmetapkg -n khmer-os-handwritten-fonts -s handwrittenmetasummary -d handwrittenmetadescription -z 4,5

%prep
%autosetup -n %{archivename}
install -p %{SOURCE11} .
%linuxtext License.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb  3 2023 Akira TAGOH <tagoh@redhat.com> - 5.0-39
- Update fontconfig priority to 68 for
  https://fedoraproject.org/wiki/Changes/NotoFontsForMoreLang

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Parag Nemade <pnemade AT redhat DOT com> - 5.0-37
- Update license tag to SPDX format

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0-33
- Rebuild to test gating tests

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Parag Nemade <pnemade AT redhat DOT com> - 5.0-31
- Convert to new fonts packaging guidelines (rh#1828983)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Parag Nemade <pnemade AT fedoraproject DOT orgf> - 5.0-25
- Update to follow latest packaging guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 30 2014 Pravin Satpute <psatpute At redhat DIT com> - 5.0-19
- Adding metainfo for gnome-software.
- Corrected url

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Jon Ciesla <limburgher@gmail.com> - 5.0-15
- Remove old obsoletes, BZ 880479.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Parag <pnemade AT redhat.com> - 5.0-13
- Resolves:rh#837520 - Malformed fontconfig config file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 12 2010 Parag <pnemade AT redhat.com> - 5.0-10
- Added License.txt in -common

* Thu May 20 2010 Parag <pnemade AT redhat.com> - 5.0-9
- Resolves:rh#586253 - No fontconfig config files provided

* Tue Feb 16 2010 Parag <pnemade AT redhat.com> - 5.0-8
- drop -common owning %%{_fontdir}
 
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Michal Nowak <mnowak@redhat.com> - 5.0-5
- provide Obsoletes and dependency on -common pkg

* Fri Jan 23 2009 Michal Nowak <mnowak@redhat.com> - 5.0-4
- changes to comply with F11 font rules

* Tue Jul 8 2008 Michal Nowak <mnowak@redhat.com> - 5.0-3
- reshaping to multiple subpackages based on font type/purpose
- license uncertainity is solved; licence field is set according
  to information from .ttf files read via gnome-font-viewer

* Mon Jul 7 2008 Michal Nowak <mnowak@redhat.com> - 5.0-2
- removing Fedora specific license
- refactoring summary and description texts (Nicolas Mailhot)

* Fri Jul 4 2008 Michal Nowak <mnowak@redhat.com> - 5.0-1
- initial release

