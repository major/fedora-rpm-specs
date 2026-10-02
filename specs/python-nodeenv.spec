Name:           python-nodeenv
Version:        1.11.0
Release:        %autorelease
Summary:        Node.js virtual environment builder

License:        BSD-3-Clause
URL:            https://github.com/ekalinin/nodeenv
# The PyPI sdist does not contain tests, so we use the GitHub archive
Source:         %{url}/archive/%{version}/nodeenv-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  help2man

# We don’t use tox, because we would have to patch out linting and coverage
# analysis from tox.ini, and the rest of the dependencies in
# requirements-dev.txt are all for linting and coverage—except pytest, which we
# handle manually, because this is easier than filtering the requirements file.
#
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  python3dist(pytest)
# For integration tests:
BuildRequires:  /usr/bin/node

%global _description %{expand:
nodeenv (node.js virtual environment) is a tool to create isolated node.js
environments.

It creates an environment that has its own installation directories, that
doesn’t share libraries with other node.js virtual environments.

Also the new environment can be integrated with the environment which was built
by virtualenv (python).}

%description %{_description}


%package -n python3-nodeenv
Summary:        %{summary}

%description -n python3-nodeenv %{_description}


%pyproject_extras_subpkg -n python3-nodeenv certifi


%prep
%autosetup -n nodeenv-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i "s@'coverage', 'run', '-p',@'%{python3}',@" tests/nodeenv_test.py

# Remove unwanted shebangs from files that will not have the executable bit set
sed -r -i '1{/^#!/d}' nodeenv.py


%generate_buildrequires
%pyproject_buildrequires -x certifi


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l nodeenv

# Generate the man page here, rather than in %%build, so that the executable
# script entry point is readily available.
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' \
    help2man --no-info --output='%{buildroot}%{_mandir}/man1/nodeenv.1' \
    '%{buildroot}%{_bindir}/nodeenv'


%check
# Requires network access:
k="${k-}${k+ and }not test_smoke"

%pytest -k "${k-}" -v


%files -n python3-nodeenv -f %{pyproject_files}
%doc README.rst
%doc README.ru.rst
%doc CHANGES

%{_bindir}/nodeenv
%{_mandir}/man1/nodeenv.1*


%changelog
%autochangelog
