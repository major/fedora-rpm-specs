# Upstream build system requires the use of libbpf sources and a pinned version
# https://bugzilla.redhat.com/show_bug.cgi?id=2184233#c5
%global libbpf_url https://github.com/libbpf/libbpf
%global libbpf_commit c5f22aca0f3aa855daa159b2777472b35e721804
%global libbpf_shortcommit %(c=%{libbpf_commit}; echo ${c:0:7})
%global libbpf_date 20241120
# see libbpf/src/Makefile for version
%global libbpf_version 1.6.0~^%{libbpf_date}git%{libbpf_shortcommit}

Name:           veristat
Version:        0.4.1
Release:        %autorelease
Summary:        Tool for loading, verifying, and debugging BPF object files

License:        BSD-2-Clause OR GPL-2.0-only
URL:            https://github.com/libbpf/veristat

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{libbpf_url}/archive/%{libbpf_commit}/libbpf-%{libbpf_version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

# libbpf deps
BuildRequires:  elfutils-libelf-devel

# upstream does not support dynamic linking
Provides:       bundled(libbpf) = %{libbpf_version}

%description
veristat is the tool for loading, verifying, and debugging BPF object files. It
allows to work with BPF object files convenient and quickly, without having to
use or modify corresponding user-space parts of an application.

%prep
%autosetup -p1

# provide the libbpf version we specify rather than using git submodule
tar xf %{SOURCE1}
rmdir libbpf
mv libbpf-%{libbpf_commit} libbpf
mv libbpf/LICENSE libbpf-LICENSE
mv libbpf/LICENSE.BSD-2-Clause libbpf-LICENSE.BSD-2-Clause
mv libbpf/LICENSE.LGPL-2.1 libbpf-LICENSE.LGPL-2.1

%build
export EXTRA_CFLAGS="%{optflags}"
export EXTRA_LDFLAGS="%{build_ldflags}"
%make_build -C src V=1

%install
%make_install -C src prefix="%{_prefix}"

%files
%license LICENSE libbpf-LICENSE*
%doc README.md
%{_bindir}/veristat

%changelog
%autochangelog
