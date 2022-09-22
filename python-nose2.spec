# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

# Upstream has vendored six in 33f5dd4f4ddc6d1f1b138c5358b4f4ed6eab125c; see:
#   https://github.com/nose-devs/nose2/commit/33f5dd4f4ddc6d1f1b138c5358b4f4ed6eab125c
# We have de-vendored six downstream.
%bcond_with vendored_six

Name:           python-nose2
Version:        0.12.0
Release:        %autorelease
Summary:        The successor to nose, based on unittest2

License:        BSD
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
# Minor fixes regarding __version__ move
#
# Docs in conf.py and the CI build used `_version.py`, and just need
# minor updates.
#
# https://github.com/nose-devs/nose2/commit/fc3d69290462930bc0fa81cb69bc4c6e15f8ae66
Patch:          %{forgeurl}/commit/fc3d69290462930bc0fa81cb69bc4c6e15f8ae66.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  hardlink

%if %{without vendored_six}
BuildRequires:  python3dist(six)
%endif

%if %{with doc_pdf}
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

%if %{without vendored_six}
# We have de-vendored six downstream.
Requires:       python3dist(six)
%else
Provides:       bundled(python3dist(six)) = 1.16
%endif

%description -n python3-nose2 %{common_description}


%package        doc
Summary:        Documentation for %{name}

%description    doc %{common_description}


%pyproject_extras_subpkg -n python3-nose2 coverage_plugin


%prep
%autosetup -n nose2-%{version} -p1

# Patch out unnecessary documentation dependency on sphinx-issues, used
# upstream for changelog generation.
sed -r -i '/"sphinx_issues",/d' docs/conf.py

%if %{without vendored_six}
cat > nose2/_vendor/six.py <<'EOF'
# This vendored copy of https://pypi.org/project/six/ has been replaced with a
# trivial wrapper around the system copy.
from six import *
EOF
%endif


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
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
%license license.txt
%doc AUTHORS
%doc README.rst

%{_bindir}/nose2
%{_mandir}/man1/nose2.1*


%files doc
%license license.txt
%doc AUTHORS
%doc README.rst
%doc docs/changelog.rst
%doc contributing.rst

%if %{with doc_pdf}
%doc docs/_build/latex/nose2.pdf
%endif


%changelog
%autochangelog
