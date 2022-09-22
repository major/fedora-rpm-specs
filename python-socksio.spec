%global srcname socksio
%global _description %{expand:
Client-side sans-I/O SOCKS proxy implementation. Supports SOCKS4, SOCKS4A, and
SOCKS5.  socksio is a sans-I/O library similar to h11 or h2, this means the
library itself does not handle the actual sending of the bytes through the
network, it only deals with the implementation details of the SOCKS protocols
so you can use it in any I/O library you want.}


Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        Client-side sans-I/O SOCKS proxy implementation
License:        MIT
URL:            https://github.com/sethmlarson/socksio
Source:         %pypi_source
# downstream-only patch
Patch:          0001-Relax-flit_core-dependency.patch
BuildArch:      noarch
BuildRequires:  python3-devel


%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  %{py3_dist pytest}


%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p 1
# drop coverage addopts
rm pytest.ini


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md
# flit does not mark licenses as License-Files yet
%license %{python3_sitelib}/*.dist-info/LICENSE


%changelog
%autochangelog
