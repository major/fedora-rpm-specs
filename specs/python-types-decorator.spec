%global pypi_name types-decorator
%global pypi_version 5.1.8.20240310

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        3%{?dist}
Summary:        Typing stubs for decorator

License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
 Typing stubs for decoratorThis is a [PEP 561]( type stub package for the
[decorator]( package. It can be used by type-checking tools like [mypy](
[pyright]( [pytype]( PyCharm, etc. to check code that uses decorator.This
version of types-decorator aims to provide accurate annotations for
decorator5.1.*. The source for this package can be found at All fixes for types
and metadata should be...

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
 Typing stubs for decoratorThis is a [PEP 561]( type stub package for the
[decorator]( package. It can be used by type-checking tools like [mypy](
[pyright]( [pytype]( PyCharm, etc. to check code that uses decorator.This
version of types-decorator aims to provide accurate annotations for
decorator5.1.*. The source for this package can be found at All fixes for types
and metadata should be...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/decorator-stubs
%{python3_sitelib}/types_decorator-%{version}.dist-info/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.8.20240310-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.1.8.20240310-2
- Review fixes.

* Tue Apr 02 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.1.8.20240310-1
- Initial package.
