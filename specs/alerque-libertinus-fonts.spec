Version: 7.051
Release: 2%{?dist}
URL: https://github.com/alerque/libertinus

%global foundry alerque
%global fontlicense       OFL

%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md
%global fontdocsex        %{fontlicenses}

%global fontfamily Libertinus
%global fontsummary The Libertinus Fonts project
%global fonts             static/OTF/*.otf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
The Libertinus Fonts project includes four main type families:

The Libertinus Serif family:

  * 6 serif typefaces cover three weights (Regular, Semibold, Bold) in each of two styles (Regular, Italic); originally forked from Linux Libertine.

The Libertinus Sans family:

  * 3 sans-serif typefaces cover Regular, a Bold weight, and an Italic style; originally forked from Linux Biolinum.

The Libertinus Mono family:

  * 1 monospace typeface derived from the serif family; originally forked from Linux Libertine Mono.

The Libertinus Math family:

  * 1 OpenType math typeface derived from the serif family with many extra glyphs and features for use in OpenType math-capable applications (such as LuaTeX, XeTeX, or MS Word 2007+).

Additionally included are 3 special-use families with a single typeface each:

  * Libertinus Serif Display: A derivative of Libertinus Serif Regular optimized for display at large sizes.

  * Libertinus Serif Initials: A derivative of Libertinus Serif with outlined variants of capital letter glyphs suitable for drop-caps or other decorations.

  * Libertinus Keyboard: A derivative of Libertinus Sans with keyboard key outlines around each character suitable for use in technical documentation.
}

Source0: https://github.com/alerque/libertinus/releases/download/v%{version}/Libertinus-%{version}.tar.zst

Source10: 60-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -n Libertinus-%{version}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.051-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Jonny Heggheim <hegjon@gmail.com> - 7.051-1
- Updated to version v7.051

* Sat Sep 21 2024 Caleb Maclennan <caleb@alerque.com> - 7.050-1
- Bump to new upstream release v7.050

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.040-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.040-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.040-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.040-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.040-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Jonny Heggheim <hegjon@gmail.com> - 7.040-1
- Initial package
