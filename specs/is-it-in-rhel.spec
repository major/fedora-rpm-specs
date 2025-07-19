Name:           is-it-in-rhel
Version:        1.0
Release:        %autorelease
Summary:        Command line tool to find out if a package is in RHEL
License:        GPL-2.0-or-later
URL:            https://pagure.io/is-it-in-rhel
Source:         https://releases.pagure.org/is-it-in-rhel/is-it-in-rhel-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel


%description
is-it-in-rhel is a command line utility to find out if a specific package is
packaged in RHEL or not.


%prep
%autosetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l is_it_in_rhel


%check
%pyproject_check_import


%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/is-it-in-rhel


%changelog
%autochangelog
