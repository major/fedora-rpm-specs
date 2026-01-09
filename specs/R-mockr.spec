Name:           R-mockr
Version:        %R_rpm_version 0.2.2
Release:        %autorelease
Summary:        Mocking in R

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a means to mock a package function, i.e., temporarily substitute
it for testing. Designed as a drop-in replacement for
'testthat::with_mock()', which may break in R 3.4.0 and later.

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
