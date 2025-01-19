Version:	1.051
Release:	6%{?dist}
URL:		https://github.com/googlefonts/morisawa-biz-ud-gothic

%global	foundry		MRSW
%global	fontlicense	OFL-1.1
%global fontlicenses	OFL.txt
%global fontdocs	README.md
%global fontdocsex	%{fontlicenses}

%global common_description	%{expand:
BIZ UD Gothic is a universal design typeface designed to be easy to
read and ideal for education and business documentation. It is a highly
legible and well-balanced design sans serif. In order to make the kanji
more clear and identifiable, the letterforms are simplified by omitting
hane (hook) and geta (the vertical lines extending beyond horizontal
strokes at the bottom of kanji). Counters and other spaces are finely
adjusted so that the overall balance of the type is not impaired even
with the use in relatively large size. The kana are made slightly
smaller than the kanji to give a good rhythm and flow when setting
long texts in the lighter weights.
}

%global fontfamily0	BIZ UDGothic
%global fontsummary0	Morisawa BIZ UD Gothic fonts, Japanese non-proportional sans-serif typeface
%global	fonts0		fonts/ttf/BIZUDGothic-*.ttf
%global	fontconfs0	%{SOURCE1}
%global fontdescription0	%{expand:
%{common_description}

This package provides a non-proportional sans-serif font.
}

%global fontfamily1	BIZ UDPGothic
%global fontsummary1	Morisawa BIZ UD PGothic fonts, Japanese proportional sans-serif typeface
%global fonts1		fonts/ttf/BIZUDPGothic-*.ttf
%global fontconfs1	%{SOURCE2}
%global fontdescription1	%{expand:
%{common_description}

This package provides a proportional sans-serif font.
}

Source0:	https://github.com/googlefonts/morisawa-biz-ud-gothic/archive/refs/tags/v%{version}.zip#/morisawa-biz-ud-gothic-%{version}.zip
Source1:	%{fontpkgname0}.fontconfig.conf
Source2:	%{fontpkgname1}.fontconfig.conf
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib


%fontpkg -a

%fontmetapkg

%prep
%autosetup -n morisawa-biz-ud-gothic-%{version}

%build 
%fontbuild -a

%install
%fontinstall -a

%check	
%fontcheck -a

%fontfiles -a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.051-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.051-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.051-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.051-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Akira TAGOH <tagoh@redhat.com> - 1.051-2
- Improve Summary.

* Tue Dec 19 2023 Akira TAGOH <tagoh@redhat.com> - 1.051-1
- New upstream release.

* Tue Mar 29 2022 Akira TAGOH <tagoh@redhat.com> - 1.002-1
- New upstream release.

* Fri Mar 25 2022 Akira TAGOH <tagoh@redhat.com> - 1.001-1
- initial release
