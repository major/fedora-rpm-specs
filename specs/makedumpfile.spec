%global eppic_ver e8844d3793471163ae4a56d8f95897be9e5bd554
%global eppic_shortver %(c=%{eppic_ver}; echo ${c:0:7})
%global enable_epic 0
Name: makedumpfile
Version: 1.7.6
Summary: make a small dumpfile of kdump
Release: 3%{?dist}

License: GPL-2.0-only
URL: https://github.com/makedumpfile/makedumpfile
Source0: https://github.com/makedumpfile/makedumpfile/archive/%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/lucchouina/eppic/archive/%{eppic_ver}/eppic-%{eppic_shortver}.tar.gz
Patch1: 0001-PATCH-fix-gcc-15-compiling-error-too-many-arguments-.patch

Conflicts: kexec-tools < 2.0.28-5
BuildRequires: make
BuildRequires: gcc
BuildRequires: zlib-devel
BuildRequires: elfutils-devel
BuildRequires: glib2-devel
BuildRequires: bzip2-devel
BuildRequires: ncurses-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: lzo-devel
BuildRequires: snappy-devel
BuildRequires: libzstd-devel
BuildRequires: pkgconfig
BuildRequires: intltool
BuildRequires: gettext

%description
makedumpfile is a tool to compress and filter out unneeded data from kernel
dumps to reduce its file size. It is typically used with the kdump mechanism.

%prep
%autosetup -p1
tar -z -x -v -f %{SOURCE1}
sed -r -i 's|/usr/sbin|%_sbindir|g' Makefile

%build
%make_build LINKTYPE=dynamic USELZO=on USESNAPPY=on USEZSTD=on

%if 0%{enable_epic}
%make_build -C eppic-%{eppic_ver}/libeppic
%make_build LDFLAGS="$LDFLAGS -Ieppic-%{eppic_ver}/libeppic -Leppic-%{eppic_ver}/libeppic" eppic_makedumpfile.so
%endif

%install
%make_install
install -m 644 -D makedumpfile.conf %{buildroot}/%{_sysconfdir}/makedumpfile.conf.sample
rm %{buildroot}/%{_sbindir}/makedumpfile-R.pl

%if 0%{enable_epic}
install -m 755 -D eppic_makedumpfile.so %{buildroot}/%{_libdir}/eppic_makedumpfile.so
%endif

%files
%{_sbindir}/makedumpfile
%{_mandir}/man5/makedumpfile.conf.5*
%{_mandir}/man8/makedumpfile.8*
%{_sysconfdir}/makedumpfile.conf.sample
%if 0%{enable_epic}
%{_libdir}/eppic_makedumpfile.so
%endif
%{_datadir}/makedumpfile/
%license COPYING

%changelog
* Tue Feb 18 2025 Coiby Xu <coxu@redhat.com> - 1.7.6-3
- fix gcc-15 compiling error (bz2340813)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 23 2024 Lichen Liu <lichliu@redhat.com> - 1.7.6-1
- Update to upstream 1.7.6

* Thu Aug 08 2024 Coiby Xu <coxu@redhat.com> - 1.7.5-13
- Workaround for segfault by "makedumpfile --mem-usage" on PPC64

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Lianbo Jiang <lijiang@redhat.com> - 1.7.5-11
- Fix failure of hugetlb pages exclusion on Linux 6.9 and later
- Fix wrong exclusion of Slab pages on Linux 6.10-rc1 and later

* Thu Nov 23 2023 Coiby Xu <coxu@redhat.com> - 1.7.5-1
- split from kexec-tools
