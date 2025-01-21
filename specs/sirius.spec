Name:		sirius
Version:	0.8.0
Release:	49%{?dist}

Summary:	Reversi game for Gnome
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
# The upstream website for sirius has disappeared and a search hasn't
# turned up a new one.
#URL:		http://sirius.bitvis.nu/
#Source0:	http://sirius.bitvis.nu/files/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
Patch0:         sirius-desktop.patch
Patch1:         sirius-libm.patch
# Don't use message as a format string
Patch2:         format-fix.patch

BuildRequires: make
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libgnomeui-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libtool intltool autoconf automake

%description
Sirius is a program for playing the game of reversi. The program includes an AI
(Artificial Intelligence) opponent which plays at a very challenging level and
is actually quite hard to beat. The AI opponent's strength can therefore be
adjusted in several ways to give you a suitable opponent.

The AI opponent uses a plain alpha-beta search with hashing to figure out which
move to make. To be able to tell a good position from a bad one, it uses a
pattern based evaluation function. The pattern used is the 9 discs surrounding
each corner and the 8 discs creating the edge of the board. The evaluation
function also takes mobility, potential mobility and parity into count. For the
initial 9 moves the AI opponent optionally uses a simple opening book. During
midgame it searches and evaluates about 200.000 nodes per second on a PIII
750 MHz, in the endgame this number is significantly higher due to more
transpositions and a less expensive evaluation function.


%prep
%setup -q
%patch -P0
%patch -P1
%patch -P2 -b .format-fix


%build
# Upstream hasn't updated their autotools output in a while and it needs
# to be rebuilt.
intltoolize --force
autoreconf -vif
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog
iconv -f iso8859-1 -t utf-8 README > README.conv && mv -f README.conv README


%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
%find_lang %{name}

desktop-file-install                 --delete-original	\
	--dir %{buildroot}%{_datadir}/applications	\
	--add-category Game				\
	%{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/sirius.desktop


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.0-48
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0-27
- Run autoreconf to update config.guess/sub for new arch support

* Thu Jun 12 2014 Bruno Wolff III <bruno@wolff.to> - 0.8.0-26
- Fix quoting in patch

* Tue Jun 10 2014 Bruno Wolff III <bruno@wolff.to> - 0.8.0-25
- Don't use message as a format string

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> - 0.8.0-22
- Remove vendor prefix from desktop file

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Bruno Wolff III <bruno@wolff.to> - 0.8.0-18
- Rebuild for libpng 1.5
- Add -lm since sqrt stopped be inlined

* Fri Jun 24 2011 Bruno Wolff III <bruno@wolff.to> - 0.8.0-17
- Note that upstream has disappeared
- Run autogen.sh, since upstreams autotools stuff is out of date
- Use iconv instead of a patch to convert doc files from latin1 to utf8
- Remove image extension in desktop file
- Correct category in desktop file - bug 485368
- Fix FTBFS - bugs 565100 and 715896
- Add build requires needed to run autogen.sh

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.0-13
- Autorebuild for GCC 4.3

* Thu Dec 20 2007 Arindam Ghosh <makghosh AT fedoraproject DOT org> - 0.8.0-12
- Rebuild for F8 

* Fri Oct 05 2007 Arindam Ghosh <makghosh AT gmail DOT com> - 0.8.0-11
- Updated specfile

* Wed Oct 03 2007 Arindam Ghosh <makghosh AT gmail DOT com> - 0.8.0-10
- Added a patch
- Updated specfile
- Bump release

* Sat Sep 29 2007 Arindam Ghosh <makghosh AT gmail DOT com> - 0.8.0-9
- Removed the patch
- Minor fixes in desktop entry

* Thu Sep 20 2007 Arindam Ghosh <makghosh AT gmail DOT com> - 0.8.0-8
- Updated License tag to GPLv2+
- Fixed Build Require to perl(XML::Parser)
- Added INSTALL option in make install
- Removed CFLAGS option from make

* Mon Sep 17 2007 Arindam Ghosh <makghosh AT gmail DOT com> - 0.8.0-7
- Added perl-XML-parser as a build require

* Fri Sep 07 2007 Arindam Ghosh <makghosh AT gmail DOT com> - 0.8.0-6
- Specfile cleanup/Bump Release

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.8.0-5
- Rebuild on all arches

