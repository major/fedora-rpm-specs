Name:           R-debugme
Version:        %R_rpm_version 1.2.0
Release:        %autorelease
Summary:        Debug R Packages

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Specify debug messages as special string constants, and control debugging
of packages via environment variables.

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
