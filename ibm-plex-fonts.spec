# SPDX-License-Identifier: MIT

Name:    ibm-plex-fonts
Version: 6.0.0
Release: 2%{?dist}
Summary: IBM Plex, the new IBM set of coordinated grotesque corporate fonts

License: OFL
URL:     https://www.ibm.com/plex/

BuildArch: noarch

%global foundry           IBM
%global fontlicense       OFL
%global fontlicenses      IBM-Plex-Sans/license.txt
#global fontdocs          *.md

%global common_description %{expand:
IBM wanted Plex to be a distinctive, yet timeless workhorse — an alternative to
its previous corporate font family, “Helvetica Neue”, for this new era. The
Grotesque style was the perfect fit. Not only do Grotesque font families
balance human and rational elements, the Grotesque style also came about during
the Industrial Age, when IBM was born.
}

%global fontfamily1       Plex Sans
%global fontsummary1      IBM Plex Sans, the new grotesque IBM corporate font family
%global fontpkgheader1    %{expand:
Suggests: font(ibmplexsansmono)
Obsoletes: ibm-plex-fonts-common          < %{version}-%{release}
Obsoletes: ibm-plex-sans-arabic-fonts     < %{version}-%{release}
Obsoletes: ibm-plex-sans-condensed-fonts  < %{version}-%{release}
Obsoletes: ibm-plex-sans-devanagari-fonts < %{version}-%{release}
Obsoletes: ibm-plex-sans-hebrew-fonts     < %{version}-%{release}
Obsoletes: ibm-plex-sans-thai-fonts       < %{version}-%{release}
}
%global fonts1            IBM-Plex-Sans/*.otf IBM-Plex-Sans-Condensed/*.otf IBM-Plex-Sans-Arabic/*.otf IBM-Plex-Sans-Hebrew/*.otf IBM-Plex-Sans-Thai/*.otf IBM-Plex-Sans-Devanagari/*.otf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}
This package provides the grotesque sans-serif variable-width IBM Plex Sans,
the main font family of the Plex set.}

%global fontfamily2       Plex Mono
%global fontsummary2      IBM Plex Mono, the monospace grotesque coding font family of the Plex set
%global fonts2            IBM-Plex-Mono/*.otf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}
This package provides the grotesque sans-serif fixed-width IBM Plex Mono, a
little something for developers, because monospace does not need to be monotone.}

%global fontfamily3       Plex Serif
%global fontsummary3      IBM Plex Serif, the hybrid grotesque serif font family of the Plex set
%global fonts3            IBM-Plex-Serif/*.otf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}
This package provides the hybrid grotesque serif variable-width IBM Plex Serif,
combining the best of Plex, Bodoni, and Janson into a contemporary serif.}

%global fontfamily4       Plex Sans Thai Looped
%global fontsummary4      IBM Plex Sans Thai Looped, a formal variant of IBM Plex Sans for Thai
%global fontpkgheader4    %{expand:
Requires: ibm-plex-sans-fonts
Enhances: ibm-plex-sans-fonts
}
%global fonts4            IBM-Plex-Sans-Thai-Looped/*.otf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}
This package provides a more formal and traditional form of Thai for the
grotesque sans-serif variable-width IBM Plex Sans, that includes loops.}

Source0:  https://github.com/IBM/plex/releases/download/v%{version}/OpenType.zip#/%{name}-%{version}.zip
Source11: 58-%{fontpkgname1}.xml
Source12: 58-%{fontpkgname2}.xml
Source13: 58-%{fontpkgname3}.xml
Source14: 59-%{fontpkgname4}.xml

%description
%{common_description}

%fontpkg -a

%fontmetapkg

%prep
%setup -n OpenType

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 01 2022 Michael Kuhn <suraia@fedoraproject.org> - 6.0.0-1
- Update to 6.0.0

* Tue Feb 01 2022 Michael Kuhn <suraia@fedoraproject.org>
- Fix packaging problems

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.0.2-7
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.0.2-6
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.0.2-5
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.0.2-4
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.0.2-3
✅ Convert to fonts-rpm-macros use

* Sun Sep 08 2019 Michael Kuhn <suraia@fedoraproject.org> - 2.0.0-1
- Initial package
