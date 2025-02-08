Name:		cqrlog
Version:	2.5.2
Release:	18%{?dist}
Summary:	An amateur radio contact logging program

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://www.cqrlog.com/
Source0:	https://github.com/ok2cqr/cqrlog/archive/v%{version}/%{name}-%{version}.tar.gz

# Fixes arm builds, translation improvements, and other bug fixes.
Patch0:         cqrlog-install.patch
Patch1:         cqrlog-desktop.patch

ExclusiveArch:  %{fpc_arches}

BuildRequires:	desktop-file-utils
BuildRequires:	fpc >= 3.0.4
BuildRequires:	lazarus >= 1.8
BuildRequires:  libappstream-glib
BuildRequires:  make

Requires:	mariadb-server
# https://bugzilla.redhat.com/show_bug.cgi?id=1486480
%if 0%{?fedora}
Requires:       mariadb-connector-c
# https://bugzilla.redhat.com/show_bug.cgi?id=1592176
Requires:       mariadb-connector-c-devel
%else
Requires:       mariadb-libs
%endif
Requires:       hamlib 
Requires:       openssl
%if 0%{?fedora}
Requires:       tqsllib
%endif


%description
CQRLOG is an advanced ham radio logger based on MySQL database. Provides radio
control based on hamlib libraries (currently support of 140+ radio types and 
models), DX cluster connection, QRZ callbook (web version), a grayliner, 
internal QSL manager database support and a most accurate country resolution 
algorithm based on country tables developed by OK1RR. CQRLOG is intended for 
daily general logging of HF, CW & SSB contacts and strongly focused on easy 
operation and maintenance.

%prep
%autosetup -p1

chmod -x src/azidis3.pas
chmod -x src/gline2.pas
chmod -x src/odbec.pas
chmod -x src/aziloc.pas
chmod -x src/znacmech.pas
chmod -x tools/cqrlog-apparmor-fix
chmod -x voice_keyer/voice_keyer.sh



%build
make %{?_smp_mflags}


%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/cqrlog.desktop

# Fix icon location
for size in 32 48 64 128 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
    mv images/icon/${size}x${size}/%{name}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
done

for file in $(find %{buildroot}%{_datadir}/%{name} -name "*.txt"); do
    sed -i 's/\r//' $file
done
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/ctyfiles/CountryDel.tab
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/ctyfiles/MASTER.SCP

iconv -f iso8859-1 -t utf-8 %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt > %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt.conv && mv -f %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt.conv %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%files
%license COPYING
%doc README.md AUTHORS CHANGELOG
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/cqrlog.1.gz


%changelog
* Thu Feb 06 2025 Richard Shaw <hobbes1069@gmail.com> - 2.5.2-18
- Rebuild for hamlib 4.6.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.2-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 2.5.2-10
- Rebuild for hamlib 4.5.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.2-7
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.2-5
- Rebuild for hamlib 4.4.

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.2-4
- Rebuild for hamlib 4.3.1.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.2-2
- Rebuild for hamlib 4.2.

* Sat Feb 13 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.2-1
- Update to 2.5.2.

* Fri Feb 05 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.1-1
- Update to 2.5.1.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.0-3
- Rebuild for hamlib 4.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.0-1
- Update to 2.5.0.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Richard Shaw <hobbes1069@gmail.com> - 2.4.0-2
- Add patch to deal with JTDX UDP issue.

* Mon Nov 11 2019 Richard Shaw <hobbes1069@gmail.com> - 2.4.0-1
- Update to 2.4.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Richard Shaw <hobbes1069@gmail.com> - 2.3.0-3
- Clean up scripts that are no longer required by the packaging guidelines.

* Sat Oct 27 2018 Jim Lieb <lieb@sea-troll.net.> - 2.3.0-3
- Fix mysql/mariadb client lib search path

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Richard Shaw <hobbes1069@gmail.com> - 2.3.0-1
- Update to 2.3.0.
- Fix dependency on libmysqlclient.so, fixes RHBZ#1592176.

