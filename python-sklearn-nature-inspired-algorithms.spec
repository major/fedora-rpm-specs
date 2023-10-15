%global _description %{expand:
Nature inspired algorithms for hyper-parameter tuning of scikit-learn models.
This package uses algorithms implementation from NiaPy.

Documentation is available at:
https://sklearn-nature-inspired-algorithms.readthedocs.io/en/stable/ }

Name:           python-sklearn-nature-inspired-algorithms
Version:        0.12.0
Release:        %autorelease
Summary:        Nature-inspired algorithms for scikit-learn

# SPDX
License:        MIT
URL:            https://github.com/timzatko/Sklearn-Nature-Inspired-Algorithms
Source:         %{url}/archive/v%{version}/Sklearn-Nature-Inspired-Algorithms-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}

%description %_description

%package -n python3-sklearn-nature-inspired-algorithms
Summary:        %{summary}

%description -n python3-sklearn-nature-inspired-algorithms %_description

%prep
%autosetup -p1 -n Sklearn-Nature-Inspired-Algorithms-%{version}
rm -fv poetry.lock

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sklearn_nature_inspired_algorithms

%check
%{py3_test_envvars} %{python3} -m unittest tests

%files -n python3-sklearn-nature-inspired-algorithms -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
