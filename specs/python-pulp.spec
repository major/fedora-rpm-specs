# test are enabled by default
%bcond tests 1

# let tests run on all arches
%global debug_package %{nil}

%global _description %{expand:
PuLP is an LP modeler written in Python. PuLP can generate MPS or LP
files and call GLPK, COIN-OR CLP/CBC, CPLEX, GUROBI, MOSEK, XPRESS,
CHOCO, MIPCL, SCIP to solve linear problems.}

Name:           python-pulp
Version:        2.9.0
Release:        %autorelease
Summary:        A python Linear Programming API

%global forgeurl https://github.com/coin-or/pulp
%global tag %{version}
%forgemeta

License:        BSD-1-Clause
URL:            https://coin-or.github.io/pulp/
Source:         %forgesource

# https://github.com/sanjayankur31/pulp/tree/fedora-2.6.0
# Do not install bundled cbc
Patch:          0001-Remove-bundled-cbc.patch

# Some tests fail
# https://github.com/coin-or/pulp/issues/799
# (This one may happen only in Koji, or may be flaky:)
# ERROR: test_time_limit_no_solution (pulp.tests.test_pulp.HiGHS_CMDTest.test_time_limit_no_solution)
# ERROR: test_invalid_var_names (pulp.tests.test_pulp.SCIP_CMDTest.test_invalid_var_names)
# FAIL: test_measuring_solving_time (pulp.tests.test_pulp.SCIP_CMDTest.test_measuring_solving_time)
Patch:          pulp-2.9.0-report-and-skip.patch

# Beginning with Fedora 42, the cbc executable in coin-or-Cbc is renamed to Cbc
# due to a file conflict with libcouchbase-tools (RHBZ#2335063). We need a
# (downstream-only) patch to correct the path.
Patch1000:      pulp-2.9.0-cbc-renamed.patch

# Don't build nor test on i686
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

%description %_description

%package -n python3-pulp
Summary:        %{summary}

BuildArch:      noarch

# Normally bundled with pulp, but we do not ship the bundled copy (both to
# avoid bundling, and because it is a precompiled executable). We could fake it
# using the system coin-or-Cbc, but we would rather not do so unless something
# really needs PULP_CBC_CMD in particular.
# - PULP_CBC_CMD
# Since we removed PULP_CBC_CMD, we make COIN_CMD (the closest equivalent) a
# hard dependency.
# - COIN_CMD
BuildRequires:  coin-or-Cbc
Requires:       coin-or-Cbc
# The bundled copy would be PULP_CBC_CMD; our package does not have that solver
# enabled. We could fake it using the system coin-or-Cbc, but we would rather
# not do so unless something really needs PULP_CBC_CMD in particular.

# We depend weakly on alternative solvers that are packaged.
# - GLPK_CMD
BuildRequires:  glpk-utils
Recommends:     glpk-utils
# - HiGHS
BuildRequires:  %{py3_dist highspy}
Recommends:     %{py3_dist highspy}
# - HiGHS_CMD
BuildRequires:  coin-or-HiGHS
Recommends:     coin-or-HiGHS
# - SCIP_CMD
BuildRequires:  scip
Recommends:     scip

# These alternative solvers appear to be free software, but are not packaged.
# - CHOCO_CMD (https://github.com/chocoteam/choco-solver)
# - COINMP_DLL
# This was previously packaged as coin-or-CoinMP, but was orphaned and retired
# for Fedora 42. It is a bit difficult to get pulp to find the shared library
# correctly, so we do not bother with supporting this in Fedora 41 and older
# even though the solver is packaged there.
# - FSCIP_CMD (https://ug.zib.de/index.php)
# According to the link, fscip/FiberSCIP this is now part of SCIP, but it is
# not remotely clear how we could build an fscip binary in our scip package.
# - MIPCL_CMD (https://github.com/tingyingwu2010/MIPCL)
# - PYGLPK (https://github.com/bradfordboyle/pyglpk)
# BuildRequires:  %%{py3_dist glpk}
# Recommends:     %%{py3_dist glpk}
# - SCIP_PY (https://github.com/scipopt/PySCIPOpt)
# BuildRequires:  %%{py3_dist PySCIPOpt}
# Recommends:     %%{py3_dist PySCIPOpt}
# - YAPOSIB (https://github.com/coin-or/yaposib)
# BuildRequires:  %%{py3_dist yaposib}
# Recommends:     %%{py3_dist yaposib}

# These supported solvers are not free software:
# - COPT
# - COPT_CMD
# - COPT_DLL
# - CPLEX_CMD
# - CPLEX_PY
# - GUROBI
# - GUROBI_CMD
# - MOSEK
# - XPRESS
# - XPRESS_CMD
# - XPRESS_PY

%description -n python3-pulp %_description

%prep
%forgeautosetup -N
%autopatch -p1 -M 999
%if %[ %{undefined fc40} && %{undefined fc41} ]
%autopatch -p1 -m 1000
%endif

# remove bundled/precompiled cbc
rm -rf pulp/solverdir/cbc
# remove bundled/precompiled libraries/executables: currently, CoinMP.dll
find pulp/solverdir -type f \
    \( -name '*.dll' -o -name '*.so' -o -executable \) \
    -print -delete

%py3_shebang_fix .
# Remove shebang from non-executable library file. Upstream may have intended
# this to be run directly during development, but it will be installed without
# the execute permission bit set, so the shebang is useless.
sed -r -i '1{/^#!/d}' pulp/pulp.py

# Increase test verbosity
sed -r \
    -e 's/(runner.*TestRunner)\(\)/\1(verbosity=2)/' \
    -i pulp/tests/run_tests.py

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
%{py3_test_envvars} pulptest
%endif

%files -n python3-pulp -f %{pyproject_files}
%doc README.rst HISTORY
%{_bindir}/pulptest

%changelog
%autochangelog
