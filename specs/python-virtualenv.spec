%bcond bootstrap 0
%bcond tests %{without bootstrap}

Name:           python-virtualenv
Version:        20.29.1
Release:        %autorelease
Summary:        Tool to create isolated Python environments

License:        MIT
URL:            http://pypi.python.org/pypi/virtualenv
Source:         %{pypi_source virtualenv}

# Add /usr/share/python-wheels to extra_search_dir
Patch:          rpm-wheels.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  fish
BuildRequires:  tcsh
BuildRequires:  gcc
# from the [test] extra, but manually filtered, version bounds removed
BuildRequires:  python3-flaky
BuildRequires:  python3-packaging
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-env
#BuildRequires: python3-pytest-freezer -- not available, tests skipped
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-randomly
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-setuptools
BuildRequires:  python3-time-machine
%endif

# RPM installed wheels
BuildRequires:  %{python_wheel_pkg_prefix}-pip-wheel
BuildRequires:  %{python_wheel_pkg_prefix}-setuptools-wheel
BuildRequires:  %{python_wheel_pkg_prefix}-wheel-wheel

%global _description %{expand:
virtualenv is a tool to create isolated Python environments.
A subset of it has been integrated into the Python standard library under
the venv module. The venv module does not offer all features of this library,
to name just a few more prominent:

- is slower (by not having the app-data seed method),
- is not as extendable,
- cannot create virtual environments for arbitrarily installed Python versions
  (and automatically discover these),
- does not have as rich programmatic API (describe virtual environments
  without creating them).}

%description %_description


%package -n     python3-virtualenv
Summary:        Tool to create isolated Python environments

# Provide "virtualenv" for convenience
Provides:       virtualenv = %{version}-%{release}

# RPM installed wheels
Requires:       %{python_wheel_pkg_prefix}-pip-wheel
# Python 3.12 virtualenvs are created without setuptools/wheel,
# but the users can still do --wheel=bundle --setuptools=bundle to force them:
Requires:       %{python_wheel_pkg_prefix}-setuptools-wheel
Requires:       %{python_wheel_pkg_prefix}-wheel-wheel
# This was a requirement for Python 3.6+2.7 virtual environments
Obsoletes:      %{python_wheel_pkg_prefix}-wheel0.37-wheel < 0.37.1-20

%description -n python3-virtualenv %_description


%prep
%autosetup -p1 -n virtualenv-%{version}

# Remove the wheels provided by RPM packages
rm src/virtualenv/seed/wheels/embed/pip-*
rm src/virtualenv/seed/wheels/embed/setuptools-*
rm src/virtualenv/seed/wheels/embed/wheel-*

test ! -f src/virtualenv/seed/embed/wheels/*.whl

# Replace hardcoded path from rpm-wheels.patch by %%{python_wheel_dir}
# On Fedora, this should change nothing, but when building for RHEL9+, it will
sed -i "s|/usr/share/python-wheels|%{python_wheel_dir}|" src/virtualenv/util/path/_system_wheels.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l virtualenv

%check
%pyproject_check_import -e '*activate_this' -e '*windows*'
%if %{with tests}
# Skip tests which requires internet or some extra dependencies
# Requires internet:
# - test_download_*
# - test_can_build_c_extensions
# Uses disabled functionalities around bundled wheels:
# - test_wheel_*
# - test_seed_link_via_app_data
# - test_base_bootstrap_via_pip_invoke
# - test_acquire.py (whole file)
# - test_bundle.py (whole file)
# Uses disabled functionalities around automatic updates:
# - test_periodic_update.py (whole file)
PIP_CERT=/etc/pki/tls/certs/ca-bundle.crt \
%pytest -vv -k "not test_bundle and \
                not test_acquire and \
                not test_periodic_update and \
                not test_wheel_ and \
                not test_download_ and \
                not test_can_build_c_extensions and \
                not test_base_bootstrap_via_pip_invoke and \
                not test_seed_link_via_app_data"
%endif

%files -n python3-virtualenv -f %{pyproject_files}
%doc README.md
%{_bindir}/virtualenv

%changelog
%autochangelog
