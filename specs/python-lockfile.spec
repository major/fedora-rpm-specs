# allow building without running the test suite
%bcond_without tests

%global pypi_name lockfile

%global common_description %{expand:
The lockfile module exports a FileLock class which provides a simple API for
locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms. The
lock mechanism relies on the atomic nature of the link (on Unix) and mkdir (on
Windows) system calls.}

Name:           python-%{pypi_name}
Summary:        Platform-independent file locking module
Epoch:          1
Version:        0.12.2
Release:        %autorelease
License:        MIT

URL:            https://github.com/openstack/pylockfile
Source0:        %{pypi_source}

# Remove __init__ method from Test classes to be able to use pytest
# Update all metadata from nose to pytest
# Upstream is dead so this is downstream only
Patch:          pytest.patch

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(pbr) >= 1.8
BuildRequires:  python3dist(sphinx)

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}


%package -n     python-%{pypi_name}-doc
Summary:        lockfile documentation
%description -n python-%{pypi_name}-doc
Documentation for lockfile


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc/source html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc ACKS AUTHORS ChangeLog README.rst RELEASE-NOTES


%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE


%changelog
%autochangelog
