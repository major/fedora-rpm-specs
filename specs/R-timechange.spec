Name:           R-timechange
Version:        %R_rpm_version 0.3.0
Release:        %autorelease
Summary:        Efficient Updating of Date-Times

# Parts of the 'CCTZ' source code, released under the Apache 2.0 License
# while the rest is GPL-3.0-or-later
License:        GPL-3.0-or-later AND Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Efficient routines for manipulation of date-time objects while accounting
for time-zones and daylight saving times. The package includes utilities
for updating of date-time components (year, month, day etc.), modification
of time-zones, rounding of date-times, period addition and subtraction etc.

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
