Name:           R-fansi
Version:        %R_rpm_version 1.0.7
Release:        %autorelease
Summary:        ANSI Control Sequence Aware String Functions

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Counterparts to R string manipulation functions that account for the
effects of ANSI text formatting control sequences.

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
