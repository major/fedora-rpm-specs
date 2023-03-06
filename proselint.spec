Name:           proselint
Version:        0.13.0
Release:        %autorelease
Summary:        A linter for English prose

License:        BSD-3-Clause
URL:            http://proselint.com/
Source0:        %pypi_source
BuildArch:      noarch

Requires:       python3-click
Requires:       python3-future
Requires:       python3-six

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

# For running the tests:
BuildRequires:  python3-click
BuildRequires:  python3-future
BuildRequires:  python3-pytest
BuildRequires:  python3-six


%description
proselint's goal is to aggregate knowledge about best practices in
writing and to make that knowledge immediately accessible to all authors
in the form of a linter for prose.  It is a command-line utility that
can be integrated into existing tools.


%prep
%autosetup -p 1 -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info


%build
%py3_build


%install
%py3_install


%check
%pytest


%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info


%changelog
%autochangelog
