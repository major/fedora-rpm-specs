Name:           R-ellipsis
Version:        %R_rpm_version 0.3.2
Release:        %autorelease
Summary:        Tools for Working with ...

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
The ellipsis is a powerful tool for extending functions. Unfortunately this
power comes at a cost: misspelled arguments will be silently ignored. The
ellipsis package provides a collection of functions to catch problems and alert
the user.

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
