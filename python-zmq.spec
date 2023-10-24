%global common_description %{expand:
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.}

Name:           python-zmq
Version:        25.1.1
Release:        %autorelease
Summary:        Software library for fast, message-based applications

License:        MPLv2.0 and ASL 2.0 and BSD
URL:            https://zeromq.org/languages/python/
Source0:        %{pypi_source pyzmq}

BuildRequires:  gcc

BuildRequires:  pkgconfig(libzmq)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
BuildRequires:  python%{python3_pkgversion}-tornado
BuildRequires:  python%{python3_pkgversion}-gevent
BuildRequires:  python%{python3_pkgversion}-numpy

%description %{common_description}


%package -n python%{python3_pkgversion}-zmq
Summary:        %{summary}
License:        MPLv2.0
%py_provides    python%{python3_pkgversion}-pyzmq

%description -n python%{python3_pkgversion}-zmq %{common_description}

This package contains the python bindings.


%package -n python%{python3_pkgversion}-zmq-tests
Summary:        %{summary}, testsuite
License:        MPLv2.0
Requires:       python%{python3_pkgversion}-zmq = %{version}-%{release}
%py_provides    python%{python3_pkgversion}-pyzmq-tests

%description -n python%{python3_pkgversion}-zmq-tests %{common_description}

This package contains the testsuite for the python bindings.


%prep
%setup -q -n pyzmq-%{version}

# Upstream is testing with cython 3 on 3.12
sed -i -e '/cython>=3/d' pyproject.toml test-requirements.txt
sed -i -e '/min_cython_version/s/"3.*"/"0.29"/' setup.py

# remove bundled libraries
rm -rf bundled

# remove the Cython .c files in order to regenerate them:
find zmq -name "*.c" -delete

# remove shebangs
grep -lr "^#\!/usr/bin/env python" | xargs sed -i "1d"

# remove excecutable bits
find . -type f -executable | xargs chmod -x

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zmq

%check
# to avoid partially initialized zmq module from cwd
cd %{_topdir}
%pytest --pyargs zmq -v --asyncio-mode auto \
%ifarch ppc64le
-k "not (test_green_device or (Green and (test_raw or test_timeout or test_poll)))"  # this crashes on Python 3.12, TODO investigate
%endif


%files -n python%{python3_pkgversion}-zmq -f %{pyproject_files}
%doc README.md
%exclude %{python3_sitearch}/zmq/tests

%files -n python%{python3_pkgversion}-zmq-tests
%{python3_sitearch}/zmq/tests


%changelog
%autochangelog

