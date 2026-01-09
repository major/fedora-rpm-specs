Name:           python-lmfit
Version:        1.3.4
Release:        %autorelease
Summary:        Non-Linear Least Squares Minimization

License:        BSD-3-Clause
URL:            https://github.com/lmfit/lmfit-py
Source:         %{url}/archive/%{version}/lmfit-py-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x test
BuildOption(install): -l lmfit

BuildArch:      noarch
%ifnarch %{ix86}
BuildRequires:  %{py3_dist pandas}
%endif
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist emcee}

%global common_description %{expand:
The lmfit Python library provides tools for non-linear least-squares
minimization and curve fitting. The goal is to make these optimization
algorithms more flexible, more comprehensible, and easier to use, with the key
feature of casting variables in minimization and fitting routines as named
parameters that can have many attributes beside just a current value.}

%description %{common_description}

%package -n     python3-lmfit
Summary:        %{summary}

%description -n python3-lmfit %{common_description}

%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%check -a
%pytest -rs

%files -n python3-lmfit -f %{pyproject_files}

%changelog
%autochangelog
