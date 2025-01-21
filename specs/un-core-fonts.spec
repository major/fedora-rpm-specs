# SPDX-License-Identifier: MIT

%global fontname un-core
%global alphatag 080608
%global archivename un-fonts-core-%{version}-%{alphatag}

BuildArch: noarch

Version: 1.0.2
Release: 0.48.%{alphatag}%{?dist}
License: GPL-2.0-only
URL:     http://kldp.net/projects/unfonts/

%global foundry           Un
%global fontlicenses      COPYING
%global fontdocs          README

%global common_description %{expand:
The UN set of Korean TrueType fonts is derived from the HLaTeX Type1 fonts \
made by Koaunghi Un in 1998. They were converted to TrueType with \
FontForge(PfaEdit) by Won-kyu Park in 2003. \
The Un Core set is composed of: \
\
- UnBatang: serif \
- UnDinaru: fantasy \
- UnDotum: sans-serif \
- UnGraphic: sans-serif style \
- UnGungseo: cursive, brush-stroke \
- UnPilgi: script
}

%global fontfamily1       Un Core Batang
%global fontsummary1      Un Core fonts - UnBatang
%global fonts1            UnBatang.ttf UnBatangBold.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

This package includes UnBatang, a serif font.
}

%global fontfamily2       Un Core Dinaru
%global fontsummary2      Un Core fonts - UnDinaru
%global fonts2            UnDinaru.ttf UnDinaruLight.ttf UnDinaruBold.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This package includes UnDinaru, a fantasy font.
}

%global fontfamily3       Un Core Dotum
%global fontsummary3      Un Core fonts - UnDotum
%global fontpkgheader3    %{expand:
Obsoletes:       %{name}-common < 1.0.2-0.43.080608
Provides:        %{name}-common = %{version}-%{release}
}
%global fonts3            UnDotum.ttf UnDotumBold.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This package includes UnDotum, a sans-serif font.
}

%global fontfamily4       Un Core Graphic
%global fontsummary4      Un Core fonts - UnGraphic
%global fonts4            UnGraphic.ttf UnGraphicBold.ttf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

This package includes UnGraphic, a sans-serif font.
}

%global fontfamily5       Un Core Gungseo
%global fontsummary5      Un Core fonts - UnGungseo
%global fonts5            UnGungseo.ttf
%global fontconfs5        %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}

This package includes UnGungseo, a cursive font.
}

%global fontfamily6       Un Core Pilgi
%global fontsummary6      Un Core fonts - UnPilgi
%global fonts6            UnPilgi.ttf UnPilgiBold.ttf
%global fontconfs6        %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}

This package includes UnPilgi, a script font.
}


Source0:  http://kldp.net/frs/download.php/4695/%{archivename}.tar.gz
Source11: 67-un-core-batang-fonts.conf
Source12: 67-un-core-dinaru-fonts.conf
Source13: 67-un-core-dotum-fonts.conf
Source14: 67-un-core-graphic-fonts.conf
Source15: 67-un-core-gungseo-fonts.conf
Source16: 67-un-core-pilgi-fonts.conf

Name:     %{fontname}-fonts
Summary:  Un Core family of Korean TrueType fonts
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
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.48.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.47.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.46.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.45.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Peng Wu <pwu@redhat.com> - 1.0.2-0.44.080608
- Fix dnf upgrade issue

* Mon Apr 10 2023 Peng Wu <pwu@redhat.com> - 1.0.2-0.43.080608
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.42.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.41.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.40.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.39.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.38.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.37.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.36.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.35.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 1.0.2-0.34.080608
- Install metainfo files under %%{_metainfodir}.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.33.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.32.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jan 30 2018 Akira TAGOH <tagoh@redhat.com> - 1.0.2-0.31.080608
- Update the priority to change the default font to Noto.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.30.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Richard Hughes <rhughes@redhat.com> - 1.0.2-0.29.080608
- Actually install the AppData files

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.28.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.27.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan  6 2016 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.26.080608
- replace %%define uses with %%global

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.25.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-0.24.080608
- Add metainfo file to show this font in gnome-software
- Remove group tag
- Remove buildroot tag

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.23.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.22.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.21.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.20.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.19.080608%{?dist}
- fix <test> usage in fontconfig files (Closes: #837525)

* Mon Feb  6 2012 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.18.080608
- update the priority for the Korean default font change
  nhn-nanum-fonts -> 65-0, un-core-fonts -> 65-1, baekmuk-ttf-fonts -> 65-2
- drop buildroot cleanup
- drop %%defattr(0644,root,root,0755) from %%files

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.17.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.16.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 25 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.15.080608
- fix trivial typos in fontconfig config files (thanks Akira TAGOH)

* Wed May 12 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.14.080608
- add "ko" as well as "ko-kr" to the lang test of .conf files to avoid
  some glyphs to be rendered with wqy-zenhei-fonts

* Thu May  6 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.13.080608
- assign higher priority (65- -> 65-0-) to .conf files to avoid the
  effects of 65-nonlatin.conf
- remove binding="same" from .conf files

* Tue May  4 2010 Jens Petersen <petersen@redhat.com> - 1.0.2-0.12.080608
- update .conf files to be locale-specific (#586877)

* Mon Apr 26 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.11.080608
- use _font_pkg macro (#581734)
- don't install un-core-fonts-*{light,bold}-fontconfig.conf

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.10.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Jens Petersen <petersen@redhat.com> - 1.0.2-0.9.080608
- update to new fonts packaging and naming (#477474)
- moved bold (and light) weights into main subpackages (#468618)
- add obsoletes for renaming and former bold subpackages (#468618)

* Fri Jun 26 2009 Jens Petersen <petersen@redhat.com> - 1.0.2-0.8.080608
- fix filelist to only include specific font (#496795)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.7.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 14 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.6.080608
- fixed subpackage description and fontconfig.

* Wed Jul 16 2008 Jens Petersen <petersen@redhat.com> - 1.0.2-0.5.080608
- add subpackages with a macro

* Mon Jul 07 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.4.080608
- Refined .spec literal

* Sun Jul 06 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.3.080608
- Added or Changed a Summary and Description.
- Removed nil item.
- Refined versioning contents.
- Renamed from un-fonts-core.spec

* Thu Jul 03 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.2.080608
- Refined .spec literal, license, versioning contents.

* Sat Jun 28 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.1.080608
- Initial release.
