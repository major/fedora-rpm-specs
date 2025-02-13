%bcond_without  check

%global forgeurl https://github.com/hugsy/gef

Name:           gdb-gef
Version:        2025.01

%global tag %{version}
%forgemeta

Release:        %autorelease
Summary:        GEF (GDB Enhanced Features)

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        gdb-gef
# https://github.com/hugsy/gef/pull/1094
Patch0:         gef-got-audit.patch
Patch1:         gef-gcc15.patch

BuildArch:      noarch
ExclusiveArch:  x86_64

Requires:       gdb
Requires:       file
Requires:       binutils
Requires:       procps-ng

%if %{with check}
# These are required for tests:
BuildRequires:  gdb
BuildRequires:  gdb-gdbserver
BuildRequires:  file
BuildRequires:  binutils
BuildRequires:  procps-ng
BuildRequires:  python3
BuildRequires:  python3-pylint
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-coverage
BuildRequires:  python3-rpyc
BuildRequires:  python3-requests
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qemu-user
BuildRequires:  git
%endif
BuildRequires:  sed


%description
GEF (pronounced ʤɛf - "Jeff") is a set of commands for x86/64, ARM,
MIPS, PowerPC and SPARC to assist exploit developers and
reverse-engineers when using old school GDB. It provides additional
features to GDB using the Python API to assist during the process of
dynamic analysis and exploit development. Application developers will
also benefit from it, as GEF lifts a great part of regular GDB
obscurity, avoiding repeating traditional commands, or bringing out
the relevant information from the debugging runtime.


%prep
%forgesetup
%patch 0 -p1
%patch 1 -p1


%build


%install
mkdir -p %{buildroot}/%{_datadir}/gdb
cp gef.py %{buildroot}/%{_datadir}/gdb/gef.py

sed -e "s:@datadir@:%{_datadir}:g" < %{SOURCE1} > %{SOURCE1}.sh
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{SOURCE1}.sh %{buildroot}/%{_bindir}/gdb-gef


%if %{with check}
%check
make -C tests/binaries
python3 -m pytest -v -m "not benchmark" -m "not online" tests/
%endif


%files
%license LICENSE
%doc docs/* README.md
%{_datadir}/gdb/gef.py
%{_bindir}/gdb-gef


%changelog
%autochangelog
