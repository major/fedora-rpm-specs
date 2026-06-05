Name:               python-websocket-client
Version:            1.9.0
Release:            %autorelease
BuildArch:          noarch
Summary:            WebSocket client for python
License:            Apache-2.0
URL:                https://github.com/websocket-client/websocket-client
Source:             %{pypi_source websocket_client}

%global common_description %{expand:
websocket-client is a WebSocket client for Python.  It provides access to low
level APIs for WebSockets.  websocket-client implements version hybi-13 of the
WebSocket protocol.  This client does not currently support the
permessage-deflate extension from RFC 7692.}


%description %{common_description}


%package -n python3-websocket-client
Summary:            %{summary}
BuildRequires:      python3-devel


%description -n python3-websocket-client %{common_description}


%prep
%autosetup -p 1 -n websocket_client-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l websocket


%check
%pytest -v websocket/tests


%files -n python3-websocket-client -f %{pyproject_files}
%doc README.md ChangeLog
%{_bindir}/wsdump


%changelog
%autochangelog
