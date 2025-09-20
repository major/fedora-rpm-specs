# test are enabled by default
%bcond tests 1

Name:           python-pulp
Version:        3.3.0
Release:        %autorelease
Summary:        Linear and mixed integer programming modeler

License:        BSD-1-Clause
URL:            https://coin-or.github.io/pulp/
%global forgeurl https://github.com/coin-or/pulp
Source:         %{forgeurl}/archive/%{version}/pulp-%{version}.tar.gz

# Do not install bundled cbc; downstream-only, as upstream obviously wants to
# keep bundling.
Patch:          0001-Remove-bundled-cbc.patch
# Downstream-only: handle system cbc renamed to Cbc
#
# Beginning with Fedora 42, the cbc executable in coin-or-Cbc is renamed to Cbc
# due to a file conflict with libcouchbase-tools (RHBZ#2335063).
Patch:          0002-Downstream-only-handle-system-cbc-renamed-to-Cbc.patch
# Skip HiGHS_CMDTest.test_time_limit_no_solution
#
# A temporary downstream workaround for
# https://github.com/coin-or/pulp/issues/832.
Patch:          0003-Skip-HiGHS_CMDTest.test_time_limit_no_solution.patch
# Expect SCIP_PY to report unbounded problems the same way as SCIP_CMD
#
# This seems to have changed from scip 9.2.0 to 9.2.2; we cannot usefully
# report it upstream until PySCIPOpt releases binary PyPI wheels based on
# scip 9.2.2 or later.
Patch:          0004-Expect-SCIP_PY-to-report-unbounded-problems-the-same.patch

# These alternative solvers appear to be free software, but are not packaged.
# - CHOCO_CMD (https://github.com/chocoteam/choco-solver)
# - COINMP_DLL (previously packaged as coin-or-CoinMP, but orphaned and retired
#   for Fedora 42)
# - CUOPT (https://www.nvidia.com/en-us/ai-data-science/products/cuopt/):
#   currently in the process of being open-sourced,
#   https://blogs.nvidia.com/blog/cuopt-open-source/?ncid=no-ncid, but may
#   still have non-free dependencies (CUDA SDK?)
# - CYLP (https://github.com/coin-or/CyLP, would be coin-or-CyLP if packaged)
# - FSCIP_CMD (https://ug.zib.de/index.php): According to the link, this is now
#   part of SCIP, but it is not remotely clear how we could build an fscip
#   binary in our scip package.
# - MIPCL_CMD
#   (https://github.com/tingyingwu2010/MIPCL)
# - PYGLPK (https://github.com/bradfordboyle/pyglpk)
# BuildRequires:  %%{py3_dist glpk}
# Recommends:     %%{py3_dist glpk}
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
# - SAS94
# - SASCAS
# - XPRESS
# - XPRESS_CMD
# - XPRESS_PY

BuildSystem:            pyproject
BuildOption(install):   -L pulp
# Omitted extras for non-free solvers: copt, cplex, gurobi, mosek, xpress
BuildOption(generate_buildrequires): %{shrink:
  -x highs
  -x scip
}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# let tests run on all arches
%global debug_package %{nil}

%global _description %{expand:
PuLP is an linear and mixed integer programming modeler written in Python.

With PuLP, it is simple to create MILP optimisation problems and solve them
with the latest open-source (or proprietary) solvers. PuLP can generate MPS or
LP files and call solvers such as GLPK, COIN-OR CLP/CBC, CPLEX, GUROBI, MOSEK,
XPRESS, CHOCO, MIPCL, HiGHS, SCIP/FSCIP.}

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
# BuildRequires is covered by the highs extra.
Recommends:     python3-pulp+highs = %{version}-%{release}
# - HiGHS_CMD
BuildRequires:  coin-or-HiGHS
Recommends:     coin-or-HiGHS
# - SCIP_CMD
BuildRequires:  scip
Recommends:     scip
# - SCIP_PY
# BuildRequires is covered by the scip extra.
Recommends:     python3-pulp+scip = %{version}-%{release}

%description -n python3-pulp %_description


%pyproject_extras_subpkg -n python3-pulp highs scip


%prep -a
# remove bundled/precompiled cbc
rm -rf pulp/solverdir/cbc
# remove bundled/precompiled libraries/executables: currently, CoinMP.dll
find pulp/solverdir -type f \
    \( -name '*.dll' -o -name '*.so' -o -executable \) \
    -print -delete

# Increase test verbosity
sed -r \
    -e 's/(runner.*TestRunner)\(\)/\1(verbosity=2)/' \
    -i pulp/tests/run_tests.py


%install -a
# Remove shebang from non-executable library file. Upstream may have intended
# this to be run directly during development, but it is installed without the
# execute permission bit set, so the shebang is useless.
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/pulp/pulp.py'
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_shebangs
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/pulp'


%check -a
%if %{with tests}
# Using pulptest binary to test the package
%{py3_test_envvars} pulptest
%endif


%files -n python3-pulp -f %{pyproject_files}
%license LICENSE
%doc AUTHORS
%doc HISTORY
%doc README.rst
%{_bindir}/pulptest


%changelog
%autochangelog
