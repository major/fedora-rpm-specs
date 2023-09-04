Name:		ibus-skk
Version:	1.4.3
Release:	16%{?dist}
Summary:	Japanese SKK input method for ibus

License:	GPL-2.0-or-later
URL:		http://github.com/ueno/ibus-skk
Source0:	http://cloud.github.com/downloads/ueno/ibus-skk/%{name}-%{version}.tar.xz

BuildRequires:	vala
BuildRequires:	intltool
BuildRequires:	libskk-devel >= 0.0.11
BuildRequires:	ibus-devel
BuildRequires:	gtk3-devel
BuildRequires:	desktop-file-utils
BuildRequires: make
Requires:	ibus, skkdic

%description
A Japanese Simple Kana Kanji Input Method Engine for ibus.

%prep
%setup -q
rm src/*vala.stamp
# don't touch XKB layout under Fedora
sed -i 's!<layout>jp</layout>!<layout>default</layout>!' src/skk.xml.in.in

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/skk.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>skk.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Simple Kana-Kanji</name>
  <summary>Japanese input method</summary>
  <description>
    <p>
      The SKK input method is designed for entering Japanese text.
      The input method was originally invented by Masahiko Sato in 1987 and it is
      quite different from other Japanese input methods in the way it handles input.
    </p>
    <p>
      While other Japanese input methods treat input as a sentence, SKK treats it as a
      word and leaves control of sentence construction to users.
      Though it is not what normal users expect, advanced users can input Japanese
      with SKK more efficiently.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/ueno/ibus-skk/</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

desktop-file-validate %{buildroot}/%{_datadir}/applications/ibus-setup-skk.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/ibus-skk
%{_libexecdir}/ibus-*-skk
%{_datadir}/ibus/component/skk.xml
%{_datadir}/applications/ibus-setup-skk.desktop


%changelog
* Sat Sep 02 2023 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.4.3-16
- Migrate to SPDX license expression

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.3-10
- Delete ibus write-cache in scriptlet

* Wed Apr 21 2021 Jens Petersen <petersen@redhat.com> - 1.4.3-9
- move post/postun scriptlets to posttrans (see #1948197)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec  3 2017 Daiki Ueno <dueno@redhat.com> - 1.4.3-1
- new upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Richard Hughes <rhughes@redhat.com> - 1.4.2-2
- Register as an AppStream component.

* Tue Nov 25 2014 Daiki Ueno <dueno@redhat.com> - 1.4.2-1
- new upstream release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun  5 2012 Daiki Ueno <dueno@redhat.com> - 1.4.1-2
- don't touch XKB layout (#828674)

* Thu Mar 29 2012 Daiki Ueno <dueno@redhat.com> - 1.4.1-1
- new upstream release

* Fri Mar  9 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.0-3
- rebuild for ibus 1.4.99.20120304

* Wed Mar  7 2012 Daiki Ueno <dueno@redhat.com> - 1.4.0-2
- recompile vala

* Wed Jan 25 2012 Daiki Ueno <dueno@redhat.com> - 1.4.0-1
- new upstream release
- drop %%defattr(-,root,root,-) from %%files
- add ChangeLog to %%doc

* Wed Jan 11 2012 Daiki Ueno <dueno@redhat.com> - 1.3.99.20120111-1
- new upstream snapshot

* Fri Jan  6 2012 Daiki Ueno <dueno@redhat.com> - 1.3.99.20120105-1
- new upstream snapshot

* Mon Dec 26 2011 Daiki Ueno <dueno@redhat.com> - 1.3.99.20111225-1
- new upstream release

* Tue Dec 20 2011 Daiki Ueno <dueno@redhat.com> - 1.3.99.20111220-1
- new upstream snapshot, which started using libskk

* Fri Sep  2 2011 Daiki Ueno <dueno@redhat.com> - 1.3.9-1
- new upstream release (fixes a typo of the symbol XML entity ref)

* Mon Aug 29 2011 Daiki Ueno <dueno@redhat.com> - 1.3.8-1
- new upstream release

* Thu Aug  4 2011 Daiki Ueno <dueno@redhat.com> - 1.3.7-2
- add ibus-skk-xx-icon-symbol.patch (closes #727020)

* Wed Jun 15 2011 Daiki Ueno <dueno@redhat.com> - 1.3.7-1
- new upstream release

* Thu May 12 2011 Daiki Ueno <dueno@redhat.com> - 1.3.6-1
- new upstream release
- disable ibus-skk-vkbd.patch, since it is experimental
- drop preparing/cleaning buildroot

* Tue Mar  8 2011 Daiki Ueno <dueno@redhat.com> - 1.3.5-4
- regenerate configure script

* Tue Mar  8 2011 Daiki Ueno <dueno@redhat.com> - 1.3.5-3
- add ibus-skk-vkbd.patch

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Daiki Ueno <dueno@redhat.com> - 1.3.5-1
- new upstream release

* Tue Nov  9 2010 Daiki Ueno <dueno@redhat.com> - 1.3.3-1
- new upstream release

* Wed Oct 13 2010 Daiki Ueno <dueno@redhat.com> - 1.3.2-1
- new upstream release

* Tue Sep 14 2010 Daiki Ueno <dueno@redhat.com> - 1.3.0-1
- new upstream release

* Mon Aug 30 2010 Daiki Ueno <dueno@redhat.com> - 1.0.0-1
- new upstream release

* Tue Aug  3 2010 Daiki Ueno <dueno@redhat.com> - 0.0.10-1
- new upstream release

* Wed Jun 30 2010 Daiki Ueno <dueno@redhat.com> - 0.0.9-1
- new upstream release

* Tue May 25 2010 Daiki Ueno <dueno@redhat.com> - 0.0.8-1
- new upstream release

* Mon Apr 26 2010 Daiki Ueno <dueno@redhat.com> - 0.0.5-1
- new upstream release
- add BuildRoot tag and clean buildroot in the install target

* Sun Jan 17 2010 Daiki Ueno <ueno@unixuser.org> - 0.0.4-2
- set BuildArch to noarch
- add pkgconfig to BR
- reformat changelog

* Mon Jan 11 2010 Daiki Ueno <ueno@unixuser.org> - 0.0.4-1
- current version

* Thu Dec 24 2009 Daiki Ueno <ueno@unixuser.org> - 0.0.2-1
- new upstream release

* Fri Dec 11 2009 Jens Petersen <petersen@redhat.com> - 0.0.1-1
- initial packaging for fedora
