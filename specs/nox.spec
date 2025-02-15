Name:           nox
Version:        2025.02.09
Release:        %autorelease
Summary:        Flexible test automation

License:        Apache-2.0
URL:            https://github.com/wntrblm/nox
# Using github source files since PyPI doesn't contain "tests" folder anymore
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-flask
BuildRequires:  python3-myst-parser
BuildRequires:  python3-pytest

%description
Nox is a command-line tool that automates testing in multiple Python
environments, similar to tox. Unlike tox, Nox uses a standard Python
file for configuration.

%prep
%autosetup -p1 -n nox-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x tox_to_nox

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nox

%check
# Skipped tests:
# - test__create_venv_options requires conda
# - test_main_requires requires alternative Python interpreters
# - test_noxfile_script_mode installs from PyPI
%pytest -k "not test__create_venv_options[nox.virtualenv.CondaEnv.create-conda-CondaEnv] and \
            not test_main_requires[sessions2-expected_order2] and not test_main_requires[sessions1-expected_order1] and\
            not test_noxfile_script_mode"

%files -f %{pyproject_files}
%{_bindir}/nox
%pycached %exclude %{python3_sitelib}/nox/tox_to_nox.py
%exclude %{python3_sitelib}/nox/tox_to_nox.jinja2
%exclude %{_bindir}/tox-to-nox

%pyproject_extras_subpkg -n nox tox_to_nox
%pycached %{python3_sitelib}/nox/tox_to_nox.py
%{python3_sitelib}/nox/tox4_to_nox.jinja2
%{_bindir}/tox-to-nox

%changelog
%autochangelog
