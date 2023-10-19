# We shouldn’t *add* ExcludeArch in a stable release, so we must skip the tests
# instead. We can remove this after F39 goes end-of-life, or when the spec
# files for older branches diverge from those in F40+.
%ifarch s390x
%if 0%{?fc38} || 0%{?fc39}
%global tests_default_off 1
%endif
%endif

%bcond tests 0%{?!tests_default_off:1}
# Run examples as additional tests?
%bcond test_examples 1

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

%global _description %{expand:
The new python parameter exploration toolkit: pypet manages exploration of the
parameter space of any numerical simulation in python, thereby storing your
data into HDF5 files for you. Moreover, pypet offers a new data container which
lets you access all your parameters and results from a single source. Data I/O
of your simulations and analyses becomes a piece of cake!}

Name:           python-pypet
Version:        0.6.1
Release:        %autorelease
Summary:        Parameter exploration toolbox

License:        BSD-3-Clause
URL:            https://github.com/SmokinCaterpillar/pypet
Source:         %{url}/archive/%{version}/pypet-%{version}.tar.gz

# Replace ConfigParser.readfp() with ConfigParser.read_file()
# https://github.com/SmokinCaterpillar/pypet/pull/69
Patch:          %{url}/pull/69.patch

# Replace deprecated/removed unittest.TestCase method aliases
# https://github.com/SmokinCaterpillar/pypet/pull/70
Patch:          %{url}/pull/70.patch

# In examples, don’t pass keywords to Figure.gca()
# https://github.com/SmokinCaterpillar/pypet/pull/71
Patch:          %{url}/pull/71.patch

# We have an arched base package and noarch binary RPMs to ensure that the
# tests always run on all architectures, since this package has a history of
# architecture-dependent failures. However, there is no compiled code in the
# package.
%global debug_package %{nil}
# ==== Exclude i686 ====
#
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
#
# Also, mandatory dependency python-tables dropped i686 support in F39 because
# python-blosc2 does not support it:
# https://src.fedoraproject.org/rpms/python-tables/c/ee27ac0dd4352ee415ad5089aee76c50f4bd2028
#
# ==== Exclude s390x ====
#
# Many python-pypet tests fail on s390x due to apparent endian issues in
# pandas.HDFStore
# https://bugzilla.redhat.com/show_bug.cgi?id=2244500
ExcludeArch:    %{ix86}
# We shouldn’t *add* ExcludeArch in a stable release. We can remove the
# conditional after F39 goes end-of-life, or when the spec files for older
# branches diverge from those in F40+.
%if !0%{?fc38} && !0%{?fc39}
ExcludeArch:    s390x
%endif

%description %_description

%package -n python3-pypet
Summary:        %{summary}

BuildArch:      noarch

BuildRequires:  python3-devel

# The setup.py file has an optional dependency on m2r; if present, the long
# description is loaded from README.md. Since this isn’t the case for the
# actual wheel on PyPI, we omit the m2r dependency for consistency.

# Needed to “smoke test” importing pypet.brian2 and for many tests and
# examples. Not a hard runtime dependency.
BuildRequires:  %{py3_dist brian2}

%if %{with tests}
BuildRequires:  hdf5
# Needed in several examples.
BuildRequires:  %{py3_dist deap}
# Needed in several tests and examples
BuildRequires:  %{py3_dist matplotlib}
%endif

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description -n python3-pypet %_description

%package doc
Summary:        %{summary}

BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n pypet-%{version} -p1
rm -rf pypet.egg-info
find . -type f -name .gitignore -print -delete
# If we run the examples as tests, it will spew output into the examples/ tree.
# Not only do we not want to package that output, but it is non-reproducible,
# which causes build failures when the noarch -doc subpackage has different
# contents on different architectures. To work around that, we have two
# options: manually install all documentation in %%build and list it with
# absolute paths in the appropriate %%files section, or install the examples
# via a relative path referencing a clean copy. That’s the simpler options, so
# here’s the clean copy:
mkdir -p _clean
cp -rp examples _clean/examples

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C doc latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C doc/build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files pypet

%check
%pyproject_check_import -e '*tests*'
# https://github.com/SmokinCaterpillar/pypet/blob/develop/ciscripts/travis/runtests.sh
# Scoop is unmaintained. I've asked upstream to drop support for it:
# https://github.com/SmokinCaterpillar/pypet/issues/56
%if %{with tests}
%{py3_test_envvars} %{python3} pypet/tests/all_tests.py
%if %{with test_examples}
pushd pypet/tests
%{py3_test_envvars} %{python3} all_examples.py
popd
%endif
%endif

%files -n python3-pypet -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc CHANGES.txt
%doc _clean/examples/
%if %{with doc_pdf}
%doc doc/build/latex/pypet.pdf
%endif

%changelog
%autochangelog
