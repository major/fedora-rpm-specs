Name:           R-scales
Version:        %R_rpm_version 1.4.0
Release:        %autorelease
Summary:        Scale Functions for Visualization

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Graphical scales map data to aesthetics, and provide methods for
automatically determining breaks and labels for axes and legends.

%prep
%autosetup -c
rm -f scales/tests/testthat/test-label-date.R # unconditional suggest, should be fixed
rm -f scales/tests/testthat/test-full-seq.R # unconditional suggest, should be fixed

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
