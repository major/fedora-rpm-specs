%{?python_enable_dependency_generator}
%global srcname sphinxcontrib-programoutput
%global _docdir_fmt %{name}

Name:           python-sphinxcontrib-programoutput
Version:        0.17
Release:        %autorelease
Summary:        Extension to insert output of commands into documents

License:        BSD
URL:            https://pypi.python.org/pypi/sphinxcontrib-programoutput
Source0:        https://github.com/NextThought/sphinxcontrib-programoutput/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-sphinx

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(sphinx) >= 1.3.5
BuildRequires:  python3-pytest
# The documentation runs commands like 'python -V' and 'python --help'.
# Any python version is fine.
BuildRequires:  python-unversioned-command
BuildRequires:  git
BuildRequires:  web-assets-devel

%description
A Sphinx extension to literally insert the output of arbitrary
commands into documents, helping you to keep your command examples
up to date.

%package -n python3-%{srcname}
Summary:       %{summary}

Requires:       js-jquery
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A Sphinx extension to literally insert the output of arbitrary
commands into documents, helping you to keep your command examples
up to date.

%prep
%autosetup -n %{srcname}-%{version} -p1
sed -r -i s/python/python3/ src/sphinxcontrib/programoutput/tests/{test_directive.py,test_command.py,test_cache.py}

%build
%py3_build
rm build/lib/sphinxcontrib/__init__.py

# workaround https://github.com/python/cpython/issues/94741
echo 'import importlib; importlib.invalidate_caches(); del importlib' > build/lib/sitecustomize.py
PYTHONPATH=build/lib sphinx-build -b html doc build/html
rm build/lib/sitecustomize.py build/lib/__pycache__/sitecustomize.*.pyc

rm -r build/html/.buildinfo build/html/.doctrees

# Seems not needed with python3.10+. Remove when older version don't need to be supported.
rm -rf build/lib/sphinxcontrib/__pycache__

%install
%py3_install
mkdir -p %{buildroot}%{_pkgdocdir}
cp -rv build/html %{buildroot}%{_pkgdocdir}/
ln -vsf %{_jsdir}/jquery/latest/jquery.min.js %{buildroot}%{_pkgdocdir}/html/_static/jquery.js

# remove .pth file which is useless under python3 and breaks namespace modules
rm %{buildroot}%{python3_sitelib}/sphinxcontrib_programoutput-*-nspkg.pth

%check
%pytest -v %{buildroot}%{python3_sitelib}/sphinxcontrib -k 'not test_standard_error_disabled'


%files -n python3-%{srcname}
%license LICENSE
%doc %{_pkgdocdir}
%{python3_sitelib}/sphinxcontrib/*
%{python3_sitelib}/sphinxcontrib_programoutput*info/

%changelog
%autochangelog
