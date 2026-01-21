%bcond_without tests

%global pypi_name vdf

Name:       python-%{pypi_name}
Version:    3.4
Release:    %autorelease
Summary:    Package for working with Valve's text and binary KeyValue format
BuildArch:  noarch

License:    MIT
URL:        https://github.com/ValvePython/vdf
Source:     %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires: python3-devel
%if %{with tests}
BuildRequires: python3dist(pytest-cov) >= 2.7.0
BuildRequires: python3dist(pytest)
%endif

%global _description %{expand:
Pure python module for (de)serialization to and from VDF that works just like
json.

VDF is Valve's KeyValue text file format.}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%if %{with tests}
%check
%pyproject_check_import
%pytest \
    %dnl # https://github.com/ValvePython/vdf/issues/33
    --ignore=tests/test_binary_vdf.py
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
