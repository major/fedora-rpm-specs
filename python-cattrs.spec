# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

# Currently, the version of python-cbor2 in Rawhide is too old; at least 5.4.6
# is required. See: https://bugzilla.redhat.com/show_bug.cgi?id=2245361
%bcond cbor2 0

# Currently, the version of python-pymongo in Rawhide is too old; at least
# 4.4.0 is required. See: https://bugzilla.redhat.com/show_bug.cgi?id=1823014
%bcond bson 0

Name:           python-cattrs
Version:        23.2.3
Release:        %autorelease
Summary:        Python library for structuring and unstructuring data

# SPDX
License:        MIT
URL:            https://github.com/python-attrs/cattrs
BuildArch:      noarch
# The GitHub archive contains tests and docs, which the PyPI sdist lacks
Source:         %{url}/archive/v%{version}/cattrs-%{version}.tar.gz

BuildRequires:  python3-devel

# There is no obvious, straightforward way to generate dependencies from
# [tool.pdm.dev-dependencies] in pyproject.toml, so we maintain them here
# manually.

# test = [
#    "hypothesis>=6.79.4",
BuildRequires:  %{py3_dist hypothesis} >= 6.79.4
#    "pytest>=7.4.0",
BuildRequires:  %{py3_dist pytest} >= 7.4
#    "pytest-benchmark>=4.0.0",
# We choose not to run benchmarks with the tests.
# BuildRequires:  %%{py3_dist pytest-benchmark} >= 4.0.0
#    "immutables>=0.20",
BuildRequires:  %{py3_dist immutables} >= 0.20
#    "typing-extensions>=4.7.1",
BuildRequires:  %{py3_dist typing-extensions} >= 4.7.1
#    "coverage>=7.2.7",
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# BuildRequires:  %%{py3_dist coverage} >= 7.2.7
#]

# Added to the test dev-dependencies upstream after the packaged release, but
# still useful to run the tests in parallel
#    "pytest-xdist>=3.4.0",
BuildRequires:  %{py3_dist pytest-xdist} >= 3.4

%if %{with doc_pdf}
# docs = [
#     "sphinx>=5.3.0",
BuildRequires:  %{py3_dist sphinx} >= 5.3
#     "furo>=2023.3.27",
BuildRequires:  %{py3_dist furo} >= 2023.3.27
#     "sphinx-copybutton>=0.5.2",
# Loosened until https://bugzilla.redhat.com/show_bug.cgi?id=2186733 is fixed.
BuildRequires:  %{py3_dist sphinx-copybutton} >= 0.5.1
#     "myst-parser>=1.0.0",
BuildRequires:  %{py3_dist myst-parser} >= 1
#     "pendulum>=2.1.2",
BuildRequires:  %{py3_dist pendulum} >= 2.1.2
#     "sphinx-autobuild",
BuildRequires:  %{py3_dist sphinx-autobuild}
#     "typing-extensions>=4.8.0",
BuildRequires:  %{py3_dist typing-extensions} >= 4.8
# ]

BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global _description %{expand:
cattrs is an open source Python library for structuring and
unstructuring data. cattrs works best with attrs classes and the usual
Python collections, but other kinds of classes are supported by
manually registering converters.}

%description %_description

%package -n python3-cattrs
Summary:        %{summary}

Obsoletes:      python3-cattrs+bson < 23.2.3-1

%description -n python3-cattrs %_description

%package        doc
Summary:        Documentation for python-cattrs

%description    doc %{_description}

%pyproject_extras_subpkg -n python3-cattrs ujson orjson msgpack pyyaml tomlkit %{?with_cbor2:cbor2} %{?with_bson:bson}

%prep
%autosetup -n cattrs-%{version}
sed -r -i 's/"(coverage)\b/# &/' pyproject.toml
# Don’t run benchmarks when testing, either
sed -r -i 's/"(pytest-benchmark)\b/# &/' pyproject.toml
sed -r -i 's/ --benchmark[^[:blank:]"]*//g' pyproject.toml
# The version-finding code in docs/conf.py relies on a real installed
# “distribution” with metadata, which we don’t have at the time the
# documentation is built.
sed -r -i 's/^(version = ).*/\1 "%{version}"/' docs/conf.py

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -x ujson,orjson,msgpack,pyyaml,tomlkit%{?with_cbor2:,cbor2}%{?with_bson:,bson}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXBUILD=sphinx-build \
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
