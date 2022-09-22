%global upstreamversion 1.7

Name:		pmdk-convert
Version:	1.7
Release:	9%{?dist}
Summary:	Conversion tool for PMDK pools
# Note: utils/cstyle is CDDL licensed. It's only used during development and it's NOT part of the binary RPM.
License:	BSD
URL:		https://github.com/pmem/pmdk-convert

Source0:	https://github.com/pmem/pmdk-convert/releases/download/%{upstreamversion}/pmdk-convert-%{upstreamversion}.tar.gz
Source1:	https://github.com/pmem/pmdk/archive/1.0.tar.gz#/nvml-1.0.tar.gz
Source2:	https://github.com/pmem/pmdk/archive/1.1.tar.gz#/nvml-1.1.tar.gz
Source3:	https://github.com/pmem/pmdk/releases/download/1.2.4/pmdk-1.2.4.tar.gz
Source4:	https://github.com/pmem/pmdk/releases/download/1.3.3/pmdk-1.3.3.tar.gz
Source5:	https://github.com/pmem/pmdk/releases/download/1.4.3/pmdk-1.4.3.tar.gz
Source6:	https://github.com/pmem/pmdk/releases/download/1.5.2/pmdk-1.5.2.tar.gz
Source7:	https://github.com/pmem/pmdk/releases/download/1.6.1/pmdk-1.6.1.tar.gz
Source8:	https://github.com/pmem/pmdk/releases/download/1.7/pmdk-1.7.tar.gz

BuildRequires:	cmake >= 3.3
BuildRequires:	glibc-devel
BuildRequires:	gcc
BuildRequires:	g++
BuildRequires:	gdb

# PMDK is currently available only on x86_64
# Relevant bug reports:
# https://bugzilla.redhat.com/show_bug.cgi?id=1340634
# https://bugzilla.redhat.com/show_bug.cgi?id=1340635
# https://bugzilla.redhat.com/show_bug.cgi?id=1340636
# https://bugzilla.redhat.com/show_bug.cgi?id=1340637
ExclusiveArch: x86_64

%description
pmdk-convert is a tool for conversion of PMDK pools from any version
to any consecutive version. Currently only libpmemobj pools require
conversion and this tool supports only those kind of pools.

%files
%{_bindir}/pmdk-convert
%{_mandir}/man1/pmdk-convert.1.gz
%dir %{_libdir}/pmdk-convert
%{_libdir}/pmdk-convert/libpmem-convert.so
%{_libdir}/pmdk-convert/pmemobj_convert_v1.so
%{_libdir}/pmdk-convert/pmemobj_convert_v2.so
%{_libdir}/pmdk-convert/pmemobj_convert_v3.so
%{_libdir}/pmdk-convert/pmemobj_convert_v4.so
%{_libdir}/pmdk-convert/pmemobj_convert_v5.so
%{_libdir}/pmdk-convert/pmemobj_convert_v6.so

%license LICENSE

%doc ChangeLog README.md

%prep
%setup -q
cp %{S:1} 1.0.tar.gz
cp %{S:2} 1.1.tar.gz
cp %{S:3} 1.2.4.tar.gz
cp %{S:4} 1.3.3.tar.gz
cp %{S:5} 1.4.3.tar.gz
cp %{S:6} 1.5.2.tar.gz
cp %{S:7} 1.6.1.tar.gz
cp %{S:8} 1.7.tar.gz

%build
mkdir build
cd build
# TESTS_USE_FORCED_PMEM=ON to speed up tests on non-pmem file systems
%cmake .. -DTESTS_USE_FORCED_PMEM=ON
%cmake_build

%install
cd build
%cmake_install

%check
cd build
%ctest

%if 0%{?__debug_package} == 0
%debug_package
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 03 2020 Adam Borowski <kilobyte@angband.pl> - 1.7-5
- Convert to new cmake macros, fixing FTBFS.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Marcin Ślusarz <marcin.slusarz@intel.com> - 1.7-1
- Update to 1.7

* Tue Oct 01 2019 Marcin Ślusarz <marcin.slusarz@intel.com> - 1.5.2-1
- Update to 1.5.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 Marcin Ślusarz <marcin.slusarz@intel.com> - 1.5.1-1
- Update to 1.5.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Marcin Ślusarz <marcin.slusarz@intel.com> - 1.5-1
- Initial RPM release
