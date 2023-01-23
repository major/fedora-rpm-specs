%define to_utf8(f:) iconv -f %{-f:%{-f*}}%{!-f:iso-8859-1} -t utf-8 < %1 > %{1}. && touch -r %1 %{1}. && mv -f %{1}. %1

Name:       swaks
Version:    20190914.0
Release:    8%{?dist}
Summary:    Command-line SMTP transaction tester

License:    GPLv2+
URL:        http://www.jetmore.org/john/code/swaks
Source0:    http://www.jetmore.org/john/code/swaks/swaks-%version.tar.gz

BuildArch:  noarch
BuildRequires: perl-generators
BuildRequires: perl-podlators

Requires:   perl(Authen::DigestMD5)
Requires:   perl(Authen::NTLM)
Requires:   perl(Authen::SASL)
Requires:   perl(Config)
Requires:   perl(Digest::SHA)
Requires:   perl(IO::Socket::INET6)
Requires:   perl(Net::DNS)
Requires:   perl(Net::SSLeay)
Requires:   perl(Time::HiRes)

%description
Swiss Army Knife SMTP: A command line SMTP tester.  Swaks can test
various aspects of your SMTP server, including TLS and AUTH.

%prep
%autosetup
%to_utf8 doc/Changes.txt

%install
install -D -p -m 0755 swaks %buildroot/%_bindir/swaks
mkdir -p %buildroot/%_mandir/man1
/usr/bin/pod2man swaks > %buildroot/%_mandir/man1/swaks.1

%files
%_bindir/swaks
%_mandir/man1/*
%license LICENSE.txt
%doc README.txt doc/Changes.txt doc/recipes.txt doc/ref.txt

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20190914.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20190914.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20190914.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190914.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190914.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190914.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190914.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 20190914.0-1
- Update to latest upstream version.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181104.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181104.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 20181104.0-2
- Remove Group tag.

* Mon Nov 05 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 20181104.0-1
- Update to new upsteam version 20181104.0.
- Account for new license file naming.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170101.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170101.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170101.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 20170101.0-2
- Add some dependencies to enable additional features.

* Tue May 16 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 20170101.0-1
- Update to 20170101.0.
- Clean up packaging.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130209.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20130209.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130209.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130209.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 20130209.0-1
- 20130209.0 bump
- Adjust documentation to POD specification

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120320.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 20120320.0-5
- Perl 5.18 rebuild

* Tue Feb 19 2013 Jason L Tibbitts III <tibbs@math.uh.edu> - 20120320.0-4
- /usr/bin/pod2man was split out of the base perl package; add the proper build
  dep.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120320.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120320.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Jason L Tibbitts III <tibbs@math.uh.edu> - 20120320.0-1
- Update to new upstream version.
- Now needs Digest::SHA instead of Digest::SHA1.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111230.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan 01 2012 Jason L Tibbitts III <tibbs@math.uh.edu> - 20111230.0-1
- Update to new upstream version.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100211.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Jason L Tibbitts III <tibbs@math.uh.edu> - 20100211.0-2
- Remove %%clean as well.

* Thu Feb 11 2010 Jason L Tibbitts III <tibbs@math.uh.edu> - 20100211.0-1
- New upstream release 20100211.0.
- New project URL, now distributed as a tarball.
- New docs, including a license file.

* Wed Jan 20 2010 Jason L Tibbitts III <tibbs@math.uh.edu> - 20061116.0-4
- Update to modern Fedora standards (no BuildRoot or rm -rf in %%install).
- No need for empty %%prep and %%build.
- I prefer %%{buildroot} these days.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061116.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061116.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 22 2007 Jason L Tibbitts III <tibbs@math.uh.edu> - 20061116.0-2
- Update license tag.

* Thu Nov 16 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 20061116.0-1
- Update to 20061116.0.
- Add perl(Digest::SHA1) requirement.

* Thu Aug 31 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 20060621.0-1
- Update to 20060621.0.

* Wed May 17 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 20050709.1-6
- Correct Authen:DigestMD5 typo.

* Mon May 15 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 20050709.1-5
- Add Authen::DigestMD5 requirement now that it's in Extras.

* Wed Mar 29 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 20050709.1-4
- Cleanups from package review

* Sun Feb 12 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 20050709.1-3
- Use versioned source file URL

* Sat Jan 28 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 20050709.1-2
- Change group.

* Sat Jan 28 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 20050709.1-1
- Initial attempt

