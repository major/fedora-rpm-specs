# doc dependecies are not packaged
%bcond_with docs

Name:           python-jaraco-collections
Version:        5.2.1
Release:        %autorelease
Summary:        Collection objects similar to those in stdlib by jaraco

License:        MIT
URL:            https://github.com/jaraco/jaraco.collections
Source0:        %{pypi_source jaraco_collections}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{summary}

%package -n     python3-jaraco-collections
Summary:        %{summary}

%description -n python3-jaraco-collections
%{summary}

%package -n python-jaraco-collections-doc
Summary:        jaraco.collections documentation

%description -n python-jaraco-collections-doc
Documentation for jaraco.collections


%prep
%autosetup -n jaraco_collections-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test%{?with_docs:,doc}


%build
%pyproject_wheel
%if %{with docs}
# generate html docs
%{python3} -m sphinx docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install
%pyproject_save_files -l jaraco


%check
%pytest


%files -n python3-jaraco-collections -f %{pyproject_files}
%doc README.rst

%if %{with docs}
%files -n python-jaraco-collections-doc
%doc html
%license LICENSE
%endif


%changelog
%autochangelog
