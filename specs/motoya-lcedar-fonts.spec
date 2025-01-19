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
%global	archivedate 20110406
%global	download_root	http://android.git.kernel.org/?p=platform/frameworks/base.git;a=blob_plain;f=data/fonts/
Version: 1.00
Release: 0.34.%{archivedate}git%{?dist}
URL:     http://android.git.kernel.org/?p=platform/frameworks/base.git;a=tree;f=data/fonts
BuildRequires: fonts-rpm-macros >= 1:2.0.5-9

# The identifier of the entity, that released the font family.
%global foundry           Motoya
# The font family license identifier. Adjust as necessary. The OFL is our
# recommended font license.
%global fontlicense       Apache-2.0
#
# The following directives are lists of space-separated shell globs
#   – matching files associated with the font family,
#   – as they exist in the build root,
#   — at the end of the %build stage:
# – legal files (licensing…)
%global fontlicenses      NOTICE
# – documentation files
%global fontdocs          README.txt
# – exclusions from the ”fontdocs” list
%global fontdocsex        %{fontlicenses}

# The human-friendly font family name, whitespace included, restricted to the
# the Basic Latin Unicode block.
%global fontfamily        MotoyaLCedar
%global fontsummary       Japanese Gothic-typeface TrueType fonts by MOTOYA Co,LTD
#
# More shell glob lists:
# – font family files
%global fonts             MTLc3m.ttf
# – fontconfig files
%global fontconfs         %{SOURCE10}
#
# A multi-line description block for the generated package.
%global fontdescription   %{expand:
Motoya font was created in 1950s, it aims beauty and readability.
"MotoyaLCedar W3 mono", Gothic-typeface font was contributed by
MOTOYA Co,LTD. for Android platform.
}

Source0:  %{download_root}MTLc3m.ttf
# Adjust as necessary. Keeping the filename in sync with the package name is a good idea.
# See the fontconfig templates in fonts-rpm-templates for information on how to
# write good fontconfig files and choose the correct priority [number].
Source10: 70-motoya-lcedar-fonts.conf
Source20: %{download_root}NOTICE
Source21: %{download_root}README.txt

%fontpkg

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE20} .
cp %{SOURCE21} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.34.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.33.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.32.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.31.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.30.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec  2 2022 Akira TAGOH <tagoh@redhat.com> - 1.00-0.29.20110406git
- Convert License tag to SPDX.

* Wed Aug 24 2022 Akira TAGOH <tagoh@redhat.com> - 1.00-0.28.20110406git
- Revise the spec file for new packaging guidelines.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.27.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.26.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.25.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.24.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.23.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.22.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.21.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 1.00-0.20.20110406git
- Install metainfo files under %%{_metainfodir}.

* Fri May 17 2019 Akira TAGOH <tagoh@redhat.com> - 1.00-0.19.20110406git
- Fix a typo in conf.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.18.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.17.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.16.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Akira TAGOH <tagoh@redhat.com> - 1.00-0.14.20110406git
- Update the priority to change the default font to Noto.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.14.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.13.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.12.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.11.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 09 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.00-0.10.20110406git
- Add metainfo file to show this font in gnome-software
- Remove %%clean section which is optional now
- Remove removal of buildroot in %%install
- Remove group tag

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.9.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.8.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.7.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.6.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Akira TAGOH <tagoh@redhat.com> - 1.00-0.5.20110406git
- Correct fontconfig config file. (#837530)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.4.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr  8 2011 Akira TAGOH <tagoh@redhat.com> - 1.00-0.3.20110406git
- Updates from upstream git.
  https://review.source.android.com/#change,22161

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.2.20100928git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 28 2010 Akira TAGOH <tagoh@redhat.com> - 1.00-0.1.20100928git
- Initial package.
