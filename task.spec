Name:           task
Version:        2.5.3
Release:        4%{?dist}
Summary:        Taskwarrior - a command-line TODO list manager
License:        MIT
URL:            https://taskwarrior.org
Source0:        %{url}/download/%{name}-%{version}.tar.gz
Patch0:         shared-libs.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

BuildRequires:  libuuid-devel
BuildRequires:  gnutls-devel

%description
Taskwarrior is a command-line TODO list manager. It is flexible, fast,
efficient, unobtrusive, does its job then gets out of your way.

Taskwarrior scales to fit your workflow. Use it as a simple app that captures
tasks, shows you the list, and removes tasks from that list. Leverage its
capabilities though, and it becomes a sophisticated data query tool that can
help you stay organized, and get through your work.

%prep
%autosetup -p1

%build
%cmake . -B%{_vpath_builddir} -GNinja -DTASK_RCDIR=share/%{name}
%ninja_build -C %{_vpath_builddir}

%install
%ninja_install -C %{_vpath_builddir}

# Move shell completion stuff to the right place
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -Dpm0644 scripts/zsh/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -Dpm0644 scripts/bash/%{name}.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datadir}/fish/completions/
install -Dpm0644 scripts/fish/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish

# Fix perms and drop shebangs
# that's only docs and it's written in README about permissings
find scripts/ -type f -exec chmod -x {} ';'
find scripts/ -type f -exec sed -i -e '1{\@^#!.*@d}' {} ';'

rm -vrf %{buildroot}%{_datadir}/doc/%{name}/

%files
%license LICENSE
%doc NEWS doc/ref/%{name}-ref.pdf
%doc scripts/vim/ scripts/hooks/
%{_bindir}/%{name}
# We don't want to have refresh script there
%exclude %{_datadir}/%{name}/refresh
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}rc.5*
%{_mandir}/man5/%{name}-color.5*
%{_mandir}/man5/%{name}-sync.5*
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/completions/
%{_datadir}/fish/completions/%{name}.fish

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Tomas Babej <tomas@tbabej.com> - 2.5.3-1
- Update to 2.5.3, latest upstream version.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5.1-10
- Fixup rcdir path

* Fri Aug 17 2018 Jeff Peeler <jpeeler@redhat.com> - 2.5.1-9
- Add command completion for fish shell

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 10 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.5.1-2
- Modernize spec

* Wed Feb 24 2016 Ralph Bean <rbean@redhat.com> - 2.5.1-1
- Latest upstream.

* Mon Feb 15 2016 Ralph Bean <rbean@redhat.com> - 2.5.1-0.1.beta1
- A beta prerelease from upstream.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 Ralph Bean <rbean@redhat.com> - 2.5.0-1
- Latest upstream.

* Sun Oct 18 2015 Ralph Bean <rbean@redhat.com> - 2.5.0-0.1.beta3
- Another beta pre-release from upstream.

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 2.5.0-0.1.beta2
- Another beta pre-release from upstream.

* Tue Sep 15 2015 Ralph Bean <rbean@redhat.com> - 2.5.0-0.1.beta1
- Latest beta pre-release from upstream.

* Tue Sep 15 2015 Ralph Bean <rbean@redhat.com> - 2.4.2-4
- Update summary and description with the latest from upstream's website.
  Include the keyword "taskwarrior" for rhbz#1262659.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 17 2015 Ralph Bean <rbean@redhat.com> - 2.4.2-1
- new version

* Mon Feb 23 2015 Ralph Bean <rbean@redhat.com> - 2.4.1-2
- Move bash completions, again.  See:
  https://bugzilla.redhat.com/show_bug.cgi?id=1190545#c7

