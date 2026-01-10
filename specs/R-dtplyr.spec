Name:           R-dtplyr
Version:        %R_rpm_version 1.3.2
Release:        %autorelease
Summary:        Data Table Back-End for 'dplyr'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a data.table backend for 'dplyr'. The goal of 'dtplyr' is to allow you
to write 'dplyr' code that is automatically translated to the equivalent, but
usually much faster, data.table code.

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
