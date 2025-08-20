%global pypi_name pyCEC
%global mod_name pycec

Name:           python-%{mod_name}
Version:        0.6.0
Release:        %autorelease
Summary:        Provide HDMI CEC devices as objects

License:        MIT
URL:            https://github.com/konikvranik/pycec/
Source0:        %{url}/archive/v%{version}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  libcec-devel
BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%description
TCP <=> HDMI bridge to control HDMI devices over TCP network.

%package -n     python3-%{mod_name}
Summary:        %{summary}
Requires:	python3-libcec

%description -n python3-%{mod_name}
TCP <=> HDMI bridge to control HDMI devices over TCP network.

%prep
%autosetup -n %{pypi_name}-%{version}

# python asyncio fix
sed -i 's/asyncio.get_event_loop/asyncio.new_event_loop/' tests/test_hdmi_network.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{mod_name}

%check
%pytest -v

%files -n python3-%{mod_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/pycec

%changelog
%autochangelog
