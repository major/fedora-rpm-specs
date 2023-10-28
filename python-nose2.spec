# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc 1

Name:           python-nose2
Version:        0.14.0
Release:        %autorelease
Summary:        The successor to nose, based on unittest2

# The entire source is BSD-2-Clause, except that unspecified portions are
# derived from unittest2 under a BSD-3-Clause. See LICENSE.
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://nose2.io/
%global forgeurl https://github.com/nose-devs/nose2
Source0:        %{forgeurl}/archive/%{version}/nose2-%{version}.tar.gz
# Man page written for Fedora in groff_man(7) format based on --help output
Source1:        nose2.1

# Keep the tox config from pulling in the dev extra. This makes sense upstream
# (so the patch is not offered there), but for us it brings in unwanted
# dependencies like coverage and linter tools, the Sphinx HTML theme and the
# sphinx-issues package used for upstream changelog management, and the
# deprecated PyPI “mock” package (which is not actually needed for the tests on
# modern Python versions).
Patch:          nose2-0.11.0-tox-no-dev-extra.patch
# Downstream-only: skip test_skip_reason_in_message on Python 3.13+
# This is a workaround while we wait for an upstream fix.
#
# Python 3.13: test_skip_reason_in_message fails
# https://github.com/nose-devs/nose2/issues/588
#
# https://bugzilla.redhat.com/show_bug.cgi?id=2246281
Patch:          0001-Downstream-only-skip-test_skip_reason_in_message-on-.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  hardlink

%if %{with doc}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
# This is in the “dev” extra as defined in setup.py, but we do not use it to
# generate BuildRequires because we would have to patch out unwanted
# dependencies like mock, coverage, and the HTML theme.
BuildRequires:  python3dist(sphinx)
# Note that sphinx-issues is used upstream for changelog management but is not
# required at build time.
%endif

%global common_description %{expand:
nose2 is the successor to nose.

It’s unittest with plugins.

nose2’s purpose is to extend unittest to make testing nicer and easier to
understand.}

%description %{common_description}


%package -n python3-nose2
Summary:        Next generation of nicer testing for Python

%description -n python3-nose2 %{common_description}


%if %{with doc}
%package        doc
Summary:        Documentation for %{name}

%description    doc %{common_description}
%endif


%pyproject_extras_subpkg -n python3-nose2 coverage_plugin


%prep
%autosetup -n nose2-%{version} -p1

# Patch out unnecessary documentation dependency on sphinx-issues, used
# upstream for changelog generation.
sed -r -i '/"sphinx_issues",/d' docs/conf.py

# Workaround for https://github.com/rpm-software-management/rpm/issues/2532:
rm -rf SPECPARTS

# Remove shebangs from non-script sources. The find-then-modify pattern
# preserves mtimes on sources that did not need to be modified.
find nose2/ -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel
%if %{with doc}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files nose2
hardlink -v '%{buildroot}%{_bindir}'
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check
%tox -e %{toxenv}-nocov


%files -n python3-nose2 -f %{pyproject_files}
%doc AUTHORS
%if %{without doc}
%doc README.rst docs/changelog.rst
%endif

%{_bindir}/nose2
%{_mandir}/man1/nose2.1*


%if %{with doc}
%files doc
%license LICENSE
%doc AUTHORS README.rst docs/changelog.rst

%doc docs/_build/latex/nose2.pdf
%endif


%changelog
%autochangelog
