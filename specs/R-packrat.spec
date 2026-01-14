Name:           R-packrat
Version:        %R_rpm_version 0.9.3
Release:        %autorelease
Summary:        Dependency Management System for R Projects

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Manage the R packages your project depends on in an isolated, portable, and
reproducible way.

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
