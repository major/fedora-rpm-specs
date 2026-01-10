Name:           R-dbplyr
Version:        %R_rpm_version 2.5.1
Release:        %autorelease
Summary:        A 'dplyr' Back End for Databases

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A 'dplyr' back end for databases that allows you to work with remote database
tables as if they are in-memory data frames. Basic features works with any
database that has a 'DBI' back end; more advanced features require 'SQL'
translation to be provided by the package author.

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
