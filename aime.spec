%global libname libaime

Name:            aime
Version:         8.20221019
Release:         1%{?dist}
Summary:         An application embeddable programming language interpreter
License:         GPLv3+
URL:             http://aime-embedded.sourceforge.net/
Source0:         http://downloads.sourceforge.net/project/aime-embedded/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:          %{name}-8.20150211-ldflags.patch
BuildRequires:   gcc
BuildRequires:   make

%description
aime is a programming language with a C like syntax, intended for application
extending purposes. The aime collection comprises the language description, an
application embeddable interpreter (libaime), the interpreter C interface
description and a standalone interpreter. Many examples on how the interpreter
can be used (embedded in an application) are also available, together with 
some hopefully useful applications, such as expression evaluators.

%package         devel
Summary:         Development files for %{name}
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description     devel
This package contains header files for developing applications that 
use %{name}.

%prep
%autosetup -p 1

%build
%configure
%make_build

%check
make check

%install
%make_install
find %{buildroot} -name '*.a' -delete -print
rm -frv %{buildroot}%{_infodir}/dir

%files
%doc README TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_infodir}/*.info*

%files devel
%{_includedir}/%{name}.h

%changelog
* Mon Oct 24 2022 Filipe Rosset <rosset.filipe@gmail.com> - 8.20221019-1
- Update to 8.20221019 fixes rhbz#2136213

* Mon Oct 17 2022 Filipe Rosset <rosset.filipe@gmail.com> - 8.20221012-1
- Update to 8.20221012

* Sat Sep 24 2022 Filipe Rosset <rosset.filipe@gmail.com> - 8.20220922-1
- Update to 8.20220922 fixes rhbz#2129308

* Wed Sep 07 2022 Filipe Rosset <rosset.filipe@gmail.com> - 8.20220904-1
- Update to 8.20220904 fixes rhbz#2124428

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.20220113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Filipe Rosset <rosset.filipe@gmail.com> - 8.20220113-1
- Update to 8.20220113 fixes rhbz#2038264

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.20210923-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Filipe Rosset <rosset.filipe@gmail.com> - 8.20210923-1
- Update to 8.20210923 fixes rhbz#1990936

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.20210510-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 10 2021 Filipe Rosset <rosset.filipe@gmail.com> - 8.20210510-1
- Update to 8.20210510 fixes rhbz#1938144

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.20210121-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Filipe Rosset <rosset.filipe@gmail.com> - 8.20210121-1
- Update to 8.20210121 fixes rhbz#1919456

* Tue Jan 19 2021 Filipe Rosset <rosset.filipe@gmail.com> - 8.20210113-1
- Update to 8.20210113 fixes rhbz#1917577

* Mon Aug 17 2020 Filipe Rosset <rosset.filipe@gmail.com> - 8.20200810-1
- Update to 8.20200810 fixes rhbz#1862338

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20200125-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20200125-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20200125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Filipe Rosset <rosset.filipe@gmail.com> - 8.20200125-1
- Updated to 8.20200125 fixes rhbz#1749471

* Thu Aug 22 2019 Filipe Rosset <rosset.filipe@gmail.com> - 8.20190821-1
- Updated to 8.20190821 fixes rhbz#1744389

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.20190626-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Filipe Rosset <rosset.filipe@gmail.com> - 8.20190626-1
- Updated to new 8.20190626 upstream version, fixes rhbz #1724451

* Tue Jun 11 2019 Filipe Rosset <rosset.filipe@gmail.com> - 8.20190609-1
- Updated to new 8.20190609 upstream version, fixes rhbz #1718871

* Thu May 16 2019 Filipe Rosset <rosset.filipe@gmail.com> - 8.20190516-1
- Updated to new 8.20190516 upstream version, fixes rhbz #1706479

* Tue Apr 16 2019 Filipe Rosset <rosset.filipe@gmail.com> - 8.20190416-1
- Updated to new 8.20190416 upstream version, fixes rhbz #1700049

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.20180811-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 8.20180811-1
- Updated to new 8.20180811 upstream version, fixes rhbz #1578595

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.20180501-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 06 2018 Filipe Rosset <rosset.filipe@gmail.com> - 8.20180501-1
- Updated to new 8.20180501 upstream version, fixes rhbz #1574484

* Sat Apr 21 2018 Filipe Rosset <rosset.filipe@gmail.com> - 8.20180417-1
- Updated to new 8.20180417 upstream version, fixes rhbz #1569267

* Sun Apr 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 8.20180223-2
- added gcc as BR

* Thu Mar 29 2018 Filipe Rosset <rosset.filipe@gmail.com> - 8.20180223-1
- Updated to new 8.20180223 upstream version, fixes rhbz #1548775

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.20180107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Filipe Rosset <rosset.filipe@gmail.com> - 8.20180107-1
- Updated to new 8.20180107 upstream version, fixes rhbz #1482916

* Sat Aug 05 2017 Filipe Rosset <rosset.filipe@gmail.com> - 8.20170803-1
- Updated to new 8.20170803 upstream version, fixes rhbz #1476248

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.20170727-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sat Jul 29 2017 Filipe Rosset <rosset.filipe@gmail.com> - 8.20170727-1
- Updated to new 8.20170727 upstream version, fixes rhbz #1476248

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.20170718-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Filipe Rosset <rosset.filipe@gmail.com> - 8.20170718-1
- Updated to new 8.20170718 upstream version, fixes rhbz #1469511

* Tue Jul 11 2017 Filipe Rosset <rosset.filipe@gmail.com> - 8.20170704-1
- Updated to new 8.20170704 upstream version, fixes rhbz #1465412

* Thu Jun 15 2017 Filipe Rosset <rosset.filipe@gmail.com> - 8.20170608-1
- Updated to new 8.20170608 upstream version, fixes rhbz #1448426

* Fri Apr 14 2017 Filipe Rosset <rosset.filipe@gmail.com> - 8.20170326-1
- Updated to new 8.20170326 upstream version, fixes rhbz #1421666

* Mon Feb 20 2017 Filipe Rosset <rosset.filipe@gmail.com> - 8.20170219-1
- Updated to new 8.20170219 upstream version, fixes rhbz #1421666

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.20170111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Filipe Rosset <rosset.filipe@gmail.com> - 8.20170111-1
- Updated to new 8.20170111 upstream version, fixes rhbz #1413563

* Wed Nov 02 2016 Filipe Rosset <rosset.filipe@gmail.com> - 8.20161011-1
- Updated to new 8.20161011 upstream version, fixes rhbz #1383674

* Sun Sep 18 2016 Filipe Rosset <rosset.filipe@gmail.com> - 8.20160916-1
- Updated to new 8.20160916 upstream version, fixes rhbz #1376995

* Mon Sep 12 2016 Filipe Rosset <rosset.filipe@gmail.com> - 8.20160903-1
- Updated to new 8.20160903 upstream version, fixes rhbz #1354181

* Sun Jun 26 2016 Filipe Rosset <rosset.filipe@gmail.com> - 8.20160626-1
- Updated to new 8.20160626 upstream version, fixes rhbz #1350199

* Tue May 17 2016 Filipe Rosset <rosset.filipe@gmail.com> - 8.20160504-1
- Updated to new 8.20160504 upstream version, fixes rhbz #1249297

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.20150211-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.20150211-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr  4 2015 Ville Skyttä <ville.skytta@iki.fi> - 8.20150211-2
- Don't strip binaries too early

* Wed Apr 01 2015 Christopher Meng <rpm@cicku.me> - 8.20150211-1
- Update to 8.20150211

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.20140511-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 21 2014 Christopher Meng <rpm@cicku.me> - 7.20140511-1
- Update to 7.20140511

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.20140427-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Christopher Meng <rpm@cicku.me> - 7.20140427-1
- Update to 7.20140427

* Mon Jan 06 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 7.20131209-2
- Use R: /sbin/install-info (Fix broken installation dependency).
- Use /sbin/install-info instead of install-info in scriptlets.
- Make %%preun compliant to the FPG.

* Sat Dec 21 2013 Christopher Meng <rpm@cicku.me> - 7.20131209-1
- Update to 7.20131209

* Fri Oct 11 2013 Christopher Meng <rpm@cicku.me> - 6.20130921-1
- Update to 6.20130921

* Mon Aug 26 2013 Christopher Meng <rpm@cicku.me> - 6.20130824-1
- Update to 6.20130824

* Mon Jul 29 2013 Christopher Meng <rpm@cicku.me> - 6.20130713-1
- Update to 6.20130713

* Fri May 31 2013 Christopher Meng <rpm@cicku.me> - 5.20130520-1
- Initial Package.
