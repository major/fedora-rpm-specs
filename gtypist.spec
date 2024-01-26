Name:			gtypist
Version: 		2.9.5
Release: 		19%{?dist}
Summary: 		GNU typing tutor
License:		GPLv3+
Url: 			ftp://ftp.gnu.org/gnu/gtypist
Source0: 		ftp://ftp.gnu.org/gnu/gtypist/gtypist-2.9.5.tar.xz
Patch0: gtypist-c99.patch
BuildRequires:  gcc
BuildRequires:		emacs
BuildRequires:		gettext
BuildRequires:		ncurses-devel
BuildRequires:		perl-generators
BuildRequires: make
Requires:		fortune-mod
Requires:		emacs-filesystem >= %{_emacs_version}
Obsoletes:		emacs-gtypist <= 2.9.4-5
Provides:		emacs-gtypist <= 2.9.4-5

%description
GNU Typist (or gtypist) is free software that assists you in learning
to type correctly.

It is intended to be used on a raw terminal without graphics. It has
been compiled and used in Unix (GNU/Linux, Aix, Solaris, openBSD) and
also in DOS/Windows (DOS 6.22, Windows 98, Windows XP).

%prep
%autosetup -p1

%build
%configure --with-lispdir='${datarootdir}/emacs/site-lisp/gtypist'
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install
%find_lang %name
rm -vf $RPM_BUILD_ROOT/usr/share/info/dir

mkdir -p $RPM_BUILD_ROOT/%{_emacs_sitelispdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_emacs_sitestartdir}
cat > gtypist-init.el <<EOF
(autoload 'gtypist-mode "gtypist-mode")
(setq auto-mode-alist (append '(("\\.typ$" . gtypist-mode)) auto-mode-alist))
EOF
cp gtypist-init.el $RPM_BUILD_ROOT/%{_emacs_sitestartdir}

%files -f %name.lang
%doc ABOUT-NLS AUTHORS NEWS COPYING QUESTIONS ChangeLog README INSTALL THANKS TODO  
%{_bindir}/*
%{_datadir}/%{name}
%{_infodir}/*
%{_mandir}/man1/*
%{_emacs_sitelispdir}/%{name}
%{_emacs_sitestartdir}/gtypist-init.el

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Florian Weimer <fweimer@redhat.com> - 2.9.5-15
- C99 compatibility fixes (#2162074)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 Zing <zing@fastmail.fm> - 2.9.5-1
- update to 2.9.5
- per emacs guidelines: addon moved into main package

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb  4 2014 Zing <zing@fastmail.fm> - 2.9.4-1
- update to 2.9.4
- drop fmt-security fix, upstream

* Mon Jan 13 2014 Zing <zing@fastmail.fm> - 2.9.3-2
- Werror=format-security fix, #1037116

* Fri Nov 22 2013 Zing <zing@fastmail.fm> - 2.9.3-1
- update to 2.9.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.9-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov  3 2011 Zing <zing@fastmail.fm> - 2.9-1
- update to 2.9
- UTF8 support

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Zing <zing@fastmail.fm> - 2.8.3-2
- add license text to emacs-gtypist subpackage

* Wed May 19 2010 Zing <zing@fastmail.fm> - 2.8.3-1
- update to 2.8.3
- fixes long standing bug of error rate display
- translation updates

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug  8 2008 Zing <zing@fastmail.fm> - 2.8.1-1
- update to 2.8.1
- license change to GPLv3+

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.7-6
- Autorebuild for GCC 4.3

* Thu Aug 16 2007 Zing <zing@fastmail.fm> - 2.7-5
- conform to Fedora Licensing Guidelines

* Fri Sep  8 2006 Zing <zing@fastmail.fm> - 2.7-4
- rebuild for FE6

* Mon Jun 12 2006 Zing <zing@fastmail.fm> - 2.7-3
- do not use makeinstall macro
- rm info dir file from buildroot?

* Wed Jun  7 2006 Zing <zing@fastmail.fm> - 2.7-2
- add preun pkg check before running install-info

* Wed Jun  7 2006 Zing <zing@fastmail.fm> - 2.7-1
- Initial RPM release.
