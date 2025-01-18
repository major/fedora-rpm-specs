Name: daniel-wikholm-segment16-fonts
Summary: Collection of fonts mimicking 16-segment digital displays
License: CC0-1.0

# I tried looking for the author's personal site, but no luck.
# Thus, I'm using a generic font catalogue website as the source.
URL: https://www.wfonts.com/font/segment16a

Version: 20171229
Release: 8%{?dist}

%global foundry  Daniel Wikholm
%global fontdocs  Segment16.txt
%global fontlicense  CC0
%global fontlicenses  cc0.txt

%global fam() %{expand:Segment16%1}
%global summ() %{expand:Segment16%1, a font mimicking 16-segment digital displays}

# -- Variant A

%global fontfamily1  %{fam A}
%global fontsummary1  %{summ A}

%global fonts1  *16A*.ttf
%global fontconfs1  %{SOURCE11}

%global fontdescription1  %{expand:Segment16A, B and C are three font families, each containing a regular,
bold, italic and bold italic version, based on sixteen segment displays.

In Segment 16A, the diagonal segments extend both to the center
and the outer corners of the character, which might resemble
some, mainly older, LCD sixteen segment alphanumeric displays.}

# -- Variant B

%global fontfamily2  %{fam B}
%global fontsummary2  %{summ B}

%global fonts2  *16B*.ttf
%global fontconfs2  %{SOURCE12}

%global fontdescription2  %{expand:Segment16A, B and C are three font families, each containing a regular,
bold, italic and bold italic version, based on sixteen segment displays.

In Segment 16B, the diagonal segments extend to the center, but stop inside
the outer segments. This may resemble some newer LCD or LED displays.}


# -- Variant C

%global fontfamily3  %{fam C}
%global fontsummary3  %{summ C}

%global fonts3  *16C*.ttf
%global fontconfs3  %{SOURCE13}

%global fontdescription3  %{expand:Segment16A, B and C are three font families, each containing a regular,
bold, italic and bold italic version, based on sixteen segment displays.

In Segment 16C, the diagonal segments are not extending to the center.
This may resemble some smaller LED or VFD type displays.}

# -- end

Source1: https://www.wfonts.com/download/data/2017/12/30/segment16a/segment16a.zip
Source2: https://www.wfonts.com/download/data/2017/12/30/segment16b/segment16b.zip
Source3: https://www.wfonts.com/download/data/2017/12/30/segment16c/segment16c.zip

Source11: 60-%{fontpkgname1}.xml
Source12: 60-%{fontpkgname2}.xml
Source13: 60-%{fontpkgname3}.xml

# The source archives do not ship a separate license file,
# but the readm files include this statement:
# > The Segment16 font families were created and assigned CC0 Public Domain
# > by Daniel Wikholm in 2017.
Source20: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt

BuildArch: noarch


%description
Daniel Wikholm's Segment16 is a collection of fonts
mimicking the look of 16-segments digital displays.


%fontpkg -a


%prep
%setup -q -c %{name}-%{version} -T
unzip -n %{SOURCE1}
unzip -n %{SOURCE2}
unzip -n %{SOURCE3}

cp %{SOURCE20} ./cc0.txt


%build
%fontbuild -a


%install
%fontinstall -a


%check
%fontcheck -a


%fontfiles -a


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20171229-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20171229-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20171229-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20171229-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20171229-4
- Rebuild for Fedora 39
- Migrate License tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20171229-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jun 27 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20171229-2
- Move each font variant into separate subpackage
- Add info about differences between Segment16 A/B/C to descriptions
- Add the license text

* Fri Jun 10 2022 Artur Iwicki <fedora@svgames.pl> - 20171229-1
- Initial packaging
