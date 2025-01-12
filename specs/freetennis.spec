Name:           freetennis
Version:        0.4.8
Release:        60%{?dist}
Summary:        Tennis simulation game
License:        GPL-2.0-or-later
URL:            http://freetennis.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        freetennis.desktop
Source2:        freetennis.png
Patch0:         freetennis-0.4.8-pathfixes.patch
Patch1:         freetennis-0.4.8-build.patch
Patch2:         freetennis-0.4.8-ocaml-4.12.patch
Patch3:         freetennis-0.4.8-ocaml-5.0.0.patch
# i686 support was dropped in OCaml 5 / Fedora 39
ExcludeArch:    sparc64 s390 s390x %{ix86}
BuildRequires:  make, ocaml, SDL_gfx-devel, SDL_mixer-devel
BuildRequires:  libXmu-devel, gtk2-devel, desktop-file-utils
BuildRequires:  SDL_ttf-devel
BuildRequires:  ocaml-camlimages-devel
BuildRequires:  ocaml-SDL-devel >= 0.9.1-34
BuildRequires:  ocaml-lablgl-devel >= 1.06-1
BuildRequires:  ocaml-lablgtk-devel >= 2.10.1-5

%description
Free Tennis is a free software tennis simulation game.  The game can be 
played against an A.I. or human-vs-human via LAN or internet.


%prep
%autosetup -p1


%build
%ifarch %{ocaml_native_compiler}
%make_build
%else
%make_build byte
%endif


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

mv freetennis $RPM_BUILD_ROOT%{_bindir}
mv graphics $RPM_BUILD_ROOT%{_datadir}/%{name}/
mv sfx $RPM_BUILD_ROOT%{_datadir}/%{name}/

desktop-file-install                                      \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/


%files
%doc CHANGES.txt AUTHORS TODO.txt web-site/
%license COPYING
%{_bindir}/freetennis
%{_datadir}/%{name}
%{_datadir}/applications/freetennis.desktop
%{_datadir}/icons/hicolor/48x48/apps/freetennis.png


%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 0.4.8-60
- OCaml 5.3.0 rebuild for Fedora 42

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug  6 2023 Jerry James <loganjerry@gmail.com> - 0.4.8-56
- Fix FTBFS on bytecode-only architectures (rhbz#2225813)
- Convert License field to SPDX
- Build with debuginfo

* Fri Aug  4 2023 Hans de Goede <hdegoede@redhat.com> - 0.4.8-56
- Fix FTBFS (rhbz#2225813)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug  2 2021 Hans de Goede <hdegoede@redhat.com> - 0.4.8-51
- Fix FTBFS (rhbz#1987488)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Richard W.M. Jones <rjones@redhat.com> - 0.4.8-46
- Rebuild against updated ocaml-SDL, ocaml-lablgl.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.8-41
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 0.4.8-37
- Rebuild for OCaml 4.04.0.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Bruno Wolff III <bruno@wolff.to> - 0.4.8-34
- Rebuild with latest ocaml-calimages

* Sat Nov 01 2014 Bruno Wolff III <bruno@wolff.to> - 0.4.8-33
- Rebuild with latest ocaml-calimages

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> - 0.4.8-29
- Remove vendor prefix from desktop file

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Bruno Wolff III <bruno@wolff.to> - 0.4.8-27
- Rebuild to pickup rebuilt (static) ocaml-calimages

* Wed Oct 17 2012 Bruno Wolff III <bruno@wolff.to> - 0.4.8-26
- Rebuild for ocaml 4.0.1

* Sun Jul 29 2012 Bruno Wolff III <bruno@wolff.to> - 0.4.8-25
- Rebuild for ocaml 4.0.0 final

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Bruno Wolff III <bruno@wolff.to> - 0.4.8-23
- Rebuild for new ocaml

* Fri May 11 2012 Bruno Wolff III <bruno@wolff.to> - 0.4.8-22
- Rebuild to use current ocaml-camlimages which was rebuilt for libtiff update

* Sat Mar 10 2012 Bruno Wolff III <bruno@wolff.to> - 0.4.8-21
- gdk-pixbuf isn't really used
- Removed some obsolete stuff from the spec file
- Use the latest icon cache script recommendations

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Hans de Goede <hdegoede@redhat.com> - 0.4.8-16
- Fix building with latest ocaml-images

* Thu Nov 20 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.8-15
- Rebuild for OCaml 3.11.0+beta1.

* Mon Sep 22 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.8-14
- patch -> patch0 (rhbz #463055).
- BR ocaml-lablgtk >= 2.10.1-5

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.8-12
- fix license tag

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.8-11
- Rebuild for OCaml 3.10.2

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> 0.4.8-10
- Rebuild for ppc64.

* Wed Feb 13 2008 Richard W.M. Jones <rjones@redhat.com> 0.4.8-9
- Missing BR ocaml-lablgl-devel and ocaml-lablgtk-devel

* Wed Feb 13 2008 Richard W.M. Jones <rjones@redhat.com> 0.4.8-8
- Make it BR on the latest ocaml-SDL.

* Wed Feb 13 2008 Richard W.M. Jones <rjones@redhat.com> 0.4.8-7
- Rebuild for OCaml 3.10.1
- OCaml packaging guidelines.

* Wed May 09 2007 Nigel Jones <dev@nigelj.com> 0.4.8-6
- Add ExcludeArch on ppc64 (Bug 239521)

* Sun May 06 2007 Nigel Jones <dev@nigelj.com> 0.4.8-5
- Add missing BuildRequires (SDL_ttf-devel)

* Fri May 04 2007 Nigel Jones <dev@nigelj.com> 0.4.8-4
- Add SportsGame to .desktop file
- Correct source URL

* Fri May 04 2007 Nigel Jones <dev@nigelj.com> 0.4.8-3
- Change builddep to ocaml-camlimages

* Thu May 03 2007 Nigel Jones <dev@nigelj.com> 0.4.8-2
- Add freetennis.png and alter freetennis.desktop to show icon
- Change builddep to ocaml-SDL-devel

* Tue Apr 10 2007 Nigel Jones <dev@nigelj.com> 0.4.8-1
- Initial spec file

