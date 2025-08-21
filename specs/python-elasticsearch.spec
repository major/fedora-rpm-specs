%global srcname elasticsearch
%global _desc %{expand: \
Low level client for Elasticsearch. It's goal is to provide common ground\
for all Elasticsearch-related code in Python. The client's features include:\
\
- Translating basic Python data types to and from json\
- Configurable automatic discovery of cluster nodes\
- Persistent connections\
- Load balancing (with pluggable selection strategy) across all available nodes\
- Failed connection penalization (time based - failed connections wont be\
  retried until a timeout is reached)\
- Thread safety\
- Pluggable architecture.}

Name:		python-elasticsearch
Version:	9.1.0
Release:	%autorelease
Summary:	Client for Elasticsearch

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		https://github.com/elasticsearch/elasticsearch-py
Source0:	%{url}/archive/v%{version}/%{srcname}-py-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-sphinx_rtd_theme

%description %{_desc}

%package -n python3-%{srcname}
Summary:	Python 3 Client for Elasticsearch

%description -n python3-%{srcname} %{_desc}

%package -n python-%{srcname}-doc
Summary:    Documentation for Python Elasticsearch

%description -n python-%{srcname}-doc
%{summary}

%prep
%autosetup -n %{srcname}-py-%{version}

# missing test dependencies
sed -i '/unasync/d' pyproject.toml
sed -i '/mapbox-vector-tile/d' pyproject.toml
sed -i '/simsimd/d' pyproject.toml
sed -i '/pyright/d' pyproject.toml
sed -i '/sentence_transformers/d' pyproject.toml
sed -i '/types-python-dateutil/d' pyproject.toml
sed -i '/types-tqdm/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -r -x dev

%build
%pyproject_wheel

# Generate the HTML documentation.
PYTHONPATH=${PWD} sphinx-build-3 docs/sphinx html
# Remove the sphinx-build leftovers.
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest -v -k 'not test_missing_required_field_raises_validation_exception and not test_boolean_doesnt_treat_false_as_empty and not test_accessing_known_fields_returns_empty_value' --ignore=test_elasticsearch/test_dsl/test_integration/test_examples/_async/test_vectors.py \
	--ignore=test_elasticsearch/test_dsl/test_integration/test_examples/_sync/test_vectors.py \
	--ignore=test_elasticsearch/test_dsl/_async/test_document.py \
	--ignore=test_elasticsearch/test_dsl/_sync/test_document.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md CONTRIBUTING.md README.md

%files -n python-%{srcname}-doc
%license LICENSE
%doc html examples 

%changelog
%autochangelog
