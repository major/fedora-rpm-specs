%define python_binding 0
%define ruby_binding 0

Name:           tomoe
Version:        0.6.0
Release:        57%{?dist}
Summary:        Handwritten input system for Japanese and Chinese

License:        LGPL-2.1-or-later
URL:            http://tomoe.sourceforge.jp/
## stripped tarball is generated as follows:
# $ wget http://downloads.sourceforge.net/sourceforge/tomoe/%{name}-%{version}.tar.gz
# $ ./strip.sh %{name}-%{version}.tar.gz
Source0:        %{name}-stripped-%{version}.tar.gz
Source1:        strip.sh
Patch0:         tomoe-0.6.0-multiarch-conflict.patch
Patch1:         tomoe-0.6.0-bz502662.patch
Patch2:         tomoe-0.6.0-fixes-glib-includes.patch
Patch3:         tomoe-0.6.0-fixes-set-parse-error.patch
Patch4:         tomoe-strerror.patch

BuildRequires:  make
BuildRequires:  glib2-devel, gettext, gtk-doc, libtool, intltool
BuildRequires:  perl(XML::Parser), python3
%if %{python_binding}
BuildRequires:  pygobject2-devel, python2-devel, pygtk2-codegen
%endif
%if %{ruby_binding}
BuildRequires:  ruby-glib2-devel
%endif
## for extra dictionary backends
#BuildRequires:  mariadb-connector-c-devel, subversion-devel, hyperestraier-devel

%description
A program which does Japanese handwriting recognition.


%package devel
Summary:    Tomoe development files
Requires:   %{name} = %{version}-%{release}

%description devel
The tomoe-devel package includes the header files for the tomoe package.
Install this package if you want to develop programs which use tomoe.


%prep
%setup -q
%patch -P0 -p0 -b .multiarch-conflict
%patch -P1 -p0 -b .bz502662
%patch -P2 -p1 -b .glib
%patch -P3 -p1 -b .compile
%patch -P4 -p1 -b .strerror

