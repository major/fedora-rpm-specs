Name:    mybashburn
Version: 1.0.2
Release: 27%{?dist}
Summary: Burn data and create songs with interactive dialogs
License: GPLv2+
URL:     http://mybashburn.sf.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Requires: bash
Requires: cdrdao 
Requires: wodim
Requires: genisoimage
Requires: dvd+rw-tools
Requires: icedax
Requires: vorbis-tools
Requires: flac
Requires: coreutils
Requires: eject
Requires: dialog >= 1.0
BuildArch: noarch

%description
MyBashBurn is a fork based on ncurses of the CD burning shell script
called BashBurn for Linux. It can burn bin/cue files, create ogg and
flac files, data, music and multisession CDs, as well as burn and create
ISO files, DVD-images, data DVDs and some other funny options.
MyBashBurn makes use of cdrecord and other back-end applications, so basically
if your writing device works with them, MyBashBurn will work flawlessly.

%prep
%setup -q
sed -i 's/\r//' {lang/Polish/burning.lang,lang/Polish/multi.lang}
iconv -f ISO-8859-1 -t UTF8 < FILES > FILES.tmp
rm -f FILES && mv FILES.tmp FILES

%build 

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}/config
install -d %{buildroot}%{_datadir}/%{name}/burning
install -d %{buildroot}%{_datadir}/%{name}/lang
install -d %{buildroot}%{_datadir}/%{name}/lang/English
install -d %{buildroot}%{_datadir}/%{name}/lang/Polish
install -d %{buildroot}%{_datadir}/%{name}/lang/Swedish
install -d %{buildroot}%{_datadir}/%{name}/lang/German
install -d %{buildroot}%{_datadir}/%{name}/lang/Czech
install -d %{buildroot}%{_datadir}/%{name}/lang/Spanish
install -d %{buildroot}%{_datadir}/%{name}/lang/Norwegian
install -d %{buildroot}%{_datadir}/%{name}/convert
install -d %{buildroot}%{_datadir}/%{name}/misc
install -d %{buildroot}%{_datadir}/%{name}/menus
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_sysconfdir}

# and now, install everything
install -pc -m755 MyBashBurn.sh %{buildroot}%{_datadir}/%{name}/MyBashBurn.sh
install -p man/mybashburn.1.gz %{buildroot}%{_mandir}/man1

cp -pR {etc/,CREDITS,HOWTO} %{buildroot}%{_datadir}/%{name}
cp -pR {lang/,config/,burning/,convert/,misc/,menus/} %{buildroot}%{_datadir}/%{name}
ln -sf ../../usr/share/mybashburn/MyBashBurn.sh %{buildroot}%{_bindir}/mybashburn

%files
%license COPYING
%{_datadir}/%{name}/
%{_bindir}/mybashburn
%doc ChangeLog FAQ FILES README TODO
%attr(0644,root,root) %{_mandir}/man1/mybashburn.1.gz

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  9 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.2-17
- Cleanup and modernise spec

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Thu Jan 27 2008 Wilmer Jaramillo <wilmer@fedoraproject.org> - 1.0.2-3
- Changed license tag with GPLv2+ for sync with fedora license list.
- Compatible with the Version Guidelines.

* Wed Jul 11 2007 Wilmer Jaramillo <wilmer@fedoraproject.org> - 1.0.2-2
- Fixed man permissions and uses macros consistently.
- Removed CREDITS and HOWTO of %%doc section because they're required as internal help.
- Removed name of the package in summary section.

* Sun Apr 22 2007 Wilmer Jaramillo <wilmer@fedoraproject.org> - 1.0.2-1
- Updated man file.

* Mon Jan 29 2007 Wilmer Jaramillo <wilmer@fedoraproject.org> - 1.0.1-2
- Fixed incoherent version in changelog.
- The following tags went used %%{__install} and %%{__rm}.

* Sun Jan 07 2007 Wilmer Jaramillo <wilmer@fedoraproject.org> - 1.0.1-1
- Better auto detection of devices cdreader.
- Removed Install.sh file by more easy and flexible Makefile.
- Added function against race conditions on temp files.
- Added statusbar feature.
- Changed the old location /usr/local/BashBurn by /usr/share/mybashburn. 
- Now MyBashBurn look for the /etc/mybashburnrc, ~/.mybashburnrc in that order.
- Updated man file.
- Support translate of cancel, exit, and help button on some dialog.
- Added more english and spanish translate.
- Option of change the 'root directory' have been deprecated for some time and will be removed.
- Cleanup functions.

* Sun Dec 10 2006 Wilmer Jaramillo <wilmer@fedoraproject.org> - 1.0-3
- Fixed DOS/Windows-like (CRLF) end-of-line encoding with %%{__sed} tag (#217197).
- Replaced %%{_bindir}/* tag of %%files section by %%{_bindir}/files.
- Cleanup in %%install section.
- Replaced %%config(noreplace) instead %%config.
- A lot de fix in man file.
- Added a new task into TODO file.
- Fixed config file place.

* Sun Dec 10 2006 Wilmer Jaramillo <wilmer@fedoraproject.org> - 1.0-2
- Added %%build section.
- Removed INSTALL in %%doc section.
- Added option for preserve timestamps in install command.
- The directory trailing use is fixed.

* Tue Nov 14 2006 Wilmer Jaramillo <wilmer@fedoraproject.org> - 1.0-1
- Initial release of MyBashBurn
- This use MyBashBurn.sh instead of BashBurn.sh
- Probe of concept for dialog box in some options
- Auto detection of devices CD/DVD RW, driver options, languages and mount point
- Added a 'lock dir' that warning about multiple instances
- Include manual file mybashburn.1.gz (man mybashburn)
- Added mybashburn.spec file
