Name:       bpfilter
Version:    0.6.0
Release:    %autorelease
Summary:    BPF-based packet filtering framework

License:    GPL-2.0-only
URL:        https://bpfilter.io
Source:     https://github.com/facebook/bpfilter/archive/refs/tags/v%{version}.tar.gz#/bpfilter-%{version}.tar.gz

BuildRequires: bison
BuildRequires: clang
BuildRequires: cmake
BuildRequires: flex
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: libbpf-devel
BuildRequires: libcmocka-devel
BuildRequires: libnl3-devel
BuildRequires: make
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: vim-common

# Only those two architectures are supported by bpfilter.
ExclusiveArch: %{x86_64} %{arm64}

%global soname_version %%(echo %%{version}} | cut -d. -f1)

%global _description %{expand:
BPF-based packet filtering framework to convert text-format filtering rules
into BPF programs attach to your kernel.}

%description    %{_description}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake -DNO_DOCS=1 -DNO_BENCHMARKS=1 -DNO_CHECKS=1 -DDEFAULT_PROJECT_VERSION=%{version}
%cmake_build -- bpfilter libbpfilter bfcli

%check
make -C %__cmake_builddir unit

%install
%cmake_install

%post
%systemd_post bpfilter.service

%preun
%systemd_preun bpfilter.service

%postun
%systemd_postun_with_restart bpfilter.service

%files
%license COPYING
%{_sbindir}/bfcli
%{_sbindir}/bpfilter
%{_libdir}/libbpfilter.so.%{soname_version}
%{_libdir}/libbpfilter.so.%{version}
%{_unitdir}/bpfilter.service

%files devel
%{_includedir}/bpfilter/
%{_libdir}/libbpfilter.so
%{_libdir}/pkgconfig/bpfilter.pc

%changelog
%autochangelog
