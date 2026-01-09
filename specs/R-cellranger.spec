Name:           R-cellranger
Version:        %R_rpm_version 1.1.0
Release:        %autorelease
Summary:        Translate Spreadsheet Cell Ranges to Rows and Columns

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Helper functions to work with spreadsheets and the "A1:D10" style of cell range
specification.

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
