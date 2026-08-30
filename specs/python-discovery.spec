Name:           python-discovery
Version:        1.6.0
Release:        %autorelease
Summary:        Python interpreter discovery

License:        MIT
URL:            https://github.com/tox-dev/python-discovery
Source:         %{url}/archive/%{version}/python-discovery-%{version}.tar.gz

# Downstream-only: avoid usage of vermin in the test suite
#
# A single test, test_script_parses_down_to_python27, uses vermin to verify
# that the script to collect interpreter information would parse on Python 2.7.
# It is not worth packaging vermin solely for this check. This patch removes
# the top-level import and skips the test that would have used it. To reduce
# the need for frequent rebasing due to changing version bounds, we use
# %%pyproject_patch_dependency to avoid generating the vermin test dependency,
# rather than adjusting pyproject.toml in this patch.
Patch:          0001-Downstream-only-avoid-usage-of-vermin-in-the-test-su.patch

BuildSystem:    pyproject
BuildOption(install): --assert-license python_discovery
BuildOption(generate_buildrequires): --dependency-groups test

BuildArch:      noarch

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-discovery
Summary:        %{summary}

%description -n python3-discovery %{common_description}


%prep -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency covdefaults:ignore
# See 0001-Downstream-only-avoid-usage-of-vermin-in-the-test-su.patch.
%pyproject_patch_dependency vermin:ignore


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%check -a
# Requires python3dist(vermin):
k="${k-}${k+ and }not test_script_parses_down_to_python27"

%pytest -k "${k-}" -rs --verbose


%files -n python3-discovery -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
