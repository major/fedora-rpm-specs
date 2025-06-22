Name:           python-flexcache
Version:        0.3
Release:        %autorelease
Summary:        Cache on disk the result of expensive calculations

License:        BSD-3-Clause
URL:            https://github.com/hgrecco/flexcache
Source:         %{pypi_source flexcache}

# Increase the value of FS_SLEEP in the tests (fix #4)
# https://github.com/hgrecco/flexcache/pull/5
#
# Fixes:
#
# test_name_by_paths fails flakily on ppc64le and s390x
# https://github.com/hgrecco/flexcache/issues/4
Patch:          %{url}/pull/5.patch

BuildSystem:            pyproject
BuildOption(install):   -l flexcache
# We remove flexcache.testsuite manually in %%install.
BuildOption(check):     -e 'flexcache.testsuite*'

BuildArch:      noarch

# See the test extra in pyproject.toml. We list test dependencies manually
# since we do not want pytest-cov
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters)
# and the other pytest plugins are spurious
# (https://github.com/hgrecco/flexacache/pull/3).
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
A robust and extensible package to cache on disk the result of expensive
calculations.}

%description %{common_description}


%package -n python3-flexcache
Summary:        %{summary}

%description -n python3-flexcache %{common_description}


%install -a
# Upstream probably doesn’t want to install flexcache.testsuite, but we don’t
# know how to suggest a fix given “[BUG] options.packages.find.exclude not
# taking effect when include_package_data = True”,
# https://github.com/pypa/setuptools/issues/3260.
#
# Still, we don’t want to install the test suite, so we just remove the files
# manually for now.
rm -rvf '%{buildroot}%{python3_sitelib}/flexcache/testsuite'
sed -r -i '/\/flexcache\/testsuite/d' %{pyproject_files}


%check -a
%pytest


%files -n python3-flexcache -f %{pyproject_files}
%doc README.rst
%doc CHANGES


%changelog
%autochangelog
