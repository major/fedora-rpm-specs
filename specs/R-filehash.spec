Name:           R-filehash
Version:        %R_rpm_version 2.4-6
Release:        %autorelease
Summary:        Simple Key-Value Database

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Implements a simple key-value style database where character string keys
are associated with data values that are stored on the disk. A simple
interface is provided for inserting, retrieving, and deleting data from
the database. Utilities are provided that allow 'filehash' databases to be
treated much like environments and lists are already used in R. These
utilities are provided to encourage interactive and exploratory analysis
on large datasets. Three different file formats for representing the
database are currently available and new formats can easily be
incorporated by third parties for use in the 'filehash' framework.

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
