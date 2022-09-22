%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		libbsr
Version:	0.5
Release:	17%{?dist}
Summary:	Barrier Synchronization Register access library

License:	LGPLv2+
URL:		http://sourceforge.net/projects/libbsr/

Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar
Patch0:		libbsr-fedoraperms.patch
ExclusiveArch:	%{power64}
Requires(pre):	shadow-utils
BuildRequires:  gcc
BuildRequires: make

%description
This is a library to expose the functionality of the Barrier Synchronization
Register (BSR) on IBM POWER Systems in Linux. This facility helps speed up
synchronization across large SMP systems

%package devel
Summary:	Barrier Synchronization Register development files
Requires:	%{name} = %{version}-%{release}

%description devel
Development package for libbsr.

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_prefix}/%{_lib}/
mkdir -p %{buildroot}/%{_includedir}/
mkdir -p %{buildroot}/%{_pkgdocdir}/examples

make install	INSTALLROOT="%{buildroot}"	\
		DESTDIR="%{buildroot}"		\
		LIBDIR="%{_prefix}/%{_lib}"	\
		INCLUDEDIR="%{_includedir}"

cp -p test-bsr.c %{buildroot}/%{_pkgdocdir}/examples/.
mkdir -p %{buildroot}/var/lib/bsr

%pre
getent group bsr >/dev/null || groupadd -f bsr

%ldconfig_scriptlets libs

%files
%{!?_licensedir:%global license %%doc}
%license LGPL-2.1
%doc README
%{_bindir}/bsr_cleanup
%{_libdir}/libbsr.so.0
%{_libdir}/libbsr.so.%{version}

%files devel
%doc %{_pkgdocdir}/examples/
%{_includedir}/bsr.h
%{_libdir}/libbsr.so

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Tony Breeds <tony@bakeyournoodle.com> - 0.5-9
- Remove ldconfig in favor of %ldconfig_scriptlets

* Mon Jul 16 2018 Tony Breeds <tony@bakeyournoodle.com> - 0.5-8
- Add gcc into BuildRequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.5-2
- Use %%license
- Package cleanups

* Thu Oct 08 2015 Karsten Hopp <karsten@redhat.com> 0.5-1
- update to 0.5
- move group permission stuff from Makefile to spec file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 20 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.2-10
- Install docs to %%{_pkgdocdir} where available (#993955).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Tony Breeds <tony@bakeyournoodle.com> 0.2-2
- Incorporate more feedback from review.

* Thu Feb 12 2009 Tony Breeds <tony@bakeyournoodle.com> 0.2-1
- Use new upstream relase

* Thu Feb 12 2009 Tony Breeds <tony@bakeyournoodle.com> 0.1-3
- No longer list "examples" twice

* Wed Feb 11 2009 Tony Breeds <tony@bakeyournoodle.com> 0.1-2
- Fixes from package review

* Tue Feb 10 2009 Tony Breeds <tony@bakeyournoodle.com> 0.1-1
- Initial RPM package for Fedora
