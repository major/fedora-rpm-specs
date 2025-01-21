Name:			xsp
Version:	4.7.1
Release:	12%{?dist}
License:	MIT
URL:			http://www.mono-project.com/Main_Page
Summary:	A small web server that hosts ASP.NET

Source0:	http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:	mono-web-devel, mono-data, mono-devel, mono-data-sqlite, mono-nunit-devel
BuildRequires:	mono-data-oracle monodoc-devel
BuildRequires:	autoconf automake libtool
Requires:	mono-core
# Mono only available on these:
ExclusiveArch: %mono_arches

%define debug_package %{nil}

%description

XSP is a standalone web server written in C# that can be used to run ASP.NET 
applications as well as a set of pages, controls and web services that you can 
use to experience ASP.NET.

%package devel
Requires: %{name} = %{version}-%{release} pkgconfig
Summary: Development files for xsp

%description devel
Development files for xsp

%package tests
Requires: %{name} = %{version}-%{release}
Summary: xsp test files

%description tests
Files for testing the xsp server

%prep
%setup -q

sed -i "s#dmcs#mcs#g" configure

%build
%configure --libdir=%{_prefix}/lib --disable-docs
make

%install
make DESTDIR=%{buildroot} install

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT/%{_prefix}/lib/pkgconfig/* $RPM_BUILD_ROOT/%{_libdir}/pkgconfig

# Remove libtool archives and static libs
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete

# Remove scripts that are referencing .NET 2.0
for f in asp-state dbsessmgr mod-mono-server fastcgi-mono-server xsp
do
  rm %{buildroot}/%{_bindir}/${f}
  rm %{buildroot}/%{_bindir}/${f}2
done

# Remove monodoc sources
rm -Rf "%{buildroot}/usr/lib/monodoc/sources"

%files
%doc NEWS README COPYING
%{_bindir}/asp-state4
%{_bindir}/dbsessmgr4
%{_bindir}/mod-mono-server4
%{_bindir}/mono-fpm
%{_bindir}/shim
%{_bindir}/xsp4
%{_bindir}/fastcgi-mono-server4
%{_prefix}/lib/xsp
%{_monogacdir}/Mono.WebServer*/
%{_monogacdir}/fastcgi-mono-server4
%{_monogacdir}/mod-mono-server*/
%{_monogacdir}/mono-fpm
%{_monogacdir}/xsp*/
%{_monodir}/4.?/Mono.WebServer2.dll
%{_monodir}/4.?/fastcgi-mono-server4.exe
%{_monodir}/4.?/mod-mono-server4.exe
%{_monodir}/4.?/mono-fpm.exe
%{_monodir}/4.?/xsp4.exe
%{_prefix}/lib/libfpm_helper.so.0*
%{_mandir}/man1/asp*
%{_mandir}/man1/dbsessmgr*
%{_mandir}/man1/mod-mono-server*
%{_mandir}/man1/xsp*
%{_mandir}/man1/fastcgi-mono-server*

%files devel
%{_libdir}/pkgconfig/xsp*
%{_prefix}/lib/libfpm_helper.so

%files tests
%{_prefix}/lib/xsp/test

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 19 2022 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.7.1-5
- remove unpackaged files for monodoc sources

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.7.1-0
- Upgrade to new version 4.7.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.5-5
- built without docs because mdoc.exe is not built with Mono 6 and mcs anymore

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 4.5-1
- Updated to 4.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-3
- mono rebuild for aarch64 support

* Thu Sep 29 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.2-2
- drop scripts that rever to .NET 2.0 binaries which we don't compile and ship anymore

* Fri Jan 29 2016 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 4.2-1
- Updated to 4.2
- Use mono macros
- Use mcs instead dmcs

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3.8-1
- Update to 3.8
- Rebuild (mono4)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 12 2011 Christian Krause <chkr@fedoraproject.org> - 2.10.2-2
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Wed Apr 27 2011 Christian Krause <chkr@fedoraproject.org> - 2.10.2-1
- Update to 2.10.2

* Wed Mar 30 2011 Christian Krause <chkr@fedoraproject.org> - 2.10-1
- Update to 2.10
- Minor spec file cleanups
- Moved mono-4.0 parts into main package

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Dan Horák <dan[at]danny.cz> - 2.8.1-2
- updated the supported arch list

* Tue Dec 07 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.8.1-1
- Bump to bugfix 2.8.1 release

* Sat Oct 09 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.8-1
- Bump to 2.8
- Remove 1.0 targets
- Add xsp-4.0 subpackage

* Wed Jul 14 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.6.5-1
- Bump to 2.6.7 pre-release
- Alter BR to require mono-2.6.7

* Mon Jun 21 2010 Christian Krause <chkr@fedoraproject.org> - 2.6.4-2
- Spec file fixes

* Tue Apr 27 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.6.4-1
- Bump to 2.6.4 release
- Spec file fixes

* Fri Mar 19 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.6.3-1
- Bump to 2.6.3 release

* Tue Dec 22 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.6-2
- Bump to release version

* Sat Oct 03 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.6-1
- Bump to 2.6 preview 1

* Tue Jun 09 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4.2-1
- Update to 2.4.2 preview
- Enable ppc64

* Mon Apr 13 2009 Jesse Keating <jkeating@redhat.com> - 2.4-8
- Re-enable ppc
- Fix release numbering

* Mon Apr 06 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-7.1
- Remove ppc build

* Thu Mar 26 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-7
- Full 2.4 release

* Wed Mar 18 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-6.RC3
- bump to RC3

* Thu Mar 12 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-5.RC2
- bump to RC2

* Fri Feb 27 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-4.RC1
- bump to RC1

* Thu Feb 05 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-3.pre2.20090502svn124651
- update from svn
- rename to pre2
- fix svn version number for package

* Fri Jan 09 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-1.20099124svn124360
- update from svn to use 2.4 branch
- altered BRs and Rs to use mono-2.4

* Fri Jan 09 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-7.RC2.20090901svn122761
- rename to RC2
- update from svn

* Wed Dec 24 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-6.RC1.20081224svn122055
- x86_64 libdir fix

* Wed Dec 24 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-5.RC1.20081224svn122055
- Added additional BRs

* Wed Dec 24 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-4.RC1.20081224svn122055
- Bump to RC1 branched svn
- Minor specfile changes

* Wed Dec 17 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-3.pre3.20081217svn121604
- bump to 2.2 preview 3
- move to svn for bug fixes

* Sat Dec 06 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-2.pre2
- bump to 2.2 preview 2
- use sed instead of patches

* Tue Nov 25 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-1.pre1
- bump to 2.2 preview 1

* Fri Oct 03 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-4
- bump to RC 4

* Mon Sep 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-3
- bump to RC 3

* Tue Sep 09 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-2
- bump to 2.0 RC 1

* Sun Aug 03 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-1
- bump to 2.0 preview 1
- spec file fixes
