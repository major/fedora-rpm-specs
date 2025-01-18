Summary: Utility to autorestart SSH tunnels
Name: autossh
Version: 1.4g
Release: 17%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://www.harding.motd.ca/autossh/
Source0: https://www.harding.motd.ca/autossh/autossh-1.4g.tgz
Source1: autossh@.service
Source2: README.service
Patch0: autossh-configure-c99.patch
BuildRequires:  gcc
BuildRequires: /usr/bin/ssh
BuildRequires: systemd
BuildRequires: make
%{?systemd_requires}
Requires(pre): shadow-utils
Requires: /usr/bin/ssh

%description
autossh is a utility to start and monitor an ssh tunnel. If the tunnel
dies or stops passing traffic, autossh will automatically restart it.

%prep
%setup -q
%patch -P0 -p1
cp -p %{SOURCE2} .

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/autossh
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p examples

cp -p autossh.host rscreen examples
chmod 0644 examples/*

install -m 0755 -p autossh $RPM_BUILD_ROOT%{_bindir}
cp -p autossh.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}

%pre
getent group autossh >/dev/null || groupadd -r autossh
getent passwd autossh >/dev/null || \
    useradd -r -g autossh -d %{_sysconfdir}/autossh -s %{_sbindir}/nologin \
    -c "autossh service account" autossh
exit 0

%post
%systemd_post autossh@.service

%preun
# https://bugzilla.redhat.com/1996234
if [ $1 -eq 0 ] && [ -x /usr/bin/systemctl ]; then
    # Package removal, not upgrade
    if [ -d /run/systemd/system ]; then
        /usr/bin/systemctl --no-reload disable --now autossh@.service || :
	systemctl stop "autossh@*.service" || :
    else
        /usr/bin/systemctl --no-reload disable autossh@.service || :
    fi
fi

%postun
%systemd_postun_with_restart "autossh@*.service"


%files
%doc CHANGES README README.service
%doc examples
%{_bindir}/*
%attr(750,autossh,autossh) %dir %{_sysconfdir}/autossh/
%{_mandir}/man1/*
%{_unitdir}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4g-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 07 2022 Peter Fordham <peter.fordham@gmail.com> - 1.4g-10
- Port configure script to C99.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 28 2021 Alexander Boström <abo@root.snowtree.se> - 1.4g-7
- Fix service template related scriptlet failure (#1996234)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4g-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Alexander Boström <abo@root.snowtree.se> - 1.4g-1
- Upgrade to 1.4g

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 23 2016 Ville SkyttÃ¤ <ville.skytta@iki.fi> - 1.4e-3
- Add systemd service

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Alexander Boström <abo@root.snowtree.se> - 1.4e-1
- Upgrade to 1.4e

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.4c-2
- Patch build to honor $LDFLAGS.

* Sun Oct 30 2011 Alexander Boström <abo@root.snowtree.se> - 1.4c-1
- Upgrade to 1.4c

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Chris Ricker <kaboom@oobleck.net> 1.4a-1
- new version

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 1.3-4
- Bump and rebuild

* Tue Feb 14 2006 Chris Ricker <kaboom@oobleck.net> 1.3-3
- Bump and rebuild

* Fri Jun 03 2005 Chris Ricker <kaboom@oobleck.net> 1.3-2%{?dist}
- Add dist tag

* Fri Jun 03 2005 Chris Ricker <kaboom@oobleck.net> 1.3-2
- Changes from Ville Skyttä (use mkdir -p, remove extraneous attr)

* Tue Apr 26 2005 Chris Ricker <kaboom@oobleck.net> 1.3-1
- Initial package
