Name: inksmoto
Version: 0.7.0
Release: 36%{?dist}
Summary: The new xmoto level editor for Inkscape

License: GPL-2.0-only
URL: http://xmoto.sourceforge.net/
Source0: http://download.tuxfamily.org/xmoto/svg2lvl/%{version}~rc1/inksmoto-%{version}.tar.gz       
BuildRequires: python3-devel
Requires: xmoto, inkscape, python3-lxml, python3-gobject
BuildArch: noarch

Patch0: inksmoto-0.7.0-pypath.patch
Patch1: inksmoto-python3.patch

%description
Inksmoto Level Editor is the new xmoto level editor. It uses Inkscape to
draw levels, then it allows you to save your drawing as a xmoto level
(.lvl file). It also allow you to edit xmoto level properties from 
within Inkscape such as make background block, strawberries, ...

Inksmoto Level Editor is written in Python, it's an Inkscape extension. 

%prep
%setup -qn extensions

%patch -P0 -p0
%patch -P1 -p1

%build
%py3_shebang_fix .

%install
mkdir -p %{buildroot}%{_datadir}/inkscape/extensions
rm -f bezmisc.py
rm -f inkex.py
cp -p *.inx *.py %{buildroot}%{_datadir}/inkscape/extensions/
chmod 644 %{buildroot}%{_datadir}/inkscape/extensions/*
cp -pr inksmoto %{buildroot}%{_datadir}/inkscape/extensions/


%files
%{_datadir}/inkscape/extensions/*
%license COPYING
%doc AUTHORS INSTALL README

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.7.0-31
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.7.0-23
- Port to Python 3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.0-20

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.0-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-9
- Update Requires, BZ 895273.

* Tue Jul 23 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.0-8
- Move from PyXML to python-lxml, BZ 842853.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 24 2010 Jon Ciesla <limb@jcomserv.net> - 0.7.0-4
- 0.7.0 final.

* Tue Jan 12 2010 Jon Ciesla <limb@jcomserv.net> - 0.7.0-3.rc1
- Patch for broken dep.

* Fri Jan 08 2010 Jon Ciesla <limb@jcomserv.net> - 0.7.0-2.rc1
- Rebuild for broken dep.

* Wed Sep 30 2009 Jon Ciesla <limb@jcomserv.net> - 0.7.0-1.rc1
- Update to 0.7.0~rc1.

* Mon Aug 24 2009 Jon Ciesla <limb@jcomserv.net> - 0.6.0-2
- 0.6.0 final.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-1.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Jon Ciesla <limb@jcomserv.net> - 0.6.0-1.rc1
- Update to 0.6.0~rc1.

* Tue Mar 17 2009 Jon Ciesla <limb@jcomserv.net> - 0.5.1-1
- New upstream, bugfix release.

* Wed Jan 21 2009 Jon Ciesla <limb@jcomserv.net> - 0.5.0-4
- New upstream, 0.5.0 final.

* Tue Jan 13 2009 Jon Ciesla <limb@jcomserv.net> - 0.5.0-3.rc2
- New upstream.

* Thu Dec 18 2008 Jon Ciesla <limb@jcomserv.net> - 0.5.0-2.rc1
- Added xmoto_install and xmoto_bitmap.

* Thu Dec 18 2008 Jon Ciesla <limb@jcomserv.net> - 0.5.0-1.rc1
- New upstream, fixes BZ 476815.

* Mon Nov 24 2008 Jon Ciesla <limb@jcomserv.net> - 0.4.1-3
- Cleaned up summary.

* Thu May 15 2008 Jon Ciesla <limb@jcomserv.net> - 0.4.1-2
- Fixed license tag.
- Fixed .py perms.

* Sat Mar 08 2008 Jon Ciesla <limb@jcomserv.net> - 0.4.1-1
- create.
