Summary: Patch stack for Git repositories
Name: stgit
Version: 1.5
Release: 4%{?dist}
License: GPLv2
URL: https://stacked-git.github.io/
Source: https://github.com/stacked-git/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: asciidoc
BuildRequires: git-core
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: xmlto
Requires: git-core
Requires: git-email
Requires: python3
Requires: vim-filesystem

%description
StGit is a Python application providing similar functionality
to Quilt (i.e. pushing/popping patches to/from a stack) on top of Git.
These operations are performed using Git commands and the patches
are stored as Git commit objects, allowing easy merging of the StGit patches
into other repositories using standard Git functionality.

Note that StGit is not an SCM interface on top of Git and it expects
a previously initialized Git repository. For standard SCM operations,
either use plain Git commands or the Cogito tool.

%prep
%setup -q

%build
make all doc

%install
make install install-doc PYTHON=python3 DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix}

# Install data files
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/completion
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/examples
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/templates
install -m 644 completion/* $RPM_BUILD_ROOT%{_datadir}/%{name}/completion/
install -m 644 examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}/examples/
install -m 644 build/lib/stgit/templates/* $RPM_BUILD_ROOT%{_datadir}/%{name}/templates/
install -m 644 -D contrib/stgbashprompt.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/contrib/stgbashprompt.sh

# Install bash completion
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
ln -s ../..%{_datadir}/%{name}/completion/stgit.bash \
    $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}

# Install vim syntax highlighting
install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax
install -m 644 contrib/vim/syntax/*.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax/
install -m 644 -D contrib/vim/ftdetect/stg.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/ftdetect/stg.vim

%files
%doc COPYING
%{_bindir}/stg
%{python3_sitelib}/*
%{_mandir}/man1/stg*
%{_sysconfdir}/bash_completion.d/
%{_datadir}/stgit/
%{_datadir}/vim/vimfiles/syntax/*.vim
%{_datadir}/vim/vimfiles/ftdetect/stg.vim

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5-2
- Rebuilt for Python 3.11

* Mon Feb 21 2022 Peter Schiffer <peter+fedora@pschiffer.eu> - 1.5-1
- resolves: #2047946
  updated to 1.5

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 07 2021 Peter Schiffer <peter+fedora@pschiffer.eu> - 1.4-1
- resolves: #2007998
  updated to 1.4

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1-2
- Rebuilt for Python 3.10

* Sat May 29 2021 Peter Schiffer <peter+fedora@pschiffer.eu> - 1.1-1
- resolves: #1955877
  updated to 1.1

* Fri Feb 19 2021 Peter Schiffer <peter+fedora@pschiffer.eu> - 1.0-1
- resolves: #1926050
  updated to 1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Zane Bitter <zbitter@redhat.com> - 0.23-3
- resolves: #1915049
  Fix bash completion

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.23-1
- resolves: #1846723
  updated to 0.23

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.22-2
- Rebuilt for Python 3.9

* Wed Mar 11 2020 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.22-1
- resolves: #1811808
  updated to 0.22

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.21-1
- resolves: #1766354
  updated to 0.21

* Mon Oct 14 2019 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.20-1
- resolves: #1758807
  updated to 0.20

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.19-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.19-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Dan Horák <dan[at]danny.cz> - 0.19-1
- updated to 0.19
- drop upstreamed patch
- switch to Python3

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.18-4
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 24 2017 Peter Schiffer <pschiffe@redhat.com> - 0.18-1
- resolves: #1513726
  updated to 0.18

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Peter Schiffer <pschiffe@redhat.com> - 0.17.1-1
- resolves: #1014240
  updated to 0.17.1
- resolves: #1004478
  added dependency on git-email package, so the stg mail command
  can function properly

* Wed Jul 31 2013 Peter Schiffer <pschiffe@redhat.com> - 0.17-3
- fixed dirty index errors when resolving conflicts

* Tue Jul 30 2013 Peter Schiffer <pschiffe@redhat.com> - 0.17-2
- included vim syntax highlighting (thanks to Zane Bitter <zbitter@redhat.com>)

* Thu Jul  4 2013 Peter Schiffer <pschiffe@redhat.com> - 0.17-1
- resolves: #979618
  updated to 0.17

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec  4 2012 Peter Schiffer <pschiffe@redhat.com> - 0.16-2
- resolves: #872651
  fixed regression when "stg new" command was ignoring patchdescr.tmpl file

* Mon Oct 22 2012 Peter Schiffer <pschiffe@redhat.com> - 0.16-1
- updated to 0.16

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.14.3-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.14.3-4
- Rebuild for Python 2.6

* Tue Dec 02 2008 James Bowes <jbowes@redhat.com> 0.14.3-3
- Try and make the summary text better

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.14.3-2
- Rebuild for Python 2.6

* Tue Jun 17 2008 James Bowes <jbowes@redhat.com> 0.14.3-1
- Update to 0.14.3

* Wed Mar 26 2008 James Bowes <jbowes@redhat.com> 0.14.2-1
- Update to 0.14.2

* Wed Dec 12 2007 James Bowes <jbowes@redhat.com> - 0.14.1-1
- Update to 0.14.1

* Thu Aug 23 2007 James Bowes <jbowes@redhat.com> - 0.13-2
- Mark license as GPLv2+

* Sun Aug 05 2007 James Bowes <jbowes@redhat.com> - 0.13-1
- Update to 0.13

* Wed Apr 25 2007 James Bowes <jbowes@redhat.com> - 0.12.1-2
- Use macro for datadir.

* Thu Apr 19 2007 James Bowes <jbowes@redhat.com> - 0.12.1-1
- Update version.
- Don't install the bash prompt shell script as executable.

* Fri Feb 02 2007 James Bowes <jbowes@redhat.com> - 0.12-1
- Initial packaging.
