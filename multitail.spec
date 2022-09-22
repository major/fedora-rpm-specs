Name:		multitail
Version:	6.5.0
Release:	7%{?dist}
Summary:	View one or multiple files like tail but with multiple windows

# License GPLv2 specified in readme.txt
License:	GPLv2
URL:		https://www.vanheusden.com/multitail/
Source:		https://www.vanheusden.com/multitail/multitail-%{version}.tgz

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	ncurses-devel

%description
MultiTail lets you view one or multiple files like the original tail
program. The difference is that it creates multiple windows on your
console (with ncurses). It can also monitor wildcards: if another file
matching the wildcard has a more recent modification date, it will
automatically switch to that file. That way you can, for example,
monitor a complete directory of files. Merging of 2 or even more
logfiles is possible.
It can also use colors while displaying the logfiles (through regular
expressions), for faster recognition of what is important and what not.
Multitail can also filter lines (again with regular expressions) and
has interactive menus for editing given regular expressions and
deleting and adding windows. One can also have windows with the output
of shell scripts and other software. When viewing the output of 
external software, MultiTail can mimic the functionality of tools like
'watch' and such.

%prep
%setup -q

# Fix up examples permissions
chmod 644 conversion-scripts/colors-example.*
chmod 644 conversion-scripts/convert-*.pl

%build
%make_build CFLAGS="%{optflags}" CONFIG_FILE=%{_sysconfdir}/%{name}.conf

%install
# Create necessary directories
mkdir -p %{buildroot}%{_sysconfdir}
%make_install PREFIX=%{_prefix} CONFIG_FILE=%{buildroot}%{_sysconfdir}/%{name}.conf

# move the configuration in the right place
mv -f %{buildroot}%{_sysconfdir}/multitail.conf{.new,}

# remove the examples (installed as docs)
rm -f %{buildroot}%{_prefix}%{_sysconfdir}/multitail/colors-example.*
mv -f %{buildroot}{%{_prefix},}%{_sysconfdir}/multitail/

# remove documentation later catched up by %%doc
rm -rf %{buildroot}%{_docdir}/

%files
%license license.txt
%doc manual*.html readme.txt conversion-scripts/colors-example.*
%config(noreplace) %{_sysconfdir}/multitail.conf
%{_sysconfdir}/multitail/
%{_bindir}/multitail
%{_mandir}/man1/multitail.1*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Robert Scheck <robert@fedoraproject.org> - 6.5.0-1
- Upgrade to 6.5.0 (#1771093)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.4.2-7
- Added gcc buildrequires.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Jon Stanley <jonstanley@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 18 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.2.1-1
- Update to 6.2.1 (BZ #1064754).
- Update license tag from GPL+ to GPLv2.
- Revert "cleaning up" made in previous release to not break EPEL branches.

* Mon Dec 16 2013 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 6.0-1
- New upstream release 6.0
  Resolves: rhbz:1035637
- Add a patch to use unversioned doc dirs. Ref: http://fedoraproject.org/wiki/Changes/UnversionedDocdirs
- Remove BuildRoot tag.
- Remove %%clean section and remove the %%defattr section from %%files
  section.

* Fri Jul 26 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.2.13-1
- Keep the conversion scripts in %%{_sysconfdir}, as they may be
  called by the configuration (see multitail.conf).
- Update to 5.2.13.
- Fixed license tag.

* Tue Feb 26 2013 Fabio M. Di Nitto <fdinitto@redhat.com> - 5.2.12-1
- New upstream release
  Resolves: rhbz#915221

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 2 2011 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 5.2.8-1
- New upstream release 5.2.8

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 10 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 5.2.6-1
- New upstream release
  Resolves: rhbz#550857
- Update spec file:
  * Fix licence tag again
  * Cleanup whitespaces
  * Cleanup macros

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.2.2-2
- fix license tag

* Tue Jul  8 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 5.2.2-1
- New upstream release
- Fix licence tag
- Fix documentation encoding to UTF8
- Install some examples in doc dir

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.2.0-3
- Autorebuild for GCC 4.3

* Mon Oct  2 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 4.2.0-2
- Rebuild (https://www.redhat.com/archives/fedora-maintainers/2006-October/msg00005.html).

* Mon Sep 18 2006 Folkert van Heuesden <folkert@vanheusden.com> - 4.2.0-1
- Updated to release 4.2.0.

* Wed Jun 28 2006 Folkert van Heuesden <folkert@vanheusden.com> - 4.0.6-1
- Updated to release 4.0.6.

* Tue Jun  6 2006 Folkert van Heuesden <folkert@vanheusden.com> - 4.0.5-1
- Updated to release 4.0.5.

* Wed May 24 2006 Folkert van Heuesden <folkert@vanheusden.com> - 4.0.4-1
- Updated to release 4.0.4.

* Wed Apr 19 2006 Folkert van Heuesden <folkert@vanheusden.com> - 4.0.3-1
- Updated to release 4.0.3.

* Wed Apr 12 2006 Folkert van Heuesden <folkert@vanheusden.com> - 4.0.0-1
- Updated to release 4.0.0.

* Thu Mar 30 2006 Folkert van Heuesden <folkert@vanheusden.com> - 3.8.10-1
- Updated to release 3.8.10.

* Tue Mar 14 2006 Folkert van Heuesden <folkert@vanheusden.com> - 3.8.9-1
- Updated to release 3.8.9.

* Thu Feb 23 2006 Udo van den Heuvel <udovdh@xs4all.nl> - 3.8.7-3
- Small changes as suggested in #182122.
- Updated to release 3.8.7-3.

* Thu Feb 23 2006 Udo van den Heuvel <udovdh@xs4all.nl> - 3.8.7-2
- Small changes as suggested in #182122.
- Updated to release 3.8.7-2.

* Thu Feb 23 2006 Udo van den Heuvel <udovdh@xs4all.nl> - 3.8.7-1
- Updated to release 3.8.7-1.

* Thu Feb 23 2006 Udo van den Heuvel <udovdh@xs4all.nl> - 3.8.7
- Updated to release 3.8.7.

* Sat Feb 18 2006 Udo van den Heuvel <udovdh@xs4all.nl> - 3.8.6
- Imported Dries' SPEC file
- Updated to release 3.8.6.

* Mon Jan 30 2006 Dries Verachtert <dries@ulyssis.org> - 3.8.5-1 - 4025/dries
- Updated to release 3.8.5.
