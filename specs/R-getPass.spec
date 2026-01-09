Name:           R-getPass
Version:        %R_rpm_version 0.2-4
Release:        %autorelease
Summary:        Masked User Input

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
A micro-package for reading "passwords", i.e.  reading user input with
masking, so that the input is not displayed as it is typed.  Currently we
have support for 'RStudio', the command line (every OS), and any platform
where 'tcltk' is present.

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
