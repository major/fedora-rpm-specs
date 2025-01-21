# SPDX-License-Identifier: MIT

%global fontname    un-extra
%global alphatag    080608
%global archivename un-fonts-extra


BuildArch: noarch

Version: 1.0.2
Release: 0.41.%{alphatag}%{?dist}
License: GPL-2.0-only
URL:     http://kldp.net/projects/unfonts/

%global foundry           Un
%global fontlicenses      COPYING
%global fontdocs          README

%global common_description %{expand:
The UN set of Korean TrueType fonts is derived from the HLaTeX Type1 fonts \
made by Koaunghi Un in 1998. They were converted to TrueType with \
FontForge(PfaEdit) by Won-kyu Park in 2003. \
The Un Extra set is composed of: \
\
- UnPen, UnPenheulim: script \
- UnTaza: typewriter style \
- UnBom: decorative \
- UnShinmun \
- UnYetgul: old Korean printing style \
- UnJamoSora, UnJamoNovel, UnJamoDotum, UnJamoBatang \
- UnVada \
- UnPilgia: script
}

%global fontfamily1       Un Extra Bom
%global fontsummary1      Un Extra fonts - UnBom
%global fonts1            UnBom.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

This package includes UnBom, a decorative font.
}

%global fontfamily2       Un Extra JamoBatang
%global fontsummary2      Un Extra fonts - UnJamoBatang
%global fonts2            UnJamoBatang.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This package includes the UnJamoBatang font.
}

%global fontfamily3       Un Extra JamoDotum
%global fontsummary3      Un Extra fonts - UnJamoDotum
%global fonts3            UnJamoDotum.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This package includes the UNJamoDotum font.
}

%global fontfamily4       Un Extra JamoNovel
%global fontsummary4      Un Extra fonts - UnJamoNovel
%global fonts4            UnJamoNovel.ttf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

This package includes the UNJamoNovel font.
}

%global fontfamily5       Un Extra JamoSora
%global fontsummary5      Un Extra fonts - UnJamoSora
%global fonts5            UnJamoSora.ttf
%global fontconfs5        %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}

This package includes the UNJamoSora font.
}

%global fontfamily6       Un Extra Pen
%global fontsummary6      Un Extra fonts - UnPen
%global fonts6            UnPen.ttf
%global fontconfs6        %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}

This package includes UnPen, a script font.
}

%global fontfamily7       Un Extra Penheulim
%global fontsummary7      Un Extra fonts - UnPenheulim
%global fonts7            UnPenheulim.ttf
%global fontconfs7        %{SOURCE17}
%global fontdescription7  %{expand:
%{common_description}

This package includes UnPenheulim, a script font.
}

%global fontfamily8       Un Extra Pilgia
%global fontsummary8      Un Extra fonts - UnPilgia
%global fonts8            UnPilgia.ttf
%global fontconfs8        %{SOURCE18}
%global fontdescription8  %{expand:
%{common_description}

This package includes UnPilgia, a script font.
}

%global fontfamily9       Un Extra Shinmun
%global fontsummary9      Un Extra fonts - UnShinmun
%global fonts9            UnShinmun.ttf
%global fontconfs9        %{SOURCE19}
%global fontdescription9  %{expand:
%{common_description}

This package includes the UnShinmun font.
}

%global fontfamily10       Un Extra Taza
%global fontsummary10      Un Extra fonts - UnTaza
%global fontpkgheader10    %{expand:
Obsoletes:       %{name}-common < 1.0.2-0.36.080608
Provides:        %{name}-common = %{version}-%{release}
}
%global fonts10            UnTaza.ttf
%global fontconfs10        %{SOURCE20}
%global fontdescription10  %{expand:
%{common_description}

This package includes UnTaza, a typewriter font.
}

%global fontfamily11       Un Extra Vada
%global fontsummary11      Un Extra fonts - UnVada
%global fonts11            UnVada.ttf
%global fontconfs11        %{SOURCE21}
%global fontdescription11  %{expand:
%{common_description}

This package includes the UnVada font.
}

%global fontfamily12       Un Extra Yetgul
%global fontsummary12      Un Extra fonts - UnYetgul
%global fonts12            UnYetgul.ttf
%global fontconfs12        %{SOURCE22}
%global fontdescription12  %{expand:
%{common_description}

This package includes UnYetgul, an old Korean printing font.
}


Source0:  http://kldp.net/frs/download.php/4696/%{archivename}-%{version}-%{alphatag}.tar.gz
Source11: 67-un-extra-bom-fonts.conf
Source12: 67-un-extra-jamobatang-fonts.conf
Source13: 67-un-extra-jamodotum-fonts.conf
Source14: 67-un-extra-jamonovel-fonts.conf
Source15: 67-un-extra-jamosora-fonts.conf
Source16: 67-un-extra-pen-fonts.conf
Source17: 67-un-extra-penheulim-fonts.conf
Source18: 67-un-extra-pilgia-fonts.conf
Source19: 67-un-extra-shinmun-fonts.conf
Source20: 67-un-extra-taza-fonts.conf
Source21: 67-un-extra-vada-fonts.conf
Source22: 67-un-extra-yetgul-fonts.conf

Name:     %{fontname}-fonts
Summary:  Un Extra family of Korean TrueType fonts
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
%setup -q -n un-fonts
%linuxtext COPYING README

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.41.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.40.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.39.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.38.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Peng Wu <pwu@redhat.com> - 1.0.2-0.37.080608
- Fix dnf upgrade issue

* Tue Apr 11 2023 Peng Wu <pwu@redhat.com> - 1.0.2-0.36.080608
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.35.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.34.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.33.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.32.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.31.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.30.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.29.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.28.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.27.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.26.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.25.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.24.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.23.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.22.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.21.080608
- replace %%define uses with %%global

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.20.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.19.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.18.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.17.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.16.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.15.080608%{?dist}
- fix <test> usage in fontconfig files (Closes: #837536)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.14.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.13.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 25 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.12.080608
- fix trivial typos in fontconfig config files

* Fri May 21 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.11.080608
- use locale-specific overrides in fontconfig.conf

* Mon Apr 26 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.10.080608
- convert to new font packaging guidelines (#477475)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.9.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.8.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 13 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.7.080608
- fixed subpackage description and fontconfig

* Sun Oct 12 2008 Nicolas Mailhot <nicolas dot mailhot at laposte dot net> - 1.0.2-0.6.080608
- complete the subpackages
- revert subpackage description macroization, it's not worth it

* Wed Oct 08 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.5.080608
- add subpackages with a macro
- add description

* Mon Jul 07 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.4.080608
- Refined .spec literal

* Sun Jul 06 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.3.080608
- Added or Changed a Summary and Description.
- Removed nil item.
- Refined versioning contents.
- Renamed from un-fonts-extra.spec

* Thu Jul 03 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.2.080608
- Refined .spec literal, license, versioning contents.

* Sat Jun 28 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.1.080608
- Initial release.
