%global prj_name geopmdpy
%global desc %{expand: \
The Global Extensible Open Power Manager (GEOPM) provides a framework to
explore power and energy optimizations on platforms with heterogeneous mixes
of computing hardware.

Users can monitor their system's energy and power consumption, and safely
optimize system hardware settings to achieve energy efficiency and/or
performance objectives.}

Name:		geopmd
Version:	3.2.1
Release:	%autorelease
Summary:	GEOPM daemon

License:	BSD-3-Clause
URL:		https://geopm.github.io
Source0:	https://github.com/geopm/geopm/archive/v%{version}/geopm-%{version}.tar.gz

ExclusiveArch:	x86_64

BuildRequires:	gcc
BuildRequires:	grpc-plugins
BuildRequires:	libgeopmd-devel >= 3.2.1
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	python3-cffi
BuildRequires:	python3-dasbus
BuildRequires:	python3-docstring-parser
BuildRequires:	python3-defusedxml
BuildRequires:	python3-jsonschema
BuildRequires:	python3-prometheus_client
BuildRequires:	python3-psutil
BuildRequires:	python3-pyyaml
BuildRequires:	systemd-units
Requires:	python3-cffi
Requires:	python3-dasbus
Requires:	python3-docstring-parser
Requires:	python3-grpcio
Requires:	python3-jsonschema
Requires:	python3-prometheus_client
Requires:	python3-protobuf
Requires:	python3-psutil
Requires:	python3-pyyaml
Requires:	python3-%{prj_name} = %{version}-%{release}
Requires:	geopmd-cli
Requires:	geopm-cli

%description
%{desc}

%package -n python3-%{prj_name}
Summary:        Python bindings for libgeopmd

%description -n python3-%{prj_name}
%{desc}

%prep
%autosetup -p1 -n geopm-%{version}

pushd %{prj_name}
echo %{version} > %{prj_name}/VERSION
popd

%build
pushd %{prj_name}
%py3_build
popd

%install
pushd %{prj_name}
%py3_install
mkdir -p %{buildroot}%{_sysconfdir}/geopm
chmod 0700 %{buildroot}%{_sysconfdir}/geopm
install -D -p -m 644 io.github.geopm.xml %{buildroot}%{_datadir}/dbus-1/interfaces/io.github.geopm.xml
install -D -p -m 644 io.github.geopm.conf %{buildroot}%{_datadir}/dbus-1/system.d/io.github.geopm.conf
install -D -p -m 644 geopm.service %{buildroot}%{_unitdir}/geopm.service

protoc \
	--python_out=geopmdpy \
	--grpc_out geopmdpy \
	--plugin=protoc-gen-grpc=/usr/bin/grpc_python_plugin \
	geopm_service.proto
cp geopm_service.proto %{buildroot}%{python3_sitearch}/%{prj_name}
popd

%check
pushd %{prj_name}
PYTHONPATH=%{buildroot}%{python3_sitearch} %{python3} -m unittest discover -p 'Test*.py' -v
popd

%files
%license LICENSE-BSD-3-Clause
%doc README.md
%{_bindir}/geopmd
%dir %{_sysconfdir}/geopm
%{_datadir}/dbus-1/interfaces/io.github.geopm.xml
%{_datadir}/dbus-1/system.d/io.github.geopm.conf
%{_unitdir}/geopm.service

%files -n python3-%{prj_name}
%{_bindir}/geopmaccess
%{_bindir}/geopmexporter
%{_bindir}/geopmread
%{_bindir}/geopmwrite
%{_bindir}/geopmsession
%{python3_sitearch}/_libgeopmd_py_cffi.abi3.so
%{python3_sitearch}/%{prj_name}
%{python3_sitearch}/%{prj_name}-*.egg-info

%changelog
%autochangelog
