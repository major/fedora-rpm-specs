Name:           python-simframe
Version:        1.0.5
Release:        %autorelease
Summary:        Python framework for setting up and running scientific simulations
License:        BSD-3-Clause
URL:            https://github.com/stammler/simframe
Source:         %{pypi_source simframe}

# Install as pure-Python
# https://github.com/stammler/simframe/pull/4
Patch0:         %{url}/pull/4.patch
# Downstream-only:
# Revert "Adjusting unit tests for deprecation warning"
#
# This reverts commit 13836da8187d3c7d2565f602d77f21de063ac48b.
#
# The new atol/rtol keywords for gmres are not available before Scipy
# 0.14.0, so we must keep using the old, deprecated tol keyword.
#
# scipy-1.14.0 is available for F42+ only
# https://bugzilla.redhat.com/show_bug.cgi?id=2211813
Patch101:       0001-Revert-Adjusting-unit-tests-for-deprecation-warning.patch

BuildArch:      noarch

BuildRequires:  python3-devel
# Needed because meson.build declares the project as using the 'c' language,
# even though there are currently no C sources.
BuildRequires:  gcc

BuildRequires:  %{py3_dist pytest}
# for %%pyproject_buildrequires -p
BuildRequires:  pyproject-rpm-macros >= 1.15.1

%global _description %{expand:
Simframe is a Python framework to facilitate scientific simulations.
The scope of the software is to provide a framework which can hold
data fields, which can be used to integrate differential equations,
and which can read and write data files.}

%description %_description


%package -n python3-simframe
Summary:        %{summary}

%description -n python3-simframe %_description


%package doc
Summary:        Documentation and examples for %{name}

%description doc
%{summary}.


%prep
# Apply patches manually
%autosetup -n simframe-%{version} -N
%autopatch -M100 -p1

# Apply scipy >= 0.14 reversal patch only for F42-
%if 0%{?fedora} < 42
%patch -P101 -p1
%endif

# fix file permissions
find . -type f -perm /0111 -exec chmod -v a-x '{}' '+'


%generate_buildrequires
%pyproject_buildrequires -p


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L simframe


%check
# Testing exact memory usage is not portable.
k="${k-}${k+ and }not test_group_memory_usage"
%pytest -k "${k-}"
# remove installed tests
rm -rf %{buildroot}/%{python3_sitelib}/tests


%files -n python3-simframe -f %{pyproject_files}
%license LICENSE
%doc README.md


%files doc
%doc README.md
%license LICENSE
%doc examples/


%changelog
%autochangelog
