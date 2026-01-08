Name:           R-globals
Version:        %R_rpm_version 0.18.0
Release:        %autorelease
Summary:        Identify Global Objects in R Expressions

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Identifies global ("unknown" or "free") objects in R expressions by code
inspection using various strategies (ordered, liberal, or conservative). The
objective of this package is to make it as simple as possible to identify
global objects for the purpose of exporting them in parallel, distributed
compute environments.

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
