Name:           R-tibble
Version:        %R_rpm_version 3.3.0
Release:        %autorelease
Summary:        Simple Data Frames

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Provides a 'tbl_df' class (the 'tibble') with stricter checking and better
formatting than the traditional data frame.

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
