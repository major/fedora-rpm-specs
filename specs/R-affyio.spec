Name:           R-affyio
Version:        %R_rpm_version 1.80.0
Release:        %autorelease
Summary:        Tools for parsing Affymetrix data files

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel

%description
Routines for parsing Affymetrix data files based upon file format 
information. Primary focus is on accessing the CEL and CDF file formats.

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
