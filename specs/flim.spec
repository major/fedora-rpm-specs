%global ver	1.14.9
%global snap	80b8121
%global snapver	^1.git%{snap}

Summary: Basic library for handling email messages for Emacs
Name: flim
Version: %{ver}%{?snapver}
Release: 0.6%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/wanderlust/flim
BuildRequires: emacs, make
BuildRequires: apel >= 10.8^1.git82eb232-0.1
BuildArch: noarch
# No releases published
Source: %{name}-%{ver}-%{snap}.tar.gz
Requires: apel

%description
FLIM is a library to provide basic features about message
representation and encoding for Emacs.


%prep
%setup -q -n %{name}-%{ver}-%{snap}


%build
rm -f mailcap*
make PREFIX=$RPM_BUILD_ROOT%{_prefix} LISPDIR=$RPM_BUILD_ROOT%{_emacs_sitelispdir} PACKAGE_LISPDIR=NONE


%install
# build for emacs
%makeinstall PREFIX=$RPM_BUILD_ROOT%{_prefix} LISPDIR=$RPM_BUILD_ROOT%{_emacs_sitelispdir} PACKAGE_LISPDIR=NONE

# remove files which shadow elisp files from emacs itself (#722186)
for i in md4 hex-util sasl-cram sasl-digest ntlm sasl sasl-ntlm hmac-def hmac-md5; do
  rm $RPM_BUILD_ROOT%{_emacs_sitelispdir}/flim/$i.el* || :
done

%files
%doc FLIM-API.en README.en README.ja
%{_emacs_sitelispdir}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9^1.git80b8121-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9^1.git80b8121-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9^1.git80b8121-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9^1.git80b8121-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 27 2023 Akira TAGOH <tagoh@redhat.com> - 1.14.9^1.git80b8121-0.2
- Add BR to the latest apel to make sure the build is successfully completed.

* Tue Sep 26 2023 Akira TAGOH <tagoh@redhat.com> - 1.14.9^1.git80b8121-0.1
- Rebase from git since original upstream is gone.
- Fix FTBFS
  Resolves: rhbz#2225807
- Clean up spec file.
- Convert License tag to SPDX.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 1.14.9-21
- Drop XEmacs support in F36 and later

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb  3 2012 Jens Petersen <petersen@redhat.com> - 1.14.9-4
- remove elisp files that shadow libraries from emacs (Andreas Schwab, #722186)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 29 2010 Jens Petersen <petersen@redhat.com> - 1.14.9-1
- update to 1.14.9
- flim-xemacs-batch-autoloads.patch no longer needed

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 1.14.8-3
- update license to GPLv2+

* Mon Sep 25 2006 Jens Petersen <petersen@redhat.com> - 1.14.8-2
- update url and source location

* Fri Aug  4 2006 Jens Petersen <petersen@redhat.com> - 1.14.8-1
- update to 1.14.8
- add flim-xemacs-batch-autoloads.patch to fix generation of autoloads
  for xemacs-21.5

* Mon May 30 2005 Jens Petersen <petersen@redhat.com> - 1.14.7-3
- Initial import into Extras
- restore xemacs subpackage

* Wed Feb 23 2005 Elliot Lee <sopwith@redhat.com> 1.14.7-2
- Remove xemacs subpackage

* Sat Oct  9 2004 Jens Petersen <petersen@redhat.com> - 1.14.7-1
- update to 1.14.7 release
- flim-1.14.6-mel-u-tempfile.patch no longer needed

* Wed Oct  6 2004 Jens Petersen <petersen@redhat.com> - 1.14.6-3
- drop requirements on emacs/xemacs for -nox users
  (Lars Hupfeldt Nielsen, 134479)

* Tue Sep 28 2004 Warren Togami <wtogami@redhat.com> - 1.14.6-2
- remove redundant docs, large changelog, tests

* Thu May 20 2004 Jens Petersen <petersen@redhat.com> - 1.14.6-1
- update to 1.14.6
- add flim-1.14.6-mel-u-tempfile.patch to fix CAN-2004-0422
- move redundant %%emacsver and %%xemacsver into requirements
- better url and summary

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> - 1.14.5-2
- rebuilt

* Sat Aug  2 2003 Jens Petersen <petersen@redhat.com> - 1.14.5-1
- update to 1.14.5

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Dec 24 2002 Jens Petersen <petersen@redhat.com> 1.14.4-1
- update to 1.14.4
- install xemacs package under datadir
- own emacs site-lisp and down
- own xemacs-packages and down

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild in current collinst

* Thu Jul 18 2002 Akira TAGOH <tagoh@redhat.com> 1.14.3-7
- add the owned directory.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Feb 22 2002 Tim Powers <timp@redhat.com>
- rebuilt in new environment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Nov 30 2001 Jens Petersen <petersen@redhat.com> 1.14.3-2
- noarch, since xemacs available on ia64 
- require apel

* Fri Oct 26 2001 Akira TAGOH <tagoh@redhat.com> 1.14.3-1
- Initial release.
  Separated from semi package.
