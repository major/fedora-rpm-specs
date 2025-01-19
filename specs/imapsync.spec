Name: imapsync
Summary: Tool to migrate email between IMAP servers
Version: 2.229
Release: 8%{?dist}
License: NLPL

URL: http://github.com/imapsync/imapsync

Source0: https://github.com/%{name}/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0: imapsync-remove-inet6-pkg.patch

BuildArch: noarch
BuildRequires: perl(App::cpanminus)
BuildRequires: perl(Authen::NTLM)
BuildRequires: perl(CGI)
BuildRequires: perl(Class::Load)
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(Data::Uniqid)
BuildRequires: perl(Digest::HMAC_MD5)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Dist::CheckConflicts)
BuildRequires: perl(Encode::IMAPUTF7)
BuildRequires: perl(English)
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::Tail)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(IO::Tee)
BuildRequires: perl(JSON::WebToken)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Mail::IMAPClient) >= 3.25
BuildRequires: perl(Module::Implementation)
BuildRequires: perl(Module::ScanDeps)
BuildRequires: perl(Net::Ping)
BuildRequires: perl(Package::Stash)
BuildRequires: perl(Package::Stash::XS)
BuildRequires: perl(PAR::Packer)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Proc::ProcessTable)
BuildRequires: perl(Readonly)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Sys::MemInfo)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::Mock::Guard)
BuildRequires: perl(Test::MockObject)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Requires)
BuildRequires: perl(Test::Simple)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(Unicode::String)
BuildRequires: perl(URI::Escape)
BuildRequires: procps-ng

%if 0%{?fedora} >= 19
BuildRequires: perl-generators
BuildRequires: perl-podlators
%endif
BuildRequires: make

Requires: perl(Authen::NTLM)
Requires: perl(Compress::Zlib)
Requires: perl(Data::Uniqid)
Requires: perl(Digest::HMAC_MD5)
Requires: perl(Digest::HMAC_SHA1)
Requires: perl(Digest::MD5)
Requires: perl(Encode::IMAPUTF7)
Requires: perl(English)
Requires: perl(File::Copy::Recursive)
Requires: perl(File::Path)
Requires: perl(File::Spec)
Requires: perl(File::Tail)
Requires: perl(IO::Socket::SSL)
Requires: perl(IO::Tee)
Requires: perl(JSON::WebToken)
Requires: perl(Mail::IMAPClient) >= 3.25
Requires: perl(Pod::Usage)
Requires: perl(Proc::ProcessTable)
Requires: perl(Regexp::Common)
Requires: perl(Readonly)
Requires: perl(Sys::MemInfo)
Requires: perl(Term::ReadKey)
Requires: perl(Test::MockObject)
Requires: perl(Test::Pod)
Requires: perl(Test::Simple)
Requires: perl(Time::HiRes)
Requires: perl(Unicode::String)
Requires: perl(URI::Escape)
Requires: procps-ng

%description
imapsync is a tool for facilitating incremental recursive IMAP
transfers from one mailbox to another. It is useful for mailbox migration,
and reduces the amount of data transferred by only copying messages that
are not present on both servers. Read, unread, and deleted flags are preserved,
and the process can be stopped and resumed. The original messages can
optionally be deleted after a successful transfer.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
  sed -e '/perl(--prefix2)/d'
EOF

%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
#chmod +x %{__perl_requires}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/W
%{__make} install DESTDIR="$RPM_BUILD_ROOT"
iconv -f iso-8859-1 -t utf-8 -o ChangeLog.utf8 ChangeLog && %{__mv} ChangeLog.utf8 ChangeLog
iconv -f iso-8859-1 -t utf-8 -o TODO.utf8 TODO && %{__mv} TODO.utf8 TODO

%files
%doc ChangeLog CREDITS INSTALL INSTALL.d TODO README FAQ FAQ.d LICENSE NOLIMIT
%{_bindir}/imapsync
%attr(644, root, root) %{_mandir}/man1/imapsync.1*

%ChangeLog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.229-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.229-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.229-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.229-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.229-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Petr Salaba <psalaba@redhat.com> - 2.229-3
- Remove deprecated IO::Socket::INET6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.229-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 5 2022 Nick Bebout <nb@fedoraproject.org> - 2.229-1
- Update to 2.229

