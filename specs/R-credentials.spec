Name:           R-credentials
Version:        %R_rpm_version 2.0.3
Release:        %autorelease
Summary:        Tools for Managing SSH and Git Credentials

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Setup and retrieve HTTPS and SSH credentials for use with 'git' and other
services. For HTTPS remotes the package interfaces the 'git-credential'
utility which 'git' uses to store HTTP usernames and passwords. For SSH
remotes we provide convenient functions to find or generate appropriate SSH
keys. The package both helps the user to setup a local git installation,
and also provides a back-end for git/ssh client libraries to authenticate
with existing user credentials.

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
