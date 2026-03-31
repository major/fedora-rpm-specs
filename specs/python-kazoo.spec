# Created by pyp2rpm-1.0.1
%global pypi_name kazoo

Name:           python-%{pypi_name}
Version:        2.11.0
Release:        %autorelease
Summary:        Higher level Python Zookeeper client

License:        Apache-2.0
URL:            https://kazoo.readthedocs.org
Source0:        https://pypi.python.org/packages/source/k/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Kazoo is a Python library designed to make working with Zookeeper a more
hassle-free experience that is less prone to errors.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        Higher level Python Zookeeper client


%description -n python3-%{pypi_name}
Kazoo is a Python library designed to make working with Zookeeper a more
hassle-free experience that is less prone to errors.


%package doc
Summary:    Documentation for %{name}
License:    Apache-2.0


%description doc
%{_description}

This package contains documentation in HTML format.


%prep
%autosetup -n %{pypi_name}-%{version}

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%generate_buildrequires
%pyproject_buildrequires -x docs

%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l kazoo

#delete tests
rm -fr %{buildroot}%{python3_sitelib}/%{pypi_name}/tests/
sed -i '\@/kazoo/tests\(/.*\)\?$@d' %{pyproject_files}

# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%check
%pyproject_check_import kazoo -e kazoo.testing -e kazoo.testing.* -e kazoo.handlers.eventlet -e kazoo.tests -e kazoo.tests.* -e kazoo.handlers.gevent


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md LICENSE


%files doc
%doc html


%changelog
%autochangelog
