Name:           R-RUnit
Version:        %R_rpm_version 0.4.33.1
Release:        %autorelease
Summary:        R Unit test framework

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}
Patch:          R-RUnit-0.4.25-no-buildroot-path-in-html.patch

BuildArch:      noarch
BuildRequires:  R-devel

%description
R functions implementing a standard Unit Testing framework, with additional
code inspection and report generation tools.

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
