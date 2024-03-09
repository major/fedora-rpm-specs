%global forgeurl https://github.com/googlefonts/RobotoMono
%global commit 3479a228ba99f69d6e504e7d798a3f8e8239bbe7

%forgemeta

Version: 3.000
Release: %autorelease
URL:     https://github.com/googlefonts/RobotoMono

# The identifier of the entity, that released the font family.
%global foundry           google
# The font family license identifier. Adjust as necessary. The OFL is our
# recommended font license.
%global fontlicense       ASL-2.0
#
# The following directives are lists of space-separated shell globs
#   – matching files associated with the font family,
#   – as they exist in the build root,
#   — at the end of the %build stage:
# – legal files (licensing…)
%global fontlicenses      LICENSE.txt
# – documentation files
%global fontdocs          README.md
# – exclusions from the ”fontdocs” list
%global fontdocsex        %{fontlicenses}

# The human-friendly font family name, whitespace included, restricted to the
# the Basic Latin Unicode block.
%global fontfamily        Roboto Mono
%global fontsummary       Google Roboto Mono fonts
#
# More shell glob lists:
# – font family files
%global fonts             fonts/ttf/*.ttf fonts/variable/*.ttf
# – fontconfig files
%global fontconfs         %{SOURCE10}
#
# A multi-line description block for the generated package.
%global fontdescription   %{expand:Roboto Mono is a monospaced addition to the Roboto type family. Like the other
members of the Roboto family, the fonts are optimized for readability on
screens across a wide variety of devices and reading environments. While the
monospaced version is related to its variable width cousin, it doesn't hesitate
to change forms to better fit the constraints of a monospaced environment. For
example, narrow glyphs like 'I', 'l' and 'i' have added serifs for more even
texture while wider glyphs are adjusted for weight. Curved caps like 'C' and
'O' take on the straighter sides from Roboto Condensed.
}

Source0: %{forgesource}
Source10: 64-%{fontpkgname}.conf

%fontpkg

%prep
%forgeautosetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
