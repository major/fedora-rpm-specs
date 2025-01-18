# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-flask-socketio
Version:        5.5.1
Release:        %autorelease
Summary:        Socket.IO integration for Flask applications

# SPDX
License:        MIT
URL:            https://github.com/miguelgrinberg/Flask-SocketIO/
Source:         %{url}/archive/v%{version}/Flask-SocketIO-%{version}.tar.gz

BuildArch:      noarch
 
BuildRequires:  python3-devel

# Documentation
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
Flask-SocketIO gives Flask applications access to low latency bi-directional
communications between the clients and the server. The client-side application
can use any of the SocketIO official clients libraries in Javascript, C++, Java
and Swift, or any compatible client to establish a permanent connection to the
server.}

%description %{common_description}


%package -n     python3-flask-socketio
Summary:        %{summary}

%description -n python3-flask-socketio %{common_description}


%package        doc
Summary:        Documentation for %{name}

%description    doc %{common_description}


%prep
%autosetup -n Flask-SocketIO-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i \
    -e 's/--cov[^[:blank:]]*//g' \
    -e '/^[[:blank:]]*(pytest-cov)[[:blank:]]*$/d' \
    tox.ini


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l flask_socketio


%check
# Because of its name, flask_socketio.test_client is mistaken for a test; then,
# pytest fails because of an import path mismatch, since that module is
# available both here in the build directory and in the buildroot. Simply
# ignoring it in test collection is perfectly correct and solves the problem.
%pytest --ignore-glob='*/test_client.py'


%files -n python3-flask-socketio -f %{pyproject_files}


%files doc
%license LICENSE
%doc CHANGES.md
%doc README.md
%doc SECURITY.md
%if %{with doc_pdf}
%doc docs/_build/latex/flask-socketio.pdf
%endif
%doc example/


%changelog
%autochangelog
