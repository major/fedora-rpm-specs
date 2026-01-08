Name:           R-pbapply
Version:        %R_rpm_version 1.7-4
Release:        %autorelease
Summary:        Adding Progress Bar to '*apply' Functions

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A lightweight package that adds progress bar to vectorized R functions 
('*apply'). The implementation can easily be added to functions where
showing the progress is useful (e.g. bootstrap). The type and style of
the progress bar (with percentages or remaining time) can be set through
options. Supports several parallel processing backends.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
