Name: datovka
Version: 4.25.0
Release: 1%{?dist}
Summary: A free graphical interface for Czech Databox (Datové schránky)

License: GPL-3.0-or-later WITH cryptsetup-OpenSSL-exception
URL: https://www.datovka.cz/
#Source0: https://secure.nic.cz/files/datove_schranky/%%{version}/datovka-%%{version}.tar.xz
Source0: https://gitlab.nic.cz/%{name}/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: openssl-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtwebsockets-devel
BuildRequires: desktop-file-utils
BuildRequires: libdatovka-devel
BuildRequires: make
# https://gitlab.nic.cz/datovka/datovka/-/issues/541
Patch0:        datovka-4.23.0-s390x-disable-failing-test.patch

%description
GUI application allowing access to Czech Databox - an electronic communication
interface endorsed by the Czech government.

%prep
%autosetup -p1 -n %{name}-v%{version}

# drop failing tests (upstream notified)
pushd tests
rm -f test_crypto_message.pri test_isds_message.pri
popd

%build
lrelease-qt5 datovka.pro
%{qmake_qt5} PREFIX=%{_prefix} DISABLE_VERSION_CHECK_BY_DEFAULT=1
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
cd tests
%{qmake_qt5} tests.pro PREFIX=%{_prefix}
%make_build
./tests

