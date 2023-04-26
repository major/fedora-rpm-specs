# SPDX-License-Identifier: LGPL-3.0-or-later

Version: 14.0.0
Release: %autorelease
URL: https://openmoji.org/

# In noto-emoji-fonts source
## noto-emoji code is in ASL 2.0 license
## Emoji fonts are under OFL license
### third_party color-emoji code is in BSD license
### third_party region-flags code is in Public Domain license
# In OpenMoji source
## OpenMoji graphics are licensed under the Creative Commons Share Alike License 4.0
## Code licensed under the GNU Lesser General Public License v3
License: OFL-1.1 AND Apache-2.0 AND CC-BY-SA-4.0 AND LGPL-3.0-only

# The OpenMoji don't, at the time of writing, have a way to build
# Google-style TTFs that we need to show colour in most of our apps.
# Instead, we'll borrow Noto's tooling.
%global forgeurl          https://github.com/googlei18n/noto-emoji/
%global commit            d5e261484286d33a1fe8a02676f5907ecc02106f
%forgemeta
%undefine distprefix

%bcond_without zopflipng

%global fontfamilybase    OpenMoji
%global fontfamilybaselc  openmoji
%global fontsummarybase   Emojis with a line-drawn style
%global foundry           hfg-gmuend
%global fontlicenses      %{fontfamilybaselc}-%{version}/LICENSE.txt
%global fontdocs          %{fontfamilybaselc}-%{version}/*.md
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
A project of students and professors of the HfG Schwäbisch Gmünd.

OpenMoji uses visual guidelines that are not linked to a specific
branding.  The emojis are designed to integrate well in combination with
text.
}

# Extra "black" to work around https://pagure.io/fonts-rpm-macros/issue/10
%global fontfamily1       %{fontfamilybase} Black
%global fontpkgname1      %{foundry}-%{fontfamilybaselc}-black-fonts
%global fontsummary1      %{fontsummarybase} (black and white)
%global fonts1            %{fontfamilybaselc}-%{version}/font/%{fontfamilybase}-Black.ttf
%global fontconfs1        %{SOURCE11}
%global fontappstreams1   %{SOURCE21}
%global fontdescription1  %{expand: %{common_description}
This package provides a black and white font.}

%global fontfamily2       %{fontfamilybase} Color
%global fontsummary2      %{fontsummarybase} (color)
%global fonts2            %{fontfamilybase}-Color.ttf
%global fontconfs2        %{SOURCE12}
%global fontappstreams2   %{SOURCE22}
%global fontdescription2  %{expand: %{common_description}
This package provides a color font.}

Source0:  %{forgesource}
Source1:  https://github.com/%{foundry}/%{fontfamilybaselc}/archive/%{version}.tar.gz#/%{fontfamilybaselc}-%{version}.tar.gz
Source2:  edit-yaml-into-tmpl.pl
Source11: 66-%{fontpkgname1}.conf
Source12: 66-%{fontpkgname2}.conf
Source21: org.openmoji.black.metainfo.xml
Source22: org.openmoji.color.metainfo.xml

Patch0:         noto-emoji-use-system-pngquant.patch
Patch1:         noto-emoji-build-all-flags.patch
Patch2:         noto-emoji-use-gm.patch
Patch3:         noto-emoji-check-sequence.patch

Name:     %{foundry}-%{fontfamilybaselc}-fonts
Summary:  %{fontsummarybase}
BuildArch: noarch
BuildRequires: GraphicsMagick
BuildRequires: cairo-devel
BuildRequires: fontconfig
BuildRequires: fontpackages-devel
BuildRequires: fonttools
BuildRequires: libappstream-glib
BuildRequires: nototools
BuildRequires: perl(XML::LibXML)
BuildRequires: perl(YAML::XS)
BuildRequires: pngquant
BuildRequires: python3-devel
BuildRequires: python3dist(fonttools)
BuildRequires: zopfli
BuildRequires: make

%description
%wordwrap -v common_description


%fontpkg -a
%fontmetapkg


%prep
%forgeautosetup
rm -rf third_party/pngquant
mv LICENSE LICENSE-BUILD


tar -xf %{SOURCE1}
%{SOURCE2} %{fontfamilybaselc}-%{version}/font/scfbuild-color.yml NotoColorEmoji.tmpl.ttx.tmpl %{fontfamilybase}-Color.tmpl.ttx.tmpl
pushd %{fontfamilybaselc}-%{version}/color/72x72/
for PNG in *.png; do
    png=${PNG,,}
    mv $PNG emoji_u${png//-/_}
done
rm emoji_u1f3f3_fe0f.png
popd


%build

# Optionally use a fake no-op zopflipng so we can build the package in
# reasonable time for testing.
%if %{without zopflipng}
mkdir bin
echo '#!/bin/sh' > bin/zopflipng
echo 'cp -- "$2" "$3"' >> bin/zopflipng
chmod +x bin/zopflipng
%endif

env PATH=`pwd`/bin:$PATH make %{?_smp_mflags} OPT_CFLAGS="$RPM_OPT_FLAGS" EMOJI=%{fontfamilybase}-Color EMOJI_SRC_DIR=%{fontfamilybaselc}-%{version}/color/72x72 FLAGS= BODY_DIMENSIONS=76x72

%fontbuild -a


%install
%fontinstall -a


%check
%fontcheck -a


%fontfiles -a


%changelog
%autochangelog
