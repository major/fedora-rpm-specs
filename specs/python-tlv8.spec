Name:           python-tlv8
Version:        0.10.0
Release:        %autorelease
Summary:        Handle type-length-value TLV encoded data

License:        Apache-2.0
URL:            https://github.com/jlusiardi/tlv8_python
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python module to handle type-length-value _TLV_ encoded data 8-bit 
type, 8-bit length, and N-byte value as described within the Apple 
HomeKit Accessory Protocol Specification Non-Commercial Version Release R2.}

%description %_description

%package -n     python3-tlv8
Summary:        %{summary}

%description -n python3-tlv8 %_description


%prep
%autosetup -p1 -n tlv8_python-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L tlv8


%check
%{py3_test_envvars} %{python3} -m unittest


%files -n python3-tlv8 -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
