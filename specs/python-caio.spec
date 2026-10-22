%bcond_without tests

Name:           python-caio
Version:        0.12.4
Release:        %autorelease
Summary:        Asynchronous file IO for Linux, MacOS or Windows

License:        Apache-2.0
URL:            https://github.com/mosquito/caio/
Source:         %{pypi_source caio}

Patch0: 0001-Replace-aiomisc-with-pytest-timeout.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libaio-devel
BuildRequires:  liburing-devel

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-rerunfailures
%endif

%global _description %{expand:
caio is a Python library providing asynchronous file operations with support for
multiple high-performance backends. It automatically selects the best available
implementation for the operating system—including Linux io_uring, Linux kernel
AIO, POSIX thread-based AIO, and a pure-Python fallback—and integrates 
seamlessly with Python's asyncio event loop.}

%description %_description

%package -n     python3-caio
Summary:        %{summary}

%description -n python3-caio %_description

%prep
%autosetup -p1 -n caio-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Clean up leftover C sources and headers from site-packages
find %{buildroot}%{python3_sitearch}/caio -type f \( -name "*.c" -o -name "*.h" \) -delete

%pyproject_save_files -l caio

# Strip any .c or .h entries from the generated pyproject file list
sed -i '/\.[ch]$/d' %{pyproject_files}

%check
# caio.linux_uring calls io_uring_setup() on import, which is blocked by 
# seccomp filters in Koji/mock build environments.
%pyproject_check_import -e 'caio.linux_uring*'

# Copy tests to a subdirectory and run pytest from there so Python imports
# the fully compiled package from buildroot instead of the raw source tree.
mkdir -p _check
cp -r tests _check/
cd _check

# - '-o asyncio_mode=auto': Allows pytest-asyncio to automatically execute async def
#   tests after removing the aiomisc pytest plugin dependency.
# - '-k "not uring and not test_env_selector"':
#     * 'not uring': Skips io_uring tests because io_uring_setup() fails (ENOSYS)
#       under seccomp security filters used in mock/Koji build environments.
#     * 'not test_env_selector': Skips subprocess tests that wipe PYTHONPATH,
#       causing ModuleNotFoundError in uninstalled build environments.
%pytest -o asyncio_mode=auto -k "not uring and not test_env_selector"

%files -n python3-caio -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
