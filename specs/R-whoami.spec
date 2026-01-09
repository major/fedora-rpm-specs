Name:           R-whoami
Version:        %R_rpm_version 1.3.0
Release:        %autorelease
Summary:        Username, Full Name, Email Address, 'GitHub' Username of the Current User

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Look up the username and full name of the current user, the current user's
email address and 'GitHub' username, using various sources of system and
configuration information.

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