* Thu Mar 01 2018 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-4
- Fix arm builds, improved translations, and other fixes.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.0-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-1
- Update to latest upstream release.
- Disable armv7hl until fpc/lazarus is fixed.

* Fri Sep 22 2017 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-2
- Fix mariadb requires for Fedora 28 and up.
  https://bugzilla.redhat.com/show_bug.cgi?id=1486480

* Mon Aug 07 2017 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-1
- Update to latest upstream release.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Richard Shaw <hobbes1069@gmail.com> - 2.0.5-1
- Update to latest upstream release, 2.0.5.
- Fix icon install location, fixes BZ#1440477.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Richard Shaw <hobbes1069@gmail.com> - 2.0.4-1
- Update to latest upstream release.

* Mon Aug 29 2016 Richard Shaw <hobbes1069@gmail.com> - 2.0.2-1
- Update to latest upstream release.

* Sat May  7 2016 Richard Shaw <hobbes1069@gmail.com> - 2.0.1-1
- Update to latest upstream release.

* Thu Mar 24 2016 Richard Shaw <hobbes1069@gmail.com> - 1.9.1-3
- Update to latest upstream release.
- Add patch to deal with newer fpc.
- Remove old dependency on openssl-devel.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec  2 2015 Richard Shaw <hobbes1069@gmail.com> - 1.9.1-1
- Update to latest upstream release.

* Thu Jul 23 2015 Richard Shaw <hobbes1069@gmail.com> - 1.9.0-2
- Bump release for new build so it's newer than the temporary COPR builds.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Richard Shaw <hobbes1069@gmail.com> - 1.9.0-1
- Update to latest upstream release.

* Fri Feb  6 2015 Richard Shaw <hobbes1069@gmail.com> - 1.8.3-1
- Update to latest upstream release.

* Fri Oct 24 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.8.1-4
- Allowing builds for ARM.

* Tue Sep 30 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.8.1-3
- Fixed empty debugging (BZ 1126233)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.8.1-1
- Program crashed with error about Exceptions.tbl when started for the first time
- After hit enter in New QSO window, it took long time to save QSO

