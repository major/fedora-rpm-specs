Name:       alleyoop
Version:    0.9.8
Release:    20%{?dist}
License:    GPLv2+
Summary:    Graphical front-end to the Valgrind memory checker for x86
URL:        http://alleyoop.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:    alleyoop.desktop

BuildRequires:  gcc
BuildRequires: valgrind >= 3.1.0
BuildRequires: libgnomeui-devel, gettext, intltool
BuildRequires: desktop-file-utils
BuildRequires: binutils-devel
BuildRequires: make

Requires: valgrind >= 3.1.0
Requires: GConf2, scrollkeeper

# valgrind available only on these
ExclusiveArch: %{ix86} x86_64 ppc ppc64 ppc64le s390x %{arm} aarch64

%description
Alleyoop is a graphical front-end to the increasingly popular Valgrind
memory checker for x86 GNU/ Linux using the Gtk+ widget set and other
GNOME libraries for the X Windows System.

Features include a right-click context menu to intelligently suppress
errors or launch an editor on the source file/jumping to the exact
line of the error condition. A searchbar at the top of the viewer can
be used to limit the viewable errors to those that match the regex
criteria entered. Also included is a fully functional Suppressions
editor.

%prep
%setup -q

%build
%configure --disable-install-schemas
make %{?_smp_mflags}

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%make_install
%find_lang %{name}

desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q

%postun
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q

%files -f %{name}.lang
%doc COPYING README NEWS AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/applications/*.desktop


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.8-3
- Valgrind is now available on aarch64, ppc64le

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Gianluca Sforna <giallu@gmail.com> - 0.9.8-1
- new upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.7-8
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.7-6
- Valgrind is available on ARM too

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.7-4
- Rebuild for new libpng

* Fri Apr 29 2011 Dan Horák <dan[at]danny.cz> - 0.9.7-3
- valgrind exists only on selected architectures

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 24 2009 Gianluca Sforna <giallu gmail com> - 0.9.7-1
- New upstream release
- Add more docs

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  9 2009 Gianluca Sforna <giallu gmail com> - 0.9.5-1
- New upstream version

* Wed Feb 25 2009 Gianluca Sforna <giallu gmail com> - 0.9.4-3
- Don't mark schemas as %%config

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  9 2009 Gianluca Sforna <giallu gmail com> - 0.9.4-1
- New upstream version

* Tue Feb 12 2008 Gianluca Sforna <giallu gmail com> - 0.9.3-4
- rebuild with gcc 4.3

* Wed Aug 22 2007 Gianluca Sforna <giallu gmail com> 0.9.3-3
- Updated License field
- Fix Source0 URL
- Remove ExclusiveArch as it seems valgrind is now available also on PPC 
- Remove obsolete X-Fedora category

* Mon Oct 2 2006 Gianluca Sforna <giallu gmail com> 0.9.3-2
- address comments from review (BZ# 201417)

* Tue Aug 15 2006 Gianluca Sforna <giallu gmail com> 0.9.3-1
- version update
- add BRs: desktop-file-utils, intlutil

* Thu Aug 3 2006 Gianluca Sforna <giallu gmail com> 0.9.2-1
- version update
- dropped patches
- raised required valgrind version

* Thu Sep  1 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-3
- add BR: gettext
- "X-Desktop-File-Install-Version=0.4" removed from alleyop.desktop
- s/X-Windows/X Window System/ in %%description
- gconftool-2 --makefile-uninstall-rule code added in %%postun
- Requires for GConf2 and scrollkeeper added
- Patch to use --log-fd (new syntax)

* Thu Jul 28 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-2
- fix stupid typo in ExclusiveArch

* Wed Jul 27 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-1
- initial package for Fedora Extras
