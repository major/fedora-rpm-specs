# This package is part of the Free Electronic Lab.

Name:           mot-adms
Version:        2.3.7
Release:        13%{?dist}
Summary:        An electrical compact device models converter

# SPDX confirmed
License:        GPL-3.0-or-later
URL:            https://github.com/Qucs/ADMS

Source0:        https://github.com/Qucs/ADMS/archive/release-%{version}/adms-%{version}.tar.gz
# Fix for C23 strict prototype
# FIXME this patch actually matches what current mot-adms is doing even with C17,
# however I don't know if this behavior is what upstream intends (mtasaka)
Patch0:         adms-2.3.7-c23-func-prototype.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  flex bison
BuildRequires:  perl(XML::LibXML)
BuildRequires:  automake autoconf
BuildRequires:  libtool
BuildRequires:  git

%description
ADMS is a code generator that converts electrical compact
device models specified in high-level description language
into ready-to-compile C code for the API of spice simulators.
Based on transformations specified in XML language, ADMS
transforms Verilog-AMS code into other target languages.

%prep
%setup -q -n ADMS-release-%{version}
%patch -P0 -p1 -b .c23

%build
autoreconf -vif
%configure --enable-maintainer-mode --disable-silent-rules

make clean
make -C admsXml \
	admstpathYacc.h \
	preprocessorYacc.h \
	verilogaYacc.y \
	%{nil}
# Disabling parallel make
make -j1

%install
make INSTALL="%{_bindir}/install -p" install DESTDIR=%{buildroot}

# Remove libtool archives and static libs
find %{buildroot} -type f '(' -name '*.la' -or -name '*.a' ')' -delete
# For now, remove these .so files
find %{buildroot} -type l -name '*.so' -delete


%files
%license COPYING
%doc AUTHORS
%doc ChangeLog
%doc README.md
%doc TODO

%{_bindir}/admsCheck
%{_bindir}/admsXml

%{_libdir}/libadms*.so.*
%dir %{_includedir}/adms
%{_includedir}/adms/*.vams

%{_mandir}/man1/admsCheck.1*
%{_mandir}/man1/admsXml.1*

%changelog
* Sat Jan 18 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.7-13
- Support C23 strict prototype

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.7-8
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  8 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.7-1
- 2.3.7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May  5 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.6-1
- 2.3.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.4-10
- Make "make" process more reliable (first make clean then re-generate files)
- Disable parallel make due to above
- Fix for gcc10 -fno-common

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.3.4-1
- Update to 2.3.4
- ship admsCheck binary
- upstream decided to kill shared libraries in 2.3.3 release
- license tag for COPYING
- enabled parallel make
- removed post(run) ldconfig calls

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.2-2
- Remove libtool archive files

* Sun Jul 20 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.2-1
- Update to 2.3.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-7.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-6.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-5.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-4.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-3.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-2.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> - 2.2.9-1.svn1186
- Setup for ngspice and qucs support

* Sun Feb 22 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.2.9-1
- New package
