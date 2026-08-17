%bcond_without tests

%global forgeurl https://github.com/solsticegamestudios/steam
Version:    1.6.1
%global tag v%{version}
%forgemeta

Name:       python-steam
Release:    %autorelease
Summary:    Python package for interacting with Steam. Fork of ValvePython/steam
BuildArch:  noarch

License:    MIT
URL:        %{forgeurl}
Source:     %{forgesource}

BuildRequires: protobuf-compiler
BuildRequires: python3-devel

%if %{with tests}
BuildRequires: python3dist(gevent) >= 1.3.0
BuildRequires: python3dist(gevent-eventemitter) >= 2.1
BuildRequires: python3dist(protobuf) >= 3.0.0
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)
BuildRequires: python3dist(vcrpy)
%endif

%global _description %{expand:
A python module for interacting with various parts of Steam.

A fork of ValvePython/steam, which has apparently been abandoned.}

%description %{_description}


%package -n python3-steam
Summary:    %{summary}

%description -n python3-steam %{_description}


%prep
%forgeautosetup
sed -i 's/urllib3<2/urllib3/' setup.py

# Regenerate protobuf files
protoc --python_out=steam/protobufs --proto_path=protobufs protobufs/*.proto
sed -i -E 's/^import ([a-zA-Z0-9_]+_pb2)/from . import \1/' steam/protobufs/*_pb2.py

# Patch tests to use built-in unittest.mock instead of mock
sed -i -E 's/from mock import/from unittest.mock import/g' tests/*.py
sed -i -E 's/import mock/from unittest import mock/g' tests/*.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l steam


%if %{with tests}
%check
%pyproject_check_import
%pytest --ignore=tests/test_webapi.py --ignore=tests/test_webauth.py -k "not test_steam64_from_url"
%endif


%files -n python3-steam -f %{pyproject_files}
%doc README.rst CHANGES.md


%changelog
%autochangelog
