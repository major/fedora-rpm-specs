Name:           python-aiomqtt
Version:        0.1.3
Release:        %autorelease
Summary:        An AsyncIO asynchronous wrapper around paho-mqtt

# Eclipse Distribution License 1.0 is BSD-3-Clause. Upstream states:
#
#   This project is dual licensed under the Eclipse Public License 1.0 and the
#   Eclipse Distribution License 1.0 as described in the epl-v10 and edl-v10
#   files.
#
# and https://www.eclipse.org/legal/eplfaq.php#DUALLIC clarifies:
#
#   For Eclipse projects which are dual-licensed, your file headers state that
#   the code is being made available under two licenses. For example: "This
#   program and the accompanying materials are made available under the terms
#   of the Eclipse Public License v1.0 and Eclipse Distribution License v. 1.0
#   which accompanies this distribution." What is meant by the use of the
#   conjunction "and"?
#
#   The code is being made available under both of the licenses. The consumer
#   of the code can select which license terms they wish to use, modify and/or
#   further distribute the code under.
#
# Therefore upstream’s “and” is our “or”.
License:        EPL-1.0 OR BSD-3-Clause
URL:            https://github.com/mossblaser/aiomqtt
Source0:        %{url}/archive/v%{version}/aiomqtt-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

# Additional requirements for tests
BuildRequires:  mosquitto

%global common_description %{expand:
This library implements a minimal Python 3 asyncio wrapper around the MQTT
client in paho-mqtt.}

%description %{common_description}


%package -n     python3-aiomqtt
Summary:        %{summary}

%description -n python3-aiomqtt %{common_description}


%prep
%autosetup -n aiomqtt-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/\b(flake8)\b/d' requirements-test.txt


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files aiomqtt


%check
%pytest


%files -n python3-aiomqtt -f %{pyproject_files}
%license LICENSE.txt edl-v10 epl-v10
%doc README.md


%changelog
%autochangelog
