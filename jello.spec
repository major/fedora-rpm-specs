Name:           jello
Version:        1.5.5
Release:        %autorelease
Summary:        Query JSON at the command line with Python syntax

# SPDX
License:        MIT
URL:            https://github.com/kellyjonbrazil/jello
# GitHub archive contains tests; PyPI sdist does not.
Source0:        %{url}/archive/v%{version}/jello-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%description
Query, filter, and transform JSON and JSON Lines at the command line with
Python syntax.


%prep
%autosetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jello

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 man/*


%check
PYTHONPATH='%{buildroot}%{python3_sitelib}' ./runtests.sh


%files -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%doc ADVANCED_USAGE.md
%doc CHANGELOG
%doc README.md

%{_bindir}/jello
%{_mandir}/man1/jello.1*


%changelog
%autochangelog
