Name:		pepc
Version:	1.5.26
Release:	%autorelease
Summary:	Power, Energy, and Performance Configurator

License:	BSD-3-Clause
Url:		https://github.com/intel/pepc
Source0:	%url/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
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
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pepclibs pepctool

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
%{_datadir}/pepc
%{_mandir}/man1/pepc*

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
