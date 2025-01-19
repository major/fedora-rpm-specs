Name:		mb2md
Version:	3.20
Release:	32%{?dist}
Summary:	Mailbox to maildir converter
License:	LicenseRef-Fedora-Public-Domain
URL:		http://batleth.sapienti-sat.org/projects/mb2md
Source0:	http://batleth.sapienti-sat.org/projects/mb2md/mb2md-%{version}.pl.gz
Source1:	http://batleth.sapienti-sat.org/projects/mb2md/changelog.txt
BuildArch:	noarch
BuildRequires:	perl-generators

%description
Convert your emails folders in mailbox format to maildirs.
Some of the current features of mb2md.pl are:
* converting the user's main mailbox that is referenced by the $MAIL variable
* converting a single mailbox into corresponding maildir
* converting multiple mailboxes in a directory into corresponding maildirs
* recursive operation on a given directory to convert the complete mail
  storage of one user
* replaces all occurrences of dots ('.') in a mailbox name by underscores ('_')
* is able to handle spaces in mailbox names
* converts mbox files in DOS format (CRLF) to Unix file format
* can strip an extension (e.g. ".mbx") from a mailbox name prior to converting
* removal of dummy message that a couple of IMAP servers (e.g. UW-IMAPD) put at
  the beginning of a mailbox
* setting the file date of a converted message according to the date found in
  the "From " line of the original mail
* setting the flags F,R,S,T (flagged, replied, seen, deleted) on the filename
  of the converted message according to the flags found in 
  "Status:"/"X-Status:"/"X-Mozilla-Status:"/"X-Evolution:" headers of the
  original mail


%prep
%setup -q -Tc -n %{name}-%{version}
# Setup executable
gunzip -c %{SOURCE0} > mb2md.pl
touch -r %{SOURCE0} mb2md.pl

# Copy changelog
cp -a %{SOURCE1} .

### Generate documentation
# #--- denotes the end of the documentation section; get everything before
# that, remove the shebang and the hash commentation
grep -B `wc -l mb2md.pl|awk '{print $1}'` "#---------" mb2md.pl | grep -v "#-----" | grep -v "#!/" | \
cut -c3- > readme.txt
touch -r %{SOURCE0} readme.txt


%build

%install
rm -rf %{buildroot}
install -D -p -m 755 mb2md.pl %{buildroot}%{_bindir}/mb2md


%files
%doc changelog.txt readme.txt
%{_bindir}/mb2md


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.20-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 05 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 3.20-4
- Bump revision to retry CVS import.

* Tue May 05 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 3.20-3
- Changed name of installed script from mb2md.pl to mb2md.
- Added generated readme file to %%doc.

* Mon Apr 27 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 3.20-2
- Fixed awk argument, trimmed description.

* Mon Apr 27 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 3.20-1
- First release.
