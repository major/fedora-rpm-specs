# Based on initial .spec file from upstream, link here 
# https://github.com/netblue30/firejail/blob/master/platform/rpm/firejail.spec
# Originally created by Firejail authors

Name: firejail
Version: 0.9.72
Release: 7%{?dist}
Summary: Linux namespaces sandbox program
BuildRequires: gcc make python3-devel
BuildRequires: libselinux-devel
Requires: xdg-dbus-proxy

# spec released under GPLv2+, contacted upstream whether it can be 
# released under MIT
License: GPL-2.0-or-later
URL: https://github.com/netblue30/firejail
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces. It includes a sandbox profile for Mozilla Firefox.

%prep
%autosetup -p1

%build
%configure --enable-selinux
%make_build

%install
%make_install
chmod 0755 %{buildroot}%{_libdir}/%{name}/lib*.so
for f in \
%{buildroot}%{_libdir}/%{name}/fj-mkdeb.py \
%{buildroot}%{_libdir}/%{name}/fjclip.py \
%{buildroot}%{_libdir}/%{name}/fjdisplay.py \
%{buildroot}%{_libdir}/%{name}/fjresize.py
do
    sed -i "1 s/^.*$/\#\!\/usr\/bin\/python3/" "$f";
done
rm %{buildroot}%{_datadir}/gtksourceview-5/language-specs/firejail-profile.lang

%files
%doc README RELNOTES CONTRIBUTING.md
%license COPYING

%{_bindir}/firecfg
%{_bindir}/firemon
%{_bindir}/jailcheck
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datarootdir}/bash-completion/completions/
%{_datarootdir}/vim/vimfiles
%{_datarootdir}/zsh/site-functions/_%{name}
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/profile.template
%{_docdir}/%{name}/redirect_alias-profile.template
%{_docdir}/%{name}/syscalls.txt
%{_mandir}/man5/%{name}-login.5.*
%{_mandir}/man5/%{name}-profile.5.*
%{_mandir}/man5/%{name}-users.5.*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.72-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.72-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.72-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.72-1
- Update to v0.9.72
- Migrate License tag to SPDX

* Tue Sep 06 2022 Maxwell G <gotmax@e.email> - 0.9.70-1
- Update to 0.9.70 (rhbz#2042724).
- Mitigates CVE-2022-31214 (rhbz#2095070).

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Ondrej Dubaj <odubaj@redhat.com> - 0.9.66-1
- Rebase to version 0.9.66

* Mon Feb 08 2021 Ondrej Dubaj <odubaj@redhat.com> - 0.9.64.4-1
- Rebase to version 0.9.64.4

* Fri Jan 29 2021 Ondrej Dubaj <odubaj@redhat.com> - 0.9.64.2-1
- Rebase to version 0.9.64.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 23 2020 Ondrej Dubaj <odubaj@redhat.com> - 0.9.64-2
- Add selinux and xdg-dbus-proxy dependencies
- Enable selinux

* Fri Oct 23 2020 Ondrej Dubaj <odubaj@redhat.com> - 0.9.64-1
- Rebase to version 0.9.64

* Tue Aug 18 2020 Ondrej Dubaj <odubaj@redhat.com> - 0.9.62.4-1
- Rebase to version 0.9.62.4

* Wed Aug 12 2020 Ondrej Dubaj <odubaj@redhat.com> - 0.9.62.2-1
- Rebase to version 0.9.62.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Ondrej Dubaj <odubaj@redhat.com> - 0.9.62-1
- Rebase to version 0.9.62

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.56-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 2019 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-9
- Resolved f31 build errors

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.56-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.56-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-6
- Added python3-devel to BuildRequires, modified python shebangs

* Wed Nov 21 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-5
- Modified path to bash completion scripts

* Mon Nov 19 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-4
- Fixed problem with bash completion scripts

* Thu Nov 15 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-3
- Fixed .spec file according to review request comments (#1645172)

* Thu Nov 8 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-2
- Fixed .spec file according to review request comments (#1645172)

* Mon Oct 22 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-1
- First firejail RPM package for Fedora
