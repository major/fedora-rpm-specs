Name:           vim-perl-support
Version:        5.3.2
Release:        16%{?dist}
Summary:        Perl-IDE for VIM


# according to plugin/perl-support.vim
License:        GPLv2
URL:            http://www.vim.org/scripts/script.php?script_id=556

# curl -o perl-support-5.3.2.zip 'http://vim.sourceforge.net/scripts/download_script.php?src_id=21048'
Source0:        perl-support-%{version}.zip

#Source0:        https://github.com/WolfgangMehner/vim-plugins/archive/perlsupport-%{version}.tar.gz
Source1:        vim-perl-support.metainfo.xml

BuildArch:      noarch
BuildRequires:      perl-generators

Requires:         vim-enhanced
Requires(post):   vim-enhanced
Requires(postun): vim-enhanced

# optional requirements

# per-line Perl profiler
Requires:         perl(Devel::SmallProf)     
# Powerful feature-rich perl source code profiler
Requires:         perl(Devel::NYTProf)
# "fast" per-line Perl profiler
Requires:         perl(Devel::FastProf)
# Critique Perl source code for best-practices
Requires:         perl(Perl::Critic)         
# Generate Ctags style tags for Perl source code
Requires:         perl(Perl::Tags)           
# Parses and beautifies perl source
Requires:         perl(Perl::Tidy)           

# the following are not yet available in fedora
# Perl debugger using a Tk GUI
#Requires:         perl(Devel::ptkdb)         
# regular expression analyzer
#Requires:         perl(YAPE::Regex::Explain) 

%global vimfiles  %{_datadir}/vim/vimfiles

# strip out false provides/requires from codesnippets
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{vimfiles}/perl-support/codesnippets
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{vimfiles}/perl-support/codesnippets


%description
Perl Support implements a Perl-IDE for Vim/gVim. It is written to considerably
speed up writing code in a consistent style.  This is done by inserting
complete statements, comments, idioms, code snippets, templates, and POD
documentation.  Reading perldoc is integrated.  Syntax checking, running a
script, running perltidy,  running perlcritics, starting a debugger and a
profiler can be done with a keystroke.


%prep
%setup -q -c


%build
# build is empty


