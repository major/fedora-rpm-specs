# Allows one additional test.
%bcond tkinter 1

Name:           python-discovery
Version:        1.2.2
Release:        %autorelease
Summary:        Python interpreter discovery

License:        MIT
URL:            https://github.com/tox-dev/python-discovery
Source:         %{url}/archive/%{version}/python-discovery-%{version}.tar.gz

# Restore support for Python 3.6 virtual environments
# Downstream only, split from virtualenv, see https://bugzilla.redhat.com/2427756
Patch:          python3.6.patch

BuildSystem:            pyproject
BuildOption(install):   -l python_discovery
BuildOption(generate_buildrequires): -x testing

BuildArch:      noarch

%if %{with tkinter}
BuildRequires:  python3-tkinter
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-discovery
Summary:        %{summary}

%description -n python3-discovery %{common_description}


%prep -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency covdefaults:ignore


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%check -a
%pytest -rs -v


%files -n python3-discovery -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
