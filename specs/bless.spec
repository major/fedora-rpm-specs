#debug info would be empty due to no binarys
%global debug_package %{nil}

Name: bless
Version: 0.6.3
Release: 16%{?dist}
Summary: High quality, full featured hex editor    

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later        
URL: https://github.com/afrantzis/bless/
Source0: https://github.com/afrantzis/bless/archive/v%{version}.tar.gz
Source1: bless.metainfo.xml
Patch1: bless-0.6.2-default-editmode-overwrite.patch
Patch2: bless-0.6.3-fix-reloading-file.patch

BuildRequires:  gcc
BuildRequires: mono-devel
BuildRequires: gtk-sharp2-devel     
BuildRequires: desktop-file-utils
BuildRequires: rarian-compat
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gettext-devel
BuildRequires: nunit-devel
BuildRequires: docbook-style-xsl
BuildRequires: itstool
BuildRequires: libappstream-glib

Requires: mono-core
Requires: gtk-sharp2

Obsoletes: %{name}-doc < 0.6.3-11

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Bless is a binary (hex) editor, a program that 
enables you to edit files as sequences of bytes.


%prep
%setup -q
%patch -P1 -p1 -b .editmodeoverwrite
%patch -P2 -p1 -b .fixreloadingfile
sed -i "s~html_xsl = 'http://docbook.sourceforge.net/release/xsl/current/html/chunk.xsl'~html_xsl = '/usr/share/sgml/docbook/xsl-stylesheets-1.79.2/xhtml/chunk.xsl'~" doc/user/meson.build

%build
%meson
%meson_build

%install
%meson_install

desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/bless.desktop

install -D -m0644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_metainfodir}/bless.metainfo.xml
appstream-util validate-relax --nonet ${RPM_BUILD_ROOT}%{_metainfodir}/bless.metainfo.xml

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/bless
%{_libdir}/bless/
%{_datadir}/bless/
%{_datadir}/icons/hicolor/48x48/apps/bless.png
%{_datadir}/applications/bless.desktop
%{_metainfodir}/bless.metainfo.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.3-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 0.6.3-11
- Simplify packaging
- Add appstream data

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.3-7
- build requires itstool

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.3-5
- Fix bug 2039108 about wrong path in code

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.3-2
- Backport fixing crash on reloading changed file (bug 1946757)

* Wed Apr 07 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.3-1
- Update to new upstream release 0.6.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.2-2
- default edit mode is now Overwrite instead of Insert

* Wed Apr 08 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.2-1
- Update to new upstream release 0.6.2

* Thu Feb 20 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.0-29
- Fix build with new mono 6, fixing confusion about System.Range and Bless.Util.Range

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-20
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 02 2016 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.0-18
- Use %%global instead of %%define

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> 0.6.0-16
- another fix for mono4

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.0-15
- Rebuild (mono4)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.0-11
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 21 2011 Dan Horák <dan[at]danny.cz> - 0.6.0-7
- updated the supported arch list

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 0.6.0-5
- ExckudeArch sparc64

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.6.0-3
- Build arch ppc64.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 22 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.6.0-1
- Update to 0.6.0

* Sat Apr 05 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-5
- Fix build with mono-1.9+ RH #440761

* Fri Jan 04 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-5
- Add post and postun requires

* Fri Jan 04 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-4
- Add ExclusiveArch

* Thu Jan 03 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-3
- Don't make it a noarch package

* Thu Jan 03 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-2
- Fix scrollkeeper scriptlet

* Wed Jan 02 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-1
- Initial build
