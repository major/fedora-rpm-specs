Name:		comps-extras
Version:	24
Release:	19%{?dist}
Summary:	Images for package groups

# while GPL isn't normal for images, it is the case here
# No version specified.
# KDE logo is LGPLv2+
# LXDE logo is GPLv2+
# MATE logo is GPLv2+
# Cinnamon logo is taken from getfedora.org and thus CC-BY-SA
# Haskell logo is a variation on MIT/X11
# Sugar and Ruby logos are CC-BY-SA
# See COPYING for more details
# Automatically converted from old format: GPL+ and LGPLv2+ and GPLv2+ and CC-BY-SA and MIT - review is highly recommended.
License:	GPL-1.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-MIT
URL:		https://pagure.io/%{name}
Source0:	https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	fdupes
BuildRequires: make

%description
This package contains images for the components included in this distribution.


%prep
%autosetup -p 1


%build
%make_build


%install
%make_install
%fdupes -s %{buildroot}%{_datadir}/pixmaps


%files
%doc comps.dtd comps-cleanup.xsl
%license COPYING
%{_datadir}/pixmaps/comps


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 24-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 24-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 22 2017 Björn Esser <besser82@fedoraproject.org> - 24-1
- Use the icon from getfedora.org for Cinnamon
- Symlink all files in %%{_datadir}/pixmaps

* Fri Apr 21 2017 Björn Esser <besser82@fedoraproject.org> - 23-6
- Updated spec-file to recent guidelines
- Update Url and Source0 to point to Pagure
- Drop obsolete stuff
- Improve readability
- Clean trailing white-spaces

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct  4 2013 Bill Nottingham <notting@redhat.com> - 23-1
- add Cinnamon logo (#1015319)

* Thu Oct  3 2013 Bill Nottingham <notting@redhat.com> - 22-1
- add MATE logo (#1014275)
- de-Fedora-ize spec file

* Fri Dec  7 2012 Bill Nottingham <notting@redhat.com> - 21-1
- add icons for toplevel environments and a couple of apps

* Fri Apr 23 2010 Bill Nottingham <notting@redhat.com> - 20-1
- update haskell icon (#583868)

* Fri Apr 16 2010 Bill Nottingham <notting@redhat.com> - 19-1
- resync against new icon theme

* Wed Feb  3 2010 Bill Nottingham <notting@redhat.com> - 18-1
- updates and tweaks

* Mon Oct 26 2009 Bill Nottingham <notitng@redhat.com> - 17-1
- add LXDE logo (#529792)
- add books, font-design icon symlinks

* Fri Dec  5 2008 Bill Nottingham <notting@redhat.com> - 16-1
- add a copy of the comps dtd & cleanup file (#204704)

* Thu Oct 23 2008 Bill Nottingham <notting@redhat.com> - 15-1
- revert back to non-echo icons
- add icons for Haskell, Ruby

* Wed Sep 24 2008 Bill Nottingham <notting@redhat.com> - 14-1
- make more echo-y

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 13-2
- fix license tag

* Tue Sep  4 2007 Bill Nottingham <notting@redhat.com> - 13-1
- add fonts icons, tweak sound & video, system tools

* Thu Apr 26 2007 Bill Nottingham <notting@redhat.com> - 12-1
- updates to match current icon theme

* Tue Apr 17 2007 Bill Nottingham <notting@redhat.com> - 11.3-1
- add icons: clustering, virt, window-managers, uncategorized

* Wed Feb  7 2007 Jeremy Katz <katzj@redhat.com> - 11.2-3
- and a few more

* Mon Feb  5 2007 Jeremy Katz <katzj@redhat.com> - 11.2-2
- tweaks from package review

* Tue Aug  1 2006 Bill Nottingham <notting@redhat.com> - 11.2-1
- tweak summary

* Thu Mar  2 2006 Bill Nottingham <notting@redhat.com> - 11.1-1
- new education icon from Diana Fong
- update XFCE icon

* Wed Mar  1 2006 Bill Nottingham <notting@redhat.com> - 11-1
- pirut/anaconda now use 24x24. update sizes
- various additions/removals
- python scripts aren't useful with current repositories, remove them

* Thu May  5 2005 Bill Nottingham <notting@redhat.com> - 10.3-1
- updated icons (<dfong@redhat.com>)

* Mon May  2 2005 Bill Nottingham <notting@redhat.com> - 10.2-1
- add some icons

* Sun Oct 17 2004 Bill Nottingham <notting@redhat.com> - 10.1-1
- fix xfce images (#136046)

* Thu Sep 30 2004 Jeremy Katz <katzj@redhat.com> - 10.0-1
- add xfce images

* Thu Apr 15 2004 Jeremy Katz <katzj@redhat.com> - 9.92-1
- image tweaks

* Sun Nov 23 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- change getnotincomps.py /usr/bin/python2.2 -> /usr/bin/python

* Thu Nov  6 2003 Jeremy Katz <katzj@redhat.com> 9.1-1
- make it so we can handle RedHat vs Fedora (run with basedir as the last
  argument)

* Wed Sep  3 2003 Jeremy Katz <katzj@redhat.com> 9.0.4-1
- copy comps icons for a few new groups

* Tue May 27 2003 Jeremy Katz <katzj@redhat.com> 9.0.3-1
- getfullcomps.py can go away now that anaconda does dep resolution in
  realtime

* Fri Apr 11 2003 Jeremy Katz <katzj@redhat.com> 9.0.2-1
- update getfullcomps.py to not prefer devel packages

* Tue Apr  8 2003 Tim Powers <timp@redhat.com> 9.0.1-2
- made getfullcomps.py importable

* Tue Mar  4 2003 Jeremy Katz <katzj@redhat.com> 9.0.1-1
- add /usr/share/comps-extras/whichcd.py to find out which cd a given
  package is on (#85343)

* Tue Dec 17 2002 Jeremy Katz <katzj@redhat.com>
- improve getfullcomps.py handling of multiple provides

* Wed Sep 04 2002 Jeremy Katz <katzj@redhat.com>
- update images again

* Wed Sep 04 2002 Michael Fulbright <msf@redhat.com>
- update images

* Thu Aug 29 2002 Jeremy Katz <katzj@redhat.com>
- update images

* Tue Jul 23 2002 Jeremy Katz <katzj@redhat.com>
- Initial build.
