Name:           mbuffer
Version:        20241007
Release:        2%{?dist}
Summary:        Measuring Buffer is an enhanced version of buffer

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.maier-komor.de/mbuffer.html
Source0:        http://www.maier-komor.de/software/mbuffer/mbuffer-%{version}.tgz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  mt-st
BuildRequires:  mhash-devel
BuildRequires:  autoconf
BuildRequires:  automake

%description
Measuring Buffer is an enhanced version of buffer. It features displayof
throughput, memory-mapped file I/O for huge buffers, and multithreading.

%prep
%autosetup -n %{name}-%{version} -p1

%build
#autoconf
# suppress detection of MD5_Init functions if openssl-devel
# is available on build system, let only mhash_init be
# detected if the md5 hash feature is enabled
export ac_cv_search_MD5_Init=no
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}/usr/etc/mbuffer.rc

%files
%doc AUTHORS ChangeLog NEWS README
%license LICENSE
%{_mandir}/man1/mbuffer.1*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/mbuffer.rc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20241007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Filipe Rosset <rosset.filipe@gmail.com> - 20241007-1
- Update to 20241007 fixes rhbz#2317034

* Fri Oct 04 2024 Filipe Rosset <rosset.filipe@gmail.com> - 20240929-1
- Update to 20240929 fixes rhbz#2315585

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 20240707-2
- convert license to SPDX

* Sat Jul 20 2024 Filipe Rosset <rosset.filipe@gmail.com> - 20240707-1
- Update to 20240707 fixes rhbz#2296189

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 20240107-1
- Update to latest upstream version 20240107

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231216-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231216-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230301-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Fabian Affolter <mail@fabian-affolter.ch> - 20230301-1
- Update to latest upstream version 20230301

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220418-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220418-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Fabian Affolter <mail@fabian-affolter.ch> - 20220418-1
- Update to latest upstream version 20220418

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20211018-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 28 2021 Fabian Affolter <mail@fabian-affolter.ch> - 20211018-1
- Update to latest upstream version 20211018

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210328-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 20210328-1
- Update to latest upstream version 20210328

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 20210209-1
- Update to latest upstream version 20210209

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200929-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 20200929-1
- Update to latest upstream version 20200929

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200505-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 20200505-1
- Update to new upstream version 20200505

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 26 2019 Fabian Affolter <mail@fabian-affolter.ch> - 20191016-1
- Update to new upstream version 20191016

* Sat Aug 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 20190725-1
- Update to new upstream version 20190725

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190127-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Fabian Affolter <mail@fabian-affolter.ch> - 20190127-1
- Update to new upstream version 20190127

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Filipe Rosset <rosset.filipe@gmail.com> - 20181119-1
- new upstream release 20181119 plus spec cleanup

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Fabian Affolter <mail@fabian-affolter.ch> - 20171011-1
- Fix BR
- Update to new upstream version 20171011 

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170515-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170515-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170515-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Fabian Affolter <mail@fabian-affolter.ch> - 20170515-1
- Update to new upstream version 20170515

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Fabian Affolter <mail@fabian-affolter.ch> - 20161115-1
- Update to new upstream version 20161115

* Mon Nov 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 20160613-1
- Update to new upstream version 20160613

* Sun Apr 03 2016 Fabian Affolter <mail@fabian-affolter.ch> - 20160228-1
- Update to new upstream version 20160228

* Thu Feb 04 2016 Fabian Affolter <mail@fabian-affolter.ch> - 20151002-1
- Update to new upstream version 20151002

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150412-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150412-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Fabian Affolter <mail@fabian-affolter.ch> - 20150412-1
- Update to new upstream version 20150412

* Fri Jan 23 2015 Fabian Affolter <mail@fabian-affolter.ch> - 20141227-1
- Update to new upstream version 20141227

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140310-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140310-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Fabian Affolter <mail@fabian-affolter.ch> - 20140310-1
- Update to new upstream version 20140310

* Thu Mar 06 2014 Fabian Affolter <mail@fabian-affolter.ch> - 20140126-1
- Update to new upstream version 20140126

* Mon Aug 05 2013 Fabian Affolter <mail@fabian-affolter.ch> - 20130220-4
- Fix FTBFS (#992214)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130220-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Fabian Affolter <mail@fabian-affolter.ch> - 20130220-2
- ARM64 support

* Fri Mar 01 2013 Fabian Affolter <mail@fabian-affolter.ch> - 20130220-1
- Update to new upstream version 20130220

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Fabian Affolter <mail@fabian-affolter.ch> - 20121111-1
- Update to new upstream version 20121111

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110724-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110724-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 20110724-1
- Update to new upstream version 20110724

* Fri Aug 12 2011 Fabian Affolter <mail@fabian-affolter.ch> - 20110317-2
- Rebuild (libmhash)

* Sun Mar 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 20110317-1
- Update to new upstream release 20110317

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100526-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 02 2010 Fabian Affolter <mail@fabian-affolter.ch> - 20100526-3
- Remove ever piece of md5

* Mon Nov 01 2010 Fabian Affolter <mail@fabian-affolter.ch> - 20100526-2
- Rebuild with md5hash as requested in #608943

* Mon Jun 14 2010 Fabian Affolter <mail@fabian-affolter.ch> - 20100526-1
- Update to new upstream version 20100526

* Sat Feb 27 2010 Fabian Affolter <mail@fabian-affolter.ch> - 20091227-1
- Update to new upstream version 20091227

* Wed Dec 23 2009 Fabian Affolter <mail@fabian-affolter.ch> - 20091122-1
- Update to new upstream version 20091122

* Fri Nov 20 2009 Fabian Affolter <mail@fabian-affolter.ch> - 20091110-1
- Update to new upstream version 20091110

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090628-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Fabian Affolter <mail@fabian-affolter.ch> - 20090628-1
- Fix license (since 20080910 GPLv3+)
- Remov --enable-networking, is no longer needed
- Add make install to install section
- Add NEWS to doc and changed COPYING to LICENSE
- Add macro for bin dir
- Update to new upstream version 20090628

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080507-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 06 2008 Dennis Gilmore <dennis@ausil.us> - 20080507-2
- Fix license tag 

* Fri Jun 06 2008 Dennis Gilmore <dennis@ausil.us> - 20080507-1
- Update to 20080507

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20070502-2
- Autorebuild for GCC 4.3

* Sat May 12 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 20070502-1
- Update to latest version.

* Sat Apr 14 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 20070401-1
- Update to latest version.

* Tue Aug 29 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 20060728-3
- Rebuild for FC6.

* Thu Aug 10 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 20060728-2
- Remove NEWS from %%doc because free of information.

* Wed Aug 09 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 20060728-1
- Update to latest version
- Adjuste project URL and Source0.

* Thu Aug 04 2005 Alexander Dalloz <alex {%} dalloz {*} de> - 20050730-3
- Switche over to mhash for md5hash option instead of
  openssl use (thanks Paul Howarth)
- md5hash disabled by default to not link against library in
  /usr/lib, mbuffer usable without /usr mounted.

* Wed Aug 03 2005 Alexander Dalloz <alex {%} dalloz {*} de> - 20050730-2
- Correct Source0 URL
- Adjust binary location in man page
- Add BR mt-st and conditional openssl-devel.

* Tue Aug 02 2005 Alexander Dalloz <alex {%} dalloz {*} de> - 20050730-1
- Initial build.
