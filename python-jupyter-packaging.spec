%global pypi_name jupyter_packaging

Name:           python-jupyter-packaging
Version:        0.12.3
Release:        %autorelease
Summary:        Tools to help build and install Jupyter Python packages

License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter-packaging
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
This package contains utilities for making Python packages with and without
accompanying JavaScript packages.}

%description %_description

%package -n python3-jupyter-packaging
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-jupyter-packaging %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Drop dependencies on coverage, linters etc.
sed -Ei 's/"(coverage|pre-commit|pytest-cov)",//g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -w -x test

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Some tests are trying to install packages to /usr
# - https://github.com/jupyter/jupyter-packaging/issues/63
%pytest -k "\
not test_build_package and \
not test_create_cmdclass and \
not test_deprecated_metadata and \
not test_develop and \
not test_install and \
not test_install_hybrid and \
not test_run \
" \
-W "ignore:pkg_resources is deprecated as an API::pkg_resources"
# ^^^
# Workaround pkg_resources deprecation warning leaking from
# setuptools:
# https://github.com/pypa/setuptools/issues/3878

%files -n python3-jupyter-packaging -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
