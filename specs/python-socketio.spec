# If necessary, we can disable tests that require uvicorn.
%bcond uvicorn 1

Name:           python-socketio
Version:        5.14.0
Release:        %autorelease
Summary:        Socket.IO server

# SPDX
License:        MIT
URL:            https://github.com/miguelgrinberg/python-socketio
Source:         %{url}/archive/v%{version}/python-socketio-%{version}.tar.gz

# Downstream-only: patch out test coverage analysis
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-test-coverage-analysis.patch

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x client,asyncio_client -t
BuildOption(install):   -l socketio

BuildArch:      noarch

# Extra testing dependencies
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
Socket.IO is a transport protocol that enables real-time bidirectional
event-based communication between clients (typically, though not always, web
browsers) and a server. The official implementations of the client and server
components are written in JavaScript. This package provides Python
implementations of both, each with standard and asyncio variants.}

%description %{common_description}


%package -n     python3-socketio
Summary:        %{summary}

# Dropped in F41; can be removed in F45.
Obsoletes:      python-socketio-doc < 5.11.2-4

%description -n python3-socketio %{common_description}


%pyproject_extras_subpkg -n python3-socketio client asyncio_client


%prep -a
%if %{without uvicorn}
sed -r -i 's/^([[:blank:]]*)(uvicorn)\b/\1# \2/' tox.ini
%endif


%check -a
%if %{without uvicorn}
ignore="${ignore-} --ignore=tests/async/test_admin.py"
%endif

%pytest ${ignore-}


%files -n python3-socketio -f %{pyproject_files}
%doc CHANGES.md
%doc README.md
%doc SECURITY.md


%changelog
%autochangelog
