%global prj_name geopmpy
%global desc %{expand: \
The Global Extensible Open Power Manager (GEOPM) provides a framework to
explore power and energy optimizations on platforms with heterogeneous mixes
of computing hardware.

Users can monitor their system's energy and power consumption, and safely
optimize system hardware settings to achieve energy efficiency and/or
performance objectives.}

Name:		python-%{prj_name}
Version:	3.2.2
Release:	%autorelease
Summary:	Python bindings for libgeopm

License:	BSD-3-Clause
URL:		https://geopm.github.io
Source0:	https://github.com/geopm/geopm/archive/v%{version}/geopm-%{version}.tar.gz

# Update usage of DataFrame.to_hdf
# https://github.com/geopm/geopm/commit/5396e439e2cc40d95a20bd829134096c12fc2286
Patch0:		5396e439e2cc40d95a20bd829134096c12fc2286.patch

ExclusiveArch:	x86_64

BuildRequires:	gcc
BuildRequires:	python3-devel
BuildRequires:	libgeopm-devel >= 3.2.2
BuildRequires:	libgeopmd-devel >= 3.2.2
Requires:	geopmd

%description
%{desc}

%package -n python3-%{prj_name}
Summary:        %{summary}

%description -n python3-%{prj_name}
%{desc}

%prep
%autosetup -p1 -n geopm-%{version}
echo %{version} > %{prj_name}/%{prj_name}/VERSION

%generate_buildrequires
cd %{prj_name}
%pyproject_buildrequires

%build
cd %{prj_name}
%pyproject_wheel

%install
cd %{prj_name}
%pyproject_install
%pyproject_save_files %{prj_name}

%check
cd %{prj_name}
%{python3} -m unittest discover -s test -p 'Test*.py' -v

%files -n python3-%{prj_name} -f %{pyproject_files}
%license LICENSE-BSD-3-Clause
%doc README.md
%{python3_sitearch}/_libgeopm_py_cffi.abi3*.so
%{_bindir}/geopmlaunch

%changelog
%autochangelog
