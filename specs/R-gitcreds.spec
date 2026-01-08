Name:           R-gitcreds
Version:        %R_rpm_version 0.1.2
Release:        %autorelease
Summary:        Query 'git' Credentials from 'R'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Query, set, delete credentials from the git credential store. Manage
GitHub tokens and other git credentials. This package is to be used by
other packages that need to authenticate to GitHub and/or other git
repositories.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
