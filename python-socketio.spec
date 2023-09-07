# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-socketio
Version:        5.9.0
Release:        %autorelease
Summary:        Socket.IO server

# SPDX
License:        MIT
URL:            https://github.com/miguelgrinberg/python-socketio
Source:         %{url}/archive/v%{version}/python-socketio-%{version}.tar.gz

# Downstream-only: patch out test coverage analysis
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-test-coverage-analysis.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Documentation
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

# Extra testing dependencies
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
Socket.IO is a transport protocol that enables real-time bidirectional
event-based communication between clients (typically, though not always, web
browsers) and a server. The official implementations of the client and server
components are written in JavaScript. This package provides Python
implementations of both, each with standard and asyncio variants.}

%description %{common_description}


%package -n     python3-socketio
Summary:        %{summary}

%description -n python3-socketio %{common_description}


%pyproject_extras_subpkg -n python3-socketio client asyncio_client


%package        doc
Summary:        Documentation for python-socketio

%description    doc %{common_description}


%prep
%autosetup -p1
# Fix “/usr/bin/env python” shebangs in the examples
%py3_shebang_fix examples
# Don’t ship package-lock.json files with the examples. Overzealous bug-filing
# scripts will file issues on this project for CVE’s in the recursive
# dependencies mentioned there even though they are not present in or used by
# this package at all.
find examples -type f -name package-lock.json -print -delete


%generate_buildrequires
%pyproject_buildrequires -x client,asyncio_client -t


%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files socketio


%check
%pytest


%files -n python3-socketio -f %{pyproject_files}


%files doc
%license LICENSE
%doc CHANGES.md
%doc README.md
%doc SECURITY.md
%if %{with doc_pdf}
%doc docs/_build/latex/python-socketio.pdf
%endif
%doc examples/


%changelog
%autochangelog
