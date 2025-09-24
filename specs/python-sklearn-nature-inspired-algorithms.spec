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
BuildRequires:  tomcli

%description %_description

%package -n python3-sklearn-nature-inspired-algorithms
Summary:        %{summary}

%description -n python3-sklearn-nature-inspired-algorithms %_description

%prep
%autosetup -p1 -n Sklearn-Nature-Inspired-Algorithms-%{version}
rm -fv poetry.lock

# Drop version pinning (we use the versions available in Fedora)
for DEP in $(tomcli get -F newline-keys pyproject.toml tool.poetry.dependencies)
do
    tomcli set pyproject.toml replace tool.poetry.dependencies.${DEP} ".*" "*"
done
# Remove 'toml' dependency. It's deprecated and not needed by the package.
tomcli set pyproject.toml del tool.poetry.dependencies.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sklearn_nature_inspired_algorithms

%check
%{py3_test_envvars} %{python3} -m unittest tests
%pyproject_check_import

%files -n python3-sklearn-nature-inspired-algorithms -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
