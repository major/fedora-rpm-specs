%global date 20220927
%global commit c556afbd8840149991b6e830f2d3d63cc50388b1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           packetdrill
Version:        2.0~%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Quick, precise tests for entire TCP/UDP/IPv4/IPv6 network stacks

License:        GPL-2.0-only
URL:            https://github.com/google/packetdrill
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
# PR#56: packetdrill: add test of tcp window clamp socket option
Patch0:         %{url}/pull/56.patch
# PR#62: Switch to Python3
Patch1:         %{url}/pull/62.patch

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  emacs
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  sed
BuildRequires:  vim-filesystem

Recommends:     %{name}-data = %{version}-%{release}

%description
The packetdrill scripting tool enables quick, precise tests for entire
TCP/UDP/IPv4/IPv6 network stacks, from the system call layer down to the NIC
hardware. packetdrill currently works on Linux, FreeBSD, OpenBSD, and NetBSD.
It can test network stack behavior over physical NICs on a LAN, or on a single
machine using a tun virtual network device.

%package        data
Summary:        Data files for %{name}

Requires:       bash
Requires:       coreutils
Requires:       emacs-filesystem
Requires:       iproute
Requires:       procps-ng
Requires:       python3
Requires:       vim-filesystem
Suggests:       emacs
Suggests:       vim

BuildArch:      noarch

%description    data
This package contains a test runner, test scripts, and editor configs for
%{name}.

%prep
%autosetup -n %{name}-%{commit} -p1

# Fix paths in the test runner
sed -i gtests/net/packetdrill/run_all.py \
    -e 's:bin_path = .*:bin_path = "%{_bindir}/%{name}":' \
    -e 's:nswrap_path = .*:nswrap_path = "%{_datadir}/%{name}/in_netns.sh":'

%build
pushd gtests/net/%{name}
# Disable the shared library, as it's only meant for internal use
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

# Bytecompile emacs config
%{_emacs_bytecompile} contrib/%{name}.el

%install
# Main binary
install -Dpm0755 -t %{buildroot}%{_bindir} \
%if 0%{?el8}
  gtests/net/%{name}/%{name}
%else
  gtests/net/%{name}/%{_vpath_builddir}/%{name}
%endif

# Test runner
install -Dpm0755 -t %{buildroot}%{_datadir}/%{name} \
  gtests/net/%{name}/{in_netns.sh,run_all.py}

# Tests
cp -PR gtests/net/{common,tcp}/ %{buildroot}%{_datadir}/%{name}/

# Editor configs
install -Dpm0644 -t %{buildroot}%{_emacs_sitelispdir} \
  gtests/net/%{name}/contrib/%{name}.{el,elc}
install -Dpm0644 -t %{buildroot}%{vimfiles_root}/syntax \
  gtests/net/%{name}/contrib/%{name}.vim

%check
# tests aren't hooked up properly to cmake
for t in checksum_test packet_parser_test packet_to_string_test; do
%if 0%{?el8}
  ./gtests/net/%{name}/${t}
%else
  ./gtests/net/%{name}/%{_vpath_builddir}/${t}
%endif
done

%files
%license LICENSE
%doc README.md syntax.md
%{_bindir}/%{name}

%files data
%license LICENSE
%{_datadir}/%{name}
%{_emacs_sitelispdir}/%{name}.el
%{_emacs_sitelispdir}/%{name}.elc
%{vimfiles_root}/syntax/%{name}.vim

%changelog
%autochangelog
