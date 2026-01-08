Name:           R-RhpcBLASctl
Version:        %R_rpm_version 0.23-42
Release:        %autorelease
Summary:        Control the Number of Threads on BLAS

# Automatically converted from old format: AGPLv3
License:        AGPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Control the number of threads on BLAS (aka GotoBLAS, OpenBLAS, ACML, BLIS and
MKL). And possible to control the number of threads in OpenMP. Get a number of
logical cores and physical cores if feasible.

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
