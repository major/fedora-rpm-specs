Name:           R-memoise
Version:        %R_rpm_version 2.0.1
Release:        %autorelease
Summary:        Memoisation of functions

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Cache the results of a function so that when you call it again with the same
arguments it returns the pre-computed value.

%prep
%autosetup -c
rm -f memoise/tests/testthat/test-filesystem.R # unconditional suggest

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
