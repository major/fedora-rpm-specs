%global _description %{expand:
cattrs is an open source Python library for structuring and
unstructuring data. cattrs works best with attrs classes and the usual
Python collections, but other kinds of classes are supported by
manually registering converters.}

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-cattrs
Version:        22.2.0
Release:        %autorelease
Summary:        Python library for structuring and unstructuring data

License:        MIT
URL:            https://github.com/python-attrs/cattrs
BuildArch:      noarch
# The GitHub archive contains tests and docs, which the PyPI sdist lacks
Source0:        %{url}/archive/v%{version}/cattrs-%{version}.tar.gz


BuildRequires:  python3-devel

# [tool.poetry.dev-dependencies]
# We can’t easily generate the “dev” dependencies from Poetry, so we maintain
# them manually:

# Test dependencies:
# hypothesis = "^6.54.5"
BuildRequires:  (python3dist(hypothesis) >= 6.54.5 with python3dist(hypothesis) < 7~~)
# immutables = "^0.18"
# Unpinned; F37 and F38 have 0.19
BuildRequires:  (python3dist(immutables) >= 0.18)
# msgpack = "^1.0.2"
BuildRequires:  (python3dist(msgpack) >= 1.0.2 with python3dist(msgpack) < 2~~)
# orjson = { version = "^3.5.2", markers = "implementation_name == 'cpython'" }
# Not yet packaged: python-orjson
# BuildRequires:  (python3dist(orjson) >= 3.5.2 with python3dist(orjson) < 4~~)
# pymongo = "^4.2.0"
BuildRequires:  (python3dist(pymongo) >= 4.2 with python3dist(pymongo) < 5~~)
# pytest = "^7.1.3"
BuildRequires:  (python3dist(pytest) >= 7.1.3 with python3dist(pytest) < 8~~)
# PyYAML = "^6.0"
BuildRequires:  (python3dist(pyyaml) >= 6 with python3dist(pyyaml) < 7~~)
# tomlkit = { version = "^0.11.4", python = "<4" }
BuildRequires:  (python3dist(tomlkit) >= 0.11.4 with python3dist(tomlkit) < 0.12~~)
# ujson = "^5.4.0"
BuildRequires:  (python3dist(ujson) >= 5.4 with python3dist(ujson) < 6~~)

# Run tests in parallel:
BuildRequires:  python3dist(pytest-xdist)

# Documentation dependencies:
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
# Sphinx = "^4.3.2"
# Unpinned; F37 and F38 have 5.x
BuildRequires:  python3dist(sphinx) >= 4.3.2
# pendulum = "^2.1.2"
BuildRequires:  (python3dist(pendulum) >= 2.1.2 with python3dist(pendulum) < 3~~)
# We won’t build HTML documentation, so we don’t need the HTML theme.
# furo = "^2022.6.21"
# docs/conf.py imports from pkg_resources
# usage removed upstream in https://github.com/python-attrs/cattrs/commit/4bfc32c5e172
BuildRequires:  python3dist(setuptools)
%endif

# Unused test dependencies; we don’t run tests via tox, and we don’t want coverage or benchmarks. See also:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# black. = "^22.8.0"
# coverage. = "^6.2"
# flake8. = "^5.0.4"
# isort. = { version = "5.10.1", python = "<4" }
# pytest-benchmark = "^3.2.3"
# tox = "^3.26.0"

# Unused Makefile help target dependency
# urllib3 = { version = "^1.26.12", python = "<4" }

%description %_description

%package -n python3-cattrs
Summary:        %{summary}

%description -n python3-cattrs %_description

%package        doc
Summary:        Documentation for python-cattrs

%description    doc %{_description}

%prep
%autosetup -n cattrs-%{version}

# loosen requirement
sed -i 's/poetry-core.*"/poetry-core"/' pyproject.toml
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/coverage run.* -m/python3 -m/' tox.ini
# Don’t run benchmarks, either.
sed -r -i 's/ --benchmark[^[:blank:]"]*//g' pyproject.toml
# The version-finding code in docs/conf.py relies on a real installed
# “distribution” with metadata, which we don’t have at the time the
# documentation is built.
sed -r -i 's/^(version = ).*/\1 "%{version}"/' docs/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files cattrs cattr

%check
# No python-orjson package for now:
k="${k-}${k+ and }not test_orjson and not test_orjson_converter"
%pytest --ignore-glob='bench/*' -k "${k-}" -n auto

%files -n python3-cattrs -f %{pyproject_files}
%license LICENSE


%files doc
%license LICENSE
%doc HISTORY.rst
%doc README.rst
%if %{with doc_pdf}
%doc docs/_build/latex/cattrs.pdf
%endif

%changelog
%autochangelog
