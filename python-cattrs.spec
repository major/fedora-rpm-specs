# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

# Currently, the version of python-cbor2 in Rawhide (and all Fedora releases)
# is too old; at least 5.4.6 is required.
%bcond_with cbor2

Name:           python-cattrs
Version:        23.1.2
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
# Unpinned; F37, F38, and F39 have 0.19
BuildRequires:  python3dist(immutables) >= 0.18
# msgpack = "^1.0.2"
BuildRequires:  (python3dist(msgpack) >= 1.0.2 with python3dist(msgpack) < 2~~)
# orjson = { version = "^3.5.2", markers = "implementation_name == 'cpython'" }
BuildRequires:  (python3dist(orjson) >= 3.5.2 with python3dist(orjson) < 4~~)
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

# https://github.com/python-attrs/cattrs/issues/369#issuecomment-1569445335
BuildRequires:  python3dist(typing-extensions)

# Documentation dependencies:
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
# Handled by an “extra”:
# cbor2 = "^5.4.5"
# Unpinned; F39 has 1.0.0
# myst-parser = "^0.18.1"
BuildRequires:  python3dist(myst-parser) >= 0.18.1
# pendulum = "^2.1.2"
BuildRequires:  (python3dist(pendulum) >= 2.1.2 with python3dist(pendulum) < 3~~)
# Sphinx = "^5.3.0"
# Unpinned; F39 has 6.x
BuildRequires:  python3dist(sphinx) >= 5.3
# sphinx-copybutton = "^0.5.0"
BuildRequires:  (python3dist(sphinx-copybutton) >= 0.5 with python3dist(sphinx-copybutton) < 0.6~~)
# We won’t build HTML documentation, so we don’t need the HTML theme.
# furo = "^2023.3.27"
# docs/conf.py imports from pkg_resources
# usage removed upstream in https://github.com/python-attrs/cattrs/commit/4bfc32c5e172
BuildRequires:  python3dist(setuptools)
%endif

# Unused test dependencies; we don’t run tests via tox, and we don’t want
# coverage or benchmarks. See also:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# black. = "^23.3.0"
# coverage. = "^6.2"
# flake8. = "^5.0.4"
# isort. = { version = "5.10.1", python = "<4" }
# pyperf = "^2.6.0"
# pytest-benchmark = "^3.2.3"
# tox = "^3.26.0"

# Unused Makefile help target dependency
# urllib3 = { version = "^1.26.12", python = "<4" }

%global _description %{expand:
cattrs is an open source Python library for structuring and
unstructuring data. cattrs works best with attrs classes and the usual
Python collections, but other kinds of classes are supported by
manually registering converters.}

%description %_description

%package -n python3-cattrs
Summary:        %{summary}

%description -n python3-cattrs %_description

%package        doc
Summary:        Documentation for python-cattrs

%description    doc %{_description}

%pyproject_extras_subpkg -n python3-cattrs ujson orjson msgpack pyyaml tomlkit %{?with_cbor2:cbor2} bson

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
%pyproject_buildrequires -x ujson,orjson,msgpack,pyyaml,tomlkit%{?with_cbor2:,cbor2},bson

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
%if %{without cbor2}
ignore="${ignore-} --ignore=tests/test_preconf.py"
%endif
%pytest --ignore-glob='bench/*' ${ignore-} -k "${k-}" -n auto

%files -n python3-cattrs -f %{pyproject_files}
%license LICENSE


%files doc
%license LICENSE
%doc HISTORY.md
%doc README.md
%if %{with doc_pdf}
%doc docs/_build/latex/cattrs.pdf
%endif

%changelog
%autochangelog
