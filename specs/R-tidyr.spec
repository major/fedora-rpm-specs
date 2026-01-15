Name:           R-tidyr
Version:        %R_rpm_version 1.3.2
Release:        %autorelease
Summary:        Tidy Messy Data

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Tools to help to create tidy data, where each column is a variable, each
row is an observation, and each cell contains a single value.  'tidyr'
contains tools for changing the shape (pivoting) and hierarchy (nesting and
'unnesting') of a dataset, turning deeply nested lists into rectangular
data frames ('rectangling'), and extracting values out of string columns.
It also includes tools for working with missing values (both implicit and
explicit).

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
