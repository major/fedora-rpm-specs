%global bash_completion_dir %(pkg-config --variable=completionsdir bash-completion || echo /etc/bash_completion.d)/

Name:           tig
Version:        2.5.8
Release:        4%{?dist}
Summary:        Text-mode interface for the git revision control system

License:        GPL-2.0-or-later
URL:            https://jonas.github.io/tig/
Source0:        https://github.com/jonas/tig/releases/download/tig-%version/tig-%version.tar.gz

BuildRequires:  asciidoc
BuildRequires:  bash-completion
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  xmlto
Requires:       git-core

%description
Tig is a repository browser for the git revision control system that
additionally can act as a pager for output from various git commands.

When browsing repositories, it uses the underlying git commands to present the
user with various views, such as summarized revision log and showing the commit
with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.


%prep
%autosetup


%build
%configure
%make_build all doc-man doc-html

#Convert to unix line endings
sed -i -e 's/\r//' *.html

# Remove shebang from bash-completion script
sed -i '/^#!bash/,+1 d' contrib/%{name}-completion.bash


%install
%make_install install-doc-man

# Setup bash completion
install -Dpm 644 contrib/%{name}-completion.bash %{buildroot}%{bash_completion_dir}/%{name}


%files
%license COPYING
%doc COPYING NEWS.adoc README.adoc *.html
%{_bindir}/tig
%{bash_completion_dir}
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_mandir}/man1/tig.1*
%{_mandir}/man5/tigrc.5*
%{_mandir}/man7/tigmanual.7*


%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 Jason L Tibbitts III <j@tib.bs> - 2.5.8-2
- Update to 2.5.8.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 26 2022 Jason L Tibbitts III <j@tib.bs> - 2.5.7-1
- Update to 2.5.7.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Jason L Tibbitts III <j@tib.bs> - 2.5.6-1
- Update to 2.5.6.

* Sun Apr 10 2022 Todd Zullinger <tmz@pobox.com> - 2.5.5-3
- replace git with git-core in BuildRequires and Requires

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Jason L Tibbitts III <j@tib.bs> - 2.5.5-1
- Update to 2.5.5.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.5.4-1
- Update to 2.5.4.

* Mon Mar 8 2021 Steve Traylen <steve.traylen@cern.ch> - 2.5.3-1
- Update to 2.5.3.

* Mon Feb 15 2021 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.5.2-1
- Update to 2.5.2.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.5.1-1
- Update to 2.5.1.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.5.0-1
- Update to 2.5.0.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.4.1-1
- Update to 2.4.1.

* Sun Jul 22 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.4.0-1
- Update to 2.4.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.3.3-3
- Add build dependency on gcc.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.3.3-1
- Update to 2.3.3.

* Tue Dec 19 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.3.2-1
- Update to 2.3.2.

* Fri Nov 17 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.3.0-1
- Update to 2.3.0.  Upstream has moved to github.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 11 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.2-3
- Move the bash completion dir thing into a macro.  I will probably just make
  this a system-wide macro at some point.

* Thu Aug 11 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.2-2
- Handle case where pkg-config fails (EL6 and EL5).  Might as well test those
  magic EPEL RPM macros.
- Use License tag.
- Remove useless delete of test-graph; hasn't done anything for ages.
- Use %%make_install.

* Thu Aug 11 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.2-1
- Update to 2.2.
- Remove needless cruft from spec and be consistent about using %%buildroot.
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.1-3
- Remove pointless %%defattr statement.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.1-1
- Update to 2.1.1.

* Thu Mar 12 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1-1
- Update to 2.1.

* Sat Feb 14 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.3-2
- Move bash completion to %%{_datadir}/bash-completion/completions

* Sun Sep 28 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.0.3-1
- New upstream release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.0.2-1
- New upstream release

* Mon Aug 26 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.2.1-1
- New upstream release
- Add bash completion (bz #1000823)

* Mon Aug 12 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.2-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.1-1
- Update to 1.1.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0-1
- Update to 1.0.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 02 2011 James Bowes <jbowes@redhat.com> 0.18-1
- Update to 0.18

* Thu Mar 10 2011 Todd Zullinger <tmz@pobox.com> - 0.17-1
- Update to 0.17

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.16.2-2
- Rebuilt for gcc bug 634757

* Wed Sep 22 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.16.2-1
- Update to 0.16.2

* Mon Sep 20 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.16.1-1
- Update to 0.16.1

* Tue Apr 13 2010 James Bowes <jbowes@redhat.com> 0.15-2
- Add tigmanual man page

* Tue Apr 13 2010 James Bowes <jbowes@redhat.com> 0.15-1
- tig-0.15

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Todd Zullinger <tmz@pobox.com> - 0.14.1-2
- Temporarily disable asciidoc's safe mode until bug 506953 is fixed

* Fri Apr 03 2009 James Bowes <jbowes@redhat.com> 0.14.1-1
- tig-0.14.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 08 2009 James Bowes <jbowes@redhat.com> 0.14-1
- tig-0.14

* Tue Dec 02 2008 James Bowes <jbowes@redhat.com> 0.12.1-1
- tig-0.12.1

* Sat Sep 27 2008 Todd Zullinger <tmz@pobox.com> 0.12-1
- tig-0.12

* Sun Apr 06 2008 James Bowes <jbowes@redhat.com> 0.11-1
- tig-0.11

* Tue Mar 25 2008 Todd Zullinger <tmz@pobox.com> 0.10.1-2
- use %%configure so ncursesw is picked up for utf-8 support
- BuildRequire git so configure finds git-config and git-repo-config
- change Requires: git-core to git

* Wed Mar 19 2008 James Bowes <jbowes@redhat.com> 0.10.1-1
- tig-0.10.1

* Mon Mar 17 2008 James Bowes <jbowes@redhat.com> 0.10-1
- tig-0.10

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.1-2
- Autorebuild for GCC 4.3

* Sun Sep 30 2007 James Bowes <jbowes@redhat.com> - 0.9.1-1
- tig-0.9.1

* Thu Sep 20 2007 James Bowes <jbowes@redhat.com> - 0.9-1
- tig-0.9

* Thu Aug 23 2007 James Bowes <jbowes@redhat.com> - 0.8-2
- Mark license as GPLv2+

* Tue Jun 19 2007 James Bowes <jbowes@redhat.com> - 0.8-1
- tig-0.8

* Sat Jun 02 2007 James Bowes <jbowes@redhat.com> - 0.7-4
- Ensure that the version string is set in the binary.

* Fri Jun 01 2007 James Bowes <jbowes@redhat.com> - 0.7-3
- Incorporate differences from jcollie's tig spec.

* Fri Jun 01 2007 James Bowes <jbowes@redhat.com> - 0.7-2
- Update spec file after review feedback.

* Thu May 31 2007 James Bowes <jbowes@redhat.com> - 0.7-1
- Initial packaging.
