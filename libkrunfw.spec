# This library just contains the guest payload to be injected by libkrun into
# the VM's memory, so no useful debug info can be generated from it.
%global debug_package %{nil}

%global kernel linux-5.15.71

Name:           libkrunfw
Version:        3.7.0
Release:        1%{?dist}
Summary:        A dynamic library bundling the guest payload consumed by libkrun
License:        LGPLv2 and GPLv2
URL:            https://github.com/containers/libkrunfw
Source0:        https://github.com/containers/libkrunfw/archive/refs/tags/v%{version}.tar.gz
# This package bundles a customized Linux kernel in a format that can only be
# consumed by libkrun, which will run it in an isolated context using KVM
# Virtualization. This kernel can't be used for booting a physical machine
# and, by being bundled in a dynamic library, it can not be mistaken as a
# regular kernel.
#
# The convenience of distributing a kernel this way and for this purpose was
# discussed here:
# https://lists.fedorahosted.org/archives/list/kernel@lists.fedoraproject.org/thread/2TMXPCE2VWF7USZA7OHQ3P2SBJAEGCSX/
Source1:        https://www.kernel.org/pub/linux/kernel/v5.x/%{kernel}.tar.xz

# libkrunfw only provides configs for x86_64 and aarch64 as libkrun (the only
# consumer of this library) only supports those architectures.
ExclusiveArch:  x86_64 aarch64

# libkrunfw + packaging requirements
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  python3-pyelftools
BuildRequires:  openssl-devel

# kernel build requirements
BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  elfutils-devel
BuildRequires:  flex
%ifarch aarch64
BuildRequires:  perl-interpreter
%endif

%description
%{summary}

%package devel
Summary: Header files and libraries for libkrunfw development
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The libkrunfw-devel package contains the libraries needed to develop
programs that consume the guest payload integrated in libkrunfw.

# SEV is a feature provided by AMD EPYC processors, so only it's only
# available on x86_64.
%ifarch x86_64
%package sev
Summary: A dynamic library bundling the guest payload consumed by libkrun-sev

%description sev
The libkrunfw-sev package contains the library bundling the guest
payload consumed by libkrun-sev.

%package sev-devel
Summary: Header files and libraries for libkrunfw-sev development
Requires: %{name}-sev%{?_isa} = %{version}-%{release}

%description sev-devel
The libkrunfw-sev-devel package contains the libraries needed to develop
programs that consume the guest payload integrated in libkrunfw-sev.
%endif

%prep
%autosetup -S git
mkdir tarballs
cp %{SOURCE1} tarballs/

%build
%{make_build}
%ifarch x86_64
    rm -fr %{kernel}
    rm kernel.c
    %{make_build} SEV=1
    pushd utils
    make
    popd
%endif

%install
%{make_install} PREFIX=%{_prefix}
%ifarch x86_64
    %{make_install} SEV=1 PREFIX=%{_prefix}
    install -D -p -m 0755 utils/krunfw_measurement %{buildroot}%{_bindir}/krunfw_measurement
%endif

%files
%{_libdir}/libkrunfw.so.3
%{_libdir}/libkrunfw.so.%{version}

%files devel
%{_libdir}/libkrunfw.so

%ifarch x86_64
%files sev
%{_libdir}/libkrunfw-sev.so.3
%{_libdir}/libkrunfw-sev.so.%{version}
%{_bindir}/krunfw_measurement

%files sev-devel
%{_libdir}/libkrunfw-sev.so
%endif

%changelog
* Tue Oct 04 2022 Sergio Lopez <slp@redhat.com> - 3.7.0-1
- Update to 3.7.0 which bundles a 5.15.71 kernel

* Wed Aug 17 2022 Sergio Lopez <slp@redhat.com> - 3.6.3-1
- Update to 3.6.3 which bundles a 5.15.60 kernel
- Add the libkrunfw-sev and libkrunfw-sev-devel subpackages with the SEV
  variant of the library.

* Wed Jul 27 2022 Sergio Lopez <slp@redhat.com> - 3.2.0-1
- Update to 3.2.0 which bundles a 5.15.57 kernel

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Sergio Lopez <slp@redhat.com> - 3.1.0-1
- Update to 3.1.0 which bundles a 5.15.52 kernel

* Fri Jun 17 2022 Sergio Lopez <slp@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Mon Jun 06 2022 Sergio Lopez <slp@redhat.com> - 2.1.1-1 
- Initial package
