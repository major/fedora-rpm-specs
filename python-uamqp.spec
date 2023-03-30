# tests are enabled by default
%bcond_without tests

%global         srcname        uamqp
%global         forgeurl       https://github.com/Azure/azure-uamqp-python/
Version:        1.6.4
# Microsoft devs released 1.6.4 on PyPi but forgot to tag the repo.
# Upstream issue: https://github.com/Azure/azure-uamqp-python/issues/364
%global         commit         0bee678087a85a8b74ca57c5b0eb0b75b6c0cd96
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        AMQP 1.0 client library for Python

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

# Still waiting on full OpenSSL 3.x support.
# https://github.com/Azure/azure-uamqp-python/issues/276
Patch0:         0001-Strip-Werror-from-compile.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
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

# Remove unexpected cmake requirement from python requirements list.
sed -i '/cmake/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files uamqp


%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc HISTORY.rst README.rst


%changelog
%autochangelog
