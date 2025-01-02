Name:           python-socketio
Version:        5.12.1
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

# Dropped in F41; can be removed in F45.
Obsoletes:      python-socketio-doc < 5.11.2-4

%description -n python3-socketio %{common_description}


%pyproject_extras_subpkg -n python3-socketio client asyncio_client


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires -x client,asyncio_client -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l socketio


%check
%pytest


%files -n python3-socketio -f %{pyproject_files}
%doc CHANGES.md
%doc README.md
%doc SECURITY.md


%changelog
%autochangelog
