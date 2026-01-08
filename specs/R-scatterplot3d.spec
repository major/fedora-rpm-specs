Name:           R-scatterplot3d
Version:        %R_rpm_version 0.3-44
Release:        %autorelease
Summary:        3D Scatter Plot

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Plots a three dimensional (3D) point cloud.

%prep
%autosetup -c
# Fix encoding.
iconv --from=latin1 --to=UTF-8 scatterplot3d/inst/CITATION > CITATION.new && \
touch -r scatterplot3d/inst/CITATION CITATION.new && \
mv CITATION.new scatterplot3d/inst/CITATION
sed -i 's/latin1/UTF-8/g' scatterplot3d/DESCRIPTION

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
