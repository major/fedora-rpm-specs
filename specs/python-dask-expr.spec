%global pypi_name dask-expr
%global forgeurl https://github.com/dask/dask-expr

# dask-expr buildrequires dask, and dask buildrequires dask-expr
# this disables dask-expr's tests and excludes dask from the
# buildrequires, for breaking the loop when bootstrapping
%bcond bootstrap 0

# Tests require `distributed` and so does `dask_expr`. But that
# dependency is neither listed nor available, yet.
%bcond tests 1

Name:           python-%{pypi_name}
Version:        1.1.21
Release:        %{autorelease}
Summary:        High Level Expressions for Dask
%forgemeta
License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(graphviz)
BuildRequires:  python3dist(pytest)
# https://github.com/dask/dask-expr/issues/1102
BuildRequires:  python3dist(xarray)
%endif

%global _description %{expand:
Dask Expressions - Dask DataFrames with query optimization.

This is a rewrite of Dask DataFrame that includes query optimization
and generally improved organization.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}
Recommends:     python3dist(distributed)

%description -n python3-%{pypi_name} %_description


%pyproject_extras_subpkg -n python3-%{pypi_name} analyze


%prep
%forgeautosetup -p1 -S git

%if %{with bootstrap}
# patch out the dask dependency so we can bootstrap it
sed -r -i '/(dask)[<=> ]+[0-9]+/d' pyproject.toml
%else
# Drop upper bound from dask
sed -r -i 's/(dask) *== *([0-9.]*)/\1 >= \2/' pyproject.toml
%endif

# Loosen version pinning on versioneer[toml]
sed -r -i 's/(versioneer\[toml\])[<=>]*/\1>=/' pyproject.toml

# Commit and tag for Versioneer
git add --all
git commit -m '[Fedora] Changes for RPM'
git tag v%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:%{!?with_bootstrap:-x analyze}}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l dask_expr


%check

%if %{with tests} && %{without bootstrap}

# Tests keep failing on `s390x`. Probably NumPy related.
# Since this is a noarch package, we cannot use %%ifarch
if [ "$(uname -m)" == "s390x" ]; then
  k="${k-}${k+ and }not test_combine_similar_no_projection_on_one_branch"
  k="${k-}${k+ and }not test_parquet_all_na_column"
fi
%pytest -v ${k+-k }"${k-}"

%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
