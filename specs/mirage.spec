%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:		mirage
Version:	0.9.5.2
Release:	47%{?dist}
Summary:	A fast and simple image viewer

# SPDX confirmed
License:	GPL-3.0-or-later
URL:		http://mirageiv.berlios.de/
Source0:	http://download.berlios.de/mirageiv/%{name}-%{version}.tar.bz2
# Fix bug 559853, backtrace when clicking middle button in some case
# Must be sent to upstream
Patch0:		mirage-0.9.3-prevmouse-not-defined-with-click.patch
# Don't call gtk.gdk.threads_init() on GLib >= 2.41,
# workaround for bug 1123953
Patch1:		mirage-0.9.5.2-glib241-init-workaround.patch
# Port to python3 + pygi + gtk3
Patch10:		mirage-0.9.5.2-py3-gtk3.patch
# Port to setuptools: PEP632
Patch11:		mirage-0.9.5.2-pep632-distutils-port.patch

BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	libX11-devel
BuildRequires:	python3-devel
BuildRequires:	desktop-file-utils
BuildRequires:	python3-setuptools
Requires:	gtk3
Requires:	python3-gobject
Requires:	python3-cairo

%description
Mirage is a fast and simple GTK+ image viewer. Because it 
depends only on PyGTK, Mirage is ideal for users who wish to 
keep their computers lean while still having a clean image viewer.

%prep
%setup -q
%patch -P0 -p1 -b .bt_prevmouse -Z
%patch -P1 -p1 -b .glib241 -Z
# Don't remove rebuilt files!
%{__sed} -i.build -e '/Cleanup/,$d' setup.py

%patch -P10 -p1 -b .py3 -Z
%patch -P11 -p1 -b .pep632 -Z

%build
%{__python3} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT
%{__python3} setup.py install --skip-build \
	--prefix %{_prefix} \
	--root $RPM_BUILD_ROOT \
	%{nil}

# remove document files
%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/[A-Z]*

# install desktop file
%{__sed} -i -e 's|%{name}.png|%{name}|' \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
desktop-file-install \
	--delete-original \
	--remove-category 'Application' \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# gettext files
%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc CHANGELOG
%license COPYING
%doc README
%doc TODO
%doc TRANSLATORS

%{_bindir}/%{name}
%{python3_sitearch}/%{name}.py*
%{python3_sitearch}/*.egg-info
%{python3_sitearch}/*.so
%{python3_sitearch}/__pycache__/%{name}*

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.png
%{_datadir}/pixmaps/*.png

%{_datadir}/applications/*%{name}.desktop

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.5.2-45
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan  5 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-42
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.5.2-40
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan  3 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-38
- Handle PEP632, switch from distutils to setuptools

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.5.2-36
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-34
- Fix small typo

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.5.2-32
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep  9 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-30
- Properly terminate PyMethodDef array with sentinel in xmouse module
  (bug 1873115)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.5.2-28
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-26
- Fix GTK v.s. thread handling mistake

* Tue Oct 15 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-25
- Update python3 + gtk3 patch

* Sun Sep 29 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-24
- Update python3 + gtk3 patch

* Fri Sep 27 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-23
- Update python3 + gtk3 patch

* Mon Sep 23 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-20
- F-31+: port to python3 + pygi + gtk3

* Sun Aug 25 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-19
- F-31+: drop optional gnome-python2-gconf dep for now

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-16
- Use %%__python2 instead of %%__python

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.2-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-7
- Don't call gtk.gdk.threads_init() on GLib >= 2.41,
  workaround for bug 1123953

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5.2-4
- F-19: kill vendorization of desktop file (fpc#247)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 10 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.5.2-1
- 0.9.5.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.5.1-1
- 0.9.5.1

* Fri Jul 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-14: ... and again rebuild for python 2.7

* Fri Jul 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.5-1
- 0.9.5

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.4-2
- F-14: Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul  2 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.4-1
- 0.9.4

* Fri Jan 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.3-5
- Fix bt when clicking middle button in some case (bug 559853)

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.3-4
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.3-3
- F-11: Mass rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.3-2
- Rebuild for Python 2.6

* Thu Mar 27 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.3-1
- 0.9.3

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43 (F-9)

* Wed Jan 30 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.2-1
- 0.9.2

* Thu Jan 10 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.1-1
- 0.9.1

* Fri Jan  4 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9-3
- Support python egginfo for F-9+

* Wed Dec  5 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9-2
- Fix icon path in desktop file for desktop-file-utils 0.14+

* Fri Oct 19 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9-1
- 0.9

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.3-2.dist.2
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.3-2.dist.1
- License update

* Fri Jun 15 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.3-2
- Remove Version= entry (on F-8+)

* Fri Jan 19 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.3-1
- 0.8.3

* Sat Dec  9 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.2-1
- 0.8.2

* Fri Dec  8 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against new python (only for devel)

* Sat Nov 18 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.1-1
- Initial packaging to import to Fedora Extras.
