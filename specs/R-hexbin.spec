Name:           R-hexbin
Version:        %R_rpm_version 1.28.5
Release:        %autorelease
Summary:        Hexagonal Binning Routines

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Binning and plotting functions for hexagonal bins.

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
