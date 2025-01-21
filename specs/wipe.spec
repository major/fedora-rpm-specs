Name:           wipe
Version:        0.21
Release:        32%{?dist}
Summary:        Secure file erasing tool

License:        GPL-1.0-or-later
URL:            http://abaababa.ouvaton.org/wipe/
Source0:        http://abaababa.ouvaton.org/wipe/wipe-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%description
Wipe is a little command for securely erasing files from magnetic media. 

%prep
%setup -q

%build
chmod +x trtur
export CFLAGS=$RPM_OPT_FLAGS
make %{?_smp_mflags} linux
iconv -f ISO8859-9 -t UTF8 <README > README.utf8
mv README.utf8 README
iconv -f ISO8859-9 -t UTF8 <wipe.tr.1 > wipe.tr.1.utf8
mv wipe.tr.1.utf8 wipe.tr.1
chmod a-x examples/wipefd0 examples/wswap.pl


%install
rm -rf $RPM_BUILD_ROOT
# There is no make install.
# So, we do the install ourselves due to so few files to install.
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1,%{_mandir}/tr/man1}
install -p wipe $RPM_BUILD_ROOT/%{_bindir}
install -p -m644 wipe.1 $RPM_BUILD_ROOT/%{_mandir}/man1
mv wipe.tr.1 wipe.1 && \
  install -p -m644 wipe.1 $RPM_BUILD_ROOT/%{_mandir}/tr/man1/

%files
%doc BUGS CHANGES GPL README examples/wipefd0 examples/wswap.pl
%{_bindir}/wipe
%{_mandir}/man1/wipe.1.gz
%{_mandir}/tr/man1/wipe.1.gz

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.21-30
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 24 2008 Scott Henson <shenson@redhat.com> - 0.21-2
- Make trtur executable
- remove secure-deletion.html 

* Mon Mar 24 2008 Scott Henson <shenson@redhat.com> - 0.21-1
- New upstream version
- use RPM_OPT_FLAGS


* Wed Jan 16 2008 Scott Henson <shenson@redhat.com> - 0.20-4
- Remove executable permissions on example scripts

* Mon Dec 31 2007 Scott Henson <shenson@redhat.com> - 0.20-3
- Change License to GPL+
- Convert wipe.tr.1 UTF8 and install it
- Identify a few more files as docs
- Switch to using -p instead of -c for install
- Fixed typo in previous changelog entry

* Thu Dec 20 2007 Scott Henson <shenson@redhat.com> - 0.20-2
- Fix the encoding of the doc files
- Capitalize the description and summary

* Mon Dec 17 2007 Scott Henson <shenson@redhat.com> - 0.20-1
 - Initial packaged version
