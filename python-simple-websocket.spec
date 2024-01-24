# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-simple-websocket
Version:        1.0.0
Release:        6%{?dist}
Summary:        Simple WebSocket server and client for Python

BuildArch:      noarch
License:        MIT
URL:            https://github.com/miguelgrinberg/simple-websocket
Source:         %{url}/archive/v%{version}/simple-websocket-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

# Documentation
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif


%description
Simple WebSocket server and client for Python


%package -n     python3-simple-websocket
Summary:        %{summary}

%description -n python3-simple-websocket
Simple WebSocket server and client for Python.


%package        doc
Summary:        Documentation for simple-websocket

%description    doc
Documentation for simple-websocket.


%prep
%autosetup -p1 -n simple-websocket-%{version}


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
%pyproject_save_files -l simple_websocket


%check
%pytest


%files -n python3-simple-websocket -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc CHANGES.md
%if %{with doc_pdf}
%doc docs/_build/latex/simple-websocket.pdf
%endif
%doc examples/


%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0.0-5
- Assert that the .dist-info directory contains a license file

* Fri Oct 27 2023 Sandro Mani <manisandro@gmail.com> - 1.0.0-4
- Add LICENSE to %%doc

* Wed Oct 18 2023 Sandro Mani <manisandro@gmail.com> - 1.0.0-3
- Simplify source URLs
- Add LICENSE to -doc
- BR pytest directly, drop coverage patch

* Tue Oct 17 2023 Sandro Mani <manisandro@gmail.com> - 1.0.0-2
- Use GitHub source
- Builds docs
- Ship examples as docs

* Tue Oct 17 2023 Sandro Mani <manisandro@gmail.com> - 1.0.0-1
- Initial package
