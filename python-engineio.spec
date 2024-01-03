# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-engineio
Version:        4.8.1
Release:        %autorelease
Summary:        Python Engine.IO server and client

# SPDX
License:        MIT
URL:            https://github.com/miguelgrinberg/python-engineio/
# The PyPY sdist now contains documentation and tests, but it still lacks
# examples and the CHANGES.md file, so we continue to use a GitHub archive.
Source:         %{url}/archive/v%{version}/python-engineio-%{version}.tar.gz

# Downstream-only: patch out test coverage analysis
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-test-coverage-analysis.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel

# Documentation
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
Engine.IO is a lightweight transport protocol that enables real-time
bidirectional event-based communication between clients (typically, though not
always, web browsers) and a server. The official implementations of the client
and server components are written in JavaScript. This package provides Python
implementations of both, each with standard and asyncio variants.}

%description %{common_description}


%package -n     python3-engineio
Summary:        %{summary}

%description -n python3-engineio %{common_description}


%pyproject_extras_subpkg -n python3-engineio client asyncio_client


%package        doc
Summary:        Documentation for python-engineio

%description    doc %{common_description}


%prep
%autosetup -p1

# Remove pre-compiled/pre-minified browser build of
# https://github.com/socketio/engine.io from the examples. This makes them less
# useful, but satisfies
# https://docs.fedoraproject.org/en-US/packaging-guidelines/JavaScript/ and
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#bundling. It
# doesn’t seem worth it to package the JavaScript implementation of Engine.IO
# just for the sake of these examples.
#
# Don’t ship package-lock.json files with the examples, to keep from having
# automated bugs filed for irrelevant CVE’s in NPM packages that are mentioned
# there. See RHBZ#2127005.
find examples -type f \( -name 'engine.io.js' -o -name 'package-lock.json' \) \
    -print -delete


%generate_buildrequires
%pyproject_buildrequires -x client,asyncio_client%{?doc_pdf:,docs} -t


%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l engineio


%check
%pytest


%files -n python3-engineio -f %{pyproject_files}


%files doc
%license LICENSE
%doc CHANGES.md
%doc README.md
%doc SECURITY.md
%if %{with doc_pdf}
%doc docs/_build/latex/python-engineio.pdf
%endif
# Bundled pre-compiled engine.io.js has been removed:
%doc examples/


%changelog
%autochangelog
