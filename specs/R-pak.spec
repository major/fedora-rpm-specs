Name:           R-pak
Version:        %R_rpm_version 0.5.1
Release:        %autorelease
Summary:        Another Approach to Package Installation

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
The goal of 'pak' is to make package installation faster and more reliable.
In particular, it performs all HTTP operations in parallel, so metadata
resolution and package downloads are fast. Metadata and package files are
cached on the local disk as well. 'pak' has a dependency solver, so it
finds version conflicts before performing the installation. This version of
'pak' supports CRAN, 'Bioconductor' and 'GitHub' packages as well.

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
