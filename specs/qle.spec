Name:           qle
Version:        0.0.18
Release:        39%{?dist}
Summary:        A QSO Logger and log Editor

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://home.kpn.nl/w.knol18/qle/qle.html
Source0:        http://home.kpn.nl/w.knol18/%{name}/%{name}-%{version}.tar.gz
Source1:        qle.desktop
Source2:        qle.png
#add script shebang & fix paths
Patch0:         qle-0.0.18-sh.patch
#Fix configuration path
Patch1:         qle-0.0.18-configlocation.patch

BuildArch:      noarch

Requires:       perl-interpreter, perl(DBI), perl(DBD::SQLite), perl(Tk), perl(PDF::Create)
#qle requires rigctld from hamlib for communicating with transciever
Requires:       hamlib
Requires:       cwdaemon
BuildRequires:  desktop-file-utils
BuildRequires:  perl-generators

%description
The qle-package is a graphic QSO log viewer, log editor and QSO logger
for amateur radio operators.

'qle' stands  for QSO Logger and  Editor. It is a  Perl/Tk script that
logs (or modifies)  QSOs directly  in a  fast and  light-weight SQLite
database.

The term QSO comes from Q code used in commercial and amateur radio
communication and in refers to a radio contact.

Intended use: casual logging of  rag-chew and contest QSOs. The logger
caters for CW operators.

Table  headings, fonts,  colours and  other  attributes are  set in  a
user-editable configuration  file. The SQLite log  schema supplied may
be  altered to  suit your  taste, provided  the configuration  file is
updated accordingly.



%prep
%setup -q
%patch -P0 -p1 -b .sh
%patch -P1 -p1 -b .configlocation

%build
#no build needed

%install
rm -rf $RPM_BUILD_ROOT
install -p -D -m 0644 kiwi-blk-52x52.xbm $RPM_BUILD_ROOT%{_datadir}/%{name}/kiwi-blk-52x52.xbm
install -p -D -m 0644 foo3.db $RPM_BUILD_ROOT%{_datadir}/%{name}/foo3.db
install -p -D -m 0644 dupeID $RPM_BUILD_ROOT%{_datadir}/%{name}/dupeID.db
install -p -D -m 0755 adifimport.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/adifimport.pl
install -p -D -m 0755 cabrilloimport.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/cabrilloimport.pl
install -p -D -m 0755 qle-%{version}.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/qle.pl
install -p -D -m 0755 showfonts.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/showfonts.pl
install -p -D -m 0755 showcolor.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/showcolor.pl
install -p -D -m 0644 master.scp $RPM_BUILD_ROOT%{_datadir}/%{name}/master.scp
install -p -D -m 0644 cty.dat $RPM_BUILD_ROOT%{_datadir}/%{name}/cty.dat
install -p -D -m 0644 exampleQSL.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/exampleQSL.jpg
install -p -D -m 0755 qle.sh $RPM_BUILD_ROOT%{_bindir}/qle
install -p -D -m 0644 qle-%{version}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/qle.conf
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
desktop-file-install \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}


%files
%doc AUTHORS BUGS NEWS README COPYING
%dir /etc/%{name}
%config(noreplace) /etc/%{name}/%{name}.conf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop


%changelog
* Thu Feb 06 2025 Richard Shaw <hobbes1069@gmail.com> - 0.0.18-39
- Rebuild for hamlib 4.6.

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.18-37
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 0.0.18-31
- Rebuild for hamlib 4.5.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 0.0.18-28
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 0.0.18-27
- 36-build-side-49086

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 0.0.18-26
- Rebuild for hamlib 4.3.1.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 0.0.18-24
- Rebuild for hamlib 4.2.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 0.0.18-23
- Rebuild for hamlib 4.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.0.18-14
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.0.18-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 10 2010 Lucian Langa <cooly@gnome.eu.org> - 0.0.18-3
- add exampleQSL.jpg to install

* Sun Jan 10 2010 Lucian Langa <cooly@gnome.eu.org> - 0.0.18-2
- sh wrapper supports multiuser
- update patches
- add dupeID to install

* Sat Jan 09 2010 Lucian Langa <cooly@gnome.eu.org> - 0.0.18-1
- new upstream release

* Mon Dec 21 2009 Lucian Langa <cooly@gnome.eu.org> - 0.0.17-2
- fix build requires

* Fri Nov 27 2009 Lucian Langa <cooly@gnome.eu.org> - 0.0.17-1
- improve desktop icon file (#530837)
- update patch0
- new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Lucian Langa <cooly@gnome.eu.org> - 0.0.13-1
- drop hamlib-perl dependency and require only hamlib
- new upstream release

* Sun Nov 23 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.10-5
- add missing patch

* Sun Nov 23 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.10-4
- add missing patch

* Thu Nov 20 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.10-3
- fix unowned dir
- fix description

* Thu Aug 28 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.10-2
- added desktop/icon file

* Wed Aug 20 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.10-1
- Misc cleanups
- Version Update

* Sat Feb 16 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.0.8-1
- Version Update
* Fri Dec 07 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.0.7-3
- Fix file permissions
- Update launcher scripts
- Add missing files
- Update license tag
- Make package noarch
- Add cwdaemon dependency
* Fri Dec 07 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.0.7-2
- Fixed File Paths

* Tue Nov 20 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.0.7-1
- Initial SPEC

