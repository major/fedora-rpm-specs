Name:           R-inline
Version:        %R_rpm_version 0.3.21
Release:        %autorelease
Summary:        Functions to Inline C, C++, Fortran Function Calls from R

License:        LGPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Functionality to dynamically define R functions and S4 methods with
'inlined' C, C++ or Fortran code supporting the .C and .Call calling
conventions.

%prep
%autosetup -c

%if ! %{?fedora}%{!?fedora:0}
# R-tinytest is not available in EPEL
sed 's/, tinytest//' -i inline/DESCRIPTION
rm inline/tests/tinytest.R
%endif

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
