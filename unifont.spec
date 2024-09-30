Name:            unifont
Version:         16.0.01
Release:         %autorelease
License:         GPL-2.0-or-later AND OFL-1.1 AND GFDL-1.3
Url:             https://savannah.gnu.org/projects/unifont
Summary:         Tools and glyph descriptions in a very simple text format

Source0:         https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:         unifont.metainfo.xml

BuildRequires:   make
BuildRequires:   gcc
BuildRequires:   perl-generators
BuildRequires:   bdftopcf
BuildRequires:   fontforge
BuildRequires:   fontpackages-devel
BuildRequires:   texinfo
BuildRequires:   ImageMagick

%description
A font with a glyph for every visible Unicode Basic Multilingual Plane code
point and more, with supporting utilities to modify the font. This package
contains tools and glyph descriptions.

%package fonts
BuildArch: noarch
Summary: Unicode font with a glyph for every visible BMP code point

Requires:        fontpackages-filesystem
Obsoletes:       %{name}-ttf-fonts < 16.0.01

%description fonts
A fixed-width Unicode font with a glyph for every visible Unicode 7.0 Basic
Multilingual Plane code point (over 55,000 glyphs) and some glyphs beyond BMP.

This font strives for very wide coverage rather than beauty, so use it only as
fallback or for special purposes.

This package contains unicode fonts in OTF format.

%package viewer
BuildArch: noarch
Summary: Graphical viewer for unifont

%description viewer
A graphical viewer for unifont source character definitions.

%prep
%setup -q -n unifont-%{version}
# Disable rebuilding during installation
sed -i 's/^install: .*/install:/' Makefile
sed -i 's/install -s/install/' src/Makefile

%build
# Makefile is broken with parallel builds
make CFLAGS='%{optflags}'
make -C doc unifont.info

%install
%make_install USRDIR=/usr COMPRESS=0 \
  OTFDEST='$(DESTDIR)/usr/share/fonts/unifont'
find %{buildroot}/usr/share/unifont/ -type f \! -name %{name}.hex -delete
rm -rv %{buildroot}/usr/share/fonts/X11
rm -v %{buildroot}%{_fontdir}/*sample*
install -Dm0644 doc/unifont.info %{buildroot}%{_infodir}/unifont.info
install -Dm0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/unifont.metainfo.xml
# Remove APL font for now
rm %{buildroot}/usr/share/consolefonts/Unifont-APL8x16.psf.gz

%files
%{_bindir}/*
%{_datadir}/%{name}/
%doc NEWS README
%license COPYING
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_infodir}/unifont.*
%exclude %{_bindir}/unifont-viewer

%_font_pkg *.otf
%{_datadir}/appdata/
%license COPYING

%files viewer
%{_bindir}/unifont-viewer
%license COPYING

%changelog
%autochangelog
