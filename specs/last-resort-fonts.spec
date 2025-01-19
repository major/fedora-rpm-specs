# SPDX-License-Identifier: MIT

Version: 15.000
Release: 7%{?dist}
URL:     https://github.com/unicode-org/last-resort-font/

%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.md
%global fontfamily        Last Resort
%global fontsummary       Special-purpose font that includes a collection of Unicode characters
%global fonts             *.ttf
%global fontdescription   %{expand:Last Resort is a special-purpose font that includes a collection of glyphs to represent types of Unicode characters. These glyphs are specifically designed to allow users to recognize that a code point is one of the following:

    * In which particular block a Unicode character is encoded
    * In the PUA (Private Use Area) for which no agreement exists
    * Unassigned (reserved for future assignment)
    * A noncharacter
}

Source0: https://github.com/unicode-org/last-resort-font/releases/download/%{version}/LastResort-Regular.ttf
Source1: https://raw.githubusercontent.com/unicode-org/last-resort-font/main/LICENSE.md

%fontpkg

%prep
%setup -q -c -T
install -m 644 -p %{SOURCE0} %{SOURCE1} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 15.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Parag Nemade <pnemade AT redhat DOT com> - 15.000-1
- Initial packaging
