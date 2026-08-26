%global pypi_name hexbytes

Name:          python-%{pypi_name}
Version:       2.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python `bytes` subclass that decodes hex, with a readable console output
License:       MIT
URL:           https://github.com/ApeWorX/hexbytes
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
# Upstream pyproject.toml does not constrain find_packages, causing docs and newsfragments to be packaged
Patch:         hexbytes-2.0.0-find-packages.patch
BuildRequires: python3-eth-utils
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
