Version:        4.0.0
Release:        %autorelease
URL:            https://google.github.io/material-design-icons/

%global fontlicense     Apache-2.0
%global fontlicenses    LICENSE
%global fontdocs        README.md
%global fontfamily      Material Icons
%global fontsummary     Google material design system icons
%global fonts           font/*.otf font/*.ttf
%global fontorg         com.google
%global fontconfs       %{SOURCE1}

%global fontdescription %{expand:
Material design icons is the official icon set from Google.  The icons
are designed under the material design guidelines.}

Source0:        https://github.com/google/material-design-icons/archive/%{version}/material-design-icons-%{version}.tar.gz
Source1:        65-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -n material-design-icons-%{version}

%build
%fontbuild

%install
%fontinstall
metainfo=%{buildroot}%{_metainfodir}/%{fontorg}.%{name}.metainfo.xml

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,updatecontact,update_contact,g' \
    -e 's,<!\[CDATA\[\(.*\)\]\]>,\1,' \
    -e 's,<font></font>,<font>Material Icons Outlined Regular</font>\n    <font>Material Icons Round Regular</font>\n    <font>Material Icons Sharp Regular</font>\n    <font>Material Icons Two Tone Regular</font>,' \
    -i $metainfo

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
