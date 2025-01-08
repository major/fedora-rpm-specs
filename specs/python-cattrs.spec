# Currently, the version of python-pymongo in Rawhide is too old; at least
# 4.4.0 is required. See: https://bugzilla.redhat.com/show_bug.cgi?id=1823014
%bcond bson 0

# Not currently in EPEL10:
%bcond cbor2 %{expr:!0%{?el10}}

# Not currently in EPEL10:
%bcond msgpack %{expr:!0%{?el10}}

# Not currently in EPEL10:
%bcond msgspec %{expr:!0%{?el10}}

# Not currently in EPEL10:
%bcond orjson %{expr:!0%{?el10}}

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute. EPEL10 does not have the
# necessary dependencies, and this will probably remain true of EPELs.
%bcond doc_pdf %{expr:!0%{?rhel}}

%global commit ae806749f02502be1a8c073fd81050c04aa56c96
%global snapdate 20241004

Name:           python-cattrs
Version:        24.1.2%{?commit:^%{snapdate}git%{sub %{commit} 1 7}}
Release:        %autorelease
Summary:        Python library for structuring and unstructuring data

# SPDX
License:        MIT
URL:            https://github.com/python-attrs/cattrs
# The GitHub archive contains tests and docs, which the PyPI sdist lacks
%if %{undefined commit}
Source:         %{url}/archive/v%{version}/cattrs-%{version}.tar.gz
%global srcversion %{version}
%else
Source:         %{url}/archive/%{commit}/cattrs-%{commit}.tar.gz
%global srcversion %(echo %{version} | cut -d '^' -f 1)
%endif

# Because an extras metapackage is conditionalized on architecture, the base
# package cannot be noarch – but the rest of the binary packages *are* noarch,
# with no compiled code.
%global debug_package %{nil}

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
#    "coverage>=7.4.0",
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# BuildRequires:  %%{py3_dist coverage} >= 7.4.0
#    "pytest-xdist>=3.4.0",
BuildRequires:  %{py3_dist pytest-xdist} >= 3.4
#]

%if %{with doc_pdf}
# docs = [
#     "sphinx>=5.3.0",
BuildRequires:  %{py3_dist sphinx} >= 5.3
#     "furo>=2024.1.29",
# furo is useful to build HTML docs, but not needed to build the PDF
# BuildRequires:  %%{py3_dist furo} >= 2024.1.29
#     "sphinx-copybutton>=0.5.2",
# Loosened until https://bugzilla.redhat.com/show_bug.cgi?id=2186733 is fixed.
BuildRequires:  %{py3_dist sphinx-copybutton} >= 0.5.1
#     "myst-parser>=1.0.0",
BuildRequires:  %{py3_dist myst-parser} >= 1
#     "pendulum>=2.1.2",
BuildRequires:  %{py3_dist pendulum} >= 2.1.2
#     "sphinx-autobuild",
# sphinx-autobuild is useful for developers, but not needed to build the docs
# BuildRequires:  %%{py3_dist sphinx-autobuild}
#     "typing-extensions>=4.8.0",
BuildRequires:  %{py3_dist typing-extensions} >= 4.8
# ]

BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  /usr/bin/xindy
BuildRequires:  tex-xetex-bin
%endif

%global msgspec_enabled 0
%if %{with msgspec}
%ifnarch s390x %{ix86}
%global msgspec_enabled 1
%endif
%endif

%global _description %{expand:
cattrs is an open source Python library for structuring and
unstructuring data. cattrs works best with attrs classes and the usual
Python collections, but other kinds of classes are supported by
manually registering converters.}

%description %_description


%package -n python3-cattrs
Summary:        %{summary}

BuildArch:      noarch

Obsoletes:      python3-cattrs+bson < 23.2.3-1

%description -n python3-cattrs %_description


%package        doc
Summary:        Documentation for python-cattrs

# If the msgspec extra (which is unavailable on s390x and i686) is enabled,
# then the -doc subpackage becomes arch-dependent, because the presence of
# msgspec affects the contents of the documentation.
%if %{without msgspec}
BuildArch:      noarch
%endif

%description    doc %{_description}


# Most extras metapackages are noarch:
%pyproject_extras_subpkg -n python3-cattrs -a ujson pyyaml tomlkit
%if %{with bson}
%pyproject_extras_subpkg -n python3-cattrs -a bson
%endif
%if %{with cbor2}
%pyproject_extras_subpkg -n python3-cattrs -a cbor2
%endif
%if %{msgspec_enabled}
# python-msgspec is ExcludeArch: s390x i686; the extras metapackage is arched
# because it is not present on every architecture
%pyproject_extras_subpkg -n python3-cattrs msgspec
%endif
%if %{with msgpack}
%pyproject_extras_subpkg -n python3-cattrs -a msgpack
%endif
%if %{with orjson}
%pyproject_extras_subpkg -n python3-cattrs -a orjson
%endif


%prep
%autosetup -n cattrs-%{?!commit:%{version}}%{?commit:%{commit}}

# Don’t run benchmarks when testing (we don’t depend on pytest-benchmark)
sed -r -i 's/ --benchmark[^[:blank:]"]*//g' pyproject.toml

# The version-finding code in docs/conf.py relies on a real installed
# “distribution” with metadata, which we don’t have at the time the
# documentation is built.
sed -r -i 's/^(version = ).*/\1 "%{srcversion}"/' docs/conf.py

# Remove bundled fonts to show they are not packaged:
rm -rv docs/_static/fonts/

# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/conf.py


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{srcversion}'
%{pyproject_buildrequires \
    -x ujson \
%if %{with orjson}
    -x orjson \
%endif
%if %{with msgpack}
    -x msgpack \
%endif
    -x pyyaml \
    -x tomlkit \
%if %{with cbor2}
    -x cbor2 \
%endif
%if %{with bson}
    -x bson \
%endif
%if %{msgspec_enabled}
    -x msgspec \
%endif
    %{nil}}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{srcversion}'
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXBUILD=sphinx-build \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l cattrs cattr


%check
%if %{without bson}
# These unconditionally import bson, so they error during test collection
ignore="${ignore-} --ignore=tests/test_preconf.py"
ignore="${ignore-} --ignore=tests/preconf/test_pyyaml.py"
%endif

%if !%{msgspec_enabled}
# These unconditionally import msgspec, so they error during test collection
ignore="${ignore-} --ignore=tests/preconf/test_msgspec_cpython.py"
%endif

# https://github.com/python-attrs/cattrs/issues/547#issuecomment-2397173866
k="${k-}${k+ and }not test_simple_roundtrip_defaults"

%pytest --ignore-glob='bench/*' ${ignore-} -k "${k-}" -n auto


%files -n python3-cattrs -f %{pyproject_files}


%files doc
%license LICENSE
%doc HISTORY.md
%doc README.md
%if %{with doc_pdf}
%doc docs/_build/latex/cattrs.pdf
%endif


%changelog
%autochangelog
