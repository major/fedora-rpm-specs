# SPDX-License-Identifier: LGPL-3.0-or-later

Version: 15.0.0
Release: %autorelease
URL: https://openmoji.org/

# OpenMoji graphics are licensed under the Creative Commons Share Alike License 4.0
# Code licensed under the GNU Lesser General Public License v3
License: CC-BY-SA-4.0 AND LGPL-3.0-only

%global fontfamilybase    OpenMoji
%global fontfamilybaselc  openmoji
%global fontsummarybase   Emojis with a line-drawn style
%global foundry           hfg-gmuend
%global fontlicenses      LICENSE.txt
%global fontdocs          *.md
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
%global fonts1            font/%{fontfamilybase}-black-glyf/%{fontfamilybase}-black-glyf.ttf
%global fontconfs1        %{SOURCE11}
%global fontappstreams1   %{SOURCE21}
%global fontdescription1  %{expand: %{common_description}
This package provides a black and white font.}

%global fontfamily2       %{fontfamilybase} Color
%global fontsummary2      %{fontsummarybase} (color, scalable)
%global fonts2            font/%{fontfamilybase}-color-glyf_colr_1/%{fontfamilybase}-color-glyf_colr_1.ttf
%global fontconfs2        %{SOURCE12}
%global fontappstreams2   %{SOURCE22}
%global fontdescription2  %{expand: %{common_description}
This package provides a color font in the scalable COLRv1 format.}

Source0:  https://github.com/%{foundry}/%{fontfamilybaselc}/archive/%{version}.tar.gz#/%{fontfamilybaselc}-%{version}.tar.gz
Source11: 66-%{fontpkgname1}.conf
Source12: 66-%{fontpkgname2}.conf
Source21: org.openmoji.black.metainfo.xml
Source22: org.openmoji.color.metainfo.xml

Name:     %{foundry}-%{fontfamilybaselc}-fonts
Summary:  %{fontsummarybase}
BuildArch: noarch
BuildRequires: fontpackages-devel
BuildRequires: libappstream-glib

%description
%wordwrap -v common_description


%fontpkg -a
%fontmetapkg


%prep
%autosetup -n %{fontfamilybaselc}-%{version}


%build
# FIXME: Build the TTFs ourselves rather than relying on the ones in the
# source package.  To do that, first we need to package nanoemoji and
# its dependencies.  https://release-monitoring.org/project/96050/

%fontbuild -a


%install
%fontinstall -a


%check
%fontcheck -a


%fontfiles -a


%changelog
%autochangelog
