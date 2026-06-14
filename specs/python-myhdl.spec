%global srcname myhdl
%global sum A python hardware description and verification language

Name:           python-%{srcname}
Version:        0.11
Release:        %autorelease
Summary:        %{sum}
License:        LGPL-2.1-or-later
URL:            https://www.myhdl.org
Source:         %{pypi_source %{srcname}}
BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{name} is a Python hardware description and verification language that 
helps you go from Python to silicon. MyHDL code can be converted to Verilog 
and VHDL. It can also be used to convert signals, do co-simulation 
with Verilog, generating test benches with test vectors for VHDL, Verilog and 
supports viewing waveform by tracing signal changes in a VCD file.


%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
%{name} is a Python3 hardware description and verification language that 
helps you go from Python to silicon. MyHDL code can be converted to Verilog 
and VHDL. It can also be used to convert signals, do co-simulation 
with Verilog, generating test benches with test vectors for VHDL, Verilog and 
supports viewing waveform by tracing signal changes in a VCD file.


%prep
%autosetup -n myhdl-%{version}
find . -type f -name "*.txt" -exec chmod a-x {} +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%{_datadir}/myhdl
%doc README.md CHANGES.txt


%changelog
%autochangelog
