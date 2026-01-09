Name:           R-plyr
Version:        %R_rpm_version 1.8.9
Release:        %autorelease
Summary:        Tools for Splitting, Applying and Combining Data

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
A set of tools that solves a common set of problems: you need to break a big
problem down into manageable pieces, operate on each piece and then put all the
pieces back together. For example, you might want to fit a model to each
spatial location or time point in your study, summarise data by panels or
collapse high-dimensional arrays to simpler summary statistics. The development
of plyr has been generously supported by Becton Dickinson.

%prep
%autosetup -c
rm -f plyr/tests/testthat/test-array.r # unconditional suggest, should be fixed
rm -f plyr/tests/testthat/test-rbind.r # unconditional suggest, should be fixed

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
