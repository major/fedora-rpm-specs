%global pypi_name sphobjinv

Name:           python-%{pypi_name}
Version:        2.4
Release:        %autorelease
Summary:        Toolkit for manipulation and inspection of Sphinx objects.inv files

License:        MIT
URL:            https://github.com/bskinn/sphobjinv
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The syntax required for a functional Sphinx cross-reference is highly
non-obvious in many cases. Sometimes Sphinx can guess correctly what
you mean, but it’s pretty hit-or-miss. The best approach is to provide
Sphinx with a completely specified cross-reference, and that’s where
sphobjinv comes in.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
Provides:       vendored(python3-fuzzywuzzy) = 0.18.0

%description -n python3-%{pypi_name}
The syntax required for a functional Sphinx cross-reference is highly
non-obvious in many cases. Sometimes Sphinx can guess correctly what
you mean, but it’s pretty hit-or-miss. The best approach is to provide
Sphinx with a completely specified cross-reference, and that’s where
sphobjinv comes in.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '1{\@^#!/usr/bin/env python@d}' src/sphobjinv/_vendored/fuzzywuzzy/{fuzz,process}.py
sed -i -e '/pytest-retry\|stdio-mgr/d' tox.ini requirements-dev.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
# Ignore test that requires stdio-mgr
%tox -- -- -v --ignore tests/test_api_good_nonlocal.py --ignore tests/test_cli.py --ignore tests/test_cli_nonlocal.py --ignore tests/test_cli_textconv.py --ignore tests/test_cli_textconv.py

%files -n python3-%{pypi_name} -f %pyproject_files
%doc README.md
%{_bindir}/sphobjinv
%{_bindir}/sphobjinv-textconv

%changelog
%autochangelog