* Sun Feb 15 2015 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Latest upstream.
- Removed obsoleted task-faq and task-tutorial man pages.
- Use CMAKE_BUILD_TYPE=release for a faster binary (at upstream's request).

* Mon Feb 09 2015 Ralph Bean <rbean@redhat.com> - 2.3.0-3
- Move shell completion pieces to the right place.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Greg Bailey <gbailey@lxpro.com> - 2.3.0-1
- task 2.3.0
- Fix bogus date RPM warnings in changelog
- Use cmake28 for EPEL6 builds

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-0.3.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 13 2014 Ralph Bean <rbean@redhat.com> - 2.3.0-0.2.beta2
- Add buildrequires on gnutls-devel so that 'task sync' will fly.

* Mon Nov 11 2013 Ralph Bean <rbean@redhat.com> - 2.3.0-0.1.beta2
- Beta2 release from upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.2.0-2
- Perl 5.18 rebuild

* Sat Jun 22 2013 Luke Macken <lmacken@redhat.com> - 2.2.0-1
- Update to task 2.2.0

* Thu Feb 21 2013 Luke Macken <lmacken@redhat.com> - 2.1.2-2
- Build against libuuid instead of using their internal
  implementation (#799664)

* Thu Feb 21 2013 Luke Macken <lmacken@redhat.com> - 2.1.2-1
- Update to task 2.1.2

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Federico Hernandez <ultrafredde@gmail.com> 2.0.0-1
  Initial RPM for task release 2.0.0
* Mon Mar  5 2012 Tom Callaway <spot@fedoraproject.org> 2.0.0-0.2.RC1
- update to 2.0.0 RC1
* Mon Feb 20 2012 Luke Macken <lmacken@redhat.com> - 2.0.0-0.1.beta4
- Update to the latest 2.0 beta
- Build with cmake
- Add task-unistd.patch to get it building
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Fri Mar 04 2011 Federico Hernandez <ultrafredde@gmail.com> - 1.9.4-1
  Intial RPM for task release 1.9.4
* Mon Nov 08 2010 Federico Hernandez <ultrafredde@gmail.com> - 1.9.3-1
  Intial RPM for task release 1.9.3
* Thu Jul 15 2010 Federico Hernandez <ultrafredde@gmail.com> - 1.9.2-2
  Wrong build config (Bugzilla 615034)
* Wed Jul 14 2010 Federico Hernandez <ultrafredde@gmail.com> - 1.9.2-1
  Intial RPM for task release 1.9.2
* Sat May 22 2010 Federico Hernandez <ultrafredde@gmail.com> - 1.9.1-1
  Intial RPM for task release 1.9.1
* Mon Feb 22 2010 Federico Hernandez <ultrafredde@gmail.com> - 1.9.0-1
  Intial RPM for task release 1.9.0
* Mon Feb 15 2010 Federico Hernandez <ultrafredde@gmail.com> - 1.9.0.beta3-1
  Intial RPM for task beta release 1.9.0.beta3
* Mon Feb 08 2010 Federico Hernandez <ultrafredde@gmail.com> - 1.9.0.beta2-1
  Intial RPM for task beta release 1.9.0.beta2
* Wed Feb 03 2010 Federico Hernandez <ultrafredde@gmail.com> - 1.9.0.beta1-1
  Intial RPM for task beta release 1.9.0.beta1
* Sat Dec 05 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.8.5-2
  Fixed wrong ChangeLog file
* Sat Dec 05 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.8.5-1
  Intial RPM for task bugfix release 1.8.5
* Tue Nov 17 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.8.4-1
  Intial RPM for task bugfix release 1.8.4
* Wed Oct 21 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.8.3-1
  Intial RPM for task bugfix release 1.8.3
* Mon Sep 07 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.8.2-1
  Intial RPM for task bugfix release 1.8.2
* Thu Aug 20 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.8.1-1
  Intial RPM for task bugfix release 1.8.1
* Tue Jul 21 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.8.0-1
  Intial RPM for task release 1.8.0
* Mon Jul 13 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.8.0.beta3-1
  Intial RPM for task beta release 1.8.0.beta3
* Wed Jul 08 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.8.0.beta2-1
  Intial RPM for task beta release 1.8.0.beta2
* Tue Jul 07 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.8.0.beta1-1
  Intial RPM for task beta release 1.8.0.beta1
* Mon Jun 08 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.7.1-2
  Fixed inclusion of manpages.
* Mon Jun 08 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.7.1-1
  Initial RPM for bugfix release 1.7.1.
  Updated references to new project homepage in spec file. 
* Tue May 19 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.7.0-2
  Changed license to GPLv2+ and removed Requires macro.
  See https://bugzilla.redhat.com/show_bug.cgi?id=501498
* Tue May 19 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.7.0-1
  Initial RPM.
