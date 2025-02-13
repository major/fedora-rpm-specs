Name:           python-quart-trio
Version:        0.12.0
Release:        %autorelease
Summary:        A Quart extension to provide trio support

# SPDX
License:        MIT
URL:            https://github.com/pgjones/quart-trio
# PyPI source distributions lack tests, changelog, etc.; use the GitHub archive
Source:         %{url}/archive/%{version}/quart-trio-%{version}.tar.gz

# Downstream-only: patch out coverage analysis
# 
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-coverage-analysis.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
Quart-Trio is an extension for Quart to support the Trio event loop. This is an
alternative to using the asyncio event loop present in the Python standard
library and supported by default in Quart.}

%description %{common_description}


%package -n python3-quart-trio
Summary:        %{summary}

%description -n python3-quart-trio %{common_description}


%prep
%autosetup -n quart-trio-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files quart_trio


%check
%tox -- -- -v


%files -n python3-quart-trio -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
