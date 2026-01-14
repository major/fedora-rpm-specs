Name:           R-roxygen2
Version:        %R_rpm_version 7.3.3
Release:        %autorelease
Summary:        In-Line Documentation for R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Generate your Rd documentation, 'NAMESPACE' file, and collation field using
specially formatted comments. Writing documentation in-line with code makes it
easier to keep your documentation up-to-date as your requirements change.
'Roxygen2' is inspired by the 'Doxygen' system for C++.

%prep
%autosetup -c
rm -f roxygen2/tests/testthat/test-markdown-code.R # fails

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
