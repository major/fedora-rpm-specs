%bcond tests 1

Name:           openapi-python-client
Version:        0.24.3
Release:        %autorelease
Summary:        Generate modern Python clients from OpenAPI

License:        MIT
URL:            https://github.com/openapi-generators/openapi-python-client
Source0:        %{url}/archive/refs/tags/v%{version}/openapi-python-client-%{version}.tar.gz
Source1:        openapi-python-client.man1

BuildRequires:  python3-devel
BuildRequires:  python3-hatchling
BuildRequires:  python3-mypy
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock

BuildArch:      noarch

%global _description %{expand:
The openapi-python-client is a powerful tool designed to generate
modern Python clients from OpenAPI 3.0+ documents supporting both
synchronous and asynchronous HTTP requests. It automates the creation of
Python classes and methods that correspond to the endpoints and schema
defined in your OpenAPI specification, making it easier to interact with
your API in a type-safe manner.}

%description %{_description}


%package -n python3-%{name}
Summary:        %{summary}

%description -n python3-%{name} %{_description}


%prep
%autosetup -p1 -n openapi-python-client-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l openapi_python_client

# Install man page
mkdir -p %{buildroot}%{_mandir}/man1
cp %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1
gzip %{buildroot}%{_mandir}/man1/%{name}.1


%check
%pyproject_check_import

%if %{with tests}
%pytest tests
%endif


%files -n %{name} -f %{pyproject_files}
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%doc README.md
%doc CHANGELOG.md
%license LICENSE


%changelog
%autochangelog
