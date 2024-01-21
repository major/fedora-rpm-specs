# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 0

Name:           gedit-latex
Version:        3.20.0
Release:        20%{?dist}
Summary:        gedit plugin for composing and compiling LaTeX documents

License:        GPLv2+ and GPLv3+
URL:            http://projects.gnome.org/gedit
Source0:        https://download.gnome.org/sources/gedit-latex/3.20/gedit-latex-%{version}.tar.xz

BuildRequires:  gedit-devel
BuildRequires:  gettext
BuildRequires:  cairo-devel
BuildRequires:  atk-devel
BuildRequires:  intltool
BuildRequires:  libpeas-devel
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires: make

Requires:       python3-gobject
Requires:       python3-dbus
Requires:       texlive
# For compiling utilities
Requires:       rubber

Obsoletes:      gedit-plugins-latex < %{version}-%{release}
Provides:       gedit-plugins-latex = %{version}-%{release}


%description
This plugin assists you in composing and compiling LaTeX documents using gedit.

# This plugin should be noarch but due to the fact that we need the plugin
# installed in libdir we need it to be arch dependent. This makes us to not
# require the debug package.
%global debug_package %{nil}

%prep
%setup -q
sed -i -e '/^#!\/.*bin\/perl/d' latex/util/eps2png.pl
# Fixing the multilib path
# https://sourceforge.net/tracker/index.php?func=detail&aid=2130308&group_id=204144&atid=988428
sed -i -e 's|_CONFIG_FILENAME = "/etc/texmf/texmf.cnf"|_CONFIG_FILENAME = "/usr/share/texlive/texmf-dist/web2c/texmf.cnf"|' latex/latex/environment.py
sed -i -e 's|_DEFAULT_TEXMF_DIR = "/usr/share/texmf-texlive"|_DEFAULT_TEXMF_DIR = "/usr/share/texmf"|' latex/latex/environment.py


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %name


%files -f %{name}.lang
%license COPYING
%doc README NEWS
%{_libdir}/gedit/plugins/*
%{_datadir}/gedit/plugins/latex/
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.latex.gschema.xml

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 09 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.20.0-13
- Set python_bytecompile_extra to 0
- Remove pygo_version macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0
- Use license macro for COPYING

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-9.20141017git8e9970b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-8.20141017git8e9970b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 3.8.0-7.20141017git8e9970b
- Checkout from upstream git, with support for gnome 3.14

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 15 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 3.8.0-4
- Correct wrong _CONFIG_FILENAME

* Sun Sep 29 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 3.8.0-3
- Add requires python3-dbus (bz 986892)
- Patch fixes python2 print (bz 986892)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.8.0-1
- New upstream release 3.8.0.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.4.1-1
- New upstream release 3.4.1.

* Mon Mar 26 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.4.0-1
- New upstream release 3.4.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 06 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.2-1
- New upstream release 3.3.2.

* Thu Oct 06 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.1-1
- New upstream release 3.3.1.

* Fri Sep 30 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.2.0-1
- New upstream release 3.2.0.

* Tue Sep 20 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.1-2
- No need for debug package.

* Tue Sep 13 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.1-1
- New upstream release 3.1.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 21 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 0.2-1
- New upstream source. Fixes bz #576598

* Thu Mar 04 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 0.2-0.5.rc3
- New upstream source

* Mon Nov 30 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 0.2-0.4.rc2
- Using virtual requires to pull in the TeX packages (bz #542611)

* Tue Nov 10 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 0.2-0.3.rc2
- Adding a dependency on pypoppler (bz #509484)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-0.2.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 0.2-0.1rc2
- New upstream source

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 01 2008 Sergio Pascual <sergiopr at fedoraproject.org> 0.1.3.2-3
- Disabled debuginfo package

* Wed Oct 01 2008 Sergio Pascual <sergiopr at fedoraproject.org> 0.1.3.2-2
- Adding %%clean
- Empty file removed
- Added empty %%build stage
- Sholud be noarch, but gedit doesn't allow it, bug filled 

* Fri Sep 26 2008 Sergio Pascual <sergiopr at fedoraproject.org> 0.1.3.2-1
- Initial RPM file
