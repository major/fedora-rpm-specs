Name:           CQRlib
Version:        1.1.2
Release:        33%{?dist}
Summary:        ANSI C API for quaternion arithmetic and rotation

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://cqrlib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/cqrlib/cqrlib/CQRlib-%{version}/CQRlib-%{version}.tar.gz
# to fix /-dynamic/-rdynamic/ issue, reported to upstream
Patch0:         CQRlib-1.0.6-dynamic.patch
# to fix tag issue
Patch1:         CQRlib-1.1.2-tag.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires: make

%description
CQRlib is an ANSI C implementation of a utility library for quaternion
arithmetic and quaternion rotation math.

%package devel
Summary:        Development tools for compiling programs using CQRlib
Requires:       %{name} = %{version}-%{release}

%description devel
The CQRlib-devel package includes the header and library files for
developing applications that use CQRlib.

%prep
%setup -q

%patch -P0 -p1 -b .dynamic
%patch -P1 -p1 -b .tag
%if "%{_lib}" == "lib64"
sed -i -e 's,$(INSTALLDIR)/lib,$(INSTALLDIR)/lib64,' -e 's,$(ROOT)/lib,$(ROOT)/lib64,' Makefile
%endif

%build
make all CFLAGS="%{optflags}" %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install CFLAGS="%{optflags}" INSTALLDIR="%{buildroot}%{_prefix}"

# remove .la and .a files
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%check
make tests

%ldconfig_scriptlets

%files
%doc README_CQRlib.html README_CQRlib.txt lgpl.txt
%{_libdir}/libCQRlib.so.*

%files devel
%{_includedir}/cqrlib.h
%{_libdir}/libCQRlib.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.2-32
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 1.1.2-20
- Fix string quoting for rpm >= 4.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Dmitrij S. kryzhevich <kryzhev@ispms.ru> - 1.1.2-16
- Fix libtool tag.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1.2-1
- update to 1.1.2

* Mon Oct 18 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1.1-2
- use "make all" instead of "make"
- add %%check

* Thu Oct 14  2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1.1-1
- initial import (#545045).

* Tue Oct 12 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1.1-0.1
- use %%{_lib} detection to fix W: %%ifarch-applied-patch

* Thu Sep 30 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1.1-0
- update to 1.1.1

* Fri Sep 10 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1-0
- update to 1.1

* Mon Aug 30 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.6-1
- update to 1.0.6
- provide 64 bit libdir fix as a patch
- provide s/dynamic/rsynamic/g as a patch

* Thu May  6 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.5-1
- update to 1.0.5

* Wed Dec  9 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-3.20090805
- remove static library

* Tue Dec  8 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-2.20090805
- fit to Fedora Packaging Guidelines
- apply changes pointed at rhbz #545045 comment #1

* Tue Aug 25 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-1.20090805
- update to 1.0.3-5Aug09

* Wed Jul 29 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-1
- initial build
