%define         debug_package %{nil}

Name:           mono-zeroconf
Version:        0.9.0
Release:        40%{?dist}
Summary:        Mono.Zeroconf networking library
License:        MIT
URL:            http://banshee-project.org/files/mono-zeroconf
Source0:        %{name}-%{version}.tar.bz2
Patch0:		mono-zeroconf-0.9.0-use-system-ndesk-dbus.patch
# Combination of:
# https://github.com/mono/Mono.Zeroconf/commit/f71474ddfae108d500e1c72fba64c50be77822a5
# https://github.com/JvetS/Mono.Zeroconf/commit/7d4a254191e0494dd2ba3ebc008f7ff20b11fe97
Patch1:		mono-zeroconf-0.9.0-fix-host-byte-order-bug.patch
# https://github.com/mono/Mono.Zeroconf/commit/e6700384f850085b93b358118521c991f6c1ae31
Patch2:		mono-zeroconf-0.9.0-async-prefix.patch
# https://github.com/mono/Mono.Zeroconf/commit/72a9cd4329661d2d03fa6934690ab20270d8912b
Patch3:		mono-zeroconf-0.9.0-correct-service-type-for-DNSServiceQueryRecord.patch
# https://github.com/mono/Mono.Zeroconf/pull/12
Patch4:		mono-zeroconf-0.9.0-ipv6-fixes.patch
# https://github.com/mono/Mono.Zeroconf/pull/11
Patch5:		mono-zeroconf-0.9.0-fix-unreliable-browse-resolve.patch
# https://github.com/mono/Mono.Zeroconf/pull/6
Patch6:		mono-zeroconf-0.9.0-fix-recursive-dispose.patch
# https://github.com/mono/Mono.Zeroconf/pull/7
Patch7:		mono-zeroconf-0.9.0-name-collision-fix.patch
# https://github.com/mono/Mono.Zeroconf/pull/9
Patch8:		mono-zeroconf-0.9.0-utf8-service-names.patch
# https://github.com/mono/Mono.Zeroconf/pull/10
Patch9:		mono-zeroconf-0.9.0-set-host-target.patch
# Fix NDesk.DBus to be just DBus
Patch10:	mono-zeroconf-0.9.0-dbus-fix.patch
# Proper libnss_mdns
Patch11:	mono-zeroconf-0.9.0-proper-libnss_mdns.patch
BuildRequires: make
BuildRequires:  mono-devel monodoc-devel dbus-sharp-devel
Requires:       mono-core dbus-sharp nss-mdns

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Mono.Zeroconf is a cross platform Zero Configuration Networking library
for Mono and .NET.

%package devel
Summary: Development files for Mono.Zeroconf
Requires: %{name} = %{version}-%{release} pkgconfig monodoc

%description devel
Development files and documentation for Mono.Zeroconf

%prep
%setup -q
%patch -P0 -p1 -b .system-dbus
%patch -P1 -p1 -b .hostbyteordere
%patch -P2 -p1 -b .prefix
%patch -P3 -p1 -b .dnsfix
%patch -P4 -p1 -b .ipv6fix
%patch -P5 -p1 -b .unreliable
%patch -P6 -p1 -b .recursivedispose
%patch -P7 -p1 -b .namecollision
%patch -P8 -p1 -b .utf8
%patch -P9 -p1 -b .hosttarget
%patch -P10 -p1 -b .dbusfix
%patch -P11 -p1 -b .2017
sed -i "s#gmcs#mcs#g" configure
sed -i "s#2.0#4.5#g" configure

%build
%configure --libdir=%{_prefix}/lib --disable-docs
#parallel build doesn't work
make

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

%files 
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/mzclient
%{_prefix}/lib/mono-zeroconf/
%{_prefix}/lib/mono/gac/Mono.Zeroconf
%{_prefix}/lib/mono/mono-zeroconf
%{_prefix}/lib/mono/gac/policy.*

%files devel
%{_libdir}/pkgconfig/mono-zeroconf.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.9.0-29
- built without docs because mdoc.exe is not built with Mono 6 and mcs anymore

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Tom Callaway <spot@fedoraproject.org> - 0.9.0-27
- rebuild for proper provides

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Tom Callaway <spot@fedoraproject.org> - 0.9.0-20
- enable signal trapping again

* Wed Jul 12 2017 Tom Callaway <spot@fedoraproject.org> - 0.9.0-19
- stop using old/broken dbus bundle
- apply lots of fixes from upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-17
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.0-14
- Rebuild (mono4)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Brent Baude <baude@us.ibm.com> - 0.9.0-11
- Changing ppc64 to power64 macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Christian Krause <chkr@fedoraproject.org> - 0.9.0-6
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Fri Feb 25 2011 Dan Horák <dan[at]danny.cz> - 0.9.0-5
- updated the supported arch list

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 29 2009 Dennis Gilmore <dennis@ausil.us> - 0.9.0-3
- ExcludeArch sparc64

* Thu Oct 22 2009 Michel Salim <salimma@fedoraproject.org> - 0.9.0-2
- Make AvahiDbus the only provider for now

* Thu Oct 22 2009 Paul Lange <palango@gmx.de> - 0.9-1
- update to version 0.9
- move docs into devel package

* Thu Aug 20 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.6-10
- Rebuild for ppc64 packages due to obsolete of packageset last time.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.7.6-9
- Build arch ppc64.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.7.6-7
- add ppc

* Thu Dec 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-6
- Another fix for x86_64

* Thu Dec 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-5
- Remove patch file (use sed)
- Additional BRs and Rs

* Thu Dec 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-4
- remove ppc build for now

* Thu Dec 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-3
- rebuild (0.8.0 is buggy)

* Thu Aug 14 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-2
- bump to new version
- libdir clean now

* Tue Apr 07 2008 David Nielsen <gnomeuser@gmail.com> - 0.7.5-4
- Our CVS has odd bugs - pointless bump to make upgrade path work

* Mon Mar 31 2008 David Nielsen <gnomeuser@gmail.com> - 0.7.5-3
- Remove debuginfo

* Fri Feb 01 2008 David Nielsen <david@lovesunix.net> - 0.7.5-2
- Exclude ppc64
- Spec fixes

* Fri Feb 01 2008 David Nielsen <david@lovesunix.net> - 0.7.5-1
- bump to 0.7.5
- patch for libdir madness

* Fri Jan 04 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.3-2
- spec fixes

* Thu Dec 29 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.3-1
- Initial import for FE
