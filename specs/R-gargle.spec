Name:           R-gargle
Version:        %R_rpm_version 1.6.0
Release:        %autorelease
Summary:        Utilities for Working with Google APIs

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides utilities for working with Google APIs
<https://developers.google.com/apis-explorer>.  This includes functions and
classes for handling common credential types and for preparing, executing, and
processing HTTP requests.

%prep
%autosetup -c
rm -f gargle/tests/testthat/test-secret.R # unconditional suggest

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
