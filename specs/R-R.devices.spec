Name:           R-R.devices
Version:        %R_rpm_version 2.17.3
Release:        %autorelease
Summary:        Unified Handling of Graphics Devices

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Functions for creating plots and image files in a unified way regardless of
output format (EPS, PDF, PNG, SVG, TIFF, WMF, etc.). Default device options
as well as scales and aspect ratios are controlled in a uniform way across
all device types. Switching output format requires minimal changes in code.
This package is ideal for large-scale batch processing, because it will
never leave open graphics devices or incomplete image files behind, even on
errors or user interrupts.

%prep
%autosetup -c
rm -f R.devices/tests/devSet.R # unconditional suggest, should be fixed

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
