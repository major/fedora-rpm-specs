Name:           fontawesome5-fonts
Summary:        Support files for the FontAwesome 5 fonts
Version:        5.15.4
Release:        3%{?dist}
License:        MIT
URL:            https://fontawesome.com/
BuildArch:      noarch

%global _desc %{expand:
Font Awesome gives you scalable vector icons that can instantly be
customized - size, color, drop shadow, and anything that can be done
with the power of CSS.}

%global fontlicense     OFL-1.1
%global fontlicenses    LICENSE.txt
%global fontdocs        CHANGELOG.md README* UPGRADING.md
%global fontorg         com.fontawesome

%global fontfamily1     FontAwesome5 Free
%global fontsummary1    Iconic font set
%global fonts1          otfs/*Free*
%global fontconfs1      %{SOURCE1}
%global fontdescription1 %{expand:%_desc
%global fontpkgheader1  %{expand:
Requires:       fontawesome5-fonts = %{version}-%{release}
}

The FontAwesome Free Fonts contain large numbers of icons packaged as
font files.}

%global fontfamily2     FontAwesome5 Brands
%global fontsummary2    Iconic font set
%global fonts2          otfs/*Brands*
%global fontconfs2      %{SOURCE2}
%global fontdescription2 %{expand:%_desc
%global fontpkgheader2  %{expand:
Requires:       fontawesome5-fonts = %{version}-%{release}
}

The FontAwesome Brand Fonts contain brand logos packaged as font files.}

Source0:        https://github.com/FortAwesome/Font-Awesome/archive/%{version}/Font-Awesome-%{version}.tar.gz
Source1:        60-%{fontpkgname1}.conf
Source2:        60-%{fontpkgname2}.conf
# Script to generate Source3
Source3:        trademarks.py
Source4:        README-Trademarks.txt

# Not for upstream.  This patch modifies the CSS to point to local OpenType font
# files, rather than to the eot, svg, ttf, woff, and woff2 web fonts, as
# required by Fedora's font packaging guidelines.
Patch0:         %{name}-opentype-css.patch

BuildRequires:  appstream

%description %_desc

This package contains CSS, SCSS and LESS style files for each of the
fonts in the FontAwesome family, as well as JSON and YAML metadata.

%fontpkg -a
%fontmetapkg

%package web
License:        CC-BY-4.0
Summary:        Iconic font set, javascript and SVG files

%description web %_desc

This package contains javascript and SVG files, which are typically used
on web pages.

%prep
%autosetup -n Font-Awesome-%{version} -p1
cp -p %{SOURCE4} .

%build
%fontbuild -a

%install
%fontinstall -a

# Install the web files
mkdir -p %{buildroot}%{_datadir}/fontawesome5
cp -a css js less metadata scss sprites svgs %{buildroot}%{_datadir}/fontawesome5

# Fix up the generated metainfo; see bz 1943727
sed -e 's,updatecontact,update_contact,g' \
    -e 's,<!\[CDATA\[\([^]]*\)\]\]>,\1,g' \
    -i %{buildroot}%{_metainfodir}/*.metainfo.xml

# Validate the metainfo
appstreamcli validate --no-net \
  %{buildroot}%{_metainfodir}/%{fontorg}.fontawesome5-free-fonts.metainfo.xml
appstreamcli validate --no-net \
  %{buildroot}%{_metainfodir}/%{fontorg}.fontawesome5-brands-fonts.metainfo.xml

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
%fontcheck -a
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%files
%dir %{_datadir}/fontawesome5/
%{_datadir}/fontawesome5/css/
%{_datadir}/fontawesome5/less/
%{_datadir}/fontawesome5/metadata/
%{_datadir}/fontawesome5/scss/

%fontfiles -a

%files web
%doc CHANGELOG.md README* UPGRADING.md
%license LICENSE.txt
%dir %{_datadir}/fontawesome5/
%{_datadir}/fontawesome5/js/
%{_datadir}/fontawesome5/sprites/
%{_datadir}/fontawesome5/svgs/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 5.15.4-3
- Convert License tags to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 18 2021 Jerry James <loganjerry@gmail.com> - 5.15.4-1
- Initial RPM
