Name:           zzuf
Version:        0.15
Release:        24%{?dist}
Summary:        Transparent application input fuzzer

License:        WTFPL
URL:            http://sam.zoy.org/zzuf/
Source0:        http://github.com/zzuf/%{name}/archive/zzuf-%{version}.tar.gz
#Source0:	http://ftp.debian.org/debian/pool/main/z/zzuf/zzuf_0.13.svn20100215.orig.tar.gz
Patch0:         %{name}-0.13-optflags.patch
# AC_TRY_CFLAGS doesn't honor CFLAGS
# Causes package to produce broken configure results
Patch1:         %{name}-0.13-Remove-AC_TRY_CFLAGS.patch
Patch2:		zzuf-0.15-glibc.patch
Patch3: zzuf-zzat-c99.patch

BuildRequires: make
BuildRequires:  gcc autoconf automake libtool
%description
zzuf is a transparent application input fuzzer.  It works by
intercepting file operations and changing random bits in the program's
input.  zzuf's behaviour is deterministic, making it easy to reproduce
bugs.


%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p0
%patch -P3 -p1
touch -r aclocal.m4 configure.*


%build
autoreconf -if
%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/zzuf/libzzuf.la



%files
%doc AUTHORS TODO doc/
%license COPYING
%{_bindir}/zzuf
%{_bindir}/zzat
%dir %{_libdir}/zzuf/
%{_libdir}/zzuf/libzzuf.so
%{_mandir}/man1/zzuf.1*
%{_mandir}/man1/zzat.1*
%{_mandir}/man3/libzzuf.3*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.15-20
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 11 2022 Florian Weimer <fweimer@redhat.com> - 0.15-18
- Port to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.15-9
- Patch out internal glibc call.

* Wed Aug 01 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.15-8
- Rebuild to potentially fix FTBFS in other packages.

* Tue Jul 31 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.15-7
- Rebuild to potentially fix FTBFS in other packages.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 Jon Ciesla <limburgher@gmail.com> - 0.15-1
- 0.15

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-12.20100215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 12 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.13-11.20100215
- Comment out AC_TRY_CFLAGS from configure.ac.
  Add zzuf-0.13-Remove-AC_TRY_CFLAGS.patch.
  (Address F23FTBFS, RHBZ#1240099).
- Remove zzuf-0.9-open.patch (Unused).
- Modernize spec.
- Add %%license.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-10.20100215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-9.20100215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-8.20100215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-7.20100215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6.20100215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5.20100215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Jon Ciesla <limburgher@gmail.com> - 0.13-4.20100215
- Update to svn snapshot to fix BZ 641024, zzcat is now zzat.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 01 2010 Jon Ciesla <limb@jcomserv.net> - 0.13-1
- 0.13.
- Updated optflags patch, dropped open patch.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 14 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.12-1
- 0.12.

* Thu May 22 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.11-1
- 0.11.

* Tue Feb 12 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.10-2
- Rebuild.

* Sat Nov  3 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.10-1
- 0.10.

* Sun Aug 19 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.9-2
- Fix build with glibc >= 2.6.90 and -D_FORTIFY_SOURCE=2, thanks to
  Jan Kratochvil.

* Tue Jul 10 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.9-1
- 0.9.

* Sat Apr  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.8.1-1
- First Fedora build.

* Thu Apr  5 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.8.1-0.1
- First build.
