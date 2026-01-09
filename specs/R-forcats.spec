Name:           R-forcats
Version:        %R_rpm_version 1.0.1
Release:        %autorelease
Summary:        Tools for Working with Categorical Variables (Factors)

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Helpers for reordering factor levels (including moving specified levels to
front, ordering by first appearance, reversing, and randomly shuffling),
and tools for modifying factor levels (including collapsing rare levels
into other, 'anonymising', and manually 'recoding').

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
