Name:           gforth
Version:        0.7.3
Release:        27%{?dist}
Summary:        Fast and portable implementation of the ANS Forth language

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/gforth/
Source:         http://www.complang.tuwien.ac.at/forth/gforth/gforth-0.7.3.tar.gz
Patch0:		gforth-0.7.0-shebang.patch
# s390 build fix from Debian (http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=544827)
Patch1:		gforth-0.7.0-compile-fix.patch
Patch2:		gforth-libtool-build.patch
Patch3:		configure-assumptions.patch
Patch4: gforth-configure-c99.patch
BuildRequires:  m4 libtool-ltdl-devel
BuildRequires:  libffi-devel
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires: make
Recommends:     libtool

%description
Gforth is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history, backtraces, a
decompiler and a powerful locals facility, and it even has a
manual. Gforth combines traditional implementation techniques with
newer techniques for portability and performance performance: its
inner innerpreter is direct threaded with several optimizations, but
you can also use a traditional-style indirect threaded interpreter.

%define emacs_sitestart_d  %{_datadir}/emacs/site-lisp/site-start.d
%define emacs_site_lisp  %{_datadir}/emacs/site-lisp
%define xemacs_sitestart_d %{_datadir}/xemacs/site-packages/lisp/site-start.d
%define xemacs_site_lisp %{_datadir}/xemacs/site-packages/lisp
%define gforth_datadir %{_datadir}/gforth


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

iconv -f latin1 -t utf8 AUTHORS > AUTHORS.new
mv -f AUTHORS.new AUTHORS


%build
autoreconf -iv
CFLAGS="${RPM_OPT_FLAGS} `pkg-config libffi --cflags`" %configure
# %%{_smp_mflags} breaks the build
make libdir=%{_libdir}


%install
%makeinstall
cat > $RPM_BUILD_ROOT%{gforth_datadir}/site-forth/siteinit.fs <<EOF
\ If you change this file, you need to recompile gforth.fi
EOF
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
mkdir -p $RPM_BUILD_ROOT%{gforth_datadir}/emacs
cp -f gforth.el $RPM_BUILD_ROOT%{gforth_datadir}/emacs
cat > $RPM_BUILD_ROOT%{gforth_datadir}/emacs/gforth-init.el <<EOF
(autoload 'forth-mode "gforth" "Forth mode" t)
(autoload 'run-forth "gforth" "Run Forth" t)
(add-to-list 'auto-mode-alist '("\\.fs$" . forth-mode))
EOF
for i in httpd.fs filedump.fs sieve.fs
do
   chmod 0755 $RPM_BUILD_ROOT%{_datadir}/gforth/%{version}/$i
done
for dir in %{emacs_sitestart_d} %{xemacs_sitestart_d}; do
    install -dm 755 $RPM_BUILD_ROOT$dir
    touch $RPM_BUILD_ROOT$dir/gforth-init.el
done
for dir in %{emacs_site_lisp} %{xemacs_site_lisp}; do
    install -dm 755 $RPM_BUILD_ROOT$dir
    touch $RPM_BUILD_ROOT$dir/gforth.el
done

find $RPM_BUILD_ROOT -name TAGS | xargs rm -f


%triggerin -- emacs-common
if [ -d %{emacs_sitestart_d} ]; then
  ln -sf %{gforth_datadir}/emacs/gforth-init.el %{emacs_sitestart_d} || :
  ln -sf %{gforth_datadir}/emacs/gforth.el %{emacs_site_lisp} || :
fi

%triggerin -- xemacs-common
if [ -d %{xemacs_sitestart_d} ]; then
  ln -sf %{gforth_datadir}/emacs/gforth-init.el %{xemacs_sitestart_d} || :
  ln -sf %{gforth_datadir}/emacs/gforth.el %{xemacs_site_lisp} || :
fi


%triggerun -- emacs-common
if [ $2 = 0 ]; then
  rm -f %{emacs_sitestart_d}/gforth-init.el* || :
  rm -f %{emacs_site_lisp}/gforth.el* || :
fi


%triggerun -- xemacs-common
if [ $2 = 0 ]; then
  rm -f %{xemacs_sitestart_d}/gforth-init.el* || :
  rm -f %{xemacs_site_lisp}/gforth.el* || :
fi


%files
%doc COPYING COPYING.DOC README README.vmgen NEWS NEWS.vmgen AUTHORS BUGS ChangeLog
%{_bindir}/*
%{_infodir}/*
%{_datadir}/gforth
%{_libdir}/gforth
%{_includedir}/gforth
%{_mandir}/man1/*
%ghost %{_datadir}/*emacs


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.3-26
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Florian Weimer <fweimer@redhat.com> - 0.7.3-21
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-17
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.3-15
- Fix FTBFS rhbz#1923279

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Adrian Reber <adrian@lisas.de> - 0.7.3-7
- Fix "Gforth missing dependency: libtool" (#1502327)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Adrian Reber <adrian@lisas.de> - 0.7.3-1
- updated to 0.7.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Adrian Reber <adrian@lisas.de> - 0.7.2-1
- updated to 0.7.2
- included patchset from GIT to build with GCC 4.9
- fixes "gforth: FTBFS in rawhide" (#1106528)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 02 2012 Adrian Reber <adrian@lisas.de> - 0.7.0-12
- fixes "vmgen.info not linked from dir" (#837349)

* Fri Jul 27 2012 Adrian Reber <adrian@lisas.de> - 0.7.0-11
- another try to fix the build with -O2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Adrian Reber <adrian@lisas.de> - 0.7.0-9
- added patches from Andrew Haley to fix build with -O2

* Thu Apr 05 2012 Adrian Reber <adrian@lisas.de> - 0.7.0-8
- build with -O0 until bug with -O2 is found

* Mon Mar 26 2012 Adrian Reber <adrian@lisas.de> - 0.7.0-7
- added BR libtool-ltdl-devel
- fixes "Missing libtool build dep can lead to strange errors" (#806688)
- removed buildroot and clean section

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 21 2011 Dan Horák <dan[at]danny.cz> - 0.7.0-5
- fix build on s390

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 28 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.7.0-2
- fixed license

* Wed Nov  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.7.0-1
- new release 0.7.0

* Sat Feb 23 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.6.2-12
- remove deprecated -force-mem flag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.2-11
- Autorebuild for GCC 4.3

* Sat Feb  3 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.6.2-8
- patch to remove buildpath from binary

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.6.2-7
- Rebuild for FE6

* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.6.2-6
- Rebuild for Fedora Extras 5

* Wed Sep 14 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.6.2-5
- changes to the trigger code

* Wed Sep 14 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.6.2-4
- use triggers to install (x)emacs files
- create not-empty siteinit.fs

* Tue Sep 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.6.2-3
- fix for building on x86_64
- patch fixing shebang executable path

* Sat Mar 19 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.6.2-2
- Included gforth.el

* Sun Feb 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:0.6.2-1
- Included patch for exec-shield

* Wed Oct 15 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:0.6.2-0.fdr.1
- First Fedora release
