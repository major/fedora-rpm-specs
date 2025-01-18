%global pkg riece
%global pkgname Riece

Name:		emacs-common-%{pkg}
Version:	8.0.0
Release:	29%{?dist}
Summary:	Yet Another IRC Client for Emacs and XEmacs

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://riece.nongnu.org
Source0:	http://dl.sv.gnu.org/releases/%{pkg}/%{pkg}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	emacs-nox, texinfo-tex
%if 0%{?fedora} < 36
BuildRequires:	xemacs
%endif
BuildRequires:	make

%description
Riece is an IRC client for Emacs.

Riece provides the following features:

- Several IRC servers may be used at the same time.
- Essential features can be built upon the extension framework (called
  "add-on") capable of dependency tracking.
- Installation is easy.  Riece doesn't depend on other packages.
- Setup is easy.  Automatically save/restore the configuration.
- Riece uses separate windows to display users, channels, and
  dialogues.  The user can select the window layout.
- Step-by-step instructions (in info format) are included.
- Mostly compliant with RFC 2812.

%package -n emacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under GNU Emacs
Requires:	emacs(bin) >= %{_emacs_version}
Requires:	emacs-common-%{pkg} = %{version}-%{release}
Provides:	emacs-%{pkg}-el = %{version}-%{release}
Obsoletes:	emacs-%{pkg}-el < %{version}-%{release}
%if 0%{?fedora} < 36
Obsoletes:	xemacs-%{pkg} < 8.0.0-20
%endif

%description -n emacs-%{pkg}
This package contains the byte compiled elisp packages to run
%{pkgname} with GNU Emacs.


%if 0%{?fedora} < 36
%package -n xemacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under XEmacs
Requires:	xemacs(bin) >= %{_xemacs_version}
Requires:	emacs-common-%{pkg} = %{version}-%{release}
Provides:	xemacs-%{pkg}-el = %{version}-%{release}
Obsoletes:	xemacs-%{pkg}-el < %{version}-%{release}

%description -n xemacs-%{pkg}
This package contains the byte compiled elisp packages to use
%{pkgname} with XEmacs.
%endif


%prep
%setup -q -n %{pkg}-%{version}

%build
%configure
cat > %{name}-init.el <<"EOF"
(autoload 'riece "riece" "Start Riece" t)
EOF

%install
make -C doc install infodir=$RPM_BUILD_ROOT%{_infodir}
# don't package but instead update in pre and post
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# byte-compile & install elisp files with emacs
make -C lisp EMACS=emacs
make -C lisp install EMACS=emacs lispdir=$RPM_BUILD_ROOT%{_emacs_sitelispdir}
%__mkdir_p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
install -m 644 %{name}-init.el $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
make -C lisp clean

%if 0%{?fedora} < 36
# byte-compile & install elisp files with xemacs
%__mkdir_p $RPM_BUILD_ROOT%{_xemacs_sitepkgdir}/etc/%{pkg}
make -C lisp EMACS=xemacs
make -C lisp install EMACS=xemacs lispdir=$RPM_BUILD_ROOT%{_xemacs_sitelispdir}

# move data files installed in site-lisp, to sitepkgdir
mv $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}/*.rb \
	$RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}/*.xpm \
	$RPM_BUILD_ROOT%{_xemacs_sitepkgdir}/etc/%{pkg}/
%__mkdir_p $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
install -m 644 %{name}-init.el $RPM_BUILD_ROOT%{_xemacs_sitestartdir}/%{pkg}-init.el
%endif

%files
%doc README README.ja NEWS NEWS.ja AUTHORS COPYING
%doc %{_infodir}/*.gz


%files -n emacs-riece
%{_emacs_sitelispdir}/riece/*.elc
%{_emacs_sitelispdir}/riece/*.el
%{_emacs_sitelispdir}/riece/*.xpm
%{_emacs_sitelispdir}/riece/*.rb
%{_emacs_sitestartdir}/*.el
%dir %{_emacs_sitelispdir}/riece


%if 0%{?fedora} < 36
%files -n xemacs-riece
%{_xemacs_sitelispdir}/riece/*.elc
%{_xemacs_sitelispdir}/riece/*.el
%{_xemacs_sitepkgdir}/etc/riece/*.rb
%{_xemacs_sitepkgdir}/etc/riece/*.xpm
%{_xemacs_sitestartdir}/*.el
%dir %{_xemacs_sitelispdir}/riece
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 8.0.0-28
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 8.0.0-20
- Drop XEmacs support in F36 and later

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Daiki Ueno <dueno@redhat.com> - 8.0.0-8
- drop -el subpackages (#1234542)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 31 2011 Daiki Ueno <dueno@redhat.com> - 8.0.0-1
- new upstream release
- remove riece-xemacs.patch since it is upstreamed

* Wed Mar 16 2011 Daiki Ueno <dueno@redhat.com> - 7.0.3-1
- new upstream release
- add riece-xemacs.patch to compile with XEmacs 21.5
- remove deprecated BuildRoot stuff

* Mon May 31 2010 Daiki Ueno <dueno@redhat.com> - 7.0.0-1
- new upstream release.

* Fri Apr 16 2010 Daiki Ueno <dueno@redhat.com> - 6.1.0-3
- fix typo; define and use pkgname for readability.

* Tue Apr  6 2010 Daiki Ueno <ueno@unixuser.org> - 6.1.0-2
- change the encoding of Japanese docs to UTF-8.

* Mon Apr  5 2010 Daiki Ueno <ueno@unixuser.org> - 6.1.0-1
- initial packaging for Fedora.
