%global debug_package %{nil}

Name:		cdcollect
Version:	0.6.0
Release:	45%{?dist}
Summary:	Simple CD/DVD catalog for GNOME

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://cdcollect.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		cdcollect-libdir.patch
Patch1:		cdcollect-0.6.0.patch
Patch2:		cdcollect-0.6.0-sqlite.patch

BuildRequires:  gcc
BuildRequires:	mono-devel >= 1.1.17, gtk-sharp2-devel >= 2.8.0, gnome-sharp-devel
BuildRequires:	glib2-devel, sqlite-devel >= 3.3.5, mono-data-sqlite, gettext
BuildRequires:	perl(XML::Parser), desktop-file-utils

# ./intltool-* perl-deps
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Wrap)
BuildRequires: make

Requires:	mono-core >= 1.1.17, gtk-sharp2 >= 2.8.0, gnome-sharp
Requires:	sqlite >= 3.3.5, mono-data-sqlite

Requires(pre):	GConf2
Requires(post):	GConf2
Requires(preun):GConf2

ExclusiveArch: %{mono_arches}

%description
CDCollect is a simple CD/DVD catalog for GNOME written in C# using Mono
and GTK#. All data are stored in a sqlite database.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1 -b .sqlite

%build
%configure --disable-schemas-install
make %{?_smp_mflags}

%install
%make_install

desktop-file-install --remove-category="Application" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%pre
if [ "$1" -gt 1 ]; then
	export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
	gconftool-2 --makefile-uninstall-rule \
		%{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
	%{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :

%preun
if [ "$1" -eq 0 ]; then
	export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
	gconftool-2 --makefile-uninstall-rule \
		%{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi


%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%license COPYING
%config(noreplace) %{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.0-44
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-26
- mono rebuild for aarch64 support

* Fri Feb 05 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.6.0-25
- Add perl deps for bundled intltool* scripts (F24FTBFS).
- Add %%license.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.0-22
- Rebuild (mono4)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 01 2013 Dan Horák <dan[at]danny.cz> - 0.6.0-18
- rebuild for aarch64 (#925136)

* Fri Feb 15 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.0-17
- disable debuginfo generation since this is a mono app

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.0-16
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan  1 2011 Dan Horák <dan[at]danny.cz> 0.6.0-11
- updated the supported arch list
- switch to Mono.Data.Sqlite bindings

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 0.6.0-10
- ExcludeArch sparc64  no mono there

* Wed Sep 23 2009 Dan Horak <dan[at]danny.cz> 0.6.0-9
- drop ExcludeArch for ppc64

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.6.0-6
- rebuild for new gnome-sharp

* Thu Feb 14 2008 Dan Horak <dan[at]danny.cz> 0.6.0-5
- rebuild for gcc 4.3

* Wed Sep 26 2007 Dan Horak <dan[at]danny.cz> 0.6.0-4
- set ExcludeArch: ppc64 as Mono doesn't exist there

* Wed Sep 26 2007 Dan Horak <dan[at]danny.cz> 0.6.0-3
- fixed URLs
- removed unneeded BR: pkgconfig

* Mon Sep 24 2007 Dan Horak <dan[at]danny.cz> 0.6.0-2
- update license tag
- fix desktop file installation

* Tue Jul 17 2007 Dan Horak <dan[at]danny.cz> 0.6.0-1
- initial version
