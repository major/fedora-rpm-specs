%global extras json,lua,valkey,vectorset

Name:           python-fakeredis
Version:        2.35.1
Release:        %autorelease
Summary:        A python implementation of Redis Protocol API

License:        BSD-3-Clause
URL:            https://github.com/cunla/fakeredis-py
Source:         %{pypi_source fakeredis}

# The `lupa` library ships with bundled lua versions in upstream, which, makes
# this code work as-is, but in our downstream versions of `python3-lupa`, we
# are packaging it without any lua source (--no-bundle), in that case, neither
# lupa or fakeredis have a way to indicate the location of lua sources when
# installed on the system. This patch aims to use `lupa.LuaRuntime()` directly,
# as it correctly picks the LuaJIT and Lua 5.1 that is installed alongside with
# python3-lupa.
Patch:          patch-script-mixing-to-use-luaruntime-directly.diff
# This patch adds a command called "fakeredis" in one of the tests, to avoid
# erroring out during the pytest execution. This has no effect on the
# get_connection function, as the `command_name` is not being used anywhere,
# but the interface for the function requires it. In newer versions of
# redis-py, this is made optional and it should work, but since python-redis is
# not being updated for a while, we need to maintain this patch.
Patch1:         patch-get_connection.diff

BuildArch:      noarch

BuildRequires:  tomcli

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
%pyproject_check_import

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
