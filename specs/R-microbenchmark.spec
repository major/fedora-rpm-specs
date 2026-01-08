Name:           R-microbenchmark
Version:        %R_rpm_version 1.5.0
Release:        %autorelease
Summary:        Accurate Timing Functions

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Provides infrastructure to accurately measure and compare the execution
time of R expressions.

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
