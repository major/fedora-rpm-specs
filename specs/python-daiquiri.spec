%global pypi_name daiquiri
%global _description %{expand:
The %{pypi_name} library provides an easy way to configure Python logging.
It also provides some custom formatters and handlers.}

Name:           python-%{pypi_name}
Version:        3.3.0
Release:        %autorelease
Summary:        Library to configure Python logging easily

License:        Apache-2.0
URL:            https://github.com/Mergifyio/daiquiri
Source:         %{pypi_source %{pypi_name}}
BuildArch:      noarch

%description    %{_description}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Library to configure Python logging easily

BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-json-logger

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

%package -n python-%{pypi_name}-doc
Summary:        daiquiri documentation

BuildRequires:  python%{python3_pkgversion}-sphinx

%description -n python-%{pypi_name}-doc
Documentation for daiquiri

%generate_buildrequires
%pyproject_buildrequires -x test

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l daiquiri

%check
%pytest -v

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html 

%changelog
%autochangelog