%install
install -m 755 -d %{buildroot}%{vimfiles}/perl-support
cp -r autoload %{buildroot}%{vimfiles}/autoload
cp -r doc %{buildroot}%{vimfiles}/doc
cp -r ftplugin %{buildroot}%{vimfiles}/ftplugin
cp -r plugin %{buildroot}%{vimfiles}/plugin
cp -r perl-support/codesnippets %{buildroot}%{vimfiles}/perl-support/codesnippets
cp -r perl-support/modules/ %{buildroot}%{vimfiles}/perl-support/modules
cp -r perl-support/templates %{buildroot}%{vimfiles}/perl-support/templates
cp -r perl-support/wordlists/ %{buildroot}%{vimfiles}/perl-support/wordlists
install -m 755 -d %{buildroot}%{vimfiles}/perl-support/scripts
install -m 755 -p perl-support/scripts/*.{pl,sh} \
    %{buildroot}%{vimfiles}/perl-support/scripts

# Install AppData.
mkdir -p %{buildroot}%{_datadir}/appdata/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/


%post
umask 022
cd %{_datadir}/vim/vimfiles/doc
vim -u NONE -esX -c "helptags ." -c quit
exit 0


%postun
if [ $1 -eq 0 ]; then
   umask 022
   cd %{_datadir}/vim/vimfiles/doc
   >tags
   vim -u NONE -esX -c "helptags ." -c quit
fi
exit 0


%files
%doc perl-support/README.perlsupport perl-support/doc/* perl-support/rc
%{vimfiles}/perl-support
%{vimfiles}/autoload/*
%{vimfiles}/doc/*.txt
%{vimfiles}/ftplugin/*.vim
%{vimfiles}/plugin/perl-support.vim
%{_datadir}/appdata/vim-perl-support.metainfo.xml



%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 07 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 5.3.2-3
- add appdata metainfo file (RHBZ#1246541)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 17 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 5.3.2-1
- Update to latest upstream version 5.3.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Iain Arnell <iarnell@gmail.com> 5.2-1
- update to latest upstream version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 5.0.1-4
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 21 2012 Iain Arnell <iarnell@gmail.com> 5.0.1-1
- update to latest upstream version

* Tue Apr 10 2012 Iain Arnell <iarnell@gmail.com> 5.0-1
- update to latest upstream version

* Fri Feb 17 2012 Iain Arnell <iarnell@gmail.com> 4.15-1
- update to latest upstream version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Iain Arnell <iarnell@gmail.com> 4.14-1
- update to latest upstream
- drop templates patch

* Fri Sep 16 2011 Iain Arnell <iarnell@gmail.com> 4.13-2
- update patch to fix more template problems

* Wed Sep 14 2011 Iain Arnell <iarnell@gmail.com> 4.13-1
- update to latest upstream version
- patch to fix handling of local templates

* Fri Jun 24 2011 Iain Arnell <iarnell@gmail.com> 4.12-1
- update to latest upstream version
- update filtering for rpm 4.9

* Thu Apr 21 2011 Iain Arnell <iarnell@gmail.com> 4.11-1
- update to latest upstream version

* Sun Feb 27 2011 Iain Arnell <iarnell@gmail.com> 4.10-1
- update to latest upstream version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Iain Arnell <iarnell@gmail.com> 4.9-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 4.8-2
- use version number in source0 filename

* Mon May 31 2010 Iain Arnell <iarnell@gmail.com> 4.8-1
- update to latest upstream version

* Tue Apr 13 2010 Iain Arnell <iarnell@gmail.com> 4.7.1-1
- update to latest upstream version

* Wed Mar 03 2010 Iain Arnell <iarnell@gmail.com> 4.7-1
- update to 4.7

* Mon Jan 25 2010 Iain Arnell <iarnell@gmail.com> 4.6.1-1
- update to 4.6.1 - fix screen refresh when using syntax check (Vim only, not
  gVim)

* Tue Jan 05 2010 Iain Arnell <iarnell@gmail.com> 4.6-1
- update to latest upstream release
- update requires/provides filtering

* Mon Oct 05 2009 Iain Arnell <iarnell@gmail.com> 4.5-1
- update to 4.5

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Iain Arnell <iarnell@gmail.com> 4.4-1
- update to 4.4

* Mon May 25 2009 Iain Arnell <iarnell@gmail.com> 4.3-1
- update to 4.3

* Fri May 08 2009 Iain Arnell <iarnell@gmail.com> 4.2-1
- update to 4.2

* Thu Apr 30 2009 Iain Arnell <iarnell@gmail.com> 4.1-3
- require Devel::FastProf and Perl::Tags
- use global macro, not define

* Mon Apr 13 2009 Iain Arnell <iarnell@gmail.com> 4.1-2
- require perl(Devel::NYTProf) now that it's available

* Tue Mar 17 2009 Iain Arnell <iarnell@gmail.com> 4.1-1
- update to latest upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Iain Arnell <iarnell@gmail.com> 4.0.1-2
- require perl(Devel::SmallProf) now that it's available

* Fri Jan 02 2009 Iain Arnell <iarnell@gmail.com> 4.0.1-1
- Bugfix: Error message in some functions that issue a prompt.

* Fri Jan 02 2009 Iain Arnell <iarnell@gmail.com> 4.0-1
- update to 4.0:
 + Completely new template system. Most menu items now user definable.
 + Plugin split into autoloadable modules (makes Vim startup faster).
 + Submenus for perlcritic severity and verbosity.
 In consequence there are some obsolete files and global variables, and some
 new files and hotkeys.
- fix bug in Perl_Input function

* Fri Nov 28 2008 Iain Arnell <iarnell@gmail.com> 3.9.1-1
- create vim-perl-support