* Sun Aug 21 2022 Jonathan Wright <nb@fedoraproject.org> - 2.200-1
- Update to 2.200
- Update URL
- Misc minor spec modernization

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.140-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 7 2022 Nick Bebout <nb@fedoraproject.org> - 2.140-2
- Add dependency on procps-ng

* Mon Feb 7 2022 Nick Bebout <nb@fedoraproject.org> - 2.140-1
- Update to 2.140

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.977-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.977-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 20 2021 Nick Bebout <nb@fedoraproject.org> - 1.977-2
- Add missing dep on perl(English)

* Tue Feb 2 2021 Nick Bebout <nb@fedoraproject.org> - 1.977-1
- Update to 1.977

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.882-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.882-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.882-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.882-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.882-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.882-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 07 2018 Nick Bebout <nb@usi.edu> - 1.882-1
- Update to 1.882

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.836-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Nick Bebout <nb@fedoraproject.org> - 1.836-1
- Update to 1.836

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.727-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.727-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Nick Bebout <nb@fedoraproject.org> - 1.727-1
- Update to 1.727

* Wed Apr 06 2016 Nick Bebout <nb@fedoraproject.org> - 1.684-1
- Update to 1.684

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.678-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Nick Bebout <nb@fedoraproject.org> - 1.678-1
- Update to 1.678

* Thu Dec 3 2015 Nick Bebout <nb@fedoraproject.org> - 1.670-1
- Update to 1.670

* Wed Nov 18 2015 Nick Bebout <nb@fedoraproject.org> - 1.644-2
- Disable releasecheck - CVE-2013-4279

* Mon Aug 24 2015 Nick Bebout <nb@fedoraproject.org> - 1.644-1
- Update to 1.644

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.637-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Nick Bebout <nb@fedoraproject.org> - 1.637-1
- Upgrade to 1.637

* Wed Nov 26 2014 Nick Bebout <nb@fedoraproject.org> - 1.607-1
- Upgrade to 1.607

* Thu Aug 14 2014 Nick Bebout <nb@fedoraproject.org> - 1.592-1
- Upgrade to 1.592

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.584-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 4 2014 Nick Bebout <nb@fedoraproject.org> - 1.584-2
- Disable releasecheck - CVE-2013-4279

* Thu Feb 13 2014 Nick Bebout <nb@fedoraproject.org> - 1.584-1
- Upgrade to 1.584

* Sun Dec 29 2013 Nick Bebout <nb@fedoraproject.org> - 1.580-1
- Upgrade to 1.580

* Thu Oct 17 2013 Nick Bebout <nb@fedoraproject.org> - 1.569-1
- Upgrade to 1.569

* Thu Sep 26 2013 Nick Bebout <nb@fedoraproject.org> - 1.567-1
- Upgrade to 1.567

* Mon Aug 19 2013 Nick Bebout <nb@fedoraproject.org> - 1.564-1
- Upgrade to 1.564

* Sun Aug 4 2013 Nick Bebout <nb@fedoraproject.org> - 1.558-1
- Upgrade to 1.558

* Sun Jul 28 2013 Nick Bebout <nb@fedoraproject.org> - 1.555-1
- Upgrade to 1.555

* Fri Jul 5 2013 Nick Bebout <nb@fedoraproject.org> - 1.547-1
- Upgrade to 1.547

* Tue May 21 2013 Nick Bebout <nb@fedoraproject.org> - 1.542-2
- Add additional perl deps to make XOAUTH work

* Mon May 20 2013 Nick Bebout <nb@fedoraproject.org> - 1.542-1
- Upgrade to 1.542

* Mon Apr 22 2013 Nick Bebout <nb@fedoraproject.org> - 1.536-1
- Upgrade to 1.536

* Wed Feb 20 2013 Nick Bebout <nb@fedoraproject.org> - 1.525-1
- Upgrade to 1.525

* Thu Jan 17 2013 Nick Bebout <nb@fedoraproject.org> - 1.518-2
- Fix spec to install COPYING file now

