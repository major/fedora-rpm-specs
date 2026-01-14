Name:           R-nycflights13
Version:        %R_rpm_version 1.0.2
Release:        %autorelease
Summary:        Flights that Departed NYC in 2013

License:        CC0-1.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Airline on-time data for all flights departing NYC in 2013. Also includes
useful 'metadata' on airlines, airports, weather, and planes.

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