%build
./autogen.sh
%configure --disable-static --enable-gtk-doc
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%if !%{ruby_binding}
rm -f $RPM_BUILD_ROOT%{_libdir}/ruby/site_ruby/*/tomoe.rb $RPM_BUILD_ROOT%{_libdir}/ruby/site_ruby/*/*-linux/*
%endif
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/xml2est.rb

# remove .la files
find ${RPM_BUILD_ROOT}%{_libdir} -name '*.la' | xargs rm

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README TODO data/kanjidic*.html
%{_libdir}/libtomoe.so.*
%if %{python_binding}
%{_libdir}/python?.?/site-packages/tomoe.so
%endif
%{_libdir}/tomoe
%{_datadir}/tomoe
%dir %{_sysconfdir}/tomoe
%config(noreplace) %{_sysconfdir}/tomoe/config


%files devel
%{_libdir}/libtomoe.so
%{_includedir}/tomoe
%{_libdir}/pkgconfig/tomoe.pc
%{_datadir}/gtk-doc
%if %{python_binding}
%{_libdir}/pkgconfig/pytomoe.pc
%endif
%if %{ruby_binding}
%{_libdir}/ruby/site_ruby/1.8/tomoe.rb
%{_libdir}/ruby/site_ruby/1.8/*-linux/*
%endif

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May  6 2023 Peng Wu <pwu@redhat.com> - 0.6.0-53
- Rebuild the package

* Sat May  6 2023 Peng Wu <pwu@redhat.com> - 0.6.0-52
- Migrate to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jeff Law <law@redhat.com> - 0.6.0-45
- Use strerror, not sys_errlist

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Peng Wu <pwu@redhat.com> - 0.6.0-43
- Disable python binding

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.0-38
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Sep 22 2017 Peng Wu <pwu@redhat.com> - 0.6.0-37
- Update BuildRequires to mariadb-connector-c-devel
- Add tomoe-0.6.0-fixes-set-parse-error.patch to fix compile

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-33
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 Peng Wu <pwu@redhat.com> - 0.6.0-28
- Add comments

* Wed Feb 12 2014 Peng Wu <pwu@redhat.com> - 0.6.0-27
- Fixes skip code license issue (rhbz#969415)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Peng Wu <pwu@redhat.com> - 0.6.0-25
- Enable gtk-doc

* Mon Mar 25 2013 Peng Wu <pwu@redhat.com> - 0.6.0-24
- Fixes aarch64 build

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012  Peng Wu <pwu@redhat.com> - 0.6.0-22
- Fixes glib includes

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.6.0-18
- Rebuilt for gcc bug 634757

* Thu Sep 16 2010 Jens Petersen <petersen@redhat.com> - 0.6.0-17
- drop dependency on gtk-doc and own the gtk-doc dir (#604416)
- update url

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun  2 2009 Ding-Yi Chen <dchen at redhat.com> - 0.6.0-14
- [Bug 502662] SCIM-tomoe doesn't load - no error msgs

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Ding-Yi Chen <dchen at redhat.com> - 0.6.0-10
- Fix [Bug 343321] multiarch conflicts in tomoe.
  Maybe cause by bug in gtk-doc.
- Also fix the errors from rpmlint:
  chmod 755 /usr/share/tomoe/xml2est.rb
  

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.0-8
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.0-7
- Rebuild for Python 2.6

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.0-6
- fix license tag

* Wed Feb 27 2008 Jens Petersen <petersen@redhat.com> - 0.6.0-5
- update license field from LGPL to LGPL2+

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.0-4
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.6.0-3
- Rebuild for selinux ppc32 issue.

* Mon Jul 16 2007 Jens Petersen <petersen@redhat.com> - 0.6.0-2
- add a build switch for python binding
- buildrequires for pygobject2-devel, python-devel, and pygtk2-codegen
- buildrequire gtk-doc
- require gtk-doc for devel package
- add a build switch for ruby binding (default off)

* Fri Jun 29 2007 Jens Petersen <petersen@redhat.com> - 0.6.0-1
- update to 0.6.0
- tomoe-modules-noversion.patch no longer needed
- buildrequire gettext, python, and perl-XML-Parser (for intltool)

* Thu Feb 15 2007 Jens Petersen <petersen@redhat.com> - 0.5.1-1
- update to 0.5.1
- add tomoe-modules-noversion.patch to unversion .so modules (#227623)
- improve the filelists (#227453)
- add more doc files including new html files for kanjidic
- moved gtk-doc files to devel
- make config file noreplace

* Sat Jan 20 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.5.0-2
- do not buildrequire libtomoe-gtk

* Sat Jan 20 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.5.0-1
- update to 0.5.0.

* Thu Dec 21 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.4.0-1
- update to 0.4.0.

* Sat Sep 15 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.2.1-6
- mass rebuilding.

* Wed Mar  1 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.2.1-4
- sync with libtomoe-gtk

* Sat Sep 3 2005 Warren Togami <wtogami@redhat.com> - 0.2.1-3
- some spec cleanup

* Sat Sep 2 2005 Ryo Dairiki <ryo-dairiki@mbm.nifty.com> - 0.2.1-2
- Sync with Jens's spec file

* Wed Aug 31 2005 Ryo Dairiki <ryo-dairiki@mbm.nifty.com> - 0.2.1-1
- Initial packaging for Extras

* Fri Jul  1 2005 Ichiro Nakai <ichiro@n.email.ne.jp>
- (0.2.0-1m)
- version 0.2.0
- add a package tomoe-devel
- add %%post and %%postun sections

* Wed Mar  2 2005 Ichiro Nakai <ichiro@n.email.ne.jp>
- (0.1.1-1m)
- initial package for Momonga Linux
- import %%description from cooker
