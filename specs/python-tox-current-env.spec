%bcond bootstrap 0
# Tests are enabled by default, unless bootstrapping (for pytest-xdist)
%bcond tests %{without bootstrap}

Name:           python-tox-current-env
Version:        0.0.15
Release:        %autorelease
Summary:        Tox plugin to run tests in current Python environment

License:        MIT
URL:            https://github.com/fedora-python/tox-current-env
Source0:        %{pypi_source tox_current_env}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%description
The tox-current-env plugin allows to run tests in current Python environment.


%package -n     python%{python3_pkgversion}-tox-current-env
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-tox-current-env}

%description -n python%{python3_pkgversion}-tox-current-env
The tox-current-env plugin allows to run tests in current Python environment.


%prep
%autosetup -n tox_current_env-%{version}


%generate_buildrequires
# Don't use %%pyproject_buildrequires -t/-e to avoid a build dependency loop
%pyproject_buildrequires %{?with_tests:-x tests}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tox_current_env


%check
# hooks[34].py are imported in hooks.py based on tox version so we have to
# exclude them here.
%pyproject_check_import -e '*.hooks?'
%if %{with tests}
# deselected tests run tox without the options for this plugin and hence they need internet
%pytest -k "not regular and not noquiet_installed_packages[None]"
%endif


%files -n python%{python3_pkgversion}-tox-current-env -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
