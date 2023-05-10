Name:           python-system-calls
Version:        6.4.0
Release:        %{autorelease}
Summary:        System calls

License:        MIT
URL:            https://github.com/hrw/python-syscalls
Source0:        %{pypi_source system-calls}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
Simple interface to get system call numbers for any architecture.
}

%description %{_description}


%package -n python3-system-calls
Summary:        %{summary}

%description -n python3-system-calls %{_description}


%prep
%autosetup -p1 -n system-calls-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files system_calls

mkdir -p %{buildroot}%{_mandir}/man1
cp -p man/syscall.1 %{buildroot}%{_mandir}/man1/



%if %{with tests}
%check
%pytest
%endif


%files -n python3-system-calls -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/syscall
%{_mandir}/man1/syscall.1*


%changelog
%autochangelog
