Name:           R-purrr
Version:        %R_rpm_version 1.2.1
Release:        %autorelease
Summary:        Functional Programming Tools

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
A complete and consistent functional programming toolkit for R.

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
