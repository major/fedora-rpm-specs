# tests are enabled by default
%bcond_without tests

%global         srcname        uamqp
%global         forgeurl       https://github.com/Azure/azure-uamqp-python/
Version:        1.6.0
# Microsoft devs released 1.6.0 on PyPi but forgot to tag the repo.
%global         commit         375b99b1c6aa890270bde6af2e2cc9e1630d8f0e
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        AMQP 1.0 client library for Python

License:        MIT
URL:            %forgeurl
Source0:        %forgesource
# Fix build with GCC 11
Patch1:         %{name}-treat-warnings-as-warnings.patch

# Relax the range checks on the OpenSSL version
# OpenSSL 3.0 has a high degree of API compatibility with the 1.1.1
# branch, so the 1.1 code branches are also valid for higher versions.
#
# Note that this patch does not address the deprecation warnings
# introduced by OpenSSL 3.0.
#
# Proposed upstream by Ubuntu folks.
# https://github.com/Azure/azure-c-shared-utility/pull/577
Patch2:         python-uamqp-openssl3.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(setuptools)

%if %{with tests}
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(six)
%endif

%global         _description %{expand:An AMQP 1.0 client library for Python.}

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%py_provides python3-%{srcname}

%description -n python3-%{srcname}
%{_description}


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files uamqp


%if %{with tests}
%check
%pytest --disable-warnings -k "not test_error_loop_arg_async"
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc HISTORY.rst README.rst


%changelog
%autochangelog
