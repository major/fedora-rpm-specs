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
Version: 1.002
Release: 18%{?dist}
URL:     https://github.com/adobe-fonts/source-han-mono/

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
%global fontlicenses      LICENSE.md
# – documentation files
%global fontdocs          README.md
# – exclusions from the ”fontdocs” list
%global fontdocsex        %{fontlicenses}

# The human-friendly font family name, whitespace included, restricted to the
# the Basic Latin Unicode block.
%global fontfamily        Source Han Mono
%global fontsummary       Adobe OpenType monospaced font for mixed Latin and CJK text
#
# More shell glob lists:
# – font family files
%global fonts             SourceHanMono.ttc
# – fontconfig files
%global fontconfs         %{SOURCE10}
#
# A multi-line description block for the generated package.
%global fontdescription   %{expand:
Source Han Mono, which is derived from Source Han Sans and Source Code Pro,
is an OpenType/CFF Collection (OTC) that includes 70 font instances—consisting
of seven weights, five languages, and two styles—and is a Pan-CJK version
of Source Han Code JP.
}

Source0:  https://github.com/adobe-fonts/source-han-mono/releases/download/%{version}/SourceHanMono.ttc
# Adjust as necessary. Keeping the filename in sync with the package name is a good idea.
# See the fontconfig templates in fonts-rpm-templates for information on how to
# write good fontconfig files and choose the correct priority [number].
Source10: 68-adobe-source-han-mono-fonts.conf
Source20: https://raw.githubusercontent.com/adobe-fonts/source-han-mono/%{version}/LICENSE.md
Source21: https://raw.githubusercontent.com/adobe-fonts/source-han-mono/%{version}/README.md

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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Akira TAGOH <tagoh@redhat.com> - 1.002-12
- Convert License tag to SPDX.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Akira TAGOH <tagoh@redhat.com> - 1.002-10
- Revise spec file for new fonts packaging guidelines.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 1.002-3
- Update sources.

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 1.002-2
- Use tagged url for sources.

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 1.002-1
- New upstream release.

* Tue Jun  4 2019 Akira TAGOH <tagoh@redhat.com> - 1.001-3
- Add BR: libappstream-glib.

* Mon Jun  3 2019 Akira TAGOH <tagoh@redhat.com> - 1.001-2
- Install appdata.xml file into %%{_metainfodir}.
- Run validator for appdata in %%check.

* Fri May 31 2019 Akira TAGOH <tagoh@redhat.com> - 1.001-1
- New upstream release.
- Add metainfo file.

* Thu May 30 2019 Akira TAGOH <tagoh@redhat.com> - 1.000-1
- Initial packaging.
