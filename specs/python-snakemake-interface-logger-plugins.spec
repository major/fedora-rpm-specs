Name:           python-snakemake-interface-logger-plugins
Version:        1.2.3
Release:        %autorelease
Summary:        Logger plugin interface for snakemake

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-logger-plugins
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-interface-logger-plugins-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.pixi.feature.dev.dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
This package provides a stable interface for interactions between Snakemake and
its logger plugins.}

%description %{common_description}


%package -n python3-snakemake-interface-logger-plugins
Summary:        %{summary}

%description -n python3-snakemake-interface-logger-plugins %{common_description}


%prep
%autosetup -n snakemake-interface-logger-plugins-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l snakemake_interface_logger_plugins


%check
# Just in case the tests are not very thorough:
%pyproject_check_import

%pytest -v tests/tests.py


%files -n python3-snakemake-interface-logger-plugins -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
