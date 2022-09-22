%global pkg tuareg
%global pkgname Tuareg-mode

# If the emacs-el package has installed a pkgconfig file, use that to
# determine install locations and Emacs version at build time,
# otherwise set defaults.
%if %($(pkg-config emacs) ; echo $?)
%global emacs_version 22.1
%global emacs_lispdir %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%else
%global emacs_version %(pkg-config emacs --modversion)
%global emacs_lispdir %(pkg-config emacs --variable sitepkglispdir)
%global emacs_startdir %(pkg-config emacs --variable sitestartdir)
%endif

%if 0%{?fedora} < 36
# If the xemacs-devel package has installed a pkgconfig file, use that
# to determine install locations and Emacs version at build time,
# otherwise set defaults.
%if %($(pkg-config xemacs) ; echo $?)
%global xemacs_version 21.5
%global xemacs_lispdir %{_datadir}/xemacs/site-lisp
%global xemacs_startdir %{_datadir}/xemacs/site-lisp/site-start.d
%else
%global xemacs_version %(pkg-config xemacs --modversion)
%global xemacs_lispdir %(pkg-config xemacs --variable sitepkglispdir)
%global xemacs_startdir %(pkg-config xemacs --variable sitestartdir)
%endif
%endif

Name:           emacs-common-%{pkg}
Version:        2.2.0
Release:        11%{?dist}
Summary:        Emacs and XEmacs mode for editing ocaml

License:        GPLv2+
URL:            https://github.com/ocaml/%{pkg}
Source0:        https://github.com/ocaml/tuareg/releases/download/%{version}/tuareg-%{version}.tar.gz
Source1:        COPYING

BuildArch:      noarch
BuildRequires:  emacs, emacs-el
%if 0%{?fedora} < 36
BuildRequires:  xemacs, xemacs-devel
%endif
BuildRequires: make

# Needs caml-types.el in order to use *.annot files properly.
Suggests:       ocaml-emacs


%description
Tuareg is an OCaml mode for GNU Emacs and XEmacs.  It handles
automatic indentation of Objective Caml and Caml Light code.  Key
parts of the code are highlighted using Font-Lock.  Support to run an
interactive Caml toplevel and debbuger is provided.

This package contains the common files.  Install emacs-%{pkg} to get
the complete package.


%package -n emacs-%{pkg}
Summary:        Compiled elisp files to run %{pkgname} under GNU Emacs
Requires:       emacs(bin) >= %{emacs_version}
Requires:       emacs-common-%{pkg} = %{version}-%{release}
# May be removed in Fedora 25.
Obsoletes:      emacs-%{pkg}-el <= %{version}-%{release}
Provides:       emacs-%{pkg}-el <= %{version}-%{release}
# May be removed in Fedora 39.
%if 0%{?fedora} >= 36
Obsoletes:      xemacs-%{pkg} < 2.2.0-8
%endif

%description -n emacs-%{pkg}
Tuareg is an OCaml mode for GNU Emacs and XEmacs.  It handles
automatic indentation of Objective Caml and Caml Light code.  Key
parts of the code are highlighted using Font-Lock.  Support to run an
interactive Caml toplevel and debbuger is provided.

Install this package if you need to edit OCaml code in Emacs.


%if 0%{?fedora} < 36
%package -n xemacs-%{pkg}
Summary:        Compiled elisp files to run %{pkgname} under XEmacs
Requires:       xemacs(bin) >= %{xemacs_version}
Requires:       emacs-common-%{pkg} = %{version}-%{release}
# May be removed in Fedora 25.
Obsoletes:      xemacs-%{pkg}-el <= %{version}-%{release}
Provides:       xemacs-%{pkg}-el <= %{version}-%{release}

%description -n xemacs-%{pkg}
Tuareg is an OCaml mode for GNU Emacs and XEmacs.  It handles
automatic indentation of Objective Caml and Caml Light code.  Key
parts of the code are highlighted using Font-Lock.  Support to run an
interactive Caml toplevel and debbuger is provided.

Install this package if you need to edit OCaml code in XEmacs.
%endif


%prep
%setup -q -n %{pkg}-%{version}