* Thu Jan 17 2013 Nick Bebout <nb@fedoraproject.org> - 1.518-1
- Upgrade to 1.518


* Tue Nov 27 2012 Nick Bebout <nb@fedoraproject.org> - 1.516-1
- Upgrade to 1.516

* Tue Sep 11 2012 Nick Bebout <nb@fedoraproject.org> - 1.508-1
- Upgrade to 1.508

* Mon Sep 10 2012 Nick Bebout <nb@fedoraproject.org> - 1.504-1
- Upgrade to 1.504

* Thu Aug 2 2012 Nick Bebout <nb@fedoraproject.org> - 1.498-1
- Upgrade to 1.498

* Mon Apr 16 2012 Nick Bebout <nb@fedoraproject.org> - 1.488-1
- Upgrade to 1.488

* Sat Feb 18 2012 Nick Bebout <nb@fedoraproject.org> - 1.484-1
- Upgrade to 1.484

* Tue Dec 13 2011 Nick Bebout <nb@fedoraproject.org> - 1.476-1
- Upgrade to 1.476

* Mon Nov 21 2011 Nick Bebout <nb@fedoraproject.org> - 1.468-1
- Upgrade to 1.468

* Thu Sep 8 2011 Nick Bebout <nb@fedoraproject.org> - 1.456-1
- Upgrade to 1.456

* Mon Jul 11 2011 Nick Bebout <nb@fedoraproject.org> - 1.452-1
- Added the --search option allowing to select messages with the powerful IMAP SEARCH command.
- Added IO::Socket::INET version info.
- Bugfix. Fixed ps call to work with Solaris 10. Thanks to Daniel Rohde.
- Kerio 7.2.0P1 success.
- MDaemon 12.0.3 success.
- Bugfix. Date reference to select messages with --maxdate --mindate is the beginning of imapsync run now.
- Added PERMANENTFLAGS output with --debugflags

* Tue May 31 2011 Nick Bebout <nb@fedoraproject.org> - 1.446-1
- Bugfix. Try to handle Markus bug in foldersizes() when select_msgs() returns a list of undef.
- Check if uidexpunge is supported at the beginning of execution, not when needed.
- Set --uidexpunge2 if --delete2 or --expunge2 if uidexpunge not supported.
- Changed all warn() calls (STDERR) to print calls (STDOUT)
- good_date() "24 Aug 77" -> "24-Aug-1977"
- Patched tests_good_date() and good_date() with Dax Kelson patches.
- Started code to deal with epoch of messages.
- Handle better folder creation, not a failure when folder "already exists" during its creation.
- Replaced default setting. Now --delete2 sets --uidexpunge2 instead of --expunge2 (unless --nouidexpunge2 is set)
- Added epoch() routine to prepare the safe bidirectional sync (maybe...)
- Adapted the usage output multiline character to Unix or Win, \ or ^
- Bugfix. Avoid a "no number" warning when size is null.
- Added "Date" in the default --useheader list. ("Message-Id", "Message-ID", "Date")
- Bugfix. Bad header beginning with a blank character.

* Tue May 24 2011 Nick Bebout <nb@fedoraproject.org> - 1.434-1
- Bugfix. Made --usecache work with --maxage or --maxsize or --min*
- Improved the way imapsync deals with headers:
-  - Stopped getting first 2KB of message. Not a good idea.
-  - If $imap2->parse_headers() fails then take the whole header (instead of body).
-  - Default is like --useheader Message-Id --useheader Message-ID
-  - Use header Message-Id and header Date as sig md5 when taking the whole header.
- Better output in debug mode.
- Options --usecache and --maxsize --minsize can safely be used if --delete is there
- Added tests of mkpath very long path > 300 char. Win32 fails on them.
- Bugfix. Added special case for Inbox vs INBOX bug creation ("Couldn't create folder [Inbox] from [INBOX]: 143 NO INBOX already exists!")
- Adapted regression tests for good_date() when no zone is given.
- Bugfix. intarnal date needs zone data. Default to  +0000.
- Bugfix. Starttls() only for 2.2.9
- Fix. Removed a debug print always printed.
- Bugfix. Changed the way imapsync knows whether a folder exists or not. Exchange might be happy and stop deconnecting for this reason.
- Added a warning and die if --usecache and one of  --maxsize--minsize --maxage --minage is used.
- Bugfix. Reconnections are well done in tls mode now.
- Zimbra 5.0.24_GA_3356.RHEL4 [host1]
- Exchange 2010 SP1 RU2 [host2]
- Added --debugsleep to have to play will kill and reconnections.

