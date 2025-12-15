%global pypi_name ipfshttpclient
%global prerelease a2

Name:          python-%{pypi_name}
Version:       0.8.0
Release:       %autorelease -p -s %{prerelease}
BuildArch:     noarch
Summary:       A Python client library for the IPFS API
License:       MIT
URL:           https://github.com/ipfs-shipyard/py-ipfs-http-client
VCS:           git:%{url}.git
Source0:       %{pypi_source %{pypi_name} %{version}%{prerelease}}
# Fedora-specific. Fedora ships a higher but still compatible versions of a
# build dependencies.
Patch:         python-ipfshttpclient-0001-Relax-dependencies.patch
# Likewise. Our pytest is a very recent.
Patch:         python-ipfshttpclient-0002-Adjust-test-for-Pytest-7.patch
Patch:         python-ipfshttpclient-0003-Adjust-to-Python-3.14.patch
BuildRequires: python3-httpcore
BuildRequires: python3-httpx
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cid
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-dependency
BuildRequires: python3-pytest-localserver
BuildRequires: python3-pytest-mock
BuildSystem:   pyproject
BuildOption(install): %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
# This test requires a working IPFS node which we don't have in Fedora. Even if
# we have one it will require internet access to operate properly which is not
# available while building.
%pytest -k 'not test_ipfs_node_available'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md RELEASE.md
%license LICENSE

%changelog
%autochangelog
