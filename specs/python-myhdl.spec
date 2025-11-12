%global srcname myhdl
%global sum A python hardware description and verification language

Name:           python-%{srcname}
Version:        0.11
Release:        %autorelease
Summary:        %{sum}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://myhdl.org
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
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
%setup -q -n myhdl-%{version}
find -name '*.txt' | xargs chmod -x

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
%doc /usr/share/myhdl/cosimulation/


%changelog
%autochangelog
