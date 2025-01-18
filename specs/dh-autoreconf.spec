Name:           dh-autoreconf
Version:        20
Release:        12%{?dist}
Summary:        debhelper add-on to call autoreconf and clean up after the build

BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/dh-autoreconf
Source0:        http://ftp.de.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz

BuildRequires:  perl-generators
BuildRequires:  perl(Pod::Text)

Requires:       debhelper
Requires:       autoconf
Requires:       automake
Requires:       libtool
Requires:       cdbs
# For /usr/bin/autopoint
Requires:       gettext-devel

%description
dh-autoreconf provides a debhelper sequence addon named 'autoreconf' and two
commands, dh_autoreconf and dh_autoreconf_clean.
 * The dh_autoreconf command creates a list of the files and their checksums,
   calls autoreconf and then creates a second list for the new files.
 * The dh_autoreconf_clean command compares these two lists and removes all
   files which have been added or changed (files may be excluded if needed).
For CDBS users, a rule is provided to call the dh-autoreconf programs at the
right time.


%prep
%setup -q


%build
# Build manpages
pod2man --section=1 dh_autoreconf dh_autoreconf.1
pod2man --section=1 dh_autoreconf_clean dh_autoreconf_clean.1
pod2man --section=7 dh-autoreconf.pod dh-autoreconf.7


%install
install -Dpm 0755 dh_autoreconf %{buildroot}%{_bindir}/dh_autoreconf
install -Dpm 0755 dh_autoreconf_clean %{buildroot}%{_bindir}/dh_autoreconf_clean
install -Dpm 0644 autoreconf.pm %{buildroot}%{perl_vendorlib}/Debian/Debhelper/Sequence/autoreconf.pm
install -Dpm 0644 autoreconf.mk %{buildroot}%{_datadir}/cdbs/1/rules/autoreconf.mk
install -Dpm 0644 ltmain-as-needed.diff %{buildroot}%{_datadir}/%{name}/ltmain-as-needed.diff
install -Dpm 0644 dh_autoreconf.1 %{buildroot}%{_mandir}/man1/dh_autoreconf.1
install -Dpm 0644 dh_autoreconf_clean.1 %{buildroot}%{_mandir}/man1/dh_autoreconf_clean.1
install -Dpm 0644 dh-autoreconf.7 %{buildroot}%{_mandir}/man7/dh-autoreconf.7


%files
%license debian/copyright
%{_bindir}/dh_autoreconf
%{_bindir}/dh_autoreconf_clean
%{perl_vendorlib}/*
%{_datadir}/cdbs/1/rules/autoreconf.mk
%{_datadir}/%{name}/
%{_mandir}/man1/dh_autoreconf.1*
%{_mandir}/man1/dh_autoreconf_clean.1*
%{_mandir}/man7/dh-autoreconf.7*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 20-5
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 20-2
- Perl 5.34 rebuild

* Mon Feb 08 2021 Sandro Mani <manisandro@gmail.com> - 20-1
- Update to 20

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 19-8
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 19-5
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 19-2
- Perl 5.28 rebuild

* Mon May 21 2018 Sandro Mani <manisandro@gmail.com> - 19-1
- Update to 19

* Wed May 16 2018 Sandro Mani <manisandro@gmail.com> - 18-1
- Update to 18

* Mon Mar 26 2018 Sandro Mani <manisandro@gmail.com> - 17-1
- Update to 17

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Sandro Mani <manisandro@gmail.com> - 16-1
- Update to 16

* Wed Nov 15 2017 Sandro Mani <manisandro@gmail.com> - 15-1
- Update to 15

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 14-2
- Perl 5.26 rebuild

* Sat Apr 01 2017 Sandro Mani <manisandro@gmail.com> - 14-1
- Update to 14

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Sandro Mani <manisandro@gmail.com> - 13-1
- Update to 13

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 12-2
- Perl 5.24 rebuild

* Sun Apr 10 2016 Sandro Mani <manisandro@gmail.com> - 12-1
- Update to 12

* Tue Feb 09 2016 Sandro Mani <manisandro@gmail.com> - 11-1
- Update to 11

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 10-2
- Perl 5.22 rebuild

* Fri Sep 26 2014 Sandro Mani <manisandro@gmail.com> - 10-1
- Update to 10

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 9-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 13 2014 Sandro Mani <manisandro@gmail.com> - 9-2
- Fix %%{perl_vendorlib} directory ownership

* Sun Feb 9 2014 Sandro Mani <manisandro@gmail.com> - 9-1
- Initial package
