Name:           R-lpSolve
Version:        %R_rpm_version 5.6.23
Release:        %autorelease
Summary:        Interface to Lp_solve to Solve Linear/Integer Programs

License:        LGPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}
# https://github.com/gaborcsardi/lpSolve/pull/5
Patch:          0001-Use-R-provided-BLAS-routines.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Lp_solve is freely available (under LGPL 2) software for solving linear,
integer and mixed integer programs. In this implementation we supply a
"wrapper" function in C and some R functions that solve general
linear/integer problems, assignment problems, and transportation problems.
This version calls lp_solve version 5.5.

%prep
%autosetup -c -p1

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
