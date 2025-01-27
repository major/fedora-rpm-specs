# EL4 doesn't have libpcap-devel
%if 0%{?rhel} && "%rhel" < "5"
%define pcapdep libpcap
%else
%define pcapdep libpcap-devel
%endif

# GCC 10 uses -fno-common by default, turn it off for now
%define _legacy_common_support 1

Name:           tcpreplay
Version:        4.5.1
Release:        5%{?dist}
Summary:        Replay captured network traffic

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://tcpreplay.appneta.com/
Source:         https://github.com/appneta/tcpreplay/releases/download/v%{version}/tcpreplay-%{version}.tar.xz
Patch0:         tcpreplay-4.5.1-txring_h.patch
Patch1:         tcpreplay-4.5.1-configure_ac.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  automake autoconf libtool
BuildRequires:  %{pcapdep} >= 0.8.0, tcpdump
%if ! 0%{?rhel}
BuildRequires:  libdnet-devel
%endif
Requires:       tcpdump

%description
Tcpreplay is a tool to replay captured network traffic. Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats. Also included, is tcpprep
a tool to pre-process capture files to allow increased performance under
certain conditions as well as capinfo which provides basic information about
capture files.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure --enable-local-libopts \
           --disable-libopts-install \
           --disable-maintainer-mode

# make sure we use proper CFLAGS
%{__sed} -i \
         -e 's/^CFLAGS.*/CFLAGS=${RPM_OPT_FLAGS} -std=gnu99 -D_U_="__attribute__((unused))" -Wno-format-contains-nul/' \
         $(find . -name Makefile)

# remove unneeded docs
%{__rm} -f docs/INSTALL docs/Makefile*

