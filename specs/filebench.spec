Name:           filebench
Version:        1.4.9.1
Release:        26%{?dist}
Summary:        A model based file system workload generator

License:        CDDL-1.1
URL:            http://filebench.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        LICENSE
Source2:        filebench.1
Patch0:         make-dofile-global.patch
Patch1:         filebench-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires: make

%description
Filebench is a file system and storage benchmark that allows to generate a
high variety of workloads. It employs extensive Workload Model Language (WML)
for detailed workload specification.


%prep
%setup -q
%patch -P0 -p1 -b .dofile
%patch -P1 -p1 -b .c99
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .


%build
%configure
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1


%files
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Florian Weimer <fweimer@redhat.com> - 1.4.9.1-19
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Hushan Jia <hushan.jia@gmail.com> 1.4.9.1-1
- Update to upstream 1.4.9.1 which have several bug fixes and enhancements
- remove arch definitions, the syscalls are now detected during configuring

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.9-11
- Fix FTBFS on ARM (RHBZ 923468)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 7 2011 Dan Horák <dan[at]danny.cz> 1.4.9-7
- fix build on secondary arches

* Fri Sep 9 2011 Hushan Jia <hushan.jia@gmail.com> 1.4.9-6
- make dofile global
- add bison to BR

* Sun Sep 4 2011 Hushan Jia <hushan.jia@gmail.com> 1.4.9-5
- fix build error on ppc64 arch

* Sat Sep 3 2011 Hushan Jia <hushan.jia@gmail.com> 1.4.9-4
- use RPM_BUILD_ROOT macro for consistency

* Sat Sep 3 2011 Hushan Jia <hushan.jia@gmail.com> 1.4.9-3
- use UTF-8 encoded LICENSE
- add man page

* Wed Aug 31 2011 Hushan Jia <hushan.jia@gmail.com> 1.4.9-2
- remove defattr tag, dont ship INSTALL
- convert LICENSE to UTF-8 encoding

* Thu Aug 25 2011 Hushan Jia <hushan.jia@gmail.com> 1.4.9-1
- FSL port became mainline, update to latest 1.4.9 version

* Sun Apr 10 2011 Hushan Jia <hjia@redhat.com> 0.8-1
- initial package
