%global extras json,lua,valkey

Name:           python-fakeredis
Version:        2.34.0
Release:        %autorelease
Summary:        A python implementation of Redis Protocol API

License:        BSD-3-Clause
URL:            https://github.com/cunla/fakeredis-py
Source:         %{pypi_source fakeredis}

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-hypothesis
BuildRequires:  python3-valkey
BuildRequires:  valkey


%global _description %{expand:
Implementation of Redis API in python without having a server running. Fully
compatible with using redis-py.}

%description %_description

%package -n     python3-fakeredis
Summary:        %{summary}

%description -n python3-fakeredis %_description

%pyproject_extras_subpkg -n python3-fakeredis %{extras}


%prep
%autosetup -p1 -n fakeredis-%{version}


%generate_buildrequires
%pyproject_buildrequires -x %{extras}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l fakeredis


%check
# fakeredis scripting mixin imports optional Lua runtimes (lupa.lua54) which
# are not always present in Fedora builds
%pyproject_check_import -e fakeredis.commands_mixins.scripting_mixin

%{_bindir}/valkey-server --bind 127.0.0.1 --port 6390 &
VALKEY_SERVER_PID=$!
# Skip the failing tests or missing dependencies ones.
%pytest \
    --ignore=test/test_mixins/test_redis_8_4.py \
    --ignore=test/test_json \
    --ignore=test/test_mixins \
    --ignore=test/test_asyncredis.py \
    --ignore=test/test_hypothesis/test_hash.py \
    --ignore=test/test_hypothesis/test_transaction.py \
    --ignore=test/test_hypothesis/test_zset.py \
    --ignore=test/test_hypothesis_joint.py \
    -m "not tcp_server"
kill $VALKEY_SERVER_PID

%files -n python3-fakeredis -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
