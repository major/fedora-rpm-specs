Name:           R-mime
Version:        %R_rpm_version 0.13
Release:        %autorelease
Summary:        Map Filenames to MIME Types

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Guesses the MIME type from a filename extension using the data derived from
/etc/mime.types in UNIX-type systems.

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
