%global pypi_name electrum_aionostr

Name:           python-electrum-aionostr
Version:        0.1.0
Release:        1%{?dist}
Summary:        asyncio nostr client

License:        BSD-3-Clause
URL:            https://pypi.org/project/electrum-aionostr/
Source0:        %pypi_source
BuildArch:      noarch

Patch0:         https://github.com/spesmilo/electrum-aionostr/pull/25.patch

%global _description %{expand:
This package provides an asyncio nostr client.

This is a fork of aionostr that does not require Coincurve.}

%description %{_description}

%package -n python3-electrum-aionostr
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-electrum-aionostr %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1

# Remove bundled egg-info
rm -fr src/electrum_aionostr.egg-info

%generate_buildrequires
%pyproject_buildrequires -x crypto,tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-electrum-aionostr -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/aionostr

%changelog
%autochangelog
