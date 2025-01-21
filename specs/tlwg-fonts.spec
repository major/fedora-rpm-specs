# SPDX-License-Identifier: MIT

%global fontname tlwg-fonts
%global archivename fonts-tlwg

BuildArch: noarch
BuildRequires: make
BuildRequires: fontforge >= 20071110

Version: 0.7.3
Release: 12%{?dist}
License: GPL-2.0-or-later AND Bitstream-Vera
URL:     https://linux.thai.net/projects/fonts-tlwg

%global foundry           TLWG
%global fontlicenses      COPYING
%global fontdocs          AUTHORS README NEWS

%global common_description %{expand:
%{archivename} provides a collection of free scalable Thai fonts.
}

%global obsoletes_thai()\
%define familyname %1 \
Obsoletes:       thai-scalable-%{familyname}-fonts < 0.7.3-7 \
Provides:        thai-scalable-%{familyname}-fonts = %{version}-%{release} \

%global fontfamily1       Garuda
%global fontsummary1      Thai Garuda fonts
%global fontpkgheader1    %{expand:
%obsoletes_thai garuda
}
%global fonts1            nf/Garuda*.otf
%global fontconfs1        %{SOURCE13}
%global fontdescription1  %{expand:
%{common_description}

This package provides the Garuda family of Thai fonts.
}

%global fontfamily2       Kinnari
%global fontsummary2      Thai Kinnari fonts
%global fontpkgheader2    %{expand:
%obsoletes_thai kinnari
}
%global fonts2            nf/Kinnari*.otf
%global fontconfs2        %{SOURCE14}
%global fontdescription2  %{expand:
%{common_description}

This package provides the Kinnari family of Thai fonts.
}

%global fontfamily3       Loma
%global fontsummary3      Thai Loma fonts
%global fontpkgheader3    %{expand:
%obsoletes_thai loma
}
%global fonts3            nectec/Loma*.otf
%global fontdescription3  %{expand:
%{common_description}

This package provides the Loma family of Thai fonts.
}

%global fontfamily4       Norasi
%global fontsummary4      Thai Norasi fonts
%global fontpkgheader4    %{expand:
%obsoletes_thai norasi
}
%global fonts4            nf/Norasi*.otf
%global fontconfs4        %{SOURCE11}
%global fontdescription4  %{expand:
%{common_description}

This package provides the Norasi family of Thai fonts.
}

%global fontfamily5       Purisa
%global fontsummary5      Thai Purisa fonts
%global fontpkgheader5    %{expand:
%obsoletes_thai purisa
}
%global fonts5            tlwg/Purisa*.otf
%global fontdescription5  %{expand:
%{common_description}

This package provides the Purisa family of Thai fonts.
}

%global fontfamily6       Sawasdee
%global fontsummary6      Thai Sawasdee fonts
%global fontpkgheader6    %{expand:
%obsoletes_thai sawasdee
}
%global fonts6            tlwg/Sawasdee*.otf
%global fontdescription6  %{expand:
%{common_description}

This package provides the Sawasdee family of Thai fonts.
}

%global fontfamily7       Tlwg Mono
%global fontsummary7      Thai Tlwg Mono fonts
%global fontpkgheader7    %{expand:
%obsoletes_thai tlwgmono
}
%global fonts7            tlwg/TlwgMono*.otf
%global fontdescription7  %{expand:
%{common_description}

This package provides the Tlwg Mono family of Thai fonts.
}

%global fontfamily8       Tlwg Typewriter
%global fontsummary8      Thai Tlwg Typewriter fonts
%global fontpkgheader8    %{expand:
%obsoletes_thai tlwgtypewriter
}
%global fonts8            tlwg/TlwgTypewriter*.otf
%global fontdescription8  %{expand:
%{common_description}

This package provides the Tlwg Typewriter family of Thai fonts.
}

%global fontfamily9       Tlwg Typist
%global fontsummary9      Thai Tlwg Typist fonts
%global fontpkgheader9    %{expand:
%obsoletes_thai tlwgtypist
}
%global fonts9            tlwg/TlwgTypist*.otf
%global fontdescription9  %{expand:
%{common_description}

This package provides the Tlwg Typist family of Thai fonts.
}

%global fontfamily10       Tlwg Typo
%global fontsummary10      Thai Tlwg Typo fonts
%global fontpkgheader10    %{expand:
%obsoletes_thai tlwgtypo
}
%global fonts10            tlwg/TlwgTypo*.otf
%global fontdescription10  %{expand:
%{common_description}

This package provides the Tlwg Typo family of Thai fonts.
}

%global fontfamily11       Umpush
%global fontsummary11      Thai Umpush fonts
%global fontpkgheader11    %{expand:
%obsoletes_thai umpush
}
%global fonts11            tlwg/Umpush*.otf
%global fontconfs11        %{SOURCE16}
%global fontdescription11  %{expand:
%{common_description}

This package provides the Umpush family of Thai fonts.
}

%global fontfamily12       Laksaman
%global fontsummary12      Thai Laksaman fonts
%global fontpkgheader12    %{expand:
%obsoletes_thai laksaman
}
%global fonts12            sipa/Laksaman*.otf
%global fontconfs12        %{SOURCE15}
%global fontdescription12  %{expand:
%{common_description}

This package provides the Laksaman family of Thai fonts.
}

%global fontfamily13       Waree
%global fontsummary13      Thai Waree fonts
%global fontpkgheader13    %{expand:
Obsoletes: thai-scalable-fonts-common < 0.7.3-7
Provides:  thai-scalable-fonts-common = %{version}-%{release}
%obsoletes_thai waree
}
%global fonts13            tlwg/Waree*.otf
%global fontconfs13        %{SOURCE12}
%global fontdescription13  %{expand:
%{common_description}

This package provides the Waree family of Thai fonts.
}


Source0:  http://linux.thai.net/pub/ThaiLinux/software/%{archivename}/%{archivename}-%{version}.tar.xz
Source11: 68-thai-scalable-norasi.conf
Source12: 68-thai-scalable-waree.conf
Source13: 90-thai-scalable-synthetic-garuda.conf
Source14: 90-thai-scalable-synthetic-kinnari.conf
Source15: 90-thai-scalable-synthetic-laksaman.conf
Source16: 90-thai-scalable-synthetic-umpush.conf


Name:     tlwg-fonts
Summary:  Thai TrueType fonts
%description
%wordwrap -v common_description


%fontpkg -a

%prep
%setup -q -n %{archivename}-%{version}

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
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Peng Wu <pwu@redhat.com> - 0.7.3-8
- Fix dnf upgrade issue
- Resolves: RHBZ#2214507

* Tue May 23 2023 Peng Wu <pwu@redhat.com> - 0.7.3-7
- Renamed from thai-scalable-fonts
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license
