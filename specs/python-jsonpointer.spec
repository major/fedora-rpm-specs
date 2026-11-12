%global pypi_name jsonpointer

Name:           python-%{pypi_name}
Version:        3.12
Release:        %autorelease
Summary:        Resolve JSON Pointers in Python

License:        BSD-3-Clause
URL:            https://github.com/stefankoegl/python-json-pointer
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Library to resolve JSON Pointers according to RFC 6901.}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name} %{pypi_name}-stubs

%check
%python3 -m unittest discover

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md AUTHORS
%{_bindir}/jsonpointer

%changelog
%autochangelog
