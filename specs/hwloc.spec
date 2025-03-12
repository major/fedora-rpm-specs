Summary:   Portable Hardware Locality - portable abstraction of hierarchical architectures
Name:      hwloc
Version:   2.12.0
Release:   %autorelease
License:   BSD-2-Clause
URL:       http://www.open-mpi.org/projects/hwloc/
Source0:   https://download.open-mpi.org/release/hwloc/v2.11/hwloc-%{version}.tar.bz2
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires: gcc
# C++ only for hwloc-hello-cpp test:
BuildRequires: gcc-c++
BuildRequires: cairo-devel
BuildRequires: libpciaccess-devel
BuildRequires: libX11-devel
BuildRequires: libxml2-devel
BuildRequires: lynx
BuildRequires: ncurses-devel
%if %{undefined rhel}
%ifarch x86_64
BuildRequires: oneapi-level-zero-devel
%endif
%endif
BuildRequireS: opencl-headers
BuildRequireS: ocl-icd-devel
BuildRequires: desktop-file-utils
BuildRequires: numactl-devel
BuildRequires: rdma-core-devel
BuildRequires: systemd-devel
%ifarch %{ix86} x86_64
%{?systemd_requires}
BuildRequires: systemd
%endif
BuildRequires: make

%description
The Portable Hardware Locality (hwloc) software package provides
a portable abstraction (across OS, versions, architectures, ...)
of the hierarchical topology of modern architectures, including
NUMA memory nodes,  shared caches, processor sockets, processor cores
and processing units (logical processors or "threads"). It also gathers
various system attributes such as cache and memory information. It primarily
aims at helping applications with gathering information about modern
computing hardware so as to exploit it accordingly and efficiently.

hwloc may display the topology in multiple convenient formats.
It also offers a powerful programming interface (C API) to gather information
about the hardware, bind processes, and much more.

%package devel
Summary:   Headers and shared development libraries for hwloc
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
%ifnarch %{arm}
Requires:  rdma-core-devel%{?_isa}
%endif

%description devel
Headers and shared object symbolic links for the hwloc.

%package libs
Summary:   Run time libraries for the hwloc

%description libs
Run time libraries for the hwloc

%package gui
Summary:   The gui-based hwloc program(s)
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}

%description gui
GUI-based tool for displaying system topology information.

%package plugins
Summary:   Plugins for hwloc
Requires:  %{name}-plugins%{?_isa} = %{version}-%{release}

%description plugins
 This package contains plugins for hwloc. This includes
  - PCI support
  - GL support
  - libxml support

%prep
%autosetup -p1

%build
%configure --enable-plugins --disable-silent-rules --runstatedir=/run
# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install

# We don't ship .la files.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

cp -p AUTHORS COPYING NEWS README VERSION %{buildroot}%{_pkgdocdir}
cp -pr doc/examples %{buildroot}%{_pkgdocdir}
# Fix for BZ1253977
mv  %{buildroot}%{_pkgdocdir}/examples/Makefile  %{buildroot}%{_pkgdocdir}/examples/Makefile_%{_arch}

desktop-file-validate %{buildroot}/%{_datadir}/applications/lstopo.desktop

# Avoid making hwloc-gui depend on hwloc
rm %{buildroot}%{_mandir}/man1/lstopo.1
ln %{buildroot}%{_mandir}/man1/lstopo-no-graphics.1 %{buildroot}%{_mandir}/man1/lstopo.1

# Deal with service file
# https://github.com/open-mpi/hwloc/issues/221
%ifarch %{ix86} x86_64
mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_datadir}/%{name}/hwloc-dump-hwdata.service %{buildroot}%{_unitdir}/
%else
rm %{buildroot}%{_datadir}/%{name}/hwloc-dump-hwdata.service
%endif

%check
LD_LIBRARY_PATH=$PWD/hwloc/.libs make check

%ifarch %{ix86} x86_64
%post
%systemd_post hwloc-dump-hwdata.service

%preun
%systemd_preun hwloc-dump-hwdata.service

%postun
%systemd_postun_with_restart hwloc-dump-hwdata.service
%endif

%files
%{_datadir}/bash-completion/completions/*
%{_bindir}/%{name}*
%{_bindir}/lstopo-no-graphics
%{_datadir}/hwloc/hwloc-ps.www/
%{_mandir}/man1/%{name}*
%{_mandir}/man1/lstopo-no-graphics*
%ifarch %{ix86} x86_64
%{_sbindir}/hwloc-dump-hwdata
%{_unitdir}/hwloc-dump-hwdata.service
%endif

%files devel
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_includedir}/%{name}.h
%{_pkgdocdir}/examples
%{_libdir}/*.so

%files libs
%{_mandir}/man7/%{name}*
%dir %{_datadir}/%{name}
%{_datadir}/hwloc/hwloc.dtd
%{_datadir}/hwloc/hwloc-valgrind.supp
%{_datadir}/hwloc/hwloc2.dtd
%{_datadir}/hwloc/hwloc2-diff.dtd
%dir %{_pkgdocdir}/
%{_pkgdocdir}/*[^c]
%{_libdir}/libhwloc*so.15*

%files gui
%{_bindir}/lstopo
%{_mandir}/man1/lstopo.1*
%{_datadir}/applications/lstopo.desktop

%files plugins
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/hwloc*

%changelog
%autochangelog
