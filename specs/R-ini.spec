Name:           R-ini
Version:        %R_rpm_version 0.3.1
Release:        %autorelease
Summary:        Read and Write '.ini' Files

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Parse simple '.ini' configuration files to an structured list. Users can
manipulate this resulting list with lapply() functions. This same structured
list can be used to write back to file after modifications.

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
