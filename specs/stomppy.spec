Name:           stomppy
Version:        9.0.0
Release:        %autorelease
Summary:        Python stomp client for messaging

License:        Apache-2.0
URL:            https://github.com/jasonrbriggs/stomp.py
Source0:        %{pypi_source stomp_py}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
stomp.py is a Python client library for accessing messaging servers 
(such as ActiveMQ or JBoss Messaging) using the STOMP protocol. It can also
be run as a standalone, command-line client for testing.}


%description %_description


%package -n python3-stomppy
Summary:        Python stomp client for messaging for python3


%description -n python3-stomppy %_description


%prep
%autosetup -n stomp_py-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l stomp


%check
# Upsteream tests require a running activemq, rabbitmq, ....
%pyproject_check_import


%files -n python3-stomppy -f %{pyproject_files}
%{_bindir}/stomp
%doc README.rst


%changelog
%autochangelog