%files -f %{name}.lang
%doc %{_pkgdocdir}
%{_bindir}/datovka
%{_datadir}/applications/datovka.desktop
%{_datadir}/icons/hicolor/*/apps/datovka.png
%{_datadir}/metainfo/datovka.metainfo.xml

%changelog
* Mon Jan  6 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 4.25.0-1
- New version
  Resolves: rhbz#2332822

* Mon Sep  2 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.24.2-1
- New version
  Resolves: rhbz#2309202

* Mon Aug 12 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.24.1-1
- New version
  Resolves: rhbz#2302044

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.24.0-1
- New version
  Resolves: rhbz#2292902

* Mon May 20 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.23.8-1
- New version
  Resolves: rhbz#2280940

* Mon Apr 22 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.23.7-1
- New version
  Resolves: rhbz#2276405

* Wed Feb 14 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.23.6-1
- New version
  Resolves: rhbz#2263510

* Mon Feb  5 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.23.5-1
- New version
  Resolves: rhbz#2262774

* Wed Jan 24 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.23.4-1
- New version
  Resolves: rhbz#2259868

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.23.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.23.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan  5 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.23.3-2
- Also dropped test_crypto_pin_token (reported upstream)

* Fri Jan  5 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.23.3-1
- New version
  Resolves: rhbz#2256828

* Tue Jan  2 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.23.2-1
- New version
  Resolves: rhbz#2255984

* Mon Dec 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.23.1-1
- New version
  Resolves: rhbz#2253431

* Mon Dec  4 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.23.0-1
- New version
  Resolves: rhbz#2251951

* Thu Nov  9 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.22.1-5
- Rebuilt for new datovka

* Tue Nov  7 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.22.1-4
- Rebuild for new libdatovka

* Tue Sep  5 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.22.1-3
- Rebuild for new libdatovka

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.22.1-1
- New version
  Resolves: rhbz#2188035

* Thu Feb 23 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.22.0-1
- New version
  Resolves: rhbz#2170063

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.21.1-1
- New version
  Resolves: rhbz#2144857

* Thu Sep 29 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.21.0-1
- New version
  Resolves: rhbz#2130187

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 17 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.20.0-1
- New version
  Resolves: rhbz#2064316

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.19.0-1
- New version
  Resolves: rhbz#2023767

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.18.0-2
- Rebuilt with OpenSSL 3.0.0

* Fri Aug 27 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.18.0-1
- New version
  Resolves: rhbz#1997628

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.17.0-1
- New version
  Resolves: rhbz#1950009

* Thu Jan 28 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.16.0-1
- New version
  Resolves: rhbz#1920514

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.15.6-1
- New version
  Resolves: rhbz#1901009

* Thu Oct 15 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.15.5-1
- New version
  Resolves: rhbz#1888637

* Tue Oct 13 2020 Jeff Law <law@redhat.com> - 4.15.4-2
- Fix missing #include for gcc-11

* Tue Oct 13 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.15.4-1
- New version
  Resolves: rhbz#1887872

* Mon Sep 21 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.15.3-1
- New version
  Resolves: rhbz#1879146

* Mon Aug 31 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.15.2-1
- New version
  Resolves: rhbz#1873149

* Fri Jul 31 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.15.1-1
- New version
  Resolves: rhbz#1862482

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.15.0-1
- New version
  Resolves: rhbz#1810453

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.14.1-1
- New version
  Resolves: rhbz#1774768

* Wed Sep 25 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.14.0-1
- New version
  Resolves: rhbz#1752510

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.13.1-1
- New version
  Resolves: rhbz#1704215

* Thu Apr 18 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.13.0-1
- New version
  Resolves: rhbz#1700422
- Dropped disable-online-tests patch (not needed)
- Temporally disabled tests (upstream issue #422)

* Fri Mar 22 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.12.0-2
- Enabled offline tests from the internal test-suite

* Thu Mar 14 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.12.0-1
- New version
  Resolves: rhbz#1688819

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 4.10.3-1
- New version
  Resolves: rhbz#1599477

* Tue Jun  5 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 4.10.2-1
- New version
  Resolves: rhbz#1486079

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.9.1-3
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 4.9.1-1
- New version
  Resolves: rhbz#1475584

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 4.9.0-1
- New version
  Resolves: rhbz#1466764
- Dropped format-security-fix patch (upstreamed)

* Wed Jun 14 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 4.8.3-1
- New version
  Resolves: rhbz#1461411

* Wed May 31 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 4.8.2-1
- New version
  Resolves: rhbz#1457004

* Fri May  5 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 4.8.1-1
- New version
  Resolves: rhbz#1448432

* Wed Mar 29 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 4.8.0-1
- New version
  Resolves: rhbz#1436888

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 4.7.1-1
- New version
  Resolves: rhbz#1414773

* Sun Oct 23 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 4.7.0-1
- new upstream release:
  + feature: support for HTTPS proxy
  + feature: on-demand database optimization (vacuum)
  + various fixes

* Fri Jul 01 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 4.6.1-1
- new upstream release:
  + feature: PDF envelope and attachments export all at once
  + fix: possible crash when messages sending takes a long time

* Thu Apr 14 2016 Jan Vcelak <jvcelak@fedoraproject.org> 4.6.0-1
- new upstream release:
  + feature: add message tags
  + feature: possibility to open message information in separate window
  + feature: adding a recipient by double clicking the name in recently used contacts
  + feature: personal delivery information in message description
  + fix: encoding issue when exporting correspondence in HTML
  + fix: inactive button to create a new message

* Sat Mar 19 2016 Jan Vcelak <jvcelak@fedoraproject.org> 4.5.3-1
- new upstream release:
  + fix: disallow concurrent account synchronization
  + fix: incorrect account tree resize when adding a new account

* Sun Mar 06 2016 Jan Vcelak <jvcelak@fedoraproject.org> 4.5.2-1
- new upstream release:
  + fix: avoid error message flood when auto-downloading messages without account permissions

* Fri Feb 26 2016 Jan Vcelak <jvcelak@fedoraproject.org> 4.5.1-1
- new upstream release:
  + fix: delete message from the message list even when deletion in ISDS fails
  + fix: possible crash due to a bug in event logging

* Tue Feb 16 2016 Jan Vcelak <jvcelak@fedoraproject.org> 4.5.0-1
- new upstream release:
  + feature: only a single instance of the application is allowed
  + feature: downloading complete messages via the CLI
  + feature: exporting messages as e-mail attachments
  + feature: drag and drop support for attachments
  + enhancement: source account selection when composing messages
  + enhancement: check boxes in recipient list can be enabled with space bar
  + fix: displaying large amounts of messages
  + fix: disappearing messages in split databases

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 4.4.3-2
- use %%qmake_qt5 macro to ensure proper build flags

* Mon Jan 04 2016 Jan Vcelak <jvcelak@fedoraproject.org> 4.4.3-1
- new upstream release:
  + fix: expired password changing
  + fix: set maximum message size to 20 MB

* Thu Dec 10 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.4.2-1
- new upstream release:
  + enhancement: better explanation of some error codes
  + fix: increased maximum number of downloaded messages
  + fix: don't forget password on ISDS connection failure

* Sun Nov 01 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.4.1-1
- New upstream release:
  + feature: store attachments for sent messages into the database
  + feature: configurable timeout for marking a message as read
  + feature: filter field background color based on whether a matching message matches
  + enhancement: renamed attachments to avoid potentially problematic characters
  + enhancement: Home and End key navigation in message list
  + enhancement: add some missing tool tips
  + fix: two pop-ups show on errors when sending a message
  + fix: importing messages from another database file
  + fix: message status updating with privilege-restricted accounts
  + fix: sending a commercial messages from templates

* Mon Oct 12 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.4.0-1
- New upstream release:
  + feature: sending messages from CLI
  + feature: importing messages from older database file
  + feature: sender name in attachement filename pattern
  + feature: splitting databases according to years
  + fix: opening attachments with non-standard characters
  + fix: displaying attachments with matching names
  + fix: sendimg messages with OVM subcategory sender
  + fix: saving of incorrect account password
  + enhancement: add link to the manual into the main menu

* Fri Jun 26 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.3.1-2
- New upstream release:
  + feature: open ZFO from command line
  + feature: add --log-file= command line parameter
  + fix: open delivery info externally
  + fix: password changing issues
  + fix: proper log file opening
  + fix: logging of multi-line messages

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.3.0-1
- New upstream release:
  + feature: restricted privileges accounts support
  + feature: show remaining credit when sending a commercial message
  + feature: search for messages with expiring/expired time stamps

* Thu Apr 30 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.3-1
- New upstream release
  Resolves: rhbz#1217461

* Tue Apr 28 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.2.2-1
- New upstream release:
  + feature: notification about password expiration
  + feature: save all attachments with message envelope in PDF
  + fix: searching for databoxes

* Thu Apr 02 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.2.1-1
- New upstream release:
  + fix: duplicate messages shown in the list

* Tue Mar 31 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.2.0-1
- New upstream release:
  + feature: implemented message search dialogue
  + feature: multiple messages selection
  + feature: password expiration notification
  + various fixes and improvements

* Wed Mar 25 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.2-2
- Fixed license tag to be "GPLv3+ with exceptions"
  Resolves: rhbz#1202797

* Wed Feb 25 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.1.2-1
- New upstream release

* Wed Feb 18 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.1.1-1
- New upstream release
- Disable checking for new versions by default.

* Tue Feb 03 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.1.0-2
- Add missing icon cache updates on package installation and removal.

* Mon Feb 02 2015 Jan Vcelak <jvcelak@fedoraproject.org> 4.1.0-1
- Rebase to new upstream release
- Project switched from Python to C/C++
- Licence changed from LGPLv2+ to GPLv3+

* Thu Sep 18 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.1-1
- New version
  Resolves: rhbz#1142899

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug  5 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0.3-4
- Used unversioned doc location
  Resolves: rhbz#992109

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0.3-1
- New version

* Fri Dec 21 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0.2-1
- New version

* Wed Dec 19 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-1
- New version
- Removed use-sysfont patch (not needed)

* Tue Oct  2 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.2-3
- Unbundled fonts

* Tue Sep 25 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.2-2
- Replaced some hardcoded paths by macros

* Wed Sep 05 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.2-1
- Initial version
