Name: beesu
Version: 2.7
# Don't ever decrease this version (unless beesu update) or the subpackages will go backwards.
# It is easier to do this than to track a separate release field.
Release: 49%{?dist}
Summary: Graphical wrapper for su
URL: http://www.honeybeenet.altervista.org
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://honeybeenet.altervista.org/beesu/files/beesu-sources/%{name}-%{version}.tar.bz2

BuildRequires: gcc-c++
BuildRequires: make

Requires: pam
Requires: usermode
Requires: usermode-gtk

Obsoletes: nautilus-beesu-manager
Obsoletes: caja-beesu-manager
Obsoletes: nemo-beesu-manager
Obsoletes: gedit-beesu-plugin
Obsoletes: pluma-beesu-plugin

%description
Beesu is a wrapper around su and works with consolehelper under
Fedora to let you have a graphic interface like gksu.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags} -fno-delete-null-pointer-checks"

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
mv %{buildroot}%{_sysconfdir}/profile.d/beesu-bash-completion.sh \
 %{buildroot}%{_sysconfdir}/bash_completion.d/


%files
%doc README
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}
%{_sysconfdir}/bash_completion.d/%{name}-bash-completion.sh
%{_sbindir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7-48
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.7-34
- Add BuildRequires gcc-c++

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 04 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 2.7-28
- re-retired beesu for f26
- drop all subpackages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Tom Callaway <spot@fedoraproject.org> - 2.7-26
- fix gedit plugin

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.7-24
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb  5 2015 Tom Callaway <spot@fedoraproject.org> - 2.7-23
- gedit plugin only works on Fedora (needs python3)
- move bash completion script to the correct place

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug  7 2014 Tom Callaway <spot@fedoraproject.org> - 2.7-21
- fix Edit with Pluma script (bz1118974)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr  7 2014 Tom Callaway <spot@fedoraproject.org>
- add Requires: /usr/bin/pluma for caja-beesu-manager
- add explicit check for /usr/bin/pluma in caja-beesu-manager

* Thu Mar 20 2014 Tom Callaway <spot@fedoraproject.org>
- add support for caja and pluma from D. Charles Pyle

* Wed Sep 25 2013 D. Charles Pyle <dcharlespyle@msn.com> and Bee <http://www.honeybeenet.altervista.org>
- 2.7-13
- Bug fixes gedit-beesu-plugin and beesu scripts to stop crashing of GNOME Shell and added a require of usermode-gtk.
- Bug fixes to nemo scripts and nautilus scripts.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 29 2013 D. Charles Pyle <dcharlespyle@msn.com> - 2.7-11
- Add fixes to nautilus scripts for better compatibility with GNOME 3.8.
- Added newly-forked Nemo scripts package to distribution.

* Tue Jun 25 2013 Tom Callaway <spot@fedoraproject.org> - 2.7-10
- add fixes for gedit 3.8 from D. Charles Pyle <dcharlespyle@msn.com>

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar  1 2012 Tom Callaway <spot@fedoraproject.org> - 2.7-7
- remove --browser from nautilus invocation
- fix gedit-beesu-plugin (this time for real)

* Fri Feb 10 2012 Tom Callaway <spot@fedoraproject.org> - 2.7-6
- fix gedit-beesu-plugin (bz 786734)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Tom Callaway <spot@fedoraproject.org> 2.7-3
- update gedit-beesu-plugin to 0.4

* Wed Dec 15 2010 Tom Callaway <spot@fedoraproject.org> 2.7-2
- update gedit-beesu-plugin to 0.3

* Thu Aug  5 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.7-1
- update beesu to 2.7
- update nautilus-beesu-manager to 1.7
- include gedit-beesu-plugin (0.2)

* Fri Jul  9 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.6-1
- update beesu to 2.6
- update nautilus-beesu-manager to 1.6

* Wed Feb 24 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.4-8
- update nautilus-beesu-manager to 1.4
  - one new script to open any file as root with GNOME's associated application

* Thu Aug  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.4-7
- fix sources

* Thu Aug  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.4-6
- beesu updated to 2.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.3-4
- nautilus-beesu-manager update to 1.2
 - one new installable script to change file access
 - new run-once script to fix the access permissions and the 
   file owner on the trash folder

* Thu Apr  9 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.3-3
- fix missing BR: desktop-file-utils

* Thu Apr  9 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.3-2
- enable nautilus-beesu-manager subpackage

* Mon Mar 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.3-1
- Update to 2.3

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.2-1
- Update to 2.2, adds bash auto completion feature

* Thu Jan 29 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-1
- slight package cleanup from Bee

* Fri Nov 28 2008 Bee <http://www.honeybeenet.altervista.org> 2.0-1
- new RPMs for Fedora 10 and some source clean up.

* Mon Oct 27 2008 Bee <http://www.honeybeenet.altervista.org> 1.0-3
- new RPMs

* Wed Oct 15 2008 Bee <http://www.honeybeenet.altervista.org> 1.0-2
- package needs to be arch specific , patch so rpm builds in mock or as non-root & clean up

* Mon Oct 13 2008 Bee <http://www.honeybeenet.altervista.org> 1.0-1
- initial release

