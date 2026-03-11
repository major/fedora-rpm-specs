Name:           python-types-pygments
Version:        2.19.0.20251121
Release:        %autorelease
Summary:        Typing stubs for Pygments

License:        Apache-2.0
URL:            https://pypi.org/project/types-Pygments/
Source:         %{pypi_source types_pygments}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a PEP 561 type stub package for the boto package. It can be used by
type-checking tools like mypy, PyCharm, pytype etc. to check code that uses
boto. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/boto. All fixes for types
and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.}

%description %_description

%package -n     python3-types-pygments
Summary:        %{summary}

%description -n python3-types-pygments %_description

%prep
%autosetup -p1 -n types_pygments-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pygments-stubs

%check
%pyproject_check_import pygments-stubs

%files -n python3-types-pygments -f %{pyproject_files}

%changelog
%autochangelog
