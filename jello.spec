Name:           jello
Version:        1.6.0
Release:        %autorelease
Summary:        Query JSON at the command line with Python syntax

# SPDX
License:        MIT
URL:            https://github.com/kellyjonbrazil/jello
# GitHub archive contains tests; PyPI sdist does not.
Source:         %{url}/archive/v%{version}/jello-%{version}.tar.gz

# Replace deprecated license_file with license_files in setup.cfg
# https://github.com/kellyjonbrazil/jello/pull/68
Patch:          %{url}/pull/68.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%description
Query, filter, and transform JSON and JSON Lines at the command line with
Python syntax.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l jello

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 man/*


%check
%{py3_test_envvars} ./runtests.sh


%files -f %{pyproject_files}
%doc ADVANCED_USAGE.md
%doc CHANGELOG
%doc README.md

%{_bindir}/jello
%{_mandir}/man1/jello.1*


%changelog
%autochangelog
