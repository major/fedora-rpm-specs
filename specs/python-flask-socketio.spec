Name:           python-flask-socketio
Version:        5.6.1
Release:        %autorelease
Summary:        Socket.IO integration for Flask applications

# SPDX
License:        MIT
URL:            https://github.com/miguelgrinberg/Flask-SocketIO/
Source:         %{url}/archive/v%{version}/Flask-SocketIO-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -t
BuildOption(install):   -l flask_socketio

BuildArch:      noarch

%global common_description %{expand:
Flask-SocketIO gives Flask applications access to low latency bi-directional
communications between the clients and the server. The client-side application
can use any of the SocketIO official clients libraries in Javascript, C++, Java
and Swift, or any compatible client to establish a permanent connection to the
server.}

%description %{common_description}


%package -n     python3-flask-socketio
Summary:        %{summary}

# PDF documentation build and -doc subpackage dropped in Fedora 44; we can
# remove this after Fedora 46 reaches end-of-life.
Obsoletes:      python-flask-socketio-doc < 5.6.0-2

%description -n python3-flask-socketio %{common_description}


%prep -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i \
    -e 's/--cov[^[:blank:]]*//g' \
    -e '/^[[:blank:]]*(pytest-cov)[[:blank:]]*$/d' \
    tox.ini


%check -a
# Because of its name, flask_socketio.test_client is mistaken for a test; then,
# pytest fails because of an import path mismatch, since that module is
# available both here in the build directory and in the buildroot. Simply
# ignoring it in test collection is perfectly correct and solves the problem.
%pytest --ignore-glob='*/test_client.py'


%files -n python3-flask-socketio -f %{pyproject_files}
%doc CHANGES.md
%doc README.md
%doc example/


%changelog
%autochangelog
