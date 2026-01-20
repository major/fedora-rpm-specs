Name:           R-blob
Version:        %R_rpm_version 1.3.0
Release:        %autorelease
Summary:        A Simple S3 Class for Representing Vectors of Binary Data ('BLOBS')

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
R's raw vector is useful for storing a single binary object. What if you want
to put a vector of them in a data frame? The blob package provides the blob
object, a list of raw vectors, suitable for use as a column in data frame.

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
