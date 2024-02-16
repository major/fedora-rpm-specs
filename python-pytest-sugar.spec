%global _description %{expand:
pytest-sugar is a plugin for pytest that shows failures and errors instantly
and shows a progress bar.}

Name:           python-pytest-sugar
Version:        1.0.0
Release:        %autorelease
Summary:        Change the default look and feel of pytest

# SPDX
License:        BSD-3-Clause
URL:            https://pypi.org/project/pytest-sugar
Source0:        %{pypi_source pytest-sugar}

BuildArch:      noarch

%description %_description

%package -n python3-pytest-sugar
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist pytest}

%description -n python3-pytest-sugar %_description


%prep
%autosetup -n pytest-sugar-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_sugar

%check
PYTHONPATH=. %{pytest} -v -s

%files -n python3-pytest-sugar -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
