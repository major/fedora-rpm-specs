Name:           R-rlang
Version:        %R_rpm_version 1.1.7
Release:        %autorelease
Summary:        Functions for Base Types and Core R and 'Tidyverse' Features

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}
Patch:          0001-Unbundle-libxxhash.patch

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libxxhash)

%description
A toolbox for working with base types, core R features like the condition
system, and core 'Tidyverse' features like tidy evaluation.

%prep
%autosetup -c -p1
rm -f rlang/tests/testthat/test-deparse.R # pillar stuff

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
