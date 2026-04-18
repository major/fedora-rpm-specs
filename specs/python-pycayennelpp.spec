%global upname pycayennelpp

Name:           python-%{upname}
Version:        2.4.0
Release:        %autorelease
Summary:        Cayenne Low Power Payload (CayenneLPP) decoder and encoder in Python

License:        MIT
URL:            https://github.com/smlng/pycayennelpp
Source:         %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

Patch1:         0001-Stop-using-pytest-runner.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies:
BuildRequires: python3dist(pytest)

%global _description %{expand:
A Cayenne Low Power Payload (CayenneLPP) decoder and encoder written in Python.

PyCayenneLPP offers a concise interface with proper encoding and decoding functionality for the CayenneLPP format, supporting many sensor types. The project aims for overall high code quality and good test coverage.
}

%description %_description

%package -n python3-%{upname}
Summary:        %{summary}
Recommends:     python3-%{upname}

%description -n python3-%{upname} %_description


%prep
%autosetup -p1 -n %{upname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l cayennelpp


%check
%pytest


%files -n python3-%{upname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
