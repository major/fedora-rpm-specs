%global _description %{expand:
Client-side sans-I/O SOCKS proxy implementation. Supports SOCKS4, SOCKS4A, and
SOCKS5.  socksio is a sans-I/O library similar to h11 or h2, this means the
library itself does not handle the actual sending of the bytes through the
network, it only deals with the implementation details of the SOCKS protocols
so you can use it in any I/O library you want.}


Name:           python-socksio
Version:        1.0.0
Release:        %autorelease
Summary:        Client-side sans-I/O SOCKS proxy implementation
License:        MIT
URL:            https://github.com/sethmlarson/socksio
Source:         %{pypi_source socksio}
# https://github.com/sethmlarson/socksio/pull/61
Patch:          0001-Unpin-flit-core-dependency.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description %{_description}


%package -n python3-socksio
Summary:        %{summary}


%description -n python3-socksio %{_description}


%prep
%autosetup -n socksio-%{version} -p 1
# drop coverage addopts
rm pytest.ini


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L socksio


%check
%pytest


%files -n python3-socksio -f %{pyproject_files}
%doc README.md CHANGELOG.md
# flit does not mark licenses as License-Files yet
%license %{python3_sitelib}/socksio-%{version}.dist-info/LICENSE


%changelog
%autochangelog
