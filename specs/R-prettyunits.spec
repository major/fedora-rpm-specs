Name:           R-prettyunits
Version:        %R_rpm_version 1.2.0
Release:        %autorelease
Summary:        Pretty, Human Readable Formatting of Quantities

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Pretty, human readable formatting of quantities.
Time intervals: 1337000 -> 15d 11h 23m 20s.
Vague time intervals: 2674000 -> about a month ago.
Bytes: 1337 -> 1.34 kB.

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
