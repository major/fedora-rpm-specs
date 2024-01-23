%?mingw_package_header

Name:           mingw-p11-kit
Version:        0.23.16.1
Release:        13%{?dist}
Summary:        MinGW Library for loading and sharing PKCS#11 modules

License:        BSD
URL:            http://p11-glue.freedesktop.org/p11-kit.html
Source0:        https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.gz

Patch0:         mingw-p11-kit-uid-check.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libffi
BuildRequires:  mingw32-libtasn1

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-libffi
BuildRequires:  mingw64-libtasn1

BuildRequires:  libtool

# Yes, really ...
BuildRequires:  pkgconfig

# For native /usr/bin/msgfmt etc.
BuildRequires:  gettext
# For native GTK HTML documentation
BuildRequires:  gtk-doc


%description
p11-kit provides a way to load and enumerate PKCS#11 modules, as well as
a standard configuration setup for installing PKCS#11 modules in such a
way that they're discoverable.  This library is cross-compiled for MinGW.


%package -n mingw32-p11-kit
Summary:        MinGW Library for loading and sharing PKCS#11 modules
Requires:       pkgconfig

%description -n mingw32-p11-kit
p11-kit provides a way to load and enumerate PKCS#11 modules, as well as
a standard configuration setup for installing PKCS#11 modules in such a
way that they're discoverable.  This library is cross-compiled for MinGW.

%package -n mingw64-p11-kit
Summary:        MinGW Library for loading and sharing PKCS#11 modules
Requires:       pkgconfig

%description -n mingw64-p11-kit
p11-kit provides a way to load and enumerate PKCS#11 modules, as well as
a standard configuration setup for installing PKCS#11 modules in such a
way that they're discoverable.  This library is cross-compiled for MinGW.


%?mingw_debug_package


%prep
%setup -q -n p11-kit-%{version}
%patch0 -p1 -b.uid


%build
%mingw_configure --disable-static --disable-silent-rules --disable-nls
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{mingw32_datadir}/info/dir
rm -f $RPM_BUILD_ROOT%{mingw64_datadir}/info/dir

# Remove .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Remove gtk-doc pages which duplicate stuff in Fedora already.
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc


%files -n mingw32-p11-kit
%{!?_licensedir:%global license %%doc}
%license COPYING
%{mingw32_bindir}/libp11-kit-0.dll
%{mingw32_bindir}/p11-kit.exe
%{mingw32_bindir}/trust.exe
%{mingw32_libdir}/libp11-kit.dll.a
%dir %{mingw32_libdir}/pkcs11/
%{mingw32_libdir}/pkcs11/p11-kit-trust.dll
%{mingw32_libdir}/pkcs11/p11-kit-trust.dll.a
%{mingw32_libdir}/pkgconfig/p11-kit-1.pc
%dir %{mingw32_libexecdir}/p11-kit/
%{mingw32_libexecdir}/p11-kit/*.exe
%{mingw32_libexecdir}/p11-kit/trust-extract-compat
%{mingw32_includedir}/p11-kit-1/
%{mingw32_datadir}/p11-kit/
%{mingw32_sysconfdir}/pkcs11/

%files -n mingw64-p11-kit
%{!?_licensedir:%global license %%doc}
%license COPYING
%{mingw64_bindir}/libp11-kit-0.dll
%{mingw64_bindir}/p11-kit.exe
%{mingw64_bindir}/trust.exe
%{mingw64_libdir}/libp11-kit.dll.a
%dir %{mingw64_libdir}/pkcs11/
%{mingw64_libdir}/pkcs11/p11-kit-trust.dll
%{mingw64_libdir}/pkcs11/p11-kit-trust.dll.a
%{mingw64_libdir}/pkgconfig/p11-kit-1.pc
%dir %{mingw64_libexecdir}/p11-kit/
%{mingw64_libexecdir}/p11-kit/*.exe
%{mingw64_libexecdir}/p11-kit/trust-extract-compat
%{mingw64_includedir}/p11-kit-1/
%{mingw64_datadir}/p11-kit/
%{mingw64_sysconfdir}/pkcs11/


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.16.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.16.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.16.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.16.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.23.16.1-9
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.16.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 30 2021 Sandro Mani <manisandro@gmail.com> - 0.23.16.1-7
- Rebuild (libffi)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.23.16.1-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Aug 20 2019 Michael Cronenworth <mike@cchtml.com> - 0.23.16.1-1
- New upstream release.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 0.23.7-3
- Fix debug files in main package

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Michael Cronenworth <mike@cchtml.com> - 0.23.7-1
- New upstream release.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 02 2016 Michael Cronenworth <mike@cchtml.com> - 0.23.2-1
- New upstream release.

* Wed Nov 25 2015 Michael Cronenworth <mike@cchtml.com> - 0.23.1-3
- Stop linking against iconv/libintl (RHBZ#1284815)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Michael Cronenworth <mike@cchtml.com> - 0.23.1-1
- New upstream release.

* Mon Oct 27 2014 Michael Cronenworth <mike@cchtml.com> - 0.22.1-1
- New upstream release.

* Sat Oct 04 2014 Michael Cronenworth <mike@cchtml.com> - 0.22.0-1
- New upstream release.

* Sun Aug 17 2014 Michael Cronenworth <mike@cchtml.com> - 0.21.1-1
- New upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 13 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.20.2-3
- Don't carry .debug files in main packages

* Sun Mar 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.20.2-2
- Rebuild against latest mingw-crt to fix Windows XP compatibility issue

* Mon Jan 27 2014 Michael Cronenworth <mike@cchtml.com> - 0.20.2-1
- New upstream release.

* Sun Sep 22 2013 Michael Cronenworth <mike@cchtml.com> - 0.20.1-1
- New upstream release.

* Mon Jul 29 2013 Michael Cronenworth <mike@cchtml.com> - 0.19.3-1
- New upstream release.

* Mon Jul 08 2013 Michael Cronenworth <mike@cchtml.com> - 0.18.4-1
- New upstream release.

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.2-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Wed May 29 2013 Michael Cronenworth <mike@cchtml.com> - 0.18.2-1
- New upstream release.

* Thu May 09 2013 Michael Cronenworth <mike@cchtml.com> - 0.18.1-1
- New upstream release.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Michael Cronenworth <mike@cchtml.com> - 0.14-1
- New upstream release.

* Sun Aug 05 2012 Michael Cronenworth <mike@cchtml.com> - 0.13-1
- New upstream release.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Michael Cronenworth <mike@cchtml.com> - 0.12-1
- New upstream release.

* Sat Mar 10 2012 Michael Cronenworth <mike@cchtml.com> - 0.10-4
- Update spec to build 64-bit package.

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 0.10-3
- Remove .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10-2
- Rebuild against the mingw-w64 toolchain

* Sun Jan 08 2012 Michael Cronenworth <mike@cchtml.com> - 0.10-1
- New upstream release (includes w64 patch)

* Wed Nov 16 2011 Michael Cronenworth <mike@cchtml.com> - 0.9-4
- Include w64 patch.
- Match release number of cross repo.

* Wed Nov 16 2011 Michael Cronenworth <mike@cchtml.com> - 0.9-1
- Initial RPM release.

