Name:           python-pytest-jupyter
Version:        0.11.0
Release:        %autorelease
Summary:        A pytest plugin for testing Jupyter libraries and extensions
# BSD for pytest-jupyter itself and
# MIT is for bundled parts of tornasync package
License:        BSD-3-Clause AND MIT
URL:            https://jupyter.org
Source:         %{pypi_source pytest_jupyter}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A set of pytest plugins for Jupyter libraries and extensions.}


%description %_description

%package -n     python3-pytest-jupyter
Summary:        %{summary}

%description -n python3-pytest-jupyter %_description


%prep
%autosetup -p1 -n pytest_jupyter-%{version}


%generate_buildrequires
%pyproject_buildrequires -x client


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_jupyter


%check
# No real tests now as there is a circular dependency
# between pytest_jupyter and jupyter_server.
# %%pytest
%pyproject_check_import

%files -n python3-pytest-jupyter -f %{pyproject_files}
%doc README.md

%pyproject_extras_subpkg -n python3-pytest-jupyter server
%pyproject_extras_subpkg -n python3-pytest-jupyter client

%changelog
%autochangelog
