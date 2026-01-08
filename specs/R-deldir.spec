Name:           R-deldir
Version:        %R_rpm_version 2.0-4
Release:        %autorelease
Summary:        Delaunay Triangulation and Dirichlet (Voronoi) Tessellation

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Calculates the Delaunay triangulation and the Dirichlet or Voronoi
tessellation (with respect to the entire plane) of a planar point set.
Plots triangulations and tessellations in various ways.  Clips
tessellations to sub-windows. Calculates perimeters of tessellations.
Summarises information about the tiles of the tessellation.

%prep
%autosetup -c
rm -r deldir/inst/code.discarded
mv deldir/inst/READ_ME deldir/inst/README

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
