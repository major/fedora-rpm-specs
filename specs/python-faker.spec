#https://homer.apps.099c.org/ tests disabled in RHEL
%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

%global srcname faker
%global _description\
Faker is a Python package that generates fake data for you. Whether you need\
to bootstrap your database, create good-looking XML documents, fill-in your\
persistence to stress test it, or anonymize data taken from a production\
service, Faker is for you.

Name: python-%{srcname}
Version: 35.0.0
Release: %autorelease
Summary: Faker is a Python package that generates fake data for you
License: MIT
URL: https://faker.readthedocs.io
Source: https://github.com/joke2k/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
%if %{with tests}
BuildRequires: python3-pytest
BuildRequires: python3-dateutil
BuildRequires: python3-freezegun
BuildRequires: python3-validators
BuildRequires: python3-pillow
%endif

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%py_provides python3-%{srcname}
Suggests: %{name}-doc = %{version}-%{release}

%description -n python3-%{srcname} %_description

%package doc
Summary: Documentation for %{name}

%description doc %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%if %{with tests}
%check
# Exclude tests that require the faker.sphinx module
%pytest --ignore-glob='tests/sphinx/*'
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/faker

%files doc
%license LICENSE.txt
%doc README.rst CHANGELOG.md CONTRIBUTING.rst RELEASE_PROCESS.rst docs/*.rst

%changelog
%autochangelog
