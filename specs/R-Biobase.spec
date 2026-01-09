Name:           R-Biobase
Version:        %R_rpm_version 2.70.0
Release:        %autorelease
Summary:        Base functions for Bioconductor

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel

%description
Base functions for Bioconductor (bioconductor.org). Biobase provides
functions that are needed by many other Bioconductor packages or which
replace R functions.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
