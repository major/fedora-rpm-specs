%global srcname  subprocess-tee
%global slugname subprocess_tee
%global forgeurl https://github.com/pycontribs/subprocess-tee

%global common_description %{expand:
This package provides an drop-in alternative to subprocess.run that captures
the output while still printing it in real time, just the way tee does.
}

%bcond_without tests

Name:           python-%{srcname}
Version:        0.4.1
%forgemeta
Release:        %autorelease
Summary:        A subprocess.run that works like tee, being able to display output in real time while still capturing it
URL:            %{forgeurl}
Source:         %{pypi_source}
Patch:          0001-Remove-unnecessary-test-deps.patch
License:        MIT
BuildArch:      noarch

BuildRequires: python3-devel

%description %{common_description}

%package -n python3-%{srcname}
Summary: %summary

%description -n python3-%{srcname} %{common_description}

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{slugname}

%if %{with tests}
%check
%pytest test -k "not test_molecule"
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
