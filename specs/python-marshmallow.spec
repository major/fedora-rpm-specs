%global __python %{__python3}
%global modname marshmallow
%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        3.25.0
Release:        %autorelease
Summary:        Python library for converting complex datatypes to and from primitive types
License:        MIT
URL:            http://marshmallow.readthedocs.org/
Source0:        https://github.com/marshmallow-code/marshmallow/archive/%{version}/%{modname}-%{version}.tar.gz
Patch0:         ordered_set.patch

BuildArch:      noarch

%global _description \
Marshmallow is a framework-agnostic library for converting complex datatypes,\
such as objects, to and from primitive Python datatypes.\
\
Marshmallow schemas can be used to:\
* Validate input data.\
* Deserialize input data to app-level objects.\
* Serialize app-level objects to primitive Python types. The serialized objects\
  can then be rendered to standard formats such as JSON for use in an HTTP API.

%description %{_description}

%package doc
Summary:        Documentation for %{name}
Provides:       python3-%{modname}-doc = %{version}
Obsoletes:      python3-%{modname}-doc < 2.8.0-1

%description doc
Documentation for %{name}.

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytz
BuildRequires:  python3-ordered-set
BuildRequires:  python3-dateutil
BuildRequires:  python3-simplejson
BuildRequires:  python3-sphinx-issues
Requires:       python3-ordered-set
Recommends:     python3-dateutil
Recommends:     python3-simplejson

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1

# remove bundled library
# instead of orderedsett we patch code to usu python-ordered-set
rm -f ./marshmallow/orderedset.py

# unsupported theme option 'donate_url' given
sed -i -e "/donate_url/d" docs/conf.py
# python3-autodocsumm is not in Fedora
# This is needed only for doc subpackage.
# this used to be patch, but this change every release
# and I am sick of change it every time
sed -i '/"autodocsumm",/d' docs/conf.py
sed -i '/"autodocsumm==/d' pyproject.toml
sed -i '/"versionwarning.extension",/d' docs/conf.py
sed -i '/"sphinx-version-warning==/d' pyproject.toml
sed -i '/"sphinx_issues",/d' docs/conf.py
sed -i '/"sphinx-issues==/d' pyproject.toml
sed -i '/version = release = importlib.metadata.version/d' docs/conf.py
# Drop the sphinx version constraint
sed -i 's/"sphinx==[^ ]*"/"sphinx"/' pyproject.toml
# the newer version is not yet in Fedora and is required just because CVEs, old version has all required functionality
sed -i '/"alabaster==/c\\"alabaster==0.7.16"' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x docs,tests

%build
%pyproject_wheel
sphinx-build -b html docs html

%install
%pyproject_install
%pyproject_save_files %{modname}
rm -rf html/{.buildinfo,.doctrees}


%check
%pyproject_check_import
%{py_test_envvars} py.test-%{python3_version} -v


%files doc
%license LICENSE
%doc html examples


%files -n python3-%{modname}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}.dist-info/


%changelog
%autochangelog
