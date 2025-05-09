Name:           python-quart-trio
Version:        0.12.0
Release:        %autorelease
Summary:        A Quart extension to provide trio support

# SPDX
License:        MIT
URL:            https://github.com/pgjones/quart-trio
# PyPI source distributions lack tests, changelog, etc.; use the GitHub archive
Source:         %{url}/archive/%{version}/quart-trio-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -t
BuildOption(install):   -L quart_trio

# Downstream-only: patch out coverage analysis
# 
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-coverage-analysis.patch

BuildArch:      noarch

%global common_description %{expand:
Quart-Trio is an extension for Quart to support the Trio event loop. This is an
alternative to using the asyncio event loop present in the Python standard
library and supported by default in Quart.}

%description %{common_description}


%package -n python3-quart-trio
Summary:        %{summary}

%description -n python3-quart-trio %{common_description}


%check -a
%tox -- -- -v


%files -n python3-quart-trio -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
