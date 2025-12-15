# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%undefine _py3_shebang_s

Name:           python-jupyter-client
Version:        8.7.0
Release:        %autorelease
Summary:        Jupyter protocol implementation and client libraries

License:        BSD-3-Clause
URL:            https://jupyter.org
Source0:        %{pypi_source jupyter_client}

BuildArch:      noarch

BuildRequires:  python3-devel

%bcond bootstrap 0
%bcond tests %{without bootstrap}

%if %{with tests}
# Optional test dependency, look for test_datetimes_msgpack
BuildRequires:  python3dist(msgpack)
# For test_load_ips
BuildRequires:  /usr/sbin/ip
BuildRequires:  /usr/sbin/ifconfig
%endif

%description
This package contains the reference implementation of the Jupyter protocol.
It also provides client and kernel management APIs for working with kernels.

It also provides the `jupyter kernelspec` entrypoint for installing kernelspecs
for use with Jupyter frontends.

%package -n     python3-jupyter-client
Summary:        %{summary}

# It fallbacks to ifconfig without this, and ifconfig is deprecated
Recommends:     python3-netifaces

Obsoletes:      python-jupyter-client-doc < 8.6.1-10

%description -n python3-jupyter-client
This package contains the reference implementation of the Jupyter protocol.
It also provides client and kernel management APIs for working with kernels.

It also provides the `jupyter kernelspec` entrypoint for installing kernelspecs
for use with Jupyter frontends.

%prep
%autosetup -p1 -n jupyter_client-%{version}
# Drop dependencies on coverage, linters etc.
sed -Ei '/"\b(codecov|coverage|mypy|pre-commit|pytest-cov)\b",/d' pyproject.toml
# Remove upper version limit for pytest
sed -i 's/"pytest<[^"]*"/"pytest"/' pyproject.toml
# Increase test timeout -- Koji builds can be slower
# Fixes https://bugzilla.redhat.com/2389378
sed -i 's/TIMEOUT = 30/TIMEOUT = 300/' tests/test_client.py


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyter_client


%if %{with tests}
%check
# The two tests testing signals for kernels are flaky because
# if it takes the kernel more than one second to respond, it's killed.
# The tests work fine outside mock.
# test_open_tunnel needs ssh and internet connections.
%pytest -Wdefault -v -k "not test_signal_kernel_subprocesses and not test_async_signal_kernel_subprocesses and not test_open_tunnel"
%endif


%files -n python3-jupyter-client -f %{pyproject_files}
%doc README.md
%{_bindir}/jupyter-kernel
%{_bindir}/jupyter-kernelspec
%{_bindir}/jupyter-run


%changelog
%autochangelog