%build
make
make elc

# Upstream sources no longer contain 'COPYING' although they are still
# licensed under the GPL.
cp %{SOURCE1} .


%install
rm -rf $RPM_BUILD_ROOT

# For unknown reasons, the upstream 'make install' rule has been
# commented out.  This code hopefully does the right thing.  Don't
# install 'tuareg-site-file.el' since the upstream source doesn't
# compile it and it didn't exist in previous versions at all.

# Emacs.
mkdir -p $RPM_BUILD_ROOT/%{emacs_lispdir}/%{pkg}
echo %{version} > $RPM_BUILD_ROOT/%{emacs_lispdir}/%{pkg}/version
install -m 0644 *.el *.elc $RPM_BUILD_ROOT/%{emacs_lispdir}/%{pkg}
rm $RPM_BUILD_ROOT/%{emacs_lispdir}/%{pkg}/tuareg-site-file.el

%if 0%{?fedora} < 36
# XEmacs.
mkdir -p $RPM_BUILD_ROOT/%{xemacs_lispdir}/%{pkg}
echo %{version} > $RPM_BUILD_ROOT/%{xemacs_lispdir}/%{pkg}/version
install -m 0644 *.el *.elc $RPM_BUILD_ROOT/%{xemacs_lispdir}/%{pkg}
rm $RPM_BUILD_ROOT/%{xemacs_lispdir}/%{pkg}/tuareg-site-file.el
%endif


%files
%doc COPYING README.md tuareg-site-file.el


%files -n emacs-%{pkg}
%doc COPYING
%{emacs_lispdir}/%{pkg}/*.elc
%{emacs_lispdir}/%{pkg}/*.el
%{emacs_lispdir}/%{pkg}/version
#%{emacs_startdir}/*.el
%dir %{emacs_lispdir}/%{pkg}


%if 0%{?fedora} < 36
%files -n xemacs-%{pkg}
%doc COPYING
%{xemacs_lispdir}/%{pkg}/*.elc
%{xemacs_lispdir}/%{pkg}/*.el
%{xemacs_lispdir}/%{pkg}/version
#%{xemacs_startdir}/*.el
%dir %{xemacs_lispdir}/%{pkg}
%endif


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Richard W.M. Jones <rjones@redhat.com> - 2.2.0-9
- Bump release and rebuild because of broken Koji

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 2.2.0-8
- Drop XEmacs support in F36 and later

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Richard W.M. Jones <rjones@redhat.com> - 2.2.0-2
- New upstream version 2.2.0.
- Change ocaml-emacs to Suggests, like Debian.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 2.0.10-1
- Upstream release 2.0.10.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-0.2.1c837e26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.10-0.1
- Move to pre-release of 2.0.10 (from git).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 28 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-1
- New upstream version 2.0.9.
- New upstream URL and source location (on github).
- Move the elisp source files into main package to comply with updated
  packaging guidelines (https://fedoraproject.org/wiki/Packaging:Emacs).
- Update COPYING from upstream git.
- README -> README.md.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 15 2013 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-1
- New upstream version 2.0.6.
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug  8 2011 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-1
- New upstream version 2.0.4 (RHBZ#729130).
- Upstream build system is much more sane than before, so remove
  a lot of non-conventional hacks and just use make/make install.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 12 2009 Richard W.M. Jones <rjones@redhat.com> - 1.45.6-9
- Improve description (RHBZ#516997).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr 30 2008 Richard W.M. Jones <rjones@redhat.com> - 1.45.6-6
- Add runtime requires ocaml-emacs, because tuareg mode uses the file
  caml-types.el in order to do type annotation (C-c C-t).

* Sat Apr 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.45.6-5
- Add commas in dependencies & rebuild.

* Thu Feb 21 2008 Richard W.M. Jones <rjones@redhat.com> - 1.45.6-4
- Disable sym-lock in xemacs - this fixes xemacs support.

* Wed Feb 20 2008 Richard W.M. Jones <rjones@redhat.com> - 1.45.6-3
- Reenable support for xemacs.

* Tue Feb 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.45.6-1
- Initial RPM release.
