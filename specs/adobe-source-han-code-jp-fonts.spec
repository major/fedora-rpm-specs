# Packaging template: basic single-family fonts packaging.
#
# SPDX-License-Identifier: MIT
#
# This template documents the minimal set of spec declarations, necessary to
# package a single font family, from a single dedicated source archive.
#
# It is part of the following set of packaging templates:
# “fonts-0-simple”: basic single-family fonts packaging
# “fonts-1-full”:   less common patterns for single-family fonts packaging
# “fonts-2-multi”:  multi-family fonts packaging
# “fonts-3-sub”:    packaging fonts, released as part of something else
#
# A font family is composed of font files, that share a single design, and
# differ ONLY in:
# — Weight        Bold, Black…
# – Width∕Stretch Narrow, Condensed, Expanded…
# — Slope/Slant   Italic, Oblique
# Optical sizing  Caption…
#
# Those parameters correspond to the default axes of OpenType variable fonts:
# https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg#registered-axis-tags
# The variable fonts model is an extension of the WWS model described in the
# WPF Font Selection Model whitepaper (2007):
# https://msdnshared.blob.core.windows.net/media/MSDNBlogsFS/prod.evol.blogs.msdn.com/CommunityServer.Components.PostAttachments/00/02/24/90/36/WPF%20Font%20Selection%20Model.pdf
#
# Do not rely on the naming upstream chose, to define family boundaries, it
# will often be wrong.
#
# Declaration order is chosen to limit divergence between those templates, and
# simplify cut and pasting.
#
Version: 2.011
Release: 17%{?dist}
URL:     https://github.com/adobe-fonts/source-han-code-jp/

# The identifier of the entity, that released the font family.
%global foundry           adobe
# The font family license identifier. Adjust as necessary. The OFL is our
# recommended font license.
%global fontlicense       OFL-1.1
#
# The following directives are lists of space-separated shell globs
#   – matching files associated with the font family,
#   – as they exist in the build root,
#   — at the end of the %build stage:
# – legal files (licensing…)
%global fontlicenses      LICENSE.txt
# – documentation files
%global fontdocs          relnotes.txt README.md README-JP.md
# – exclusions from the ”fontdocs” list
%global fontdocsex        %{fontlicenses}

# The human-friendly font family name, whitespace included, restricted to the
# the Basic Latin Unicode block.
%global fontfamily        Source Han Code JP
%global fontsummary       Adobe OpenType UI font for mixed Latin and Japanese text
#
# More shell glob lists:
# – font family files
%global fonts             OTF/SourceHanCodeJP-RegularIt.otf OTF/SourceHanCodeJP-Regular.otf OTF/SourceHanCodeJP-NormalIt.otf OTF/SourceHanCodeJP-Normal.otf OTF/SourceHanCodeJP-MediumIt.otf OTF/SourceHanCodeJP-Medium.otf OTF/SourceHanCodeJP-LightIt.otf OTF/SourceHanCodeJP-Light.otf OTF/SourceHanCodeJP-HeavyIt.otf OTF/SourceHanCodeJP-Heavy.otf OTF/SourceHanCodeJP-ExtraLightIt.otf OTF/SourceHanCodeJP-ExtraLight.otf OTF/SourceHanCodeJP-BoldIt.otf OTF/SourceHanCodeJP-Bold.otf
# – fontconfig files
%global fontconfs         %{SOURCE10}
#
# A multi-line description block for the generated package.
%global fontdescription   %{expand:
Source Han Code JP is a derivative of Source Han Sans that replaces
its proportional Latin glyphs with fixed-width 667-unit glyphs from
Source Code Pro. The Latin glyphs are scaled to match the glyphs for
Japanese kana and kanji, and their widths are adjusted to be exactly
667 units (two-thirds of an EM). Source Han Code JP is intended to be
used as a UI font for mixed Latin and Japanese text on displays,
for programming, editing HTML/CSS, viewing text or inputing to
the command line in a terminal app, and so on.
}

Source0:  https://github.com/adobe-fonts/source-han-code-jp/archive/2.011R/source-han-code-jp-2.011R.zip
# Adjust as necessary. Keeping the filename in sync with the package name is a good idea.
# See the fontconfig templates in fonts-rpm-templates for information on how to
# write good fontconfig files and choose the correct priority [number].
Source10: 68-adobe-source-han-code-jp-fonts.conf

%fontpkg

%prep
%setup -q -n source-han-code-jp-%{version}R
chmod 0644 README.md README-JP.md

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Akira TAGOH <tagoh@redhat.com> - 2.011-11
- Convert License tag to SPDX.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Akira TAGOH <tagoh@redhat.com> - 2.011-9
- Revise spec file for new packaging guidelines.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Akira TAGOH <tagoh@redhat.com> - 2.011-1
- Update to 2.011.

* Wed Jul 18 2018 Akira TAGOH <tagoh@redhat.com> - 2.000-6
- Update the priority to make Noto default.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Akira TAGOH <tagoh@redhat.com> - 2.000-3
- Correct fontconfig config.

* Mon Oct 30 2017 Akira TAGOH <tagoh@redhat.com> - 2.000-2
- Correct the file permission for README.md
- Correct the source URL.

* Fri Oct 27 2017 Akira TAGOH <tagoh@redhat.com> - 2.000-1
- Initial packaging.
