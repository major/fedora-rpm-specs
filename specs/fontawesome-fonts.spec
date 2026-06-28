Name:		fontawesome-fonts
Summary:	Support files for the FontAwesome fonts
Epoch:		1
Version:	7.3.0
Release:	%autorelease

License:	MIT
URL:		https://fontawesome.com/
VCS:		git:https://github.com/FortAwesome/Font-Awesome.git
BuildArch:	noarch

%global _desc %{expand:Font Awesome gives you scalable vector icons that can instantly be customized
— size, color, drop shadow, and anything that can be done with the power of
CSS.}

%global fontlicense	OFL-1.1-RFN
%global fontlicenses	LICENSE.txt
%global fontdocs	CHANGELOG.md README.md UPGRADING.md
%global fontorg		com.fontawesome

%global fontfamily1	FontAwesome 7 Free
%global fontsummary1	Iconic font set
%global fonts1		otfs/*Free*
%global fontconfs1	%{SOURCE3}
%global fontpkgheader1	%{expand:
# This can be removed when F48 reaches EOL
Obsoletes:	fontawesome-6-free-fonts < 7.0.0
Provides:	fontawesome-6-free-fonts = %{version}-%{release}
Provides:	font(fontawesome6free)
Provides:	font(fontawesome6freeregular)
Provides:	font(fontawesome6freesolid)
}
%global fontdescription1 %{expand:%_desc

The FontAwesome Free Fonts contain large numbers of icons packaged as
font files.}

%global fontfamily2	FontAwesome 7 Brands Regular
%global fontsummary2	Iconic font set
%global fonts2		otfs/*Brands*
%global fontconfs2	%{SOURCE4}
%global fontpkgheader2	%{expand:
# This can be removed when F48 reaches EOL
Obsoletes:	fontawesome-6-brands-fonts < 7.0.0
Provides:	fontawesome-6-brands-fonts = %{version}-%{release}
Provides:	font(fontawesome6brands)
Provides:	font(fontawesome6brandsregular)
}
%global fontdescription2 %{expand:%_desc

The FontAwesome Brand Fonts contain brand logos packaged as font files.}

Source0:	https://github.com/FortAwesome/Font-Awesome/archive/%{version}/Font-Awesome-%{version}.tar.gz
# Script to generate Source2
Source1:	trademarks.py
Source2:	README-Trademarks.txt
Source3:	60-%{fontpkgname1}.conf
Source4:	60-%{fontpkgname2}.conf

%description
%_desc

%fontpkg -a
%fontmetapkg -d _desc

%package web
License:	CC-BY-4.0
Summary:	Iconic font set, JavaScript and SVG files

%description web
%_desc

This package contains CSS, SCSS and LESS style files for each of the fonts in
the FontAwesome family, as well as JSON and YAML metadata.  It also contains
JavaScript, SVG, and WOFF2 files, which are typically used on web pages.

%prep
%autosetup -n Font-Awesome-%{version}
cp -p %SOURCE2 .

# Modify the CSS to point to local OpenType font files, rather than to the eot,
# svg, ttf, woff, and woff2 web fonts, as required by Fedora's font packaging
# guidelines.
sed -ri \
    -e 's,url\("?\.\./webfonts/fa-brands-400\.woff2"?\)( format\("woff2"\))?,local("fontawesome-brands-fonts/Font Awesome 7 Brands-Regular-400") format("opentype"),g' \
    -e 's,url\("?\.\./webfonts/fa-regular-400\.woff2"?\)( format\("woff2"\))?,local("fontawesome-free-fonts/Font Awesome 7 Free-Regular-400") format("opentype"),g' \
    -e 's,url\("?\.\./webfonts/fa-solid-900\.woff2"?\)( format\("woff2"\))?,local("fontawesome-free-fonts/Font Awesome 7 Free-Solid-900") format("opentype"),g' \
    -e 's,url\("?\.\./webfonts/fa-v4compatibility\.woff2"?\),local("fontawesome-4-compatibility-fonts/fa-v4compatibility"),g' \
    css/all{,.min}.css \
    css/brands{,.min}.css \
    css/regular{,.min}.css \
    css/solid{,.min}.css \
    css/v4-font-face{,.min}.css \
    css/v5-font-face{,.min}.css

%build
%fontbuild -a

%install
%fontinstall -a

# Install the web files
mkdir -p %{buildroot}%{_datadir}/fontawesome
cp -a css js metadata schemas scss sprites* svg* webfonts \
   %{buildroot}%{_datadir}/fontawesome

# Fix up the generated metainfo; see bz 1943727
sed -e 's,<!\[CDATA\[\([^]]*\)\]\]>,\1,g' \
    -i %{buildroot}%{_metainfodir}/*.metainfo.xml

%check
%fontcheck -a

%fontfiles -a

%files web
%doc CHANGELOG.md README.md UPGRADING.md
%license LICENSE.txt
%{_datadir}/fontawesome/

%changelog
%autochangelog
