Name:           R-showtext
Version:        %R_rpm_version 0.9-7
Release:        %autorelease
Summary:        Using Fonts More Easily in R Graphs

# Main: ASL 2.0
# src/tidy.h, src/utf8.c and src/utf8.h: libpng/zlib
# Automatically converted from old format: ASL 2.0 and zlib - review is highly recommended.
License:        Apache-2.0 AND Zlib
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)

%description
Making it easy to use various types of fonts (TrueType, OpenType, Type 1, web
fonts, etc.) in R graphs, and supporting most output formats of R graphics
including PNG, PDF and SVG. Text glyphs will be converted into polygons or
raster images, hence after the plot has been created, it no longer relies on
the font files. No external software such as Ghostscript is needed to use this
package.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
