%global forgeurl https://github.com/dask/distributed
%global srcname distributed

# Can be used to deal with the dependency loop:
# dask -> dask-expr -> distributed -> dask -> distributed
# drops the dask requirement, so this can be built before
# dask-expr and then dask
%bcond bootstrap 0

Name:           python-%{srcname}
Version:        2024.12.1
%global tag     2024.12.1
Release:        %autorelease
Summary:        Distributed scheduler for Dask
%forgemeta

# Main files: BSD-3-Clause
# distributed/comm/tcp.py
#   - Backport from Tornado 6.2: Apache-2.0
#   - Backport from Trio: Apache-2.0 OR MIT
# distributed/compatibility.py:
#   - Backport from Tornado 6.2: Apache-2.0
#   - Backport from Python 3.12 and 3.10: Python-2.0.1
# distributed/_concurrent_futures_thread.py:
#   - Copied from Python 3.6: Python-2.0.1
# distributed/threadpoolexecutor.py:
#   - Copied from Python 3.5: Python-2.0.1
# distributed/http/static/js/anime.min.js: MIT 
# distributed/http/static/js/reconnecting-websocket.min.js: MIT
License:        BSD-3-Clause AND Apache-2.0 AND (Apache-2.0 OR MIT) AND Python-2.0.1 AND MIT
URL:            https://distributed.dask.org
# PyPI sources do not contain tests.
Source:         %forgesource
# Fedora specific.
Patch:          0001-Increase-test-timeout-for-slower-architectures.patch
Patch:          0002-Install-test-packages.patch
Patch:          0003-Disable-warnings-as-errors-in-tests.patch
Patch:          0004-Loosen-up-some-dependencies.patch
# https://github.com/dask/distributed/pull/7765
Patch:          0005-Skip-doc-test-when-not-running-from-a-git-checkout.patch
# Fix TLS certs to work with OpenSSL 3.
# https://github.com/dask/distributed/issues/8701
# https://github.com/dask/distributed/pull/8707
Patch:          0006-Update-make_tls_certs.py-work-with-openssl-3-8701.patch
# Drop this patch when we get pytest 8.
Patch:          0007-Revert-test-changes-for-pytest-8.patch
# Point the test at the uninstalled version.
Patch:          0008-Avoid-using-sys.prefix-in-CLI-test.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc
BuildRequires:  python3-devel
# Test dependencies
BuildRequires:  python3dist(aiohttp)
# asyncssh must be skipped because we don't have an ssh server we can connect to.
# BuildRequires:  python3dist(asyncssh)
# Tests need a newer version than currently available.
# BuildRequires:  python3dist(bokeh)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(ipywidgets)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(lz4)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
# paramiko must be skipped because we don't have an ssh server we can connect to.
# BuildRequires:  python3dist(paramiko)
BuildRequires:  python3dist(prometheus-client)
BuildRequires:  python3dist(pyarrow)
BuildRequires:  python3dist(pytest) >= 4
BuildRequires:  python3dist(pytest-repeat)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(pytest-timeout)
# https://github.com/dask/distributed/issues/5186
# BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pyzmq)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(zstandard)

%description
Dask.distributed is a lightweight library for distributed computing in Python.
It extends both the concurrent.futures and dask APIs to moderate sized
clusters.


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildArch:      noarch

%description -n python3-%{srcname}
Dask.distributed is a lightweight library for distributed computing in Python.
It extends both the concurrent.futures and dask APIs to moderate sized
clusters.


%prep
%forgeautosetup -p1

%if %{with bootstrap}
# patch out the dask dependency so we can bootstrap it
sed -r -i '/(dask)[<=> ]+[0-9]+/d' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%if %{without bootstrap}
pushd docs

# protocol/tests/test_protocol.py
# https://github.com/dask/distributed/issues/8700
k="${k-}${k+ and }not test_deeply_nested_structures"

# tests/test_client.py
# https://github.com/dask/distributed/issues/8708
k="${k-}${k+ and }not test_upload_file_zip"

# https://github.com/dask/distributed/pull/8709
k="${k-}${k+ and }not test_git_revision"

# https://github.com/dask/distributed/issues/8437
k="${k-}${k+ and }not test_steal_twice"

pytest_args=(
  -m 'not avoid_ci and not flaky and not slow'

  -k "${k-}"

  --timeout_method=signal

  --pyargs %{srcname}
)

# Remove JUPYTER_PLATFORM_DIRS after we get jupyter-core >=7.
# Disable IPv6 because it sometimes doesn't work:
# https://github.com/dask/distributed/issues/4514
DESTDIR=%{buildroot} DISABLE_IPV6=1 JUPYTER_PLATFORM_DIRS=1 \
    %{pytest} "${pytest_args[@]}"
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc AUTHORS.md CONTRIBUTING.md README.rst
%{_bindir}/dask-scheduler
%{_bindir}/dask-ssh
%{_bindir}/dask-worker

%changelog
%autochangelog
