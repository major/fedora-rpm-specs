# SPDX-License-Identifier: MIT
%global forgeurl  https://github.com/googlefonts/literata/
%global tag       %{version}
%forgemeta

Version: 2.200

Release: 12%{?dist}
URL:     %{forgeurl}

%global foundry           TypeTogether
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Literata
%global fontsummary       Literata, a contemporary serif font family for long-form reading
%global fonts             *ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Literata is one of the most distinct free font families for digital books. It
was commissioned as the default font family for all Google Play Books in 2014,
balancing a brand-able look with the strict needs of a comfortable reading
experience on a wide range of devices with varying screen resolutions and
rendering technologies — not an easy task.

TypeTogether solved these problems by designing a familiar roman style (varied
texture, slanted stress, and less mechanic structure) paired with an uncommon
upright italic that accounts for the inherent limitations of the square pixel
grid.

It was released under the SIL Open Font License in January 2019.}

Source0:  %{forgesource}
Source1:  %{forgeurl}/releases/download/%{version}/%{fontfamily}-v%{version}.zip
Source10: 57-%{fontpkgname}.xml

%fontpkg

%prep
%forgesetup
unzip -j -q  %{SOURCE1}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.200-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.200-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.200-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.200-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.200-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.200-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.200-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.200-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.200-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.200-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.200-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.200-1
✅ Initial packaging
