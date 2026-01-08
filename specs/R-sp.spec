Name:           R-sp
Version:        %R_rpm_version 2.2-0
Release:        %autorelease
Summary:        Classes and Methods for Spatial Data

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 2.2.0

%description
Classes and methods for spatial data; the classes document where the spatial
location information resides, for 2D or 3D data. Utility functions are
provided, e.g. for plotting data as maps, spatial selection, as well as methods
for retrieving coordinates, for subsetting, print, summary, etc.

%prep
%autosetup -c
rm -f sp/tests/agg.R* sp/tests/over2.R* # whole file requires rgeos

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
