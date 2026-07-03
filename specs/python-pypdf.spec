%global srcname pypdf
%global forgeurl https://github.com/py-pdf/pypdf

Name:           python-%{srcname}
Version:        6.14.2
Release:        %autorelease
Summary:        Pure-Python PDF library

License:        BSD-3-Clause
URL:            https://pypdf.readthedocs.io
# PyPI tarball doesn't include tests
Source:         %{forgeurl}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  sed
# Test dependencies added manually since pyproject.toml doesn't specify them
# separately from dev dependencies.
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-socket)
BuildRequires:  python3dist(pytest-timeout)

%global _description %{expand:
pypdf is a free and open-source pure-python PDF library capable of splitting,
merging, cropping, and transforming the pages of PDF files. It can also add
custom data, viewing options, and passwords to PDF files. pypdf can retrieve
text and metadata from PDFs as well.}

%description %_description

%package -n     python3-pypdf
Summary:        %{summary}

%description -n python3-pypdf %_description

%pyproject_extras_subpkg -n python3-pypdf crypto,fonts,image,full

%package        doc
Summary:        Documentation for %{name}
Requires:       python3-docs

%description    doc
This package provides additional documentation for %{name}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/\{python_version\}|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py

%generate_buildrequires
%pyproject_buildrequires -x crypto,fonts,image,full,docs

%build
%pyproject_wheel

# Build docs
sphinx-build-3 docs html
rm -rf html/{.buildinfo,.doctrees}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# Deselect tests downloading files from external hosts and tests requiring
# sample files which are not included in the source tarball.
%pytest -m "not enable_socket and not samples"

%files -n python3-%{srcname} -f %{pyproject_files}
# https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/thread/4Y2VRLVAR3DJXBSFVDYJMU3G4ZNPGEU6/
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTORS.md

%files doc
%license LICENSE
%doc html

%changelog
%autochangelog

