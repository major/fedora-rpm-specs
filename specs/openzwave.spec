Name:     openzwave
Version:  1.6.1914
Release:  10%{?dist}
Summary:  Sample Executables for OpenZWave
URL:      http://www.openzwave.net
License:  LGPL-3.0-or-later
Source0:  http://old.openzwave.com/downloads/openzwave-%{version}.tar.gz
#Source0:  https://github.com/OpenZWave/open-zwave/archive/%{commit0}.tar.gz#/%{name}-%{short0}.tar.gz

# New SwitchMultilevel command class support is broken so disable it
#Patch1:   openzwave-1.6-SwitchMultilevel.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: hidapi-devel
BuildRequires: systemd-devel
BuildRequires: tinyxml-devel


%description
OpenZWave is an open-source, cross-platform library designed to enable anyone to
add support for Z-Wave home-automation devices to their applications, without
requiring any in depth knowledge of the Z-Wave protocol.


%package -n libopenzwave
Summary: Library to access Z-Wave interfaces


%description -n libopenzwave
OpenZWave is an open-source, cross-platform library designed to enable anyone to
add support for Z-Wave home-automation devices to their applications, without
requiring any in depth knowledge of the Z-Wave protocol.


%package -n libopenzwave-devel
Summary: Open-ZWave header files
Requires: libopenzwave%{?_isa} = %{version}-%{release}


%description -n libopenzwave-devel
Header files needed when you want to compile your own
applications using openzwave


%package -n libopenzwave-devel-doc
Summary: Open-ZWave API documentation files
Requires: libopenzwave-devel%{?_isa} = %{version}-%{release}


%description -n libopenzwave-devel-doc
API documentation files needed when you want to compile your own
applications using openzwave


%prep
%setup -q -n %{name}-%{version}
#patch1 -p1 -b.switchmultilevel
# don't use projects compiler flags
sed -i 's/^RELEASE_CFLAGS.*/RELEASE_CFLAGS :=/' cpp/build/Makefile
sed -i 's/^RELEASE_CFLAGS.*/RELEASE_CFLAGS :=/' cpp/examples/MinOZW/Makefile


%build
major_ver=$(echo %{version} | awk -F \. {'print $1'})
minor_ver=$(echo %{version} | awk -F \. {'print $2'})
revision=$(echo %{version} | awk -F \. {'print $3'})
CFLAGS="-fPIC -DNDEBUG -Wformat %{optflags} '-DSYSCONFDIR=\"%{_sysconfdir}/openzwave/\"' -DOPENZWAVE_ENABLE_EXCEPTIONS" \
LDFLAGS="%{__global_ldflags}" \
VERSION_MAJ=$major_ver \
VERSION_MIN=$minor_ver \
VERSION_REV=$revision \
PREFIX=/usr \
sysconfdir=%{_sysconfdir}/openzwave/ \
includedir=%{_includedir} \
docdir=%{_defaultdocdir}/openzwave-%{version} \
instlibdir=%{_libdir} \
USE_HID=1 \
USE_BI_TXML=0 \
make %{?_smp_mflags} SHELL='sh -x'


%install
rm -rf %{buildroot}/*
major_ver=$(echo %{version} | awk -F \. {'print $1'})
minor_ver=$(echo %{version} | awk -F \. {'print $2'})
revision=$(echo %{version} | awk -F \. {'print $3'})
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_defaultdocdir}/openzwave-%{version}/
mkdir -p %{buildroot}/%{_sysconfdir}/
mkdir -p %{buildroot}/%{_includedir}/openzwave/
DESTDIR=%{buildroot} \
VERSION_MAJ=$major_ver \
VERSION_MIN=$minor_ver \
VERSION_REV=$revision \
PREFIX=/usr \
sysconfdir=%{_sysconfdir}/openzwave/ \
includedir=%{_includedir}/openzwave/ \
docdir=%{_defaultdocdir}/openzwave-%{version} \
instlibdir=%{_libdir} \
USE_HID=1 \
USE_BI_TXML=0 \
make install
rm %{buildroot}%{_defaultdocdir}/openzwave-%{version}/Doxyfile.in
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/html/
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/default.htm
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/general/
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/images+css/
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/api/
# Upstream does not use it anymore
# https://github.com/OpenZWave/open-zwave/commit/d62a9fd09b14303bf27323758f4a7bf9dcf14455
rm -f %{buildroot}%{_defaultdocdir}/openzwave-%{version}/ChangeLog.old


%files
%{_bindir}/MinOZW


%files -n libopenzwave
%license licenses/*.txt
%doc docs/default.htm docs/general/ docs/images+css/
%{_libdir}/libopenzwave.so.*
%dir %{_sysconfdir}/openzwave/
%config(noreplace) %{_sysconfdir}/openzwave/*


%files -n libopenzwave-devel
%{_bindir}/ozw_config
%{_includedir}/openzwave/
%{_libdir}/libopenzwave.so
%{_libdir}/pkgconfig/libopenzwave.pc


%files -n libopenzwave-devel-doc
%doc docs/api/


%ldconfig_scriptlets -n libopenzwave


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1914-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1914-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.1914-8
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1914-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1914-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1914-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1914-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1914-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1914-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Michael Cronenworth <mike@cchtml.com> - 1.6.1914-1
- version update

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1545-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1545-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Michael Cronenworth <mike@cchtml.com> - 1.6.1545-1
- version update

* Thu Jul 30 2020 Michael Cronenworth <mike@cchtml.com> - 1.6.1240-1
- version update

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1069-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 24 2020 Michael Cronenworth <mike@cchtml.com> - 1.6.1069-1
- version update

* Wed Feb 05 2020 Michael Cronenworth <mike@cchtml.com> - 1.6.1026-1
- version update

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.992-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Michael Cronenworth <mike@cchtml.com> - 1.6.992-1
- version update

* Wed Oct 09 2019 Michael Cronenworth <mike@cchtml.com> - 1.6.935-1
- version update

* Sat Aug 31 2019 Michael Cronenworth <mike@cchtml.com> - 1.6.899-1
- Version update

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.20180625git1e36dcc.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.20180624git1e36dcc.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Michael Cronenworth <mike@cchtml.com> - 1.5.0-0.20180623git1e36dcc.0
- Update to 20180623 git checkout to fix FTBFS
- Drop patches that revert BARRIER_OPERATOR support and use newer version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.20171212gitc3b0e31.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Michael Cronenworth <mike@cchtml.com> - 1.5.0-0.20171211gitc3b0e31.0
- Update to 20171211 git checkout
- Revert new BARRIER_OPERATOR support and use older version

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.20170725gitde1c0e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Michael Cronenworth <mike@cchtml.com> - 1.5.0-0.20170724gitde1c0e6
- Update to a git checkout, execeptions patch is upstream
- Fixes crashing issues with domoticz

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.164-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Michael Cronenworth <mike@cchtml.com> - 1.4.164-1
- Initial spec
