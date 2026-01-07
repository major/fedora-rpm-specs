Name:           R-clipr
Version:        %R_rpm_version 0.8.0
Release:        %autorelease
Summary:        Read and Write from the System Clipboard

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Requires:       xsel

%description
Simple utility functions to read from and write to the Windows, OS X, and
X11 clipboards.

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
