%global pkg spice-mode
%global pkgname Emacs-spice-mode

%if %($(pkg-config emacs) ; echo $?)
%global emacs_version 21.1
%global emacs_lispdir %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%else
%global emacs_version %(pkg-config emacs --modversion)
%global emacs_lispdir %(pkg-config emacs --variable sitepkglispdir)
%global emacs_startdir %(pkg-config emacs --variable sitestartdir)
%endif

Name:		emacs-%{pkg}
Version:	1.2.25
Release:	36%{?dist}
Summary:	SPICE Mode for GNU Emacs

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://spice-mode.4t.com/
Source0:	http://spice-mode.4t.com/spice-mode-1.2.25.tar.gz
Source1:	%{pkg}-init.el
#Patch provided by shakthi kannan - shakthimaan AT gmail dot com and chitlesh goorah - chitlesh AT gmail dot com
#Fixes free variables and backquote,adds nguntmeg to simulators list and minor fixes
Patch0:		emacs-spice-mode-fix.patch

BuildArch:	noarch
BuildRequires:	emacs emacs-el
Requires:	emacs >= %{emacs_version} gnucap

Provides:	%{name}-el = %{version}-%{release}
Obsoletes:	%{name}-el < 1.2.25-33

%description
This package provides an Emacs major mode for editing SPICE decks.

%prep
%setup -q -n %{pkg}
%patch -P0 -p2

%build
emacs -batch -f batch-byte-compile %{pkg}.el

%install
install -pm 755 -d %{buildroot}%{emacs_lispdir}/%{pkg}/
install -pm 755 -d %{buildroot}%{emacs_startdir}	
install -pm 644 %{pkg}.* %{buildroot}%{emacs_lispdir}/%{pkg}/
install -pm 644 %{SOURCE1} %{buildroot}%{emacs_startdir}


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS BUGS Changes README test_netlist.cir
%{emacs_lispdir}/%{pkg}/*.el
%{emacs_lispdir}/%{pkg}/*.elc
%{emacs_startdir}/%{pkg}-init.el
%dir %{emacs_lispdir}/%{pkg}
%dir %{emacs_startdir}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.25-35
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 15 2024 Tim Landscheidt <tim@tim-landscheidt.de> - 1.2.25-33
- Obsolete -el subpackage (#1234532)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.25-16
- Modernise spec
- Use %%license

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.25-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.25-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.25-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.2.25-10
- Removed requires gwave

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Arun SAG <sagarun@gmail.com> - 1.2.25-7
- Fix: Remove gwave as a dependency from F15-F17 

* Thu  Nov 10 2011 Arun SAG <sagarun@gmail.com> 1.2.25-6
- Fix: Remove gwave from requires for F15

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 22 2010 Arun SAG <sagarun@gmail.com> - 1.2.25-4
- Fixed instllation failure due to failed dependency gwave in EL5

* Wed Dec 16 2009 Arun SAG <sagarun [AT] gmail dot com> - 1.2.25-3
- Exculded ppc64 which caused broken dependencies

* Mon Dec 13 2009 Arun SAG <sagarun [AT] gmail dot com> - 1.2.25-2
- More file extenstions are handled by spice-mode
- Default simulator is now Gnucap
- Default wave form viewer is now Gwave
- Added gnucap and gwave to requires
- Fixed free variables and blackquote


* Sun Dec 06 2009 Arun SAG <sagarun [AT] gmail dot com> - 1.2.25-1
- Initial release 1.2.25-1
