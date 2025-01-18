Name:		dt
Version:	21.27.git8d78d78
Release:	15%{?dist}
Summary:	Generic data test program
License:	MIT
URL:		https://github.com/RobinTMiller/dt
BuildRequires:  gcc, libuuid-devel
BuildRequires: make
# Generated from new official github repo
# https://github.com/RobinTMiller/dt by command:
# git archive --format=tar.xz --prefix=dt.v21.27.git8d78d78/ 8d78d78 > dt-source-v21.27.git8d78d78.tar.xz
Source0: dt-source-v%{version}.tar.xz
Patch0: dt-manpage.patch

%description
dt is a generic data test program used to verify proper operation of
peripherals, file systems, device drivers, or any data stream supported by the
operating system. In its' simplest mode of operation, dt writes and then
verifies its' default data pattern, then displays performance statistics and
other test parameters before exiting. Since verification of data is performed,
dt can be thought of as a generic diagnostic tool.

dt command lines are similar to the dd program, which is popular on most UNIX
systems. It contains numerous options to give the user control of various test
parameters.

dt has been used to successfully test disks, tapes, serial lines, parallel
lines, pipes, and memory mapped files. In fact, dt can be used for any device
that allows the standard open, read, write, and close system calls. Special
support is necessary for some devices, such as serial lines, for setting up the
speed, parity, data bits, etc.

Available documentation is located in %{_defaultdocdir}/%{name}. Sample
scripts and config data are installed in %{_datadir}/%{name}.

%global __requires_exclude_from ^%{_datadir}/%{name}/.*$
%prep
%setup -q -n dt.v%{version}
%patch -P0 -p1

%build
mkdir tmp
cd tmp
make %{?_smp_mflags} CFLAGS="%{optflags} -I.. -DAIO -DMMAP -D__linux__ -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -DSCSI" -f ../Makefile.linux VPATH=.. OS=linux

%install
install -d -m755 $RPM_BUILD_ROOT%{_sbindir}
install -d -m755 $RPM_BUILD_ROOT%{_mandir}/man8
install -d -m755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/html
install -m755 tmp/dt $RPM_BUILD_ROOT%{_sbindir}
install -m644 Documentation/dt.man $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8
install -m755 Scripts/dt? $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m644 data/pattern_* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m644 html/* $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/html

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc Documentation/dt-UsersGuide.txt Documentation/ReleaseNotes-dt*.txt html
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man8/%{name}.*.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 21.27.git8d78d78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Ondrej Kozina <okozina@redhat.com> - 21.27.git8d78d78-1
- Update to 21.27

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.32-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 18.32-9
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 18.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 19 2015 Ondrej Kozina <okozina@redhat.com> - 18.32-3
- mitigate annoying rpm dependancy on tcsh pulled by examples

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Ondrej Kozina <okozina@redhat.com> - 18.32-1
- Update to 18.32

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.66-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.66-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Ondrej Kozina <okozina@redhat.com> - 17.66-5
- fix possible security problem with malformed message format
- Resolves: #1037043

* Mon Aug 05 2013 Ondrej Kozina <okozina@redhat.com> - 17.66-4
- remove version suffix from all install directives related to documentation (reflects recent change in %%doc macro)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Ondrej Kozina <okozina@redhat.com> - 17.66-1
- Update to the lastest release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Ondrej Kozina <okozina@redhat.com> - 17.55-1
- Initial build
