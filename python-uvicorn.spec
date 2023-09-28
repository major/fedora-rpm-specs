Name:           python-uvicorn
Version:        0.23.2
Release:        %autorelease
Summary:        The lightning-fast ASGI server
License:        BSD-3-Clause
URL:            https://www.uvicorn.org
# PyPI tarball doesn't have tests
Source:         https://github.com/encode/uvicorn/archive/%{version}/uvicorn-%{version}.tar.gz
BuildArch:      noarch

%global common_description %{expand:
Uvicorn is an ASGI web server implementation for Python.  Until recently Python
has lacked a minimal low-level server/application interface for async
frameworks.  The ASGI specification fills this gap, and means we are now able
to start building a common set of tooling usable across all async frameworks.
Uvicorn supports HTTP/1.1 and WebSockets.}


%description %{common_description}


%package -n python3-uvicorn
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-a2wsgi
BuildRequires:  python3-cryptography
BuildRequires:  python3-httpx
BuildRequires:  python3-trustme
BuildRequires:  python3-watchgod
BuildRequires:  python3-wsproto


%description -n python3-uvicorn %{common_description}


%pyproject_extras_subpkg -n python3-uvicorn standard


%prep
%autosetup -p 1 -n uvicorn-%{version}


%generate_buildrequires
%pyproject_buildrequires -x standard


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files uvicorn


%check
%pytest --verbose \
    -k 'not test_run_startup_failure and not test_fragmentation and not test_send_binary_data_to_server_bigger_than_default_on_websockets'


%files -n python3-uvicorn -f %{pyproject_files}
%doc README.md
%{_bindir}/uvicorn


%changelog
%autochangelog