* Mon Jul 21 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.8.0-1
- after click to "Upload all" qso to online logs, info about disabled services is not shown
- added new optimized MySQL configuration file (log should be faster and won't show error about missing tables)
- additional date formats for QSL label printing added (Tom, DL7BJ)
- alert for for callsign on specific mode and band added
- %%h CW macro added (sends GM/GA/GE calculated from wkd station local time)
- %%rs CW macro added (sends RST_S and replace 9 with N)
- design of gridlists can be changed in Preferences/Fonts/Gridlist settings (Tom, DL7BJ)
- additional options to split RST (TX and RX) in three fields for QSL label printing (Tom, DL7BJ)
- K3NG key support added
- "Use '+' key to add spots to band map" option added to Preferences -> Band map
- program crashed with error about Exceptions.tbl when started for the first time
- Shift+F12 didn't cancel the filtr - fixed
- "Filter is USED!" info wasn't canceled after click to Sort button (filter was disabled)
- reading signal strength from RBN spots fixed
- RBN default port is 7000 not 7300 - fixed
- fixed a bug in DXCC statistics, mode 'Paper QSL only' (Tom, DL7BJ)
- program crashed after close - fixed
- program crashed after click to Cancel in DB connection window
- sunrise, sunse and greeting info was broken - fixed
- xplanet opened from the "New QSO Window" was not centred on own lattitude and longitude

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.7.4-1
- F keys to CW type window added
- address to RBN server can be changed in Preferences
- full date (not only year,month) is supported in membership files
- Close the "Status of log upload" window after successful upload added
- moved to new LoTW url and updated upload routines
- band button description is editable (Preferences -> TRX control -> Change default frequencies)
- 6W/MM0NDX was marked as unknown country instead of Senegal - fixed
- after View QSO and CTRL+F2 fields was still read-only - fixed
- QSL information was added to Commend to QSO even if it already exists
- '+' character is now allowed in any field in New QSO window
- log could not recover from a wrong upload of updated QSO - fixed
- '+' as hotkey to add to bandmap function removed, use CTRL+A instead
- any result from ClubLog with 'Skipping QSO' won't stop uploading of the log

* Fri Feb 07 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.7.3-1
- after hitting ESC in any window opened from NewQSO, cursor will be returned to callsign edit field
- frequency in New QSO and QSO list wondow is formated to 0.0000
- added Help -> Keys and shortcut to menu in QSO window
- RBN integration into GrayLine showed CW speed instead of signal strench - fixed
- DXCC entity window didn't show when compiled in Debian Sid and Ubuntu 13.10 - fixed
- when CQRLOG was run for the first time, two mysqld proccesses opened the same database - fixed
- upload to ClubLog didn't work after enter QSO and delete - fixed (big thanks to Pawel, SQ5LTL)
- TRX control window's layout was broken with some font sizes - fixed

* Wed Jan 29 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.7.1-1
- "When TRX control is not active, use frequency and mode from NewQSO window" option to Preferences->Band map added
- CTRL+N hotkey to QSO list window added (do NOT send QSL)
- TRX control window was not sizeable - fixed
- when ESC was pressed twice in Remote mode, log crashed - fixed
- program crashed when freq was entered with comma as decimal separator - fixed
- broken grid square statistic fixed


* Wed Jan 15 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.7.0-1
- online QSO upload to HamQTH, ClubLog and HRDLog added
- improved QSL managers import, should be faster a bit
- "Long Path" button to Rotor Control added (Darek, SP2MKI)
- COMMENT field is exported to eQSL server
- Always overwrite info from previous QSO with callbook data option added
- help updated
- country files updated
- membership files updated
- layout improved (mostly new QSO window)
- LoTW QSL RCVD was not imported when ADIF didn't include LOTW_QSLRDATE value - fixed
- CONTESTIA mode was saved as CONSTESTI (increased max length of mode to 10 characters) - fixed
- ReverseBeacon support in Gray line didn't work - fixed
- after click to OK button in Preferences, bandmap stopped deleting old spots - fixed
- bandmap was not updated when any spot was not added - fixed
- station was added to bandmap when offline mode was activated - fixed
- big square statistics didn't work in newer versions of distributions - fixed
- QSO JT65* mode were not confirmed by eQSL - fixed

* Wed Dec 25 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.6.1-2
- Let rpmbuild strip executable (#1008236).

* Thu Nov 14 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.6.1-1
- 630M band added
- added OQRS (online QSL request system) to QSL sent menu
- added "Always sort by QSO date" option to Search function
- cursor is moved to last opened log in DB connection window
- "Ask before creating a backup" option to "Auto backup" added
- band map is much faster, a few optimization added
- program froze for a few milliseconds with every bandmap refresh - fixed
- "MySQL server has gone away" problem fixed
- membership values collation were case sensitive - fixed
- ADIF import sometimes crashed with access violation, now will show what happened
- qrz search with right click on a call in the recent QSOs list didn't work
- band map font settings was not loaded when program started

* Tue Sep 10 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.6.0-2
- Fixed rpmlint problems.

* Tue Sep 10 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.6.0-1
- your CQ received by RBN will be visible in gray line map
- local mysqld is executed only when the log is stored to local machine
- added JT9 to list of modes
- added Power field to filter window
- option to show distance in miles instead of km added
- limit of max QSO on QSL label increased
- added whole new bandmap with frequecy indicator
- double click on bandmap didn't work when the spot had split info - fixed
- propagation info in spot notes has correct format
- existing band map record was not updated from dx cluster
- program didn't accept ITU zones 78 and 90 - fixed
- program used QTH from previous QSO even is the station was /P - fixed

* Mon Aug 12 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.8-5
- Added exclusion for armv7hl arch.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.8-3
- Fixed libmysqlclient.so.18 dependency

* Wed Jul 10 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.8-2
- Fixed openssl dependency.

* Tue Jul 9 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.8-1
- Upgraded to version 1.5.8
- Nothing happened after double click on bandmap spot - fixed
- Enter key in Filter window will activate the filter
- Blank locator field in Group edit clears locator field
- ADIF export didn't contain DXCC field with ADIF id of the country
- grayline caused program crash after compile with recent FPC and Lazarus versions
- When the grid was in lowercase, the Big square statistic was broken
- Bandmap didn't worked if the freq of QSO precision was to one Hz
- Debug level settings didn't worked at all
- QSO will be confirmed when time difference between QSO and QSO from LoTW is not more than 10 minutes


* Wed Jun 19 2013 Eric "Sparks" Christensen - 1.5.6-1
- Upgrade to version 1.5.6
- if any error message about LoTW import appear, you can open it in external app directly from CQRLOG
- LoTW upload url changed
- fixed "An invalid integer value" error during label export
- import of QSO with custom digi mode didn't worked if the list of modes didn't ended with comma (,) - fixed
- bandmap didn't worked if the freq of QSO precision was to ten Hz
- station with /AM and /MM caused error "You must enter correct WAZ zone!" - fixed
- removed mode from search criteria to confirm QSO via LoTW
- QSO will be confirmed when time difference between QSO and QSO from LoTW is not more than 1 hour
- default debug level is set 0, if you want to get more info what cqrlog does, run it with debug=1 or more

* Fri Mar 29 2013 Eric "Sparks" Christensen - 1.5.4-1
- Upgrade to version 1.5.4
- fixed problem with MASTER.SCP
- added support for Super Check Partial (Window -> Super Check Partial)
- added Tune function (for WinKeyerUSB and cwdaemon), hotkey CTRL+T
- added Repair table function to database connection window (Utils button)
- improved export for QSL labels printing (labels are sorted by dxcc, you can choose what fields will be be printed)
- updated membership tables
- fixed program crash when editing DX cluster info
- CW keys window doesn't show caption for F9 and F10 keys
- ADIF export ignored delimitter in TX_PWR (0.5 was exported as 05)
- CQRLOG killed rigctld even when autostart was disabled
- double click to spots listed with SH/DX didn't work
- QSO list window showed filter is enabled after reopen (filter was disabled)
- login to eQSL with password containing special character didn't work
- when QSO passed over the midnight, the qso was saved with wrong date

* Thu Feb 28 2013 Eric "Sparks" Christensen - 1.5.2-6
- Fixed OpenSSL requirements

* Fri Feb 22 2013 Eric "Sparks" Christensen - 1.5.2-5
- Repaired desktop category

* Fri Feb 22 2013 Eric "Sparks" Christensen - 1.5.2-4
- Changed openssl-devel from BuildRequires to Requires as it is needed for LoTW functionality

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 9 2012 Dan Horák <dan[at]danny.cz> - 1.5.2-2
- set ExcludeArch to match fpc

* Mon Oct 8 2012 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.2-1
- added CTRL+W hotkey to send spots to dxcluster
- DX cluster shows also country name next to the spot (must be enabled in Prefereces)
- international characters in New QSO window should work again
- DX spots with freq eqauls to the start of the band (21.000, 14.000 etc., usually notes) are ignored
- HamQTH added to dx clusters list
- fixed reading A-index (was 1 even when actually was 10)
- /MM, /AM and stations with unknown DXCC country didn't appear in bandmap
- database update hangs
- fixed xml request address of qrz.com
- DXCC CFM count function didn't uses eQSL cfm QSO
- fixed reading mode from FT-920 (returned MEMO as VFO)
- fixed bug in dxcluster caused program crashed randomly
- program didn't apply eQSL rcvd when the band was in lowercase

* Tue Aug 14 2012 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.1-1
- Initial package
