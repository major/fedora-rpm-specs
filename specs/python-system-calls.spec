Name:           python-system-calls
Version:        6.13.0
Release:        %{autorelease}
Summary:        System calls

License:        MIT
URL:            https://github.com/hrw/python-syscalls
Source0:        %{pypi_source system-calls}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Simple interface to get system call numbers for any architecture.
}

%description %{_description}


%package -n python3-system-calls
Summary:        %{summary}

%description -n python3-system-calls %{_description}


%prep
%autosetup -p1 -n system_calls-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files system_calls

mkdir -p %{buildroot}%{_mandir}/man1
cp -p man/syscall.1 %{buildroot}%{_mandir}/man1/


%check
%pyproject_check_import
%pytest -v ./system_calls/tests/test*.py


%files -n python3-system-calls -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/syscall
%{_mandir}/man1/syscall.1*


%changelog
%autochangelog
