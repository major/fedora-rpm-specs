%global pypi_name mrtparse
%global srcname mrtparse

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        3%{?dist}
Summary:        MRT format data parser

License:        Apache-2.0
URL:            https://github.com/t2mune/mrtparse/
Source0:        %{pypi_source %{srcname}}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
mrtparse is a module to read and analyze the MRT format data.
The MRT format can be used to export routing protocol messages, state changes,
and routing information base contents, and is defined in RFC6396.
Programs like FRRouting, Quagga, Zebra, BIRD, OpenBGPD and PyRT can dump the
MRT format data.
You can also download archives from the Route Views Projects, RIPE NCC.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%check
%pyproject_check_import
# Test the example scripts
for bgp in samples/*_bgp; do
    PYTHONPATH=. %{__python3} examples/mrt2bgpdump.py $bgp > /dev/null
done
for rib in samples/*_rib*; do
    PYTHONPATH=. %{__python3} examples/mrt2exabgp.py $rib > /dev/null
done
for file in samples/*_bgp samples/*_rib*; do
    PYTHONPATH=. %{__python3} examples/mrt2json.py $file > /dev/null
done


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst examples samples


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.14

* Fri Apr 11 2025 Aurelien Bompard <abompard@fedoraproject.org> - 2.2.0-1
- Initial package.
