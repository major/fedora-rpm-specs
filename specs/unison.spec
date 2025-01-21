%bcond doc 1
%bcond gtk 1

%ifarch %{ocaml_native_compiler}
%global native true
%else
%global native false
%endif

# OCaml i686 support was dropped in OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

Name:           unison
Version:        2.53.5
Release:        5%{?dist}
Summary:        File Synchronizer

%global         forgeurl https://github.com/bcpierce00/%{name}/
%global         tag v%{version}
%forgemeta

# LGPL-2.0-only
#   src/ubase/myMap.ml{,i}
#   src/ubase/uarg.ml{,i}
# LGPL-2.1-only
#   src/fsmonitor/inotify/inotify.ml{,i}
#   src/fsmonitor/inotify/inotify_stubs.c
#   src/hash_compat.c
# LGPL-2.1-or-later
#   src/lwt
License:        GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-2.1-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{name}.desktop
Source2:        %{name}.metainfo.xml

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%if %{with gtk}
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib
BuildRequires:  ocaml-lablgtk3-devel
BuildRequires:  ocaml-cairo-devel
%endif
%if %{with doc}
BuildRequires:  hevea
BuildRequires:  lynx
BuildRequires:  tex-latex
%endif

Provides:       bundled(ocaml-inotify)

%description
Unison is a file-synchronization tool for POSIX-compliant systems (e.g. *BSD,
GNU/Linux, macOS) and Windows. It allows two replicas of a collection of files
and directories to be stored on different hosts (or different disks on the same
host), modified separately, and then brought up to date by propagating the
changes in each replica to the other.

%if %{with gtk}
%package        gtk
Summary:        Unison File Synchronizer GTK interface
Requires:       gdk-pixbuf2-modules-extra
Requires:       hicolor-icon-theme
%description    gtk
%{summary}.
%endif

%if %{with doc}
%package        doc
Summary:        Unison File Synchronizer documentation
BuildArch:      noarch
%description    doc
%{summary}.
%endif

%prep
%forgeautosetup

%build
%make_build        \
  NATIVE=%{native} \
  tui              \
  fsmonitor        \
  manpage

%if %{with gtk}
%make_build        \
  NATIVE=%{native} \
  gui
%endif

%if %{with doc}
%make_build        \
  NATIVE=%{native} \
  docs
%endif

%install
%make_install       \
  NATIVE=%{native}  \
  PREFIX=%{_prefix}

%if %{with gtk}
# Install the various icons according to the "Icon Theme Specification"
# https://specifications.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html
for size in 16 24 32 48 256; do
  format="${size}x${size}"
  install -Dpm0644 icons/U.${format}x16m.png \
    %{buildroot}%{_datadir}/icons/hicolor/${format}/apps/%{name}.png
done
install -Dpm0644 icons/U.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm0644 -t %{buildroot}%{_metainfodir} %{SOURCE2}
%endif

%if %{with doc}
install -Dpm0644 -t %{buildroot}%{_docdir}/%{name} doc/%{name}-manual.{html,pdf,txt}
%endif

%check
make test          \
  NATIVE=%{native}
%if %{with gtk}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%endif

%files
%doc NEWS.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-fsmonitor
%{_mandir}/man1/%{name}.1*

%if %{with gtk}
%files          gtk
%license LICENSE
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.metainfo.xml
%endif

%if %{with doc}
%files          doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/%{name}-manual.{html,pdf,txt}
%endif

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 2.53.5-4
- OCaml 5.3.0 rebuild for Fedora 42

