# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%undefine _py3_shebang_s

Name:           python-jupyter-client
Version:        8.6.1
Release:        %autorelease
Summary:        Jupyter protocol implementation and client libraries

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://jupyter.org
Source0:        %{pypi_source jupyter_client}

# Avoid a DeprecationWarning on Python 3.13+
Patch:          https://github.com/jupyter/jupyter_client/pull/1027.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%bcond tests 1

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
