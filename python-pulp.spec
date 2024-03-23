# test are enabled by default
%bcond_without tests

# let tests run on all arches
%global debug_package %{nil}

%global _description %{expand:
PuLP is an LP modeler written in Python. PuLP can generate MPS or LP
files and call GLPK, COIN-OR CLP/CBC, CPLEX, GUROBI, MOSEK, XPRESS,
CHOCO, MIPCL, SCIP to solve linear problems.}

Name:           python-pulp
Version:        2.8.0
Release:        %autorelease
Summary:        A python Linear Programming API

License:        BSD-1-Clause
URL:            https://coin-or.github.io/pulp/
Source0:        https://github.com/coin-or/pulp/archive/%{version}/pulp-%{version}.tar.gz

# https://github.com/sanjayankur31/pulp/tree/fedora-2.6.0
# Do not install bundled cbc
Patch0:         0001-Remove-bundled-cbc.patch
Patch1:         0002-increase-test-verbosity.patch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  git-core

%if %{with tests}
BuildRequires:  %{py3_dist amply}
BuildRequires:  coin-or-Cbc
%endif

# Solver
# https://coin-or.github.io/pulp/main/installing_pulp_at_home.html?highlight=cbc
Requires:       coin-or-Cbc

%description %_description

%package -n python3-pulp
Summary:        %{summary}
BuildArch:      noarch

%description -n python3-pulp %_description

%prep
%autosetup -n pulp-%{version} -S git

# remove bundled cbc
rm -rf pulp/solverdir/cbc

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pulp

%check
# Using pulptest binary to test the package
%if %{with tests}
export PATH=$PATH:%{buildroot}%{_bindir}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
pulptest
%endif

%files -n python3-pulp -f %{pyproject_files}
%doc README.rst HISTORY
%{_bindir}/pulptest

%changelog
%autochangelog
