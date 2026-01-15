Name:           R-cli
Version:        %R_rpm_version 3.6.5
Release:        %autorelease
Summary:        Helpers for Developing Command Line Interfaces

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
A suite of tools to build attractive command line interfaces ('CLIs'), from
semantic elements: headings, lists, alerts, paragraphs, etc. Supports
custom themes via a 'CSS'-like language. It also contains a number of lower
level 'CLI' elements: rules, boxes, trees, and 'Unicode' symbols with
'ASCII' alternatives. It support ANSI colors and text styles as well.

%prep
%autosetup -c
rm -f cli/tests/testthat/test-utils.R # unconditional suggest, should be fixed
rm -f cli/tests/testthat/test-type.R # unconditional suggest, should be fixed
rm -f cli/tests/testthat/test-tree.R # unconditional suggest, should be fixed

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
