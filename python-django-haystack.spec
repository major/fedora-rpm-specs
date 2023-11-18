# tests require running a solr server
%bcond_with tests

%global pypi_name django-haystack

Name:           python-%{pypi_name}
Version:        3.2.1
Release:        %autorelease
Summary:        Pluggable search for Django

License:        BSD-3-Clause
URL:            http://haystacksearch.org/
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Haystack provides modular search for Django. It features a unified, familiar
API that allows you to plug in different search backends (such as Solr,
Elasticsearch, Whoosh, Xapian, etc.) without having to modify your code.

Haystack is BSD licensed, plays nicely with third-party app without needing to
modify the source and supports advanced features like faceting, More Like This,
highlighting, spatial search and spelling suggestions.

You can find more information at http://haystacksearch.org/.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        Haystack provides modular search for Django - Python 3 version

BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %_description

This package provides Python 3 build of %{pypi_name}.


%package docs
Summary: Documentation for Django Haystack pluggable search
# Not requiring the main package, as users may wish to install
# the documentation separately.

BuildRequires:  make
BuildRequires:  python3dist(sphinx)
# Those two sphinxcontrib dependencies are pulled by default by upstream Sphinx,
# but in preparation for their separation, we explicitly list them to build
# htmlhelp, json and pickle docs.
# Upstream's tox.ini is not a good place for those, becasue it only builds html.
BuildRequires:  python3dist(sphinxcontrib-htmlhelp)
BuildRequires:  python3dist(sphinxcontrib-serializinghtml)

%description docs
Documentation for Django Haystack pluggable search

%_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}


%build
%pyproject_wheel

# Re-generate documentation
# Docs cannot be built in parallel
# We cannot build 'linkcheck' because it requires network access

pushd docs
make clean html htmlhelp latex json pickle changes
popd


%install
%pyproject_install
%pyproject_save_files haystack


%check
# currently does not work: can't find test_haystack
# export DJANGO_SETTINGS_MODULE=test_haystack.settings
# export PYTHONPATH="%{buildroot}%{python3_sitelib}:$PWD"
# pyproject_check_import
%if %{with tests}
%tox
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc PKG-INFO README.rst AUTHORS
%license LICENSE

%files docs
%doc docs/


%changelog
%autochangelog
