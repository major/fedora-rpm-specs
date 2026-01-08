Name:           R-remotes
Version:        %R_rpm_version 2.5.0
Release:        %autorelease
Summary:        R Package Installation from Remote Repositories

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Download and install R packages stored in GitHub, GitLab, Bitbucket,
Bioconductor, or plain subversion or git repositories. This package provides
the 'install_*' functions in devtools. Indeed most of the code was copied over
from devtools.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