# fix wrong permissions
%{__chmod} -x src/*.c src/common/*.c

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%doc docs/*
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Wed Jan 22 2025 Bojan Smojver <bojan@rexursive com> - 4.5.1-5
- Drop unknown configure option --enable-tcpreplay-edit
- Change tcpdump dependency to package
- Remove checks for TX_RING support to avoid build problems

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 4.5.1-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 13 2024 Bojan Smojver <bojan@rexursive com> - 4.5.1-1
- Update to 4.5.1

* Sat Mar 16 2024 Bojan Smojver <bojan@rexursive com> - 4.4.4-5
- Patch CVE-2023-4256

* Sat Mar 16 2024 Bojan Smojver <bojan@rexursive com> - 4.4.4-4
- Patch CVE-2023-43279

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Bojan Smojver <bojan@rexursive com> - 4.4.4-1
- Update to 4.4.4

* Sat May  6 2023 Bojan Smojver <bojan@rexursive com> - 4.4.3-3
- CVE-2023-27783 CVE-2023-27784 CVE-2023-27785 CVE-2023-27786
  CVE-2023-27787 CVE-2023-27788 CVE-2023-27789

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  2 2023 Bojan Smojver <bojan@rexursive com> - 4.4.3-1
- bump up to 4.4.3
- remove merged patch from https://github.com/appneta/tcpreplay/pull/757

* Thu Nov 24 2022 Florian Weimer <fweimer@redhat.com> - 4.4.2-2
- Avoid implicit int, implicit function declarations in configure

* Sat Aug 27 2022 Bojan Smojver <bojan@rexursive com> - 4.4.2-1
- bump up to 4.4.2
- CVE-2022-27939, CVE-2022-27940, CVE-2022-27941, CVE-2022-27942,
- CVE-2022-28487, CVE-2022-37047, CVE-2022-37048, CVE-2022-37049

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 13 2022 Bojan Smojver <bojan@rexursive com> - 4.4.1-1
- bump up to 4.4.1

* Mon Jan 31 2022 Bojan Smojver <bojan@rexursive com> - 4.4.0-1
- bump up to 4.4.0
- fix CVE-2021-45386 and CVE-2021-45387

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May  2 2021 Bojan Smojver <bojan@rexursive com> - 4.3.4-1
- bump up to 4.3.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Bojan Smojver <bojan@rexursive com> - 4.3.3-2
- CVE-2020-24265, CVE-2020-24266

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Bojan Smojver <bojan@rexursive com> - 4.3.3-1
- bump up to 4.3.3
- CVE-2020-12740

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Bojan Smojver <bojan@rexursive com> - 4.3.2-1
- bump up to 4.3.2

* Wed Mar 13 2019 Bojan Smojver <bojan@rexursive com> - 4.3.1-3
- patch CVE-2019-8376, CVE-2019-8377 and CVE-2019-8381

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 Bojan Smojver <bojan@rexursive com> - 4.3.1-1
- bump up to 4.3.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Bojan Smojver <bojan@rexursive com> - 4.2.5-5
- add gcc build requirement

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May  9 2017 Bojan Smojver <bojan@rexursive com> - 4.2.5-1
- bump up to 4.2.5

* Thu Apr 27 2017 Bojan Smojver <bojan@rexursive com> - 4.2.4-1
- bump up to 4.2.4

* Fri Mar 24 2017 Bojan Smojver <bojan@rexursive com> - 4.2.1-1
- bump up to 4.2.1

* Tue Mar 21 2017 Bojan Smojver <bojan@rexursive com> - 4.2.0-1
- bump up to 4.2.0

* Tue Mar  7 2017 Bojan Smojver <bojan@rexursive com> - 4.1.2-3
- patch for CVE-2017-6429
- use autosetup

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Bojan Smojver <bojan@rexursive com> - 4.1.2-1
- bump up to 4.1.2

* Fri Jul  8 2016 Bojan Smojver <bojan@rexursive com> - 4.1.1-2
- fix bug #1353525: CVE-2016-6160

* Fri Apr 29 2016 Bojan Smojver <bojan@rexursive com> - 4.1.1-1
- bump up to 4.1.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 18 2014 Bojan Smojver <bojan@rexursive com> - 4.1.0-1
- bump up to 4.1.0

* Sun Sep  7 2014 Bojan Smojver <bojan@rexursive com> - 4.0.5-1
- bump up to 4.0.5

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Bojan Smojver <bojan@rexursive com> - 4.0.4-1
- bump up to 4.0.4

* Wed Feb  5 2014 Bojan Smojver <bojan@rexursive com> - 4.0.3-1
- bump up to 4.0.3

* Thu Jan 30 2014 Bojan Smojver <bojan@rexursive com> - 4.0.2-1
- bump up to 4.0.2

* Mon Jan  6 2014 Bojan Smojver <bojan@rexursive com> - 4.0.0-2
- update licence: GPLv3
- update URL

* Mon Jan  6 2014 Bojan Smojver <bojan@rexursive com> - 4.0.0-1
- bump up to 4.0.0

* Wed Jan  1 2014 Bojan Smojver <bojan@rexursive com> - 4.0.0-0.beta2.1
- bump up to 4.0.0beta2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 11 2010 Bojan Smojver <bojan@rexursive com> - 3.4.4-1
- bump up to 3.4.4

* Tue Mar 16 2010 Bojan Smojver <bojan@rexursive.com> 3.4.3-3
- fix buffer overflow from bug #556813

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Bojan Smojver <bojan@rexursive com> - 3.4.3-1
- bump up to 3.4.3

* Wed May 20 2009 Bojan Smojver <bojan@rexursive com> - 3.4.2-1
- bump up to 3.4.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Bojan Smojver <bojan@rexursive com> - 3.4.1-1
- bump up to 3.4.1

* Thu Jan 15 2009 Bojan Smojver <bojan@rexursive com> - 3.4.0-2
- correct libdnet BR logic

* Thu Jan 15 2009 Bojan Smojver <bojan@rexursive com> - 3.4.0-1
- bump up to 3.4.0
- add libdnet-devel to BR

* Mon Jun 23 2008 Bojan Smojver <bojan@rexursive com> - 3.3.2-1
- bump up to 3.3.2

* Sun May 18 2008 Bojan Smojver <bojan@rexursive com> - 3.3.1-1
- bump up to 3.3.1

* Tue May  6 2008 Bojan Smojver <bojan@rexursive com> - 3.3.0-1
- bump up to 3.3.0

* Thu May  1 2008 Bojan Smojver <bojan@rexursive com> - 3.3-0.rc2.1
- bump up to 3.3.rc2

* Mon Apr 28 2008 Bojan Smojver <bojan@rexursive com> - 3.3-0.rc1.1
- bump up to 3.3.rc1

* Sat Feb  9 2008 Bojan Smojver <bojan@rexursive com> - 3.2.5-2
- rebuild for GCC 4.3

* Thu Jan 24 2008 Bojan Smojver <bojan@rexursive com> - 3.2.5-1
- bump up to 3.2.5

* Fri Jan 18 2008 Bojan Smojver <bojan@rexursive com> - 3.2.4-1
- bump up to 3.2.4
- use --enable-tcpreplay-edit when building

* Fri Nov 02 2007 Bojan Smojver <bojan@rexursive com> - 3.2.3-1
- bump up to 3.2.3
- drop compilation fix patch, now upstream

* Thu Nov 01 2007 Bojan Smojver <bojan@rexursive com> - 3.2.2-2
- fix compilation

* Thu Nov 01 2007 Bojan Smojver <bojan@rexursive com> - 3.2.2-1
- bump up to 3.2.2

* Fri Oct 26 2007 Bojan Smojver <bojan@rexursive com> - 3.2.1-1
- bump up to 3.2.1

* Mon Aug 27 2007 Bojan Smojver <bojan@rexursive com> - 3.2.0-1
- bump up to 3.2.0
- drop -enable-64bits option to configure - this is now default

* Fri Jul 20 2007 Bojan Smojver <bojan@rexursive com> - 3.1.1-1
- bump up to 3.1.1
- drop the patch for libpcap.so detection, fixed upstream

* Fri May 04 2007 Bojan Smojver <bojan@rexursive com> - 3.0.1-2
- static libraries not shipped in FC7 - fix libpcap.so detection

* Thu May 03 2007 Bojan Smojver <bojan@rexursive com> - 3.0.1-1
- Bump up to new release 3.0.1
- flowreplay doesn't compile, will enable when it does

* Tue Apr 17 2007 Bojan Smojver <bojan@rexursive com> - 2.3.5-4
- Remove Makefile from docs

* Tue Apr 17 2007 Bojan Smojver <bojan@rexursive com> - 2.3.5-3
- Implement suggestions from package review process

* Tue Apr 03 2007 Bojan Smojver <bojan@rexursive com> - 2.3.5-2
- Add tcpdump to build and runtime dependencies
- Cater for EL4, where there is no libpcap-devel

* Mon Apr 02 2007 Bojan Smojver <bojan@rexursive com> - 2.3.5-1
- Initial release, 2.3.5
- Based on package provided by Dag Wieers
