%bcond_without docs

# Created by pyp2rpm-3.3.5
%global pypi_name usort

%global common_description %{expand:
μsort is a safe, minimal import sorter. Its primary goal is to make no
"dangerous" changes to code, and to make no changes on code style. This is
achieved by detecting distinct "blocks" of imports that are the most likely to
be safely interchangeable, and only reordering imports within these blocks
without altering formatting. Code style is left as an exercise for linters and
formatters.}

Name:           python-%{pypi_name}
Version:        1.1.3
Release:        %autorelease
Summary:        A small, safe import sorter

License:        MIT
URL:            https://github.com/facebook/usort
Source:         %{pypi_source}

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(volatile)
%if %{with docs}
BuildRequires:  python3-docs
# upstream bundles this with unrelated dependencies in
# requirements-dev.txt; manually declare the docs deps
BuildRequires:  python3dist(sphinx) >= 5.3.0
BuildRequires:  python3dist(sphinx-mdinclude) >= 0.5.3
%endif

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}

%if %{with docs}
%package doc
Summary:        Documentation for %{name}
Requires:       python3-docs

%description doc
Documentation for %{name}.
%endif


%prep
%autosetup -n %{pypi_name}-%{version} -p1
sed -e 's/python/python3/g' -i Makefile
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%if %{with docs}
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -e 's|https://python-stdlib-list.readthedocs.io/en/latest|%{_docdir}/python-stdlib-list-doc/html|' \
    -i docs/conf.py
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import
%pytest -v usort/tests/__init__.py -k 'not test_format_permission_error'


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md
%{_bindir}/usort

%if %{with docs}
%files doc
%doc html
%license LICENSE
%endif


%changelog
%autochangelog
