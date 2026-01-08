Name:           R-plogr
Version:        %R_rpm_version 0.2.0
Release:        %autorelease
Summary:        C++ Logging Library for R
Summary:        Devel files for R-plogr

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.2.0

%description
A simple header-only logging library for C++. Add 'LinkingTo: plogr' to
'DESCRIPTION', and '#include <plogr.h>' in your C++ modules to use it.

%prep
%autosetup -c

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
