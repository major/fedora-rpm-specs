Name:           python-snakemake-interface-common
Version:        1.15.0
Release:        %autorelease
Summary:        Common functions and classes for Snakemake and its plugins

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-common
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-interface-common-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-interface-common
Summary:        %{summary}

%description -n python3-snakemake-interface-common %{common_description}


%prep
%autosetup -n snakemake-interface-common-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_interface_common


%check
# Just in case the tests are not very thorough:
%pyproject_check_import

%pytest -v tests/tests.py


%files -n python3-snakemake-interface-common -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
