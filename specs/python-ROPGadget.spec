%global srcname ropgadget

Name:           python-ROPGadget
Version:        7.6
Release:        %autorelease
Summary:        A tool to find ROP gadgets in program files

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/R/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/JonathanSalwan/ROPgadget/c29c50773ec7fb3df56396ce27fb71c3898c53ae/LICENSE_BSD.txt
Source2:        https://raw.githubusercontent.com/JonathanSalwan/ROPgadget/c29c50773ec7fb3df56396ce27fb71c3898c53ae/README.md

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
ROPGadget lets you search your gadgets on your binaries to facilitate
your ROP exploitation. ROPgadget supports ELF, PE and Mach-O format on
x86, x64, ARM, ARM64, PowerPC, SPARC and MIPS architectures.}

%description %_description

%package -n python3-ROPGadget
Summary:        %{summary}
%{?python_provide:%python_provide python3-ROPGadget}
Requires:       %{py3_dist capstone}

%description -n python3-ROPGadget %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

cp -p %SOURCE1 .
cp -p %SOURCE2 .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
for lib in $(find %{buildroot}%{python3_sitelib}/ropgadget/ -name "*.py"); do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done
%pyproject_save_files -l ropgadget

%check
%pyproject_check_import

%files -n python3-ROPGadget -f %{pyproject_files}
%doc LICENSE_BSD.txt README.md
%{_bindir}/*

%changelog
%autochangelog
