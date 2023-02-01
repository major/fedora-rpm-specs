%global sdkver 1.3.239.0

Name:           spirv-headers
Version:        1.5.5
Release:        %autorelease
Summary:        Header files from the SPIR-V registry

License:        MIT
URL:            https://github.com/KhronosGroup/SPIRV-Headers/
Source0:        %url/archive/sdk-%{sdkver}.tar.gz#/SPIRV-Headers-sdk-%{sdkver}.tar.gz

BuildArch:      noarch

%description
%{summary}

This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry file

%package        devel
Summary:        Development files for %{name}

%description    devel
%{summary}

This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry fil

%prep
%autosetup -n SPIRV-Headers-sdk-%{sdkver}
chmod a-x include/spirv/1.2/spirv.py


%build


%install
mkdir -p %buildroot%{_includedir}/
mv include/* %buildroot%{_includedir}/

%files devel
%license LICENSE
%doc README.md
%{_includedir}/spirv/

%changelog
%autochangelog
