# tests are enabled by default
%bcond_without tests

%global         reponame        azure-uamqp-python
%global         srcname         uamqp

# Upstream doesn't tag/release consistently.
%global         commit          e506d70252bf5838045d7754829bada85428792e

Name:           python-%{srcname}
Version:        1.6.5
Release:        %autorelease
Summary:        AMQP 1.0 client library for Python

License:        MIT
URL:            https://github.com/Azure/azure-uamqp-python/
Source0:        %{url}/archive/%{commit}/%{srcname}-%{version}.tar.gz

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
%autosetup -p1 -n %{reponame}-%{commit}

# Remove unexpected cmake requirement from python requirements list.
sed -i '/cmake/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files uamqp


%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc HISTORY.rst README.rst


%changelog
%autochangelog
