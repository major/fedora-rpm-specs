Name:		fcode-utils
Version:	1.0.2
Release:	27.svn1354%{?dist}
Summary:	Utilities for dealing with FCode
# The entire source code is GPLv2 except localvalues/ and documentation/ which are CPL-licensed
License:	GPLv2 and CPL
URL:		http://www.openfirmware.info/FCODE_suite
## svn co http://code.coreboot.org/svn/openbios/trunk/fcode-utils-devel@1354 fcode-utils-1.0.2
## tar --exclude-vcs -cvJf fcode-utils-1.0.2.tar.xz fcode-utils-1.0.2/
Source0:	%{name}-%{version}.tar.xz
# Fedora-specific patch
Patch1:		fcode-utils-0001-Allow-overriding-some-more-Makefile-variables.patch
# For tests only
BuildRequires:  gcc
BuildRequires:	tcsh
BuildRequires: make


%description
Utilities for dealing with FCode, a Forth programming language dialect
compliant with ANS Forth.


%prep
%setup -q
%patch1 -p1 -b .more_overrides
install -p -m 0644 detok/README README.detok
install -p -m 0644 toke/README README.toke


%build
CFLAGS="%{optflags}" STRIP="/bin/true" make %{?_smp_mflags}


%install
make DESTDIR="%{buildroot}/usr" install
# Install data-files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a localvalues $RPM_BUILD_ROOT%{_datadir}/%{name}


%check
make tests


%files
%license COPYING
%doc README README.detok README.toke documentation
%{_bindir}/detok
%{_bindir}/romheaders
%{_bindir}/toke
%{_datadir}/%{name}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-27.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-26.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-25.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-24.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-23.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-22.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-21.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-19.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-18.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14.svn1354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Peter Lemenkov <lemenkov@gmail.com> 1.0.2-13.svn1354
- Update to the latest svn trunk
- Remove merged patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Peter Lemenkov <lemenkov@gmail.com> 1.0.2-3
- Added comment about licensing

* Sat Feb 28 2009 Peter Lemenkov <lemenkov@gmail.com> 1.0.2-2
- Added localvalues (and added license CPL to spec header)
- Added patch from Debian

* Sat Feb 28 2009 Peter Lemenkov <lemenkov@gmail.com> 1.0.2-1
- Initial build
