Name:           R-gplots
Version:        %R_rpm_version 3.3.0
Release:        %autorelease
Summary:        Various R Programming Tools for Plotting Data

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Various R programming tools for plotting data, including:
- calculating and plotting locally smoothed summary function,
- enhanced versions of standard plots,
- manipulating colors,
- calculating and plotting two-dimensional data summaries,
- enhanced regression diagnostic plots,
- formula-enabled interface to 'stats::lowess' function,
- displaying textual data in plots,
- plotting a matrix where each cell contains a dot whose size reflects the
  relative magnitude of the elements,
- plotting "Venn" diagrams,
- displaying Open-Office style plots,
- plotting multiple data on same region, with separate axes,
- plotting means and confidence intervals,
- spacing points in an x-y plot so they don't overlap.

%prep
%autosetup -c

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
