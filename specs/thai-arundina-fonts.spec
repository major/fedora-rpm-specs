# SPDX-License-Identifier: MIT

%global archivename fonts-sipa-arundina-%{version}

BuildArch: noarch
BuildRequires: fontforge make

Version: 0.2.2
Release: 17%{?dist}
License: Bitstream-Vera
URL:     http://linux.thai.net/projects/fonts-sipa-arundina

%global foundry           Thai
%global fontlicenses      COPYING
%global fontdocs          README AUTHORS NEWS

%global common_description %{expand:
Arundina fonts were created aiming at Bitstream Vera / Dejavu \
compatibility, under SIPA's initiation.  They were then further \
modified by TLWG for certain aspects, such as Latin glyph size \
compatibility and OpenType conformance.
}

%global fontfamily1       Arundina Sans
%global fontsummary1      Variable-width sans-serif Thai Arundina fonts
%global fontpkgheader1    %{expand:
Obsoletes:       %{name}-common < 0.2.2-13
Provides:        %{name}-common = %{version}-%{release}
}
%global fonts1            arundina/ArundinaSans.ttf arundina/ArundinaSans-Bold.ttf arundina/ArundinaSans-Oblique.ttf arundina/ArundinaSans-BoldOblique.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

This package consists of the Thai Arundina sans-serif variable-width
font faces.
}

%global fontfamily2       Arundina Serif
%global fontsummary2      Variable-width serif Thai Arundina fonts
%global fontpkgheader2    %{expand:
Obsoletes:       %{name}-common < 0.2.2-13
Provides:        %{name}-common = %{version}-%{release}
}
%global fonts2            arundina/ArundinaSerif.ttf arundina/ArundinaSerif-Bold.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This package consists of the Thai Arundina serif variable-width
font faces.
}

%global fontfamily3       Arundina Sans Mono
%global fontsummary3      Monospace sans-serif Thai Arundina fonts
%global fontpkgheader3    %{expand:
Obsoletes:       %{name}-common < 0.2.2-13
Provides:        %{name}-common = %{version}-%{release}
}
%global fonts3            arundina/ArundinaSansMono.ttf arundina/ArundinaSansMono-Bold.ttf arundina/ArundinaSansMono-Oblique.ttf arundina/ArundinaSansMono-BoldOblique.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This package consists of the Thai Arundina sans-serif monospace font
faces.
}


Source0:  http://linux.thai.net/pub/thailinux/software/fonts-sipa-arundina/%{archivename}.tar.xz
Source11: 67-thai-arundina-sans-fonts.conf
Source12: 67-thai-arundina-serif-fonts.conf
Source13: 67-thai-arundina-sans-mono-fonts.conf

Name:     thai-arundina-fonts
Summary:  Thai Arundina fonts
%description
%wordwrap -v common_description

%fontpkg -a

%prep
%setup -q -n %{archivename}
%linuxtext %{fontdocs}

%build
%configure
make
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr  3 2023 Peng Wu <pwu@redhat.com> - 0.2.2-13
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Peng Wu <pwu@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 10 2016 Daiki Ueno <dueno@redhat.com> - 0.2.1-1
- new upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 16 2014 Richard Hughes <richard@hughsie.com> - 0.2.0-6
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 15 2012 Daiki Ueno <dueno@redhat.com> - 0.2.0-1
- new upstream release
- change %%archivename to fonts-sipa-arundina per upstream

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Daiki Ueno <dueno@redhat.com> - 0.1.3-1
- new upstream release

* Thu Mar 31 2011 Daiki Ueno <dueno@redhat.com> - 0.1.2-2
- add fontconfig files
- remove buildroot cleanup in %%install

* Mon Mar 28 2011 Daiki Ueno <dueno@redhat.com> - 0.1.2-1
- initial packaging for Fedora
