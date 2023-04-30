Name:           python-posix-ipc
Version:        1.1.1
Release:        %autorelease
Summary:        POSIX IPC primitives for Python
License:        BSD-3-Clause
URL:            https://github.com/osvenskan/posix_ipc
Source:         %{pypi_source posix_ipc}

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
posix_ipc is a Python module (written in C) that permits creation and manipulation
of POSIX inter-process semaphores, shared memory and message queues on platforms
supporting the POSIX Realtime Extensions a.k.a. POSIX 1003.1b-1993.
This includes nearly all Unices and Windows + Cygwin ≥ 1.7.}


%description %_description

%package -n     python3-posix-ipc
Summary:        %{summary}
# The original package python3-posix_ipc was retired
# so I take that opportunity to rename the package
# to python3-posix-ipc when unretiring it.
Obsoletes:      python3-posix_ipc < 1
%py_provides    python3-posix_ipc


%description -n python3-posix-ipc %_description


%prep
%autosetup -p1 -n posix_ipc-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files posix_ipc


%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m unittest discover


%files -n python3-posix-ipc -f %{pyproject_files}
%license LICENSE
%doc README.md USAGE.md


%changelog
%autochangelog
