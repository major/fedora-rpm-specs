Name:           R-testit
Version:        %R_rpm_version 0.15
Release:        %autorelease
Summary:        A Simple Package for Testing R Packages

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides two convenience functions assert() and test_pkg() to facilitate
testing R packages.

%prep
%autosetup -c

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
