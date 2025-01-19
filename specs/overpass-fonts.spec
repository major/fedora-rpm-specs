Version:        3.0.4
Release:        15%{?dist}
URL:            https://github.com/RedHatBrand/overpass/

%global         fontlicense     OFL-1.1 or LGPL-2.0-or-later
%global         fontlicenses    LICENSE.md
%global         fontdocsex      %{fontlicenses}

%global common_description %{expand:
Free and open source typeface based on the U.S. interstate highway road signage\
type system.}

%global fontfamily0       Overpass
%global fontsummary0      Typeface based on the U.S. interstate highway road signage type system
%global fonts0            desktop-fonts/overpass/overpass-*.otf
%global fontconfs0        %{SOURCE10}
%global fontdocs0         README.md overpass-specimen.pdf
%global fontdescription  %{expand:
%{common_description}

This package provide sans-serif fonts which are suitable for both body and \
titling text.}

%global fontfamily1       Overpass Mono
%global fontsummary1      Monospace version of overpass fonts
%global fonts1            desktop-fonts/overpass-mono/overpass-*.otf
%global fontconfs1        %{SOURCE11}
%global fontdocs1         README.md overpass-mono-specimen.pdf
%global fontdescription1  %{expand:
%{common_description}

This package provide monospace version of overpass fonts.}

Source0: https://github.com/RedHatBrand/Overpass/archive/%{version}.tar.gz
Source10: 60-%{fontpkgname0}.conf
Source11: 60-%{fontpkgname1}.conf

%fontpkg -a

%prep
%autosetup -n Overpass-%{version}

%build
%fontbuild -a

%install
%fontinstall -a
# I do not think this is useful to package, but if it is...
%if 0
mkdir -p %{buildroot}/usr/lib/node_modules/overpass/
cp -a bower.json package.json %{buildroot}/usr/lib/node_modules/overpass/
%endif

%check
%fontcheck -a

%fontfiles -z 0
%if 0
/usr/lib/node_modules/overpass/
%endif

%fontfiles -z 1

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 03 2022 Parag Nemade <pnemade AT redhat DOT com> - 3.0.4-9
- Convert spec to new fonts packaging guidelines

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec  6 2019 Tom Callaway <spot@fedoraproject.org> - 3.0.4-2
- fix incorrect fontconfig file (thanks to lazybvr)

* Tue Nov 26 2019 Tom Callaway <spot@fedoraproject.org> - 3.0.4-1
- update to 3.0.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Tom Callaway <spot@fedoraproject.org> - 3.0.3-1
- update to 3.0.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun  1 2017 Tom Callaway <spot@fedoraproject.org> - 3.0.2-1
- update to 3.0.2
- move to otf files

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Tom Callaway <spot@fedoraproject.org> - 3.0-1
- update to 3.0
- add mono subpackage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Pravin Satute <psatute AT redhat DOT com> - 2.1-1
- Upstream new release with ttfautohint
- Changed url to https://github.com/RedHatBrand/overpass/, https://overpassfont.org looks dead.

* Tue Aug 25 2015 Tom Callaway <spot@fedoraproject.org> - 1.01-11
- update to new overpass fonts (they now claim to be 1.000, but we're not going backwards)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 03 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.01-9
- Fix metainfo file error (rh#1159700)

* Sat Oct 18 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.01-8
- Add metainfo file to show this font in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Tom Callaway <spot@fedoraproject.org> - 1.01-6
- add Light variant font

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Tom Callaway <spot@fedoraproject.org>
- License is now OFL or ASL 2.0

* Mon Sep 24 2012 Tom Callaway <spot@fedoraproject.org> - 1.01-2
- fix spaces vs tabs issue

* Mon Aug 27 2012 Tom Callaway <spot@fedoraproject.org> - 1.01-1
- initial package
