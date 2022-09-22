# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-typeguard
Version:        2.13.3
Release:        %autorelease
Summary:        Run-time type checker for Python

# SPDX
License:        MIT
URL:            https://github.com/agronholm/typeguard
Source0:        %{pypi_source typeguard}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
This library provides run-time type checking for functions defined with PEP 484
argument (and return) type annotations.}

%description %{common_description}


%package -n python3-typeguard
Summary:        %{summary}

%description -n python3-typeguard %{common_description}


%package doc
Summary:        Documentation for typeguard

%description doc %{common_description}


%prep
%autosetup -n typeguard-%{version}

# Normally, we should skip linters and typecheckers
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters).
# In this case, it could make sense to allow the tests to depend on mypy for
# this package since it is itself a typechecker, and some tests seem to want to
# compare results against mypy. However, the tests are brittle in that they
# depend on the exact messages produced by a particular version of mypy, which
# makes them unsuitable for downstream testing.
sed -r -i '/\b(mypy)\b/d' setup.cfg
# In future versions, with project metadata migrated to pyproject.toml:
# sed -r -i 's/^([[:blank:]]*)(.(mypy))\b/\1# \2/' \
#     pyproject.toml

# Because we do not build Sphinx-generated HTML documentation, and conf.py does
# not import the HTML theme package, we do not need to require it at build
# time.
sed -r -i '/\b(sphinx_rtd_theme)\b/d' setup.cfg
# In future versions, with project metadata migrated to pyproject.toml:
# sed -r -i 's/^([[:blank:]]*)(.(sphinx_rtd_theme))\b/\1# \2/' \
#     pyproject.toml

# In docs/conf.py, pkg_resources is used to access the version from the
# typeguard package distribution. This works for upstream, but it doesn’t work
# when we haven’t installed the package with proper dist-info metadata yet.
sed -r -i \
    's/get_distribution\(.*\)\.parsed_version/parse_version\("%{version}"\)/' \
    docs/conf.py

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py


%generate_buildrequires
%pyproject_buildrequires -x test%{?with_doc_pdf:,doc}


%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files typeguard


%check
# The test_cached_module test fails to find a byte-compiled .pyc module where
# it is expecting it. Manually byte-compiling the tests (%%py_byte_compile
# %%{python3} tests) doesn’t help. This is almost certainly specific to the RPM
# build environment and not a real bug.
#
# See also:
#   2.13.3: pytest is failing in three units
#   https://github.com/agronholm/typeguard/issues/248
k="${k-}${k+ and }not test_cached_module"

# Tests comparing against mypy output are too brittle—tightly coupled to
# particular mypy versions—so we skip them downstream.
k="${k-}${k+ and }not test_positive"
k="${k-}${k+ and }not test_negative"

%pytest -k "${k-}"


%files -n python3-typeguard -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”


%files doc
%license LICENSE
%doc README.rst
%if %{with doc_pdf}
%doc docs/_build/latex/typeguard.pdf
%endif


%changelog
%autochangelog
