Name:           R-microbenchmark
Version:        %R_rpm_version 1.5.0
Release:        %autorelease
Summary:        Accurate Timing Functions

License:        BSD-2-Clause
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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
