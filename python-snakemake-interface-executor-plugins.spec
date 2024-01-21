# Work around a circular dependency on snakemake and on
# python-snakemake-executor-plugin-cluster-generic.
%bcond bootstrap 0

Name:           python-snakemake-interface-executor-plugins
Version:        8.2.0
Release:        %autorelease
Summary:        Stable interface for interactions between Snakemake and its executor plugins

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-executor-plugins
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-interface-executor-plugins-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{without bootstrap}
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8
BuildRequires:  %{py3_dist snakemake-executor-plugin-cluster-generic}
%endif

%global common_description %{expand:
This package provides a stable interface for interactions between Snakemake and
its executor plugins.}

%description %{common_description}


%package -n python3-snakemake-interface-executor-plugins
Summary:        %{summary}

%description -n python3-snakemake-interface-executor-plugins %{common_description}


%prep
%autosetup -n snakemake-interface-executor-plugins-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_interface_executor_plugins


%check
# Just in case the tests are not very thorough:
%pyproject_check_import

%if %{without bootstrap}
%pytest -v tests/tests.py
%endif


%files -n python3-snakemake-interface-executor-plugins -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

# Note that rpmlint will complain about the fact that
# %%{python3_sitelib}/snakemake_interface_executor_plugins/executors/remote.py
# has a shebang line and is not executable. Normally, it would make sense to
# remove the shebang for something that is not an executable script, but in
# this case the file may be copied to remote hosts and chmod’ed, so it’s
# correct to retain the shebang line even though the installed script lacks
# executable permissions (both here and in the bdist installed directly from
# PyPI via pip).


%changelog
%autochangelog
