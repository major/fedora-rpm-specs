Name:           python-throttler
Version:        1.2.2
Release:        %autorelease
Summary:        Easy throttling with asyncio support

# SPDX
License:        MIT
URL:            https://github.com/uburuntu/throttler
# GitHub archive contains tests and examples; PyPI sdist does not
Source:         %{url}/archive/v%{version}/throttler-%{version}.tar.gz

# Fix tests for Python 3.14
# https://github.com/uburuntu/throttler/pull/6
Patch:          %{url}/pull/6.patch

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x dev,bogus
BuildOption(install):   -l throttler

BuildArch:      noarch

# Run tests in parallel; this speeds up the build quite a bit.
BuildRequires:  %{py3_dist pytest-xdist}

%global common_description %{expand:
Zero-dependency Python package for easy throttling with asyncio support.}

%description %{common_description}


%package -n python3-throttler
Summary:        %{summary}

%description -n python3-throttler %{common_description}


%prep -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^(codecov|flake8|pytest-cov)/# &/' requirements-dev.txt


%check -a
%pytest -n auto -v


%files -n python3-throttler -f %{pyproject_files}
%doc examples/


%changelog
%autochangelog
