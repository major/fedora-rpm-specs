#global pre pre2

Name:           yapet
Version:        2.6
Release:        6%{?pre}%{?dist}
Summary:        Yet Another Password Encryption Tool
# Automatically converted from old format: GPLv3+ with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv3+-with-exceptions
URL:            http://yapet.guengel.ch/
Source0:        http://yapet.guengel.ch/downloads/%{name}-%{version}%{?pre}.tar.xz
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  cppunit-devel
BuildRequires:  libargon2-devel

%if 0%{?rhel} == 7
BuildRequires:  devtoolset-7-gcc-c++
%endif

%description
YAPET is a text based password manager using the AES-256 encryption
algorithm to store passwords and associated information encrypted on
disk. Its primary aim is to provide a safe way to store passwords in a
file on disk while having a small footprint, and compiling and running
under today's most popular Unix Systems.

The password records are protected by a master password which is used
to encrypt and decrypt the password records.

%prep
%setup -qn %{name}-%{version}%{?pre}

%build
%if 0%{?rhel} == 7
source /opt/rh/devtoolset-7/enable
%endif

%configure --disable-install-doc   \
           --disable-source-doc    \
           --disable-install-doci  \
           --disable-silent-rules

%make_build

%install
%make_install
# Console running is OK.
rm -frv %{buildroot}%{_datadir}/applications/

# %%doc instead.
rm -frv %{buildroot}%{_docdir}

%find_lang %{name}
%find_lang libyacurs

%check
# RNG tests need /dev/urandom OR /dev/random!
# Failed at messagebox1. Digging.
#make check

%files -f %{name}.lang -f libyacurs.lang
%doc AUTHORS BUGS NEWS README
%license COPYING LICENSE
%{_bindir}/*yapet*
%{_mandir}/man*/*yapet*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Greg Bailey <gbailey@lxpro.com> - 2.6-1
- Update to 2.6
- Remove unnecessary patch

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.3-9
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 2.3-4
- Fix mising #includes for gcc-10

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Remi Collet <remi@fedoraproject.org> - 2.3-2
- rebuild for libargon2 new soname

* Sun Mar  3 2019 Greg Bailey <gbailey@lxpro.com> - 2.3-1
- Update to 2.3 (#1678913)
- Use devtoolset for EPEL 7 builds (needs C++14 language features)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Greg Bailey <gbailey@lxpro.com> - 1.1-2
- No longer any need to rebuild configure script

* Wed Mar 28 2018 Greg Bailey <gbailey@lxpro.com> - 1.1-1
- Update to 1.1
- Update URL
- Remove unnecessary patches

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  1 2017 Greg Bailey <gbailey@lxpro.com> - 1.0-9
- Patch to fix build issues with GCC 6 and OpenSSL 1.1 (#1424564)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 14 2016 Greg Bailey <gbailey@lxpro.com> - 1.0-7
- Patch GCC6 compilation error from void function returning a value (#1308262)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Christopher Meng <rpm@cicku.me> - 1.0-1
- Update to 1.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.6.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.5.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.4.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.3.pre2
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.2.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 15 2011 Simon Wesp <cassmdodiah@fedoraproject.org> - 0.8-0.1.pre2
- Update

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 14 2010 Simon Wesp <cassmdodiah@fedoraproject.org> - 0.7-1
- New upstream release

* Mon Oct 12 2009 Simon Wesp <cassmdodiah@fedoraproject.org> - 0.6-2
- Correct License and patch integration
- Add LICENSE to DOC

* Mon Oct 12 2009 Simon Wesp <cassmdodiah@fedoraproject.org> - 0.6-1
- Initial Package build
