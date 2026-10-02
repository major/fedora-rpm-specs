Name:		pepc
Version:	2.0.7
Release:	%autorelease
Summary:	Power, Energy, and Performance Configurator

License:	BSD-3-Clause
Url:		https://github.com/intel/pepc
Source0:	%url/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-tkinter
Requires:	python3-pepc = %{version}-%{release}

%description
Pepc stands for "Power, Energy, and Performance Configurator".
This is a command-line tool for configuring various Linux and Hardware 
power management features.

%package -n python3-%{name}
Summary:	Pepc Python libraries

%description -n python3-%{name}
Pepc Python libraries

%prep
%autosetup

%if 0%{?rhel} == 9
# build with hatchling
sed -i '/license-files/d' pyproject.toml
cat >> pyproject.toml << 'EOF'

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["pepclibs", "pepctools", "pepcdata"]
EOF
%elif 0%{?rhel} > 9
# PEP 639 fix
sed -e 's|license = "BSD-3-Clause"|license = {text = "BSD-3-Clause"}|g' -i pyproject.toml
sed -i '/license-files/d' pyproject.toml
cat >> pyproject.toml << 'EOF'

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"
EOF
%else
cat >> pyproject.toml << 'EOF'

[build-system]
build-backend = "setuptools.build_meta"
requires = ["setuptools>=61"]
EOF
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pepclibs pepctools pepcdata

%check
# skip heavy tests for non-x86_64 archs
%pytest \
%ifnarch x86_64 %{ix86}
  -k 'test_cpuinfo_get' \
%endif
  -v

%files
%license LICENSE.md
%doc README.md CHANGELOG.md
%{_bindir}/pepc

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
