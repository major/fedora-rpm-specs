%global __R_whitelist testit

Name:           R-formatR
Version:        %R_rpm_version 1.14
Release:        %autorelease
Summary:        Format R Code Automatically

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a function tidy_source() to format R source code. Spaces and indent
will be added to the code automatically, and comments will be preserved under
certain conditions, so that R code will be more human-readable and tidy. There
is also a Shiny app as a user interface in this package (see tidy_app()).

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
