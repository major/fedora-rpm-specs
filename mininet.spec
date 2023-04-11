%global snapdate 20220711
%global commit 3f5503d7737a0f07eafce03594cf9ed5112e5ae8
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mininet
Version:        2.3.1~b1%{?snapdate:^git%{snapdate}.%{shortcommit}}
Release:        %autorelease
Summary:        Emulator for rapid prototyping of Software Defined Networks

License:        BSD-3-Clause
URL:            https://github.com/%{name}/%{name}
%if 0%{?snapdate}
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  help2man
Requires:       openvswitch
Requires:       libcgroup-tools
Requires:       xterm, openssh-clients
Requires:       which, psmisc, procps-ng
Requires:       iproute, ethtool, net-tools
Requires:       telnet, socat, iperf

%description
Mininet emulates a complete network of hosts, links, and switches on a single
machine. To create a sample two-host, one-switch network, just run: 'sudo mn'

Mininet is useful for interactive development, testing, and demos, especially
those using OpenFlow and SDN. OpenFlow-based network controllers prototyped
in Mininet can usually be transferred to hardware with minimal changes for
full line-rate execution.


%prep
%if 0%{?snapdate}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-%{version}
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
export PYTHON=%{python3}
export CC="gcc %{optflags}"
%make_build man
%make_build mnexec


%install
install -D mnexec %{buildroot}%{_bindir}/mnexec
install -D -t %{buildroot}%{_mandir}/man1 mn.1 mnexec.1
%pyproject_install
%pyproject_save_files %{name}


%check
%pyproject_check_import -t


%files -f %{pyproject_files}
%doc README.* CONTRIBUTORS
%license LICENSE
%{_bindir}/mn
%{_bindir}/mnexec
%{_mandir}/man1/mn.1*
%{_mandir}/man1/mnexec.1*


%autochangelog
