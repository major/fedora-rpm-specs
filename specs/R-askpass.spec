Name:           R-askpass
Version:        %R_rpm_version 1.2.1
Release:        %autorelease
Summary:        Safe Password Entry for R, Git, and SSH

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Cross-platform utilities for prompting the user for credentials or a
passphrase, for example to authenticate with a server or read a protected key.
Includes native programs for MacOS and Windows, hence no 'tcltk' is required.
Password entry can be invoked in two different ways: directly from R via the
askpass() function, or indirectly as password-entry back-end for 'ssh-agent' or
'git-credential' via the SSH_ASKPASS and GIT_ASKPASS environment variables.
Thereby the user can be prompted for credentials or a passphrase if needed when
R calls out to git or ssh.

%prep
%autosetup -c
rm askpass/inst/mac-* # macOS stuff

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
