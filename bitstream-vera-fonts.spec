# SPDX-License-Identifier: MIT
Version: 1.10
Release: 47%{?dist}
License: Bitstream Vera
URL:     http://www.gnome.org/fonts/

BuildArch: noarch

%global source_name       bitstream-vera-fonts

%global foundry           Bitstream
%global fontlicenses      COPYRIGHT.TXT
%global fontdocs          *.TXT
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
The Vera font families are high-quality Latin typefaces donated by Bitstream.}

%global fontfamily1       Vera Sans
%global fontsummary1      Bitstream Vera Sans, a variable-width sans-serif font family
%global fontpkgheader1    %{expand:
Obsoletes: bitstream-vera-fonts-common < %{version}-%{release}
Suggests: font(dejavusans)
}
%global fonts1            *.ttf
%global fontconfngs1      %{SOURCE11}
%global fontsex1          %{fonts2} %{fonts3}
%global fontdescription1 %{expand:
%{common_description}

This package consists of the Bitstream Vera Sans sans-serif variable-width
font family.}

%global fontfamily2       Vera Serif
%global fontsummary2      Bitstream Vera Serif, a variable-width serif font family
%global fontpkgheader2    %{expand:
Suggests: font(dejavuserif)
}
%global fonts2            VeraSe*ttf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2 %{expand:
%{common_description}

This package consists of the Bitstream Vera Serif serif variable-width font
family.}

%global fontfamily3       Vera Sans Mono
%global fontsummary3      Bitstream Vera Sans Mono, a mono-space sans-serif font family
%global fontpkgheader3    %{expand:
Suggests: font(dejavusansmono)
}
%global fonts3            VeraMo*ttf
%global fontconfngs3      %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This package consists of the Bitstream Vera Sans Mono mono-space sans-serif font
family.}

%global archivename ttf-bitstream-vera

Source0:  ftp://ftp.gnome.org/pub/GNOME/sources/%{archivename}/%{version}/%{archivename}-%{version}.tar.bz2
Source11: 55-%{fontpkgname1}.xml
Source12: 55-%{fontpkgname2}.xml
Source13: 55-%{fontpkgname3}.xml

Name:     bitstream-vera-fonts
Summary:  The Bitstream Vera font families
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
%setup -q -n %{archivename}-%{version}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 03 2021 David King <amigadave@amigadave.com> - 1.10-44
- Fix build in F34+ (#1930508)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.10-42
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.10-41
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.10-40
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.10-39
✅ Lint, lint, lint and lint again

* Thu Feb 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.10-38
✅ Switch fontconfig priority to 55

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.10-37
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.10-36
✅ Convert to fonts-rpm-macros use

* Tue Jun 10 2003 Owen Taylor <otaylor@redhat.com> 1.10-1
- Base package on spec file from Nicolas Mailhot <nim@fedoraproject.org>
- Cleanups from Warren Togami and Nicolas Mailhot
