Name:		sigscheme
Version:	0.9.1
Release:	12%{?dist}
License:	BSD-3-Clause
URL:		https://github.com/uim/sigscheme
BuildRequires: make
BuildRequires:	libgcroots-devel
BuildRequires:	gcc

Source0:	https://github.com/uim/sigscheme/releases/download/%{version}/%{name}-%{version}.tar.bz2
Patch1:		%{name}-vararg-func.patch


Summary:	R5RS Scheme interpreter for embedded use

%description
sigscheme is a R5RS Scheme interpreter that features small footprint,
low memory consumption, multibytes characters handling and more.

%package devel
Summary:	Development files for sigscheme
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
sigscheme is a R5RS Scheme interpreter that features small footprint,
low memory consumption, multibytes characters handling and more.

This package contains header files and development library.

%prep
%autosetup -p1

%build
%configure --disable-static --with-libgcroots=installed
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

# Remove unnecessary files
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}/sigscheme

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS QALog README RELNOTE TODO
%doc doc/*.html doc/*.txt
%{_bindir}/sscm
%{_libdir}/libsscm.so.3*
%{_datadir}/sigscheme

%files devel
%license COPYING
%doc AUTHORS NEWS QALog README RELNOTE TODO
%{_includedir}/sigscheme
%{_libdir}/libsscm.so
%{_libdir}/pkgconfig/sigscheme.pc

%changelog
* Mon Jan 27 2025 Akira TAGOH <tagoh@redhat.com> - 0.9.1-12
- Fix FTBFS.
  Resolves: rhbz#2341349

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec  5 2022 Akira TAGOH <tagoh@redhat.com> - 0.9.1-6
- Convert License tag to SPDX.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Akira TAGOH <tagoh@redhat.com> - 0.9.1-1
- New upstream release.
  Resolves: rhbz#1872256

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Akira TAGOH <tagoh@redhat.com> - 0.9.0-1
- New upstream release. (#1667853)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Akira TAGOH <tagoh@redhat.com> - 0.8.5-16
- Add BR: gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Akira TAGOH <tagoh@redhat.com> - 0.8.5-6
- Rebuilt for aarch64 support (#926527)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  8 2010 Akira TAGOH <tagoh@redhat.com> - 0.8.5-1
- New upstream release.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May  7 2008 Akira TAGOH <tagoh@redhat.com> - 0.8.3-1
- New upstream release.

* Wed Mar  5 2008 Akira TAGOH <tagoh@redhat.com> - 0.7.6-2
- Get rid of the explicit dependency of ldconfig. (#436059)
- Fix the timestamp issue.

* Wed Mar  5 2008 Akira TAGOH <tagoh@redhat.com> - 0.7.6-1
- Initial packaging.

