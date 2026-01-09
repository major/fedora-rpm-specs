Name:           R-hms
Version:        %R_rpm_version 1.1.4
Release:        %autorelease
Summary:        Pretty Time of Day

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Implements an S3 class for storing and formatting time-of-day values, based
on the 'difftime' class.

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
