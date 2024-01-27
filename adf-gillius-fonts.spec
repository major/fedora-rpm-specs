# SPDX-License-Identifier: MIT
Version: 1.009
Release: %autorelease
URL:     http://arkandis.tuxfamily.org/adffonts.html

%global foundry           ADF
%global fontlicense       GPL-2.0-or-later WITH Font-exception-2.0
%global fontlicenses      OTF/COPYING
%global fontdocs          NOTICE

%global common_description %{expand:
The Gillius family from the Arkandis Digital Foundry is a set of sans-serif
typefaces intended as an alternative to Gill Sans. Its two widths, regular and
condensed, both feature a roman and an italic, and each includes a regular and
bold weight.
}

%global fontfamily0       Gillius
%global fontsummary0      ADF Gillius sans-serif typeface family, a GillSans alternative
%global fontpkgheader0    %{expand:
Obsoletes: adf-gillius-fonts-common < %{version}-%{release}
}
%global fonts0            OTF/GilliusADF-*
%global fontconfs0        %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

This is the base variant.}

%global fontfamily2       Gillius-2
%global fontsummary2      ADF Gillius No2 sans-serif typeface family. a GillSans alternative
%global fonts2            OTF/GilliusADFNo2-*
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

A slightly rounder variant, which features the same set of weights,
widths, and slopes.}


%global archivename Gillius-Collection-20110312

Source0:   http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   http://arkandis.tuxfamily.org/docs/%{fontfamily}-cat.pdf
Source10:  69-%{fontpkgname}.conf
Source12:  69-%{fontpkgname2}.conf



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
%linuxtext NOTICE OTF/COPYING

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
