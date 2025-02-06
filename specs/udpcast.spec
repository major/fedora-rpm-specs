Name:          udpcast
Summary:       UDP broadcast file distribution and installation
Version:       20211207
Release:       10%{?dist}
License:       GPL-2.0-or-later AND BSD-2-Clause-first-lines AND MPL-1.1
URL:           http://udpcast.linux.lu/
Source:        https://www.udpcast.linux.lu/download/%{name}-%{version}.tar.gz

# Fix console.c:89:7: warning: ignoring return value of 'read'
Patch1:        udpcast-20200328-read-warn.patch

# Fix hardcoded sbin dir
Patch2:        udpcast-20211207-makefile-in.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: m4
BuildRequires: perl-interpreter
BuildRequires: /usr/bin/pod2man


%description
Command-line client for UDP sender and receiver.  Udpcast is an
application for multicasting data to multiple targets.


%package devel
Summary:        Development headers for %{name}
Requires:       %{name} = %{version}-%{release}


%description devel
Command-line client for UDP sender and receiver.  Udpcast is an
application for multicasting data to multiple targets.


%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc Changelog.txt cmd.html COPYING
%{_sbindir}/udp-sender
%{_sbindir}/udp-receiver
%{_mandir}/man1/udp-sender.1*
%{_mandir}/man1/udp-receiver.1*


%files devel
%doc COPYING
%{_includedir}/udpcast/rateGovernor.h


%changelog
* Tue Feb 04 2025 Lukáš Zapletal <lzap+rpm@redhat.com> - 20211207-10
- Updated licenses
- Fedora sbin–>bin patch

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20211207-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 20211207-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20211207-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20211207-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20211207-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20211207-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20211207-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20211207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Richard W.M. Jones <rjones@redhat.com> - 20211207-1
- New upstream version 2021/12/07

* Wed Nov 24 2021 Doncho Gunchev <dgunchev@gmail.com> - 20200328-0
- New upstream version 20200328.
- Port/update the patches
- Use new macros like %%autosetup

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Richard W.M. Jones <rjones@redhat.com> - 20120424-15
- Remove buildroot.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20120424-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120424-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120424-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120424-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120424-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Ville Skytta <ville.skytta@iki.fi> - 20120424-5
- Sanitize CFLAGS and LDFLAGS (#914704).
- Move %%configure to %%build section, build with %%{_smp_mflags}.
- Fix bogus date in %%changelog.

* Wed Feb 20 2013 Richard W.M. Jones <rjones@redhat.com> - 20120424-4
- Add patch to try to fix build failure on Rawhide.
- +BR /usr/bin/pod2man.

* Mon Feb 18 2013 Richard W.M. Jones <rjones@redhat.com> - 20120424-1
- New upstream version 20120424.
- Modernize the spec file.
- Make a -devel package.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071228-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071228-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071228-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071228-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 Ville Skytta <ville.skytta@iki.fi> - 20071228-7
- Use bzipped upstream tarball.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071228-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071228-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun May  4 2008 Richard W.M. Jones <rjones@redhat.com> - 20071228-4
- Since using configure macro, don't need the other parameters.

* Fri May  2 2008 Richard W.M. Jones <rjones@redhat.com> - 20071228-3
- Remove '-s' flag from Makefile.
- Remove unused udpcast_version macro.
- Use configure macro.
- Fix the license, GPLv2+ and BSD.
- BuildRequires perl.

* Mon Apr 21 2008 Richard W.M. Jones <rjones@redhat.com> - 20071228-2
- BR m4.

* Mon Apr 21 2008 Richard W.M. Jones <rjones@redhat.com> - 20071228-1
- Initial packaging for Fedora.

* Fri Jun  1 2007 Alain Knaff <alain@knaff.lu>
- Patch to fix parallel make & make DESTDIR=/tmp/xxx install
- Address gcc4 warnings
- Remove some #define fn udpc_fn lines

* Wed May 30 2007 Jan Oelschlaegel <joe77@web.de>
- Adapt to Solaris 10 x86 (added includes and configure checks)
- Tested on Linux and Solaris 10 (maybe some other OS are broken now...)

* Fri Mar 23 2007 Alain Knaff <alain@knaff.lu>
- Fixed typoes in socklib.c

* Tue Mar 6 2007 Alain Knaff <alain@knaff.lu>
- Fix issue with pipes and no destination file on receiver

* Sun Feb 18 2007 Alain Knaff <alain@knaff.lu>
- Documentation fix

* Mon Feb 5 2007 Alain Knaff <alain@knaff.lu>
- Adapt to busybox 1.4.1 (Config.in)

* Wed Jan 31 2007 Alain Knaff <alain@knaff.lu>
- Added #include <linux/types.h> to make it compile under (K)ubuntu
- Fix uninitialized variable in udp-receiver

* Mon Jan 29 2007 Alain Knaff <alain@knaff.lu>
- Adapt to busybox 1.3.2

* Wed Dec 20 2006 Alain Knaff <alain@knaff.lu>
- Adapt to new busybox 1.3.0

* Sat Dec 16 2006 Alain Knaff <alain@knaff.lu>
- Added startTimeout flag: abort if sender does not start within specified
time
- Darwin build fixes patch
- Refactoring to postpone file creation until sender is located

* Fri Oct 20 2006 Alain Knaff <alain@knaff.lu>
- Fix usage message to use full names for --mcast-data-address and
mcast-rdv-address

* Thu Sep 21 2006 Alain Knaff <alain@knaff.lu>
- Include uio.h into socklib.h, needed with older include files for iovec
- Avoid variable name "log", apparently, for older compilers, this shadows the
name of a built-in

* Wed Sep 20 2006 Alain Knaff <alain@knaff.lu>
- Added missing format string to printMyIp

* Sun Sep 17 2006 Alain Knaff <alain@knaff.lu>
- If --rexmit-hello-interval set on sender, still only display prompt
once on receiver
- Improved logging (on sender, offer option to periodically log
instantaneous bandwidth, log retransmission, and added datestamp to
all log)
- Enable autoconf (configure) in order to make it easier to compile it
on other Unices
- Reorganized cmd.html file to make it cleaner HTML (all the man stuff
now in separate files)
- Fix a buffer overrun on Windows

* Sat Mar 25 2006 Alain Knaff <alain@knaff.lu>
- Separate commandline spec file and mkimage spec file
