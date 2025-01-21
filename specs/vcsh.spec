Name:           vcsh
Version:        2.0.8
Release:        4%{?dist}
Summary:        Version Control System for $HOME

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/RichiH/%{name}
Source0:        https://github.com/RichiH/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildArch:      noarch
Requires:       git

BuildRequires:  git
BuildRequires:  make


%description
vcsh allows you to have several git repositories, all maintaining their working
trees in $HOME without clobbering each other. That, in turn, means you can have
one repository per config set (zsh, vim, ssh, etc), picking and choosing which
configs you want to use on which machine.


%prep
%setup -q


%build
%configure
%make_build


%install
%{make_install} DOCDIR=%{_pkgdocdir} ZSHDIR=%{_datadir}/zsh/site-functions


%files
%{_bindir}/%{name}
%{_mandir}/man*/%{name}*
%{_datadir}/bash-completion/
%{_datadir}/zsh/
%{_docdir}/%{name}
%{_defaultlicensedir}/%{name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.8-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 28 2024 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.8-1
- Bumped version to 2.0.8

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.3-1
- Bumped version to 2.0.3

* Sun Sep 05 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.2-1
- Bumped version to 2.0.2

* Sun Aug 29 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.1-1
- Bumped version to 2.0.1

* Sat Aug 21 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.0-1
- Bumped version to 2.0.0
- Changed source URL to a download link
- Added bash completion

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20190621-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 06 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20190621-1
- Bumped version to 1.20190621

* Wed Mar 31 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20190619-1
- Bumped version to 1.20190619
- Added rubygem-ronn dependency

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20151229-2
- Declare %%_docdir in %%files

* Wed Feb 10 2016 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20151229-1
- Bumped version to 1.20151229

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20141026-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20141026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 26 2014 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20141026-1
- Bumped version to 1.20141026

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20140508-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20140508-1
- Bumped version to 1.20140508
- Switched to a commit tarball from github

* Sun Dec 15 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20131229-1
- Bumped version to 1.20131229

* Sun Dec 15 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20131214-1
- Bumped version to 1.20131214

* Tue Oct 22 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20130909-3
- The Makefile patch has been submitted upstream

* Sat Oct 19 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20130909-2
- Switched to _pkgdocdir
- Removed unnecessary `rm -rf %%{buildroot}' in clean and install

* Sat Oct 12 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.20130909-1
- Initial package
