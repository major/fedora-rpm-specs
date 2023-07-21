%global pkg ess
%global pkgname Emacs Speaks Statistics

%global plevel_appendix %{?plevel:-%{plevel}}

Name:           emacs-common-%{pkg}
Version:        18.10.2
Release:        9%{?dist}
Summary:        %{pkgname} add-on package for Emacs

# The ess license is GPLV+2, the license of julia-mode.el is MIT
License:        GPLv2+ and MIT
URL:            http://ess.r-project.org/
Source0:        http://ess.r-project.org/downloads/ess/ess-%{version}%{plevel_appendix}.tgz

# install el files (taken from upstream commit)
Patch0:         ess-18.10.2-install_el_files.patch

BuildArch:      noarch

BuildRequires:  emacs
BuildRequires:  make
BuildRequires:  R-core
BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)
BuildRequires:  tex(parskip.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(svn.sty)
BuildRequires:  tex(epsf.tex)

# Merge back -el subpackage for emacs
Obsoletes:      emacs-ess-el  < 15.03
Provides:       emacs-ess-el  < 15.03

# Support for xemacs has been dropped upstream
Obsoletes:      xemacs-ess    < 15.03
Obsoletes:      xemacs-ess-el < 15.03

%description

%{pkgname} (ESS) is an add-on package for GNU Emacs.
It provides Emacs-based front ends for popular statistics packages.

ESS provides an intelligent, consistent interface between the user and
the software.  ESS interfaces with S-PLUS, R, SAS, BUGS and other
statistical analysis packages under the Unix, Microsoft Windows, and
Apple Mac OS operating systems.  ESS is a package for the GNU Emacs
whose features ESS uses to streamline the creation and use of
statistical software.  ESS knows the syntax and grammar of statistical
analysis packages and provides consistent display and editing features
based on that knowledge.  ESS assists in interactive and batch
execution of statements written in these statistical analysis
languages.

This package contains the files common to GNU Emacs %{pkgname}
package.

%package -n emacs-%{pkg}
Summary:        Files to run %{pkgname} under GNU Emacs
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-common-%{pkg} = %{version}-%{release}

%description -n emacs-%{pkg}
This package contains the files to run %{pkgname} with GNU Emacs.

%package -n emacs-%{pkg}-doc
Summary:        Documentation of %{pkgname}

%description -n emacs-%{pkg}-doc
This package contains the documentation of %{pkgname}.


%prep
%autosetup -p1 -n %{pkg}-%{version}%{plevel_appendix}
( cd doc && chmod u+w html info ) # fix perms to ensure builddir can be deleted

%build
make

# create an init file that is loaded when a user starts up emacs to
# tell emacs to autoload our package's Emacs code when needed
cat > %{name}-init.el <<"EOF"
;;; Set up %{name} for Emacs.
;;;
;;; This file is automatically loaded by emacs's site-start.el
;;; when you start a new emacs session.

(require 'ess-site)

EOF


%install
INITDIR=${RPM_BUILD_ROOT}%{_emacs_sitestartdir}
PKGLISP=${RPM_BUILD_ROOT}%{_emacs_sitelispdir}/%{pkg}
ETCDIR=${PKGLISP}/etc
INFODIR=${RPM_BUILD_ROOT}%{_infodir}

%{__install} -m 755 -d $INITDIR
%{__install} -m 644 %{name}-init.el $INITDIR/%{pkg}-init.el
%{__install} -m 755 -d $PKGLISP
%{__install} -m 755 -d $INFODIR
%{__make} install \
          PREFIX=${RPM_BUILD_ROOT}%{_prefix} \
          LISPDIR=$PKGLISP \
          INFODIR=$INFODIR \
	  DOCDIR=${RPM_BUILD_ROOT}%{_docdir}/emacs-%{pkg}-doc \
          ETCDIR=$ETCDIR

%{__rm} -f $INFODIR/dir # don't package but instead update in pre and post

## now fix permissions on doc files that aren't UTF-8
for i in ChangeLog ChangeLog.lisp doc/TODO
do
    /usr/bin/iconv -f iso8859-1 -t utf-8 $i > $i.conv && /bin/mv -f $i.conv $i
done
# Copy documentation
for file in README VERSION doc/*.css doc/html doc/*.pdf
do
  cp -pr $file ${RPM_BUILD_ROOT}%{_docdir}/emacs-%{pkg}-doc
done

%files
%license COPYING
%doc README ANNOUNCE VERSION ChangeLog
%doc fontlock-test
%doc LDA
%doc etc/R-ESS-bugs.R
%doc etc/other
%doc %{_infodir}/*.gz

%files -n emacs-%{pkg}
%license COPYING
%{_emacs_sitelispdir}/%{pkg}
%{_emacs_sitestartdir}/*.el

%files -n emacs-%{pkg}-doc
%license COPYING
%{_docdir}/emacs-%{pkg}-doc

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.10.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 22 2020 José Matos <jamatos@fedoraproject.org> - 18.10.2-2
- also install el files in the package directory

* Sat Mar 21 2020 José Matos <jamatos@fedoraproject.org> - 18.10.2-1
- update to 18.10.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 José Matos <jamatos@fedoraproject.org> - 17.11-1
- update to 17.11
- remove julia.el from sources since it already there

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 José Matos <jamatos@fedoraproject.org> - 16.10-3
- add ess-julia.jl that was missing and is required to run julia on ess (bz 1435576)

* Thu Mar 16 2017 José Matos <jamatos@fedoraproject.org> - 16.10-2
- download separately julia-mode.el and use as source1

* Wed Mar 15 2017 José Matos <jamatos@fedoraproject.org> - 16.10-1
- update to 16.10

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May  8 2016 José Matos <jamatos@fedoraproject.org> - 16.04-1
- update to 16.04

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 José Matos <jamatos@fedoraproject.org> - 15.03-2
- Provide the -el sub-package for old versions

* Mon Jul 27 2015 José Matos <jamatos@fedoraproject.org> - 15.03-1
- Update to 15.03-1
- remove xemacs support since it was dropped upstream in version 12.04
- absorve -el supbackpage
- add documentation subpackage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 12.09-2
- Add additional "BuildRequires:  tex(epsf.tex)" workaround for (#868011)

* Sat Nov 17 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 12.09-1
- Update to upstream 12.09 (#808707)
- Add BuildRequires for individual tex packages (e.g. parskip)
  for build of PDF docs for texlive 2012 (only in f18+)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild


* Wed Sep 21 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.14-1
- Update to upstream 5.14 (#654727)
- Drop XEmacs patch, workaround has now been implemented upstream.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 15 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.11-2
- Add patch to use ".r$" as regex in start start (workaround for problems
  with XEmacs misidentify Perl scripts as R scripts #631707)

* Sun Jul 18 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.11-1
- Update to upstream 5.11 (#594669)

* Sun May 16 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.8-1
- Update to upstream 5.8 (#544472).
- Fixes problems with help() function in recent R releases.

* Wed Nov  4 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.5-1
- Update to latest upstream (5.5)
- Build all docs, PDF, DVI no longer distributed in tarball

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.3.10-1
- Update to latest upstream (5.3.10)
- Add BR: texinfo-tex
- Fix paths to installation of documentation

* Mon Aug  4 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.3.8-1
- Update to latest upstream (5.3.8)

* Tue Apr 29 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.3.7-1
- Update to new upstream release (5.3.7)

* Sun Nov 18 2007 <alexlan@fedoraproject.org> - 5.3.6-2
- Moved all non-code related files in etc/ to documentation directory
- Make sure all doc files are UTF-8
- Fix post, preun scriptlets and add Requires for installing info
  files

* Tue Nov 13 2007 <alexlan@fedoraproject.org> - 5.3.6-1
- Initial packaging, borrowed some elements of package by Tom Moertel
  <tom-rpms@moertel.com>
