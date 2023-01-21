Summary:        C library for analyzing BGP related dump files
Name:           libbgpdump
Version:        1.6.0
Release:        11%{?dist}
License:        MIT and GPLv2+
URL:            https://bitbucket.org/ripencc/bgpdump/wiki
Source:         https://ris.ripe.net/source/bgpdump/%{name}-%{version}.tgz
Patch0:         libbgpdump-1.6.0-buildsys.patch
Patch1:         libbgpdump-1.6.0-soname-versioning.patch
Patch2:         libbgpdump-1.6.0-ldshared.patch
BuildRequires:  gcc, make, zlib-devel, bzip2-devel

%description
Libbgpdump is a C library designed to help with analyzing BGP related
dump files in Zebra/Quagga or MRT RIB (Multi-Threaded Routing Toolkit
Routing Information Base) format, e.g. produced by Zebra/Quagga, BIRD,
OpenBGPD or PyRT.

%package devel
Summary:        Development files for the bgpdump library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The libbgpdump-devel package includes header files and libraries necessary
for developing programs which use the bgpdump C library.

%package -n bgpdump
Summary:        MRT file reader for handling BGP related data

%description -n bgpdump
Bgpdump translates (possibly compressed) binary MRT RIB dump files, e.g.
produced by Zebra/Quagga, BIRD, OpenBGPD or PyRT, into human readable
output. Publicly available MRT RIB dump files are e.g. supplied by the
RIPE NCC routing information service (RIPE RIS).

%prep
%setup -q
%patch0 -p1 -b .buildsys
%patch1 -p1 -b .soname-versioning
%patch2 -p1 -b .ldshared

%build
%configure
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.a

%ldconfig_scriptlets

%files
%license COPYING
%doc ChangeLog README
%{_libdir}/%{name}.so.0*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/bgpdump_attr.h
%{_includedir}/bgpdump_formats.h
%{_includedir}/bgpdump_lib.h
%{_includedir}/bgpdump_mstream.h

%files -n bgpdump
%{_bindir}/bgpdump

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 26 2020 Robert Scheck <robert@fedoraproject.org> 1.6.0-5
- Added patch to avoid -shared linking for bgpdump (#1818875)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Robert Scheck <robert@fedoraproject.org> 1.6.0-2
- Add corrections from package review (#1702017 #c1)

* Mon Apr 22 2019 Robert Scheck <robert@fedoraproject.org> 1.6.0-1
- Upgrade to 1.6.0 (#1702017)
- Initial spec file for Fedora and Red Hat Enterprise Linux