* Mon May 16 2011 Nick Bebout <nb@fedoraproject.org> - 1.422-1
- Added --debugLIST to track messages list uid or number only.
- Bugfix: a lack of variable initialisation caused to fetch no existing messages.
-  The APPEND error then the FETCH 0 byte error may be fixed now.
- relogin1 before each folder select.
- --splitX are set into sub login_imap() now.
- Added --relogin1 option (--relogin1 5) to force a reconnection when FETCH message fails on host1.
- Added --debugcontent to avoid debugging content (can be big) with --debug option.
- Added --debugflags to permit flag debugging only.
- Added --flagsCase to correct flag case that are not RFC compliant \SEEN -> \Seen (on by default).
- Added output to track 0 byte messages during the fetch on host1.
- Bugfix. --proxyauth2 was setting proxyauth1!
-  Thanks to Denis BREAN!
- MDaemon 12
- Exchange 6.5 host1
- Bugfix. Modified create_folder() to avoid Inbox -> INBOX problem ("already exists").
- Bugfix. --maxsize --minsize now work with --useuid
- Bugfix. flag sync of already transfered messages now take care of --maxsize --minsize options.
- --delete2 implies --expunge2 now unless --noexpunge2 is given.
- exit if --delete and --delete2 are given together.
- Same behavior for --expunge or --expunge1.
- Added 0 length message tracking when fetching host1.

* Sun Apr 24 2011 Nick Bebout <nb@fedoraproject.org> - 1.411-1
- Bugfix for "Folders in host2 not in host1" list when
- folders are given by --folder option or equivalent.
- The old list listed too many folders with --folder INBOX for example.
- Updated success list.
- Added --takebody option.
- Added  Gimap (Gmail imap) success.
- Added IMail 11.03 [host1] success
- Made --delete2 works with --uselib or --usecache
- No longer --useuid with --fast
- Debug output with permanentflags.
- Added isync url.
- Sleep 2 seconds after foldersizes calls.

* Sat Apr 2 2011 Nick Bebout <nb@fedoraproject.org> - 1.404-3
- Add dependency on Authen::NTLM

* Wed Mar 16 2011 Nick Bebout <nb@fedoraproject.org> - 1.404-2
- Remove dependency on Date::Manip and Mail::Box

* Mon Feb 21 2011 Nick Bebout <nb@fedoraproject.org> - 1.404-1
- Upgrade to 1.404

* Wed Feb 16 2011 Nick Bebout <nb@fedoraproject.org> - 1.398-1
- Upgrade to 1.398

* Sun Dec 5 2010 Nick Bebout <nb@fedoraproject.org> - 1.366-1
- Upgrade to 1.366

* Tue Aug 10 2010 Nick Bebout <nb@fedoraproject.org> - 1.340-1
- Upgrade to 1.340

* Thu Jul 22 2010 Nick Bebout <nb@fedoraproject.org> - 1.337-1
- Upgrade to 1.337

* Wed Jun 16 2010 Nick Bebout <nb@fedoraproject.org> - 1.315-1
- Upgrade to 1.315

* Fri May 28 2010 Nick Bebout <nb@fedoraproject.org> - 1.311-1
- Upgrade to 1.311
- License is now WTFPL

* Tue Aug 4 2009 Nick Bebout <nb@fedoraproject.org> - 1.286-1
- Upgrade to 1.286

* Fri Aug  8 2008 Lubomir Rintel <lkundrak@v3.sk> - 1.255-3
- Attempt to patch around too new Mail::IMAPClient

* Wed Aug  6 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.255-2
- Upstream release

* Tue May 27 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.252-2
- Upstream release
- Dependency fix (BZ#447800)

* Thu Apr 10 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.249-1
- Initial build.
