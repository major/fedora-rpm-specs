# SPDX-License-Identifier: MIT
Version: 1.8
Release: %autorelease
URL:     http://arkandis.tuxfamily.org/adffonts.html

%global foundry           ADF
%global fontlicense       GPL-2.0-or-later WITH Font-exception-2.0
%global fontlicenses      OTF/COPYING
%global fontdocs          NOTICE.txt

%global common_description %{expand:
A Latin font family published by Hirwen Harendal’s Arkandis Digital Foundry,
Accanthis was inspired from the “Cloister Oldstyle” font family found in the
“American Specimen Book of Typefaces Suplement”. Its medium contrast is
sufficient to be reader-friendly and deliver an elegant and refined experience.

Accanthis is a modernized garaldic font family and is well suited to book
typesetting and refined presentations.}

%global fontfamily0       Accanthis
%global fontsummary0      ADF Accanthis, a modernized garaldic serif font family, “Galliard” alternative
%global fontpkgheader0    %{expand:
Obsoletes: adf-accanthis-fonts-common < %{version}-%{release}
}
%global fonts0            OTF/AccanthisADFStd-*.otf
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

This variant is intended to serve as alternative to the “Galliard” font family.}

%global fontfamily2       Accanthis-2
%global fontsummary2      ADF Accanthis Nᵒ2, a modernized garaldic serif, “Horley old style” alternative
%global fonts2            OTF/AccanthisADFStdNo2-*.otf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This variant is closer to the “Horley old style” font family than the original
version.}

%global fontfamily3       Accanthis-3
%global fontsummary3      ADF Accanthis Nᵒ3, a modernized garaldic serif font family
%global fonts3            OTF/AccanthisADFStdNo3-*.otf
%global fontconfngs3      %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This variant remixes a slightly modified Accanthis №2 with elements from the
original Italic and changes to k, p, z and numbers.}

%global archivename Accanthis-Std-20101124

Source0:   http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   http://arkandis.tuxfamily.org/docs/Accanthis-Cat.pdf
Source10:  60-%{fontpkgname}.xml
Source12:  60-%{fontpkgname2}.xml
Source13:  60-%{fontpkgname3}.xml


%fontpkg -a

%fontmetapkg

%package   doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
%linuxtext NOTICE.txt OTF/COPYING

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%files doc
%defattr(644, root, root, 0755)
%license OTF/COPYING
%doc *.pdf

%changelog
%autochangelog
