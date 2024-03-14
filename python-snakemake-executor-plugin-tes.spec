# The tests require network access and a running server; see
# .github/workflows/ci.yml for details.
%bcond tests 0

Name:           python-snakemake-executor-plugin-tes
Version:        0.1.3
Release:        %autorelease
Summary:        A Snakemake executor plugin for submitting jobs via GA4GH TES

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-tes
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-tes-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  snakemake >= 8
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist snakemake-storage-plugin-s3}
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-executor-plugin-tes
Summary:        %{summary}

%description -n python3-snakemake-executor-plugin-tes %{common_description}


%prep
%autosetup -n snakemake-executor-plugin-tes-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_executor_plugin_tes


%check
%pyproject_check_import

%if %{with tests}
%pytest -v tests/tests.py
%endif


%files -n python3-snakemake-executor-plugin-tes -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
