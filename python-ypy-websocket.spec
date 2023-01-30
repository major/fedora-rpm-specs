Name:           python-ypy-websocket
Version:        0.8.2
Release:        1%{?dist}
Summary:        WebSocket connector for Ypy
License:        MIT
URL:            https://github.com/y-crdt/ypy-websocket
Source:         %{pypi_source ypy_websocket}

BuildArch:      noarch
BuildRequires:  python3-devel
# Manual test requires because upstream [test] extra
# contains also mypy and pre-commit.
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-websockets

%global _description %{expand:
ypy-websocket is an async WebSocket connector for Ypy.}

%description %_description

%package -n     python3-ypy-websocket
Summary:        %{summary}

%description -n python3-ypy-websocket %_description


%prep
%autosetup -p1 -n ypy_websocket-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ypy_websocket


%check
# test_ypy_yjs.py requires https://www.npmjs.com/package/yjs
%pytest --ignore=tests/test_ypy_yjs.py


%files -n python3-ypy-websocket -f %{pyproject_files}
%doc README.md

%changelog
* Thu Jan 05 2023 Lumír Balhar <lbalhar@redhat.com> - 0.8.2-1
- Initial package