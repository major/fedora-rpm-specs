Name:           python-autodocsumm
Version:        0.2.15
Release:        %autorelease
Summary:        Extended sphinx autodoc including automatic summaries

License:        Apache-2.0
URL:            https://github.com/Chilipp/autodocsumm
Source:         %{url}/archive/v%{version}/autodocsumm-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(pytest)
# Documentation
BuildRequires:  python3dist(installer)
BuildRequires:  python3dist(sphinx)
BuildRequires:  texinfo

%global _description %{expand:
Welcome! This Sphinx extension adds functionality to the Sphinx
autodoc extension:

- It creates a Table of Contents in the style of the autosummary extension with
  methods, classes, functions and attributes
- As you can include the __init__ method documentation for via the
  autoclass_content configuration value, we provide the autodata_content
  configuration value to include the documentation from the __call__ method
- You can exclude the string representation of specific objects. E.g. if you
  have a large dictionary using the not_document_data configuration value.}

%description %_description

%package -n     python3-autodocsumm
Summary:        %{summary}

%description -n python3-autodocsumm %_description


%prep
%autosetup -p1 -n autodocsumm-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
pushd docs
%python3 -m installer --destdir=tempinstall %{_pyproject_wheeldir}/*.whl
PYTHONPATH="tempinstall/usr/lib/python%{python3_version}/site-packages/:$PYTHONPATH" \
 sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook autodocsumm.texi
popd

%install
%pyproject_install
%pyproject_save_files -l autodocsumm
install -pDm0644 docs/texinfo/autodocsumm.xml \
  %{buildroot}%{_datadir}/help/en/autodocsumm/autodocsumm.xml

%check
%pyproject_check_import
%pytest

%files -n python3-autodocsumm -f %{pyproject_files}
%doc README.rst
%dir  %{_datadir}/help/en
%doc %lang(en) %{_datadir}/help/en/autodocsumm

%changelog
%autochangelog