* Fri Sep 20 2024 Matthew Krupcale <mkrupcale@gmail.com> - 2.53.5-3
- Add package Requires for GDK Pixbuf XPM image loader module

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 18 2024 Matthew Krupcale <mkrupcale@gmail.com> - 2.53.5-1
- Re-package latest upstream v2.53.5

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Richard W.M. Jones <rjones@redhat.com> - 2.40.128-11
- Use unsafe-string with OCaml 4.06.
- Add small hack to keep it working with new lablgtk.
- Enable debugging.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Richard W.M. Jones <rjones@redhat.com> - 2.40.128-7
- Small fix for compiling against OCaml 4.04 (RHBZ#1392152).

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 2.40.128-5
- Rebuild for OCaml 4.04.0.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.128-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 2.40.128-3
- Use global instead of define.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.128-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Richard W.M. Jones <rjones@redhat.com> - 2.40.128-1
- New upstream version 2.40.128 (RHBZ#1178444).
- Remove missing documentation patch, now included upstream.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.102-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.102-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 01 2014 Rex Dieter <rdieter@fedoraproject.org> - 2.40.102-6
- own alternatives target

* Mon Sep 09 2013 Gregor Tätzner <brummbq@fedoraproject.org> - 2.40.102-5
- ship 2 versions of unison: text only and gtk2 user interface
- move binaries into subpackages
- enable dependency generator

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.102-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Richard W.M. Jones <rjones@redhat.com> - 2.40.102-2
- Rebuild for OCaml 4.00.1.

* Thu Nov 15 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 2.40.102-1
- 2.40.102
- fixes incompatibility between unison ocaml3 and ocaml4 builds

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.63-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 22 2012 Gregor Tätzner <brummbq@fedoraproject.com> - 2.40.63-6
- Patch built-in documentation.

* Sat Jan 21 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 2.40.63-5
- Add unison-manual.html.

* Fri Jan 13 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 2.40.63-4
- Remove ocaml minimum version.
- Add Requires and provides scripts.

* Tue Sep 27 2011 Gregor Tätzner <brummbq@fedoraproject.org> - 2.40.63-3
- Remove vendor tag.

* Sun Sep 04 2011 Gregor Tätzner <brummbq@fedoraproject.org> - 2.40.63-2
- Remove xorg-x11-font-utils Requirement.
- Enable THREADS=true.

* Tue Aug 30 2011 Gregor Tätzner <brummbq@fedoraproject.org> - 2.40.63-1
- Version bump.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.57-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.57-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 8 2009 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.27.57-11
- Add Requires: xorg-x11-fonts-misc

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 2.27.57-10
- Rebuild for OCaml 3.11.0+rc1.

* Sat May 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.27.57-9
- Rebuild with OCaml 3.10.2-2 (fixes bz 441685, 445545).

* Sun Mar 30 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.27.57-8
- Don't use alternatives for desktop and icon files, to avoid duplicate
  menu entries.

* Wed Mar 19 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.27.57-7
- Fix license to match correct interpretation of source & GPL
- Remove Excludes for ppc64, since ocaml is available there now, in devel

* Sat Mar 15 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.27.57-6
- Rename package unison2.27 -> unison227 to match Fedora naming rules
- Automatically calculate ver_priority using the shell; easier maintenance

* Sat Mar 1 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.27.57-5
- Use Provides/Obsoletes to provide upgrade path, per:
  http://fedoraproject.org/wiki/Packaging/NamingGuidelines

* Thu Feb 28 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.27.57-4
- Explicitly conflict with existing unison package

* Fri Feb 22 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.27.57-3
- Derived unison2.27 package from unison2.13 package

* Mon Feb  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.27.57-2
- exclude arch ppc64

* Mon Feb  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.27.57-1
- new release 2.27.57

* Tue Aug 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.13.16-3
- Rebuild for FE6

* Tue Feb 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.13.16-2
- Rebuild for Fedora Extras 5

* Thu Sep  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.13.16-1
- New Version 2.13.16

* Sun Jul 31 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.12.0-0
- New Version 2.12.0

* Fri May 27 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.10.2-7
- Bump and rebuild with new ocaml and new lablgtk

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.10.2-6
- rebuild on all arches

* Mon May 16 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.10.2-5
- Patch: http://groups.yahoo.com/group/unison-users/message/3200

* Thu Apr 7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Feb 24 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:2.10.2-2
- BR gtk2-devel
- Added NEWS and README docs

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.10.2-1
- New Version 2.10.2

* Wed Apr 28 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:2.9.74-0.fdr.1
- New Version 2.9.74
- Added icon

* Tue Jan 13 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:2.9.72-0.fdr.1
- New Version 2.9.72

* Tue Dec  9 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.9.70-0.fdr.2
- Changed Summary
- Added .desktop file

* Fri Oct 31 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.9.70-0.fdr.1
- First Fedora release
