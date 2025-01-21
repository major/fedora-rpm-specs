Name:           techtalk-pse
Version:        1.2.0
Release:        18%{?dist}
Summary:        Presentation software designed for technical people

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://git.annexia.org/?p=techtalk-pse.git;a=summary
# No website hosts the tarballs at present:
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(Gtk3::WebKit)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  vte291
BuildRequires:  /usr/bin/pod2man

# This shouldn't have to be explicit but it is omitted from the
# generated Requires for some reason (RHBZ#1997749).
Requires: vte291


%description
Tech Talk PSE is is Linux Presentation Software designed by technical people to
give technical software demonstrations to other technical people. It is
designed to be simple to use (for people who know how to use an editor and the
command line) and powerful, so that you can create informative, technically
accurate and entertaining talks and demonstrations.

Tech Talk PSE is good at opening editors at the right place, opening shell
prompts with preloaded history, compiling and running things during the
demonstration, displaying text, photos, figures and video.

Tech Talk PSE is bad at slide effects, chart junk and bullet points.


%prep
%setup -q
echo '// empty' >> examples/simple/code.js


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc COPYING README TODO examples
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jan 25 2022 Richard Jones <rjones@redhat.com> - 1.2.0-11
- Add Requires vte291 (RHBZ#1997749)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Richard Jones <rjones@redhat.com> - 1.2.0-1
- New upstream version 1.2.0.
- Supports Gtk3::WebKit.
- Fixed other BuildRequires.
- Remove BuildRoot, clean.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Richard Jones <rjones@redhat.com> - 1.1.0-9
- Remove useless defattr in files section.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 1.1.0-5
- Perl 5.18 rebuild

* Mon Feb 18 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-4
- +BR /usr/bin/pod2man.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-1
- New upstream development version 1.1.0.
- This version requires Gtk2::WebKit (WebKit bindings) and Gnome2::Vte
  (VTE - a GNOME terminal emulator).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Ian Weller <iweller@redhat.com> - 1.0.1-1
- New upstream release

* Mon Jun 21 2010 Ian Weller <iweller@redhat.com> - 1.0.0-3
- New patch: patch-1.0.0-ensure-display-of-labels.diff
  "There's a problem in 1.0.0 [upstream] that labels
  are not displayed with certain versions of perl-Gtk2."
  This patch resolves this issue.
- Go totally OCD and change the RPM build root macros

* Tue Jun  8 2010 Ian Weller <iweller@redhat.com> - 1.0.0-2
- Include examples
- Use macros in source URL

* Mon Jun  7 2010 Ian Weller <iweller@redhat.com> - 1.0.0-1
- First build
