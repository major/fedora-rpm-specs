Name:           R-date
Version:        %R_rpm_version 1.2-42
Release:        %autorelease
Summary:        Functions for Handling Dates

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Functions for handling dates.

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
