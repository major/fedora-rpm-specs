Name:           R-polyclip
Version:        %R_rpm_version 1.10-7
Release:        %autorelease
Summary:        Polygon Clipping

# Automatically converted from old format: Boost - review is highly recommended.
License:        BSL-1.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  polyclipping-devel

%description
R port of Angus Johnson's open source library Clipper. Performs polygon
clipping operations (intersection, union, set minus, set difference) for
polygonal regions of arbitrary complexity, including holes. Computes
offset polygons (spatial buffer zones, morphological dilations, Minkowski
dilations) for polygonal regions and polygonal lines. Computes Minkowski
Sum of general polygons. There is a function for removing
self-intersections from polygon data.

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
