Name:           R-S7
Version:        %R_rpm_version 0.2.1
Release:        %autorelease
Summary:        An Object Oriented System Meant to Become a Successor to S3 and S4

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
A new object oriented programming system designed to be a successor to S3
and S4. It includes formal class, generic, and method specification, and
a limited form of multiple dispatch. It has been designed and implemented
collaboratively by the R Consortium Object-Oriented Programming Working
Group, which includes representatives from R-Core, 'Bioconductor',
'Posit'/'tidyverse', and the wider R community.

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
