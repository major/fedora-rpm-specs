%global pypi_name ajsonrpc

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        %autorelease
Summary:        Lightweight JSON-RPC 2.0 protocol implementation and asynchronous server

License:        MIT
URL:            https://github.com/pavlov99/ajsonrpc
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Lightweight JSON-RPC 2.0 protocol implementation and asynchronous server
powered by asyncio. This library is a successor of json-rpc and written by the
same team.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md
%{_bindir}/async-json-rpc-server

%changelog
%autochangelog
