Name:           python-tox-uv
Version:        1.35.2
Release:        %autorelease
Summary:        Integration of uv with tox

License:        MIT
URL:            https://github.com/tox-dev/tox-uv
Source:         https://github.com/tox-dev/tox-uv/archive/%{version}/tox-uv-%{version}.tar.gz

# as with python-tox, those tests run on the CI only, as they need internet access
%bcond ci_tests 0

BuildArch:      noarch
BuildRequires:  python3-devel

# For tests
# See tests/test_tox_uv_venv.py test_uv_env_python_preference_complex parameters
BuildRequires:  python3.10


%global _description %{expand:
tox-uv is a tox plugin, which replaces virtualenv and pip with uv in your tox
environments. Note that you will get both the benefits (performance)
or downsides (bugs) of uv.

Installing this package changes the behavior of tox.
It also complicates usage of tox with a Python version not supported by uv.
Use `tox --runner virtualenv` to disable this plugin.}

%description %_description


%package -n     python3-tox-uv
Summary:        %{summary}
# Tighten the generated dependency on python3dist(tox-uv-bare)
Requires:       python3-tox-uv-bare = %{version}-%{release}

%description -n python3-tox-uv %_description


%package -n     python3-tox-uv-bare
Summary:        Plugin-only python3-tox-uv without the uv dependency
# Ensure clean upgrade path from before the package was split
Conflicts:      python3-tox-uv < 1.32.0

%description -n python3-tox-uv-bare %_description

This package does not have the dependency on uv, you need to bring your own
or install python3-tox-uv.


%prep
%autosetup -p1 -n tox-uv-%{version}
# Remove a build dependency of tox-uv on tox-uv-bare (we build both)
%pyproject_patch_dependency tox-uv-bare:ignore:br_only

# Remove unpackaged (devpi-process) and coverage test dependencies
%pyproject_patch_dependency devpi-process:ignore
%pyproject_patch_dependency covdefaults:ignore
%pyproject_patch_dependency diff-cover:ignore
%pyproject_patch_dependency pytest-cov:ignore

# Relax some build/test dependencies
%pyproject_patch_dependency hatchling:drop_constraints
%pyproject_patch_dependency hatch-vcs:drop_constraints
%pyproject_patch_dependency pytest:drop_constraints
%pyproject_patch_dependency pytest-mock:drop_constraints


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -g test
%pyproject_buildrequires -d meta


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%pyproject_wheel -d meta


%install
%pyproject_install


%check
# only works with the package actually installed
k="${k-}${k+ and }not test_tox_version"
k="${k-}${k+ and }not test_uv_version"

# only works with tox-uv-bare installed without tox-uv
k="${k-}${k+ and }not test_plugin_version_info_without_uv_package"

# only works when managed Pythons are allowed in uv + requires internet
k="${k-}${k+ and }not (test_uv_env_python_preference_complex and onlymanaged)"

%if %{without ci_tests}
# requires internet
k="${k-}${k+ and }not test_uv_dependency_present"
k="${k-}${k+ and }not test_uv_install"
k="${k-}${k+ and }not test_uv_package_editable_legacy"
k="${k-}${k+ and }not test_uv_package_no_pyproject"
k="${k-}${k+ and }not test_uv_package_requirements"
k="${k-}${k+ and }not test_uv_package_workspace"
k="${k-}${k+ and }not test_uv_python_set"
k="${k-}${k+ and }not test_version_injected_into_dependency"
k="${k-}${k+ and }not test_wheel_contains_"
k="${k-}${k+ and }not test_wheel_does_not_contain_"
%endif

# Some test invoke building (self?) with hatch-vcs
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%pytest -v "${k:+-k $k}"


%files -n python3-tox-uv
%{python3_sitelib}/tox_uv-%{version}.dist-info/
%{python3_sitelib}/tox_uv_meta/

%files -n python3-tox-uv-bare
%doc README.md
%{python3_sitelib}/tox_uv_bare-%{version}.dist-info/
%license %{python3_sitelib}/tox_uv_bare-%{version}.dist-info/licenses/LICENSE
# beware, the tox_uv module is part of the bare package!
%{python3_sitelib}/tox_uv/


%changelog
%autochangelog
