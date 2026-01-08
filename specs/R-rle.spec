Name:           R-rle
Version:        %R_rpm_version 0.10.0
Release:        %autorelease
Summary:        Common Functions for Run-Length Encoded Vectors

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Common 'base' and 'stats' methods for 'rle' objects, aiming to make it
possible to treat them transparently as vectors.

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
