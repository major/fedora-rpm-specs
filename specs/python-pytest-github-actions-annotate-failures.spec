%global pypi_name pytest-github-actions-annotate-failures

Name:           python-%{pypi_name}
Version:        0.4.2
Release:        %{autorelease}
Summary:        Pytest plugin to annotate failed tests in GitHub Actions

%global forgeurl https://github.com/pytest-dev/pytest-github-actions-annotate-failures
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pkg-resources
BuildRequires:  python3-pytest-rerunfailures
BuildRequires:  python3-pytest-xdist

%global _description %{expand:
Pytest plugin to annotate failed tests with a workflow command for
GitHub Actions.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pytest_github_actions_annotate_failures


%check
# Test fails with pytest >= 7.4 (F40+)
%if %{fedora} >= 40
k="${k-}${k+ and }not test_annotation_pytest_error"
%endif

%pytest -v ${k+-k }"${k-}"

# Additional smoke test
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
