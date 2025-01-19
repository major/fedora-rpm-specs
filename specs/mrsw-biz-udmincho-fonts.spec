Version:	1.06
Release:	6%{?dist}
URL:		https://github.com/googlefonts/morisawa-biz-ud-mincho

%global	foundry		MRSW
%global	fontlicense	OFL-1.1
%global fontlicenses	OFL.txt
%global fontdocs	README.md
%global fontdocsex	%{fontlicenses}

%global common_description	%{expand:
BIZ UD Mincho is a universal design typeface designed to be easy to
read and ideal for education and business documentation. It combines
high quality in readability and legibility while carrying on the stately
Japanese Mincho type tradition. BIZ UD Mincho bases its design on one of
the typefaces from the Morisawa font library, which has thicker horizontal
lines than the traditional Mincho type style. Because most Mincho types
have thin horizontal strokes, the style can be difficult to read on some
displays or signs and for people with low vision. For the universal
design version, dakuten (゛) and handakuten (゜) voicing marks are designed
to be more legible, and the letterforms are adjusted to maintain their
balance while having a larger face and wider counters.
}

%global fontfamily0	BIZ UDMincho
%global fontsummary0	Morisawa BIZ UD Mincho fonts, Japanese non-proportional serif typeface
%global	fonts0		fonts/ttf/BIZUDMincho-*.ttf
%global	fontconfs0	%{SOURCE1}
%global fontdescription0	%{expand:
%{common_description}

This package provides a non-proportional serif font.
}

%global fontfamily1	BIZ UDPMincho
%global fontsummary1	Morisawa BIZ UD PMincho fonts, Japanese proportional serif typeface
%global fonts1		fonts/ttf/BIZUDPMincho-*.ttf
%global fontconfs1	%{SOURCE2}
%global fontdescription1	%{expand:
%{common_description}

This package provides a proportional serif font.
}

Source0:	https://github.com/googlefonts/morisawa-biz-ud-mincho/archive/refs/tags/v%{version}.zip#/morisawa-biz-ud-mincho-%{version}.zip
Source1:	%{fontpkgname0}.fontconfig.conf
Source2:	%{fontpkgname1}.fontconfig.conf
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib


%fontpkg -a

%fontmetapkg

%prep
%autosetup -n morisawa-biz-ud-mincho-%{version}

%build 
%fontbuild -a

%install
%fontinstall -a

%check	
%fontcheck -a

%fontfiles -a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Akira TAGOH <tagoh@redhat.com> - 1.06-2
- Improve Summary.

* Tue Dec 19 2023 Akira TAGOH <tagoh@redhat.com> - 1.06-1
- New upstream release.

* Tue Mar 29 2022 Akira TAGOH <tagoh@redhat.com> - 1.002-1
- New upstream release.

* Fri Mar 25 2022 Akira TAGOH <tagoh@redhat.com> - 1.001-1
- initial release
