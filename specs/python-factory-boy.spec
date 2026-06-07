# tests disabled in RHEL
%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

%global srcname factory_boy
%global desc factory_boy is a fixtures replacement based on thoughtbot's factory_girl\
<http://github.com/thoughtbot/factory_girl>.\
\
Its features include:\
\
- Straightforward syntax\
- Support for multiple build strategies (saved/unsaved instances, attribute\
  dicts, stubbed objects)\
- Powerful helpers for common cases (sequences, sub-factories, reverse\
  dependencies, circular factories, ...)\
- Multiple factories per class support, including inheritance\
- Support for various ORMs (currently Django, Mogo, SQLAlchemy)\

Name: python-factory-boy
Version: 3.3.3
Release: %autorelease
Summary: A versatile test fixtures replacement based on thoughtbot's factory_girl
License: MIT
URL: https://github.com/rbarrois/factory_boy
Source0: https://github.com/rbarrois/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
%if %{with tests}
BuildRequires: python3-pytest
BuildRequires: python3-faker >= 0.7.0
BuildRequires: python3-sqlalchemy
BuildRequires: python3-sqlalchemy-utils
BuildRequires: python3-coverage
BuildRequires: python3-flake8
BuildRequires: python3-isort
BuildRequires: python3-pillow
BuildRequires: tox
BuildRequires: python3-django
BuildRequires: python3-flask
BuildRequires: python3-flask-sqlalchemy
%endif

%description
%desc

%package -n python3-factory-boy
Summary: A versatile test fixtures replacement based on thoughtbot's factory_girl
Suggests: %{name}-doc = %{version}-%{release}

%description -n python3-factory-boy
%desc

%package doc
Summary: API documentation for %{name}

%description doc
Documentation for the %{name} API

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Clean the doc dir
rm -f docs/Makefile
rm -rf docs/_static
find examples -type f -print0 | xargs -0 chmod 0644

%install
%pyproject_install
%pyproject_save_files -l factory

%if %{with tests}
%check
SKIP_MONGOENGINE=1 %pytest
%endif

%files -n python3-factory-boy -f %{pyproject_files}

%files doc
%doc README.rst CODE_OF_CONDUCT.md CONTRIBUTING.rst CREDITS docs examples
%license LICENSE

%changelog
%autochangelog
