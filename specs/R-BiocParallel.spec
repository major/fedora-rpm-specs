Name:           R-BiocParallel
Version:        %R_rpm_version 1.44.0
Release:        %autorelease
Summary:        Bioconductor facilities for parallel evaluation

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel

%description
This package provides modified versions and novel implementation of functions
for parallel evaluation, tailored to use with Bioconductor objects.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
