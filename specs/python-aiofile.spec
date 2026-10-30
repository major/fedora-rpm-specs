%bcond_without tests

Name:           python-aiofile
Version:        3.12.3
Release:        %autorelease
Summary:        Asynchronous file operations

License:        Apache-2.0
URL:            https://github.com/mosquito/aiofile
Source:         %{pypi_source aiofile}

Patch0: 0001-tests-do-not-use-event_loop-fixture.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
%endif


%global _description %{expand:
AIOFile provides real asynchronous file operations for Python with asyncio
support. It utilizes the caio library to provide multiple async I/O backends,
automatically choosing the best available option based on system compatibility.
Supported backends include Linux native io_uring and libaio, as well as
thread-based implementations for POSIX and pure Python fallback scenarios.
It features both a high-level file-like API and a low-level API for concurrent,
independent I/O operations.}



%description %_description

%package -n     python3-aiofile
Summary:        %{summary}

%description -n python3-aiofile %_description


%prep
%autosetup -p1 -n aiofile-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l aiofile


%check
%pyproject_check_import
%pytest -o asyncio_mode=auto


%files -n python3-aiofile -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
