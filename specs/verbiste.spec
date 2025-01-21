%global with_mate 0

Name:           verbiste
Version:        0.1.49
Release:        2%{?dist}
Summary:        French conjugation system
License:        GPL-2.0-or-later
URL:            http://sarrazip.com/dev/verbiste.html
Source:         http://perso.b2b2c.ca/~sarrazip/dev/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libgnomeui-devel
BuildRequires:  libxml2-devel
BuildRequires:  libtool
BuildRequires:  automake
%if 0%{?with_mate}
BuildRequires:  mate-panel-devel
%endif
BuildRequires:  perl(XML::Parser)

%description
This package contains a database of French conjugation templates
and a list of more than 7000 regular and irregular French verbs
with their corresponding template. It also comes with two command-line 
tools named french-conjugator and french-deconjugator.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libxml2-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package        gnome
Summary:        GNOME Panel applet for Verbiste
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description    gnome
GNOME Panel applet and application based on Verbiste.

%if 0%{?with_mate}
%package        mate
Summary:        MATE Desktop Panel applet for Verbiste
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    mate
MATE Desktop Panel applet and application based on Verbiste.
%endif

%prep
%setup -q
# convert doc files to unicode
for DOCFILE in README NEWS HACKING LISEZMOI; do
    iconv -f ISO8859-15 -t UTF8 < $DOCFILE > $DOCFILE.tmp
    mv -f $DOCFILE.tmp $DOCFILE
done

%build
autoreconf -ivf
%configure \
%if 0%{?with_mate}
           --with-mate-applet \
%endif
           --with-gnome-app \
           --disable-maintainer-mode \
           --without-examples \
           --disable-rpath
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete -print

# This file gets created on x86_64 for no apparent reason.
# It's owned by glibc-common.
#rm -f %%{buildroot}%%{_datadir}/locale/locale.alias
desktop-file-install \
  --delete-original                          \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

rm -frv %{buildroot}%{_docdir}

%find_lang %{name} --with-man
%find_lang french-conjugator --with-man
%find_lang french-deconjugator --with-man

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING HACKING LISEZMOI NEWS README THANKS
%{_bindir}/french-*
%{_datadir}/verbiste*
%{_libdir}/*.so.*
%{_mandir}/man1/french-*.1*

%files devel
%{_includedir}/verbiste-0.1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files gnome -f %{name}.lang -f french-conjugator.lang -f french-deconjugator.lang
%{_bindir}/verbiste
%{_bindir}/verbiste-gtk
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/texmf/tex/latex/verbiste
%{_mandir}/man3/verbiste.3*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Didier Fabert <didier.fabert@gmail.com> - 0.1.49-1
- Update to 0.1.49

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 28 2023 Didier Fabert <didier.fabert@gmail.com> - 0.1.48-2
- migrated to SPDX license

* Thu Aug 03 2023 Didier Fabert <didier.fabert@gmail.com> - 0.1.48-1
- Update to 0.1.48

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.47-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.47-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.47-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.47-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021  Didier Fabert <didier.fabert@gmail.com> - 0.1.47-6
- Remove BTBFS run autoreconf to fix rpath

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019  Didier Fabert <didier.fabert@gmail.com> - 0.1.47-1
- Update to 0.1.47

* Mon Jul 29 2019  Didier Fabert <didier.fabert@gmail.com> - 0.1.46-1
- Update to 0.1.46

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Didier Fabert <didier.fabert@gmail.com> - 0.1.45-3
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=1606642

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018  Didier Fabert <didier.fabert@gmail.com> - 0.1.45-1
- Update to 0.1.45

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.44-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Didier Fabert <didier.fabert@gmail.com> - 0.1.44-1
- Update to 0.1.44

* Wed Apr 13 2016 Didier Fabert <didier.fabert@gmail.com> - 0.1.43-1
- Update to 0.1.43

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.41-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Christopher Meng <rpm@cicku.me> - 0.1.41-1
- Update to 0.1.41

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.1.32-6
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Spec cleanup

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.32-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.32-2
- Rebuild for new libpng

* Mon Feb 28 2011 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.32-1
- Update to the latest release
- Build without gnome-panel (not compatible with gnome-3)
- Move manpage for gnome app into -gnome.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.26-1
- New version 0.1.26
- possible to save a conjugation in a LaTeX file
- verb additions

* Tue Mar 24 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.25-1
- New version 0.1.25
- New verbs and several conjugation fixes.
- Minor UI tweaks and programming cleanups.
- BR: perl-XML-Parser (during build).
- Remove empty THANKS from doc.

* Wed Mar 04 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.24-2
- Fix source URL.

* Wed Mar 04 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.24-1
- New version 0.1.24
- About a hundred verbs have been added.
- Small usability fixes.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 30 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.23-1
- Upstream 0.1.23

* Sun Feb 17 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.22-1
- Upstream 0.1.22

* Fri Sep 14 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.21-1
- Upstream 0.1.21
- Adjust license to match expected standard
- Make sure docs are utf-8

* Sun Apr 01 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.20-1
- Upstream 0.1.20

* Fri Jan 12 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.19-1
- Upstream 0.1.19

* Sun Dec 17 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.17-1
- Upstream 0.1.17

* Tue Sep 26 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.16-2
- Do a better job packaging docs.

* Sun Sep 03 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.16-1
- Version 0.1.16

* Sun Jul 09 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.15-1.1
- Rebuild.

* Sun Jul 09 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.15-1
- Version 0.1.15

* Wed Jun 28 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.14-2
- BuildRequire gettext
- Run update-desktop-database in post/postun for -gnome

* Mon Feb 13 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.14-1.1
- FC5 Rebuild

* Mon Dec 12 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.14-1
- Version 0.1.14
- Switch to RPM_BUILD_ROOT notation

* Thu Oct 13 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.13-1
- Version 0.1.13.

* Fri Sep 23 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.1.12-1
- Version 0.1.12.
- Disttagging.

* Mon May 09 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.1.11-2
- Remove /usr/share/locale/locale.alias created on x86_64 on the
  buildsystem.

* Fri May 06 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.1.11-1
- Version 0.1.11.

* Tue Apr 12 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.1.10-3
- Modify the description to be more descriptive of what the main
  package does.

* Tue Apr 12 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.1.10-3
- Require version-release instead of just version for -devel and -gnome.
- Require gnome-panel-devel instead of libgnomeui-devel

* Tue Apr 12 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.1.10-2
- Use find_lang.
- Require libxml2-devel in -devel.

* Tue Apr 12 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.1.10-1
- Adapt the specfile to conform to the Fedora Extras standard.
- Create the changelog section.
