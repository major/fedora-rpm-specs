Name:           bpftool
Version:        7.5.0
Release:        2%{?dist}
Summary:        Inspection and simple manipulation of eBPF programs and maps

%global libname libbpf
%global sources %{name}-%{libname}-v%{version}-sources

License:        GPL-2.0-only OR BSD-2-Clause
URL:            https://github.com/libbpf/bpftool
Source:         https://github.com/libbpf/bpftool/releases/download/v%{version}/%{sources}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  binutils-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  libcap-devel
BuildRequires:  llvm-devel
BuildRequires:  clang
BuildRequires:  python3-docutils
BuildRequires:  kernel-devel

%description
This package contains the bpftool, which allows inspection and simple
manipulation of eBPF programs and maps.

%prep
%autosetup -p1 -n %{sources}

%build
# We need to use vmlinux.h from kernel-devel rather than the one from the running system
%define kernel_version %(rpm -q --qf "%%{VERSION}-%%{RELEASE}.%%{ARCH}" kernel-devel)
%make_build -C src/ EXTRA_CFLAGS="%{build_cflags}" EXTRA_LDFLAGS="%{build_ldflags}" VMLINUX_H="/usr/src/kernels/%{kernel_version}/vmlinux.h"

%install
%make_install -C src/ prefix=%{_prefix} bash_compdir=%{bash_completions_dir} mandir=%{_mandir} doc-install

%files
# bpftool Makefile hard-codes installation to {_prefix}/sbin but {_sbindir} now
# resolves to /usr/bin so we need to explicitly use {_prefix}/sbin here.
# In the end, /usr/sbin is a symlink to /usr/bin.
# Details: https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin
%{_prefix}/sbin/bpftool
%{bash_completions_dir}/bpftool
%{_mandir}/man8/bpftool*.8*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 21 2024 Viktor Malik <vmalik@redhat.com> - 7.5.0-1
- Create the package
