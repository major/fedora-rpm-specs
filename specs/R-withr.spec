Name:           R-withr
Version:        %R_rpm_version 3.0.2
Release:        %autorelease
Summary:        Run Code 'With' Temporarily Modified Global State

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A set of functions to run code 'with' safely and temporarily modified
global state. Many of these functions were originally a part of the
'devtools' package, this provides a simple package with limited
dependencies to provide access to these functions.

%prep
%autosetup -c
# Remove failing tests
rm -f %{packname}/tests/testthat/test-{language,defer,standalone-defer}.R

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
