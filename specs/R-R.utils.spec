Name:           R-R.utils
Version:        %R_rpm_version 2.13.0
Release:        %autorelease
Summary:        Various Programming Utilities

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Utility functions useful when programming and developing R packages.

%prep
%autosetup -c
rm -f R.utils/tests/touchFile.R # unconditional suggest, should be fixed

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
