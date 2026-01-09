Name:           R-xopen
Version:        %R_rpm_version 1.0.1
Release:        %autorelease
Summary:        Open System Files, 'URLs', Anything

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
BuildRequires:  /usr/bin/xdg-open
Requires:       /usr/bin/xdg-open

%description
Cross platform solution to open files, directories or 'URLs' with their
associated programs.

%prep
%autosetup -c
# Depend on system executable instead.
rm xopen/inst/xdg-open

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
