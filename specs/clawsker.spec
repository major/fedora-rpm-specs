# Review at https://bugzilla.redhat.com/show_bug.cgi?id=620191

Name:           clawsker
Version:        1.4.0
Release:        2%{?dist}
Summary:        Dialog to edit Claws Mail's hidden preferences

License:        GPL-3.0-or-later
URL:            http://www.claws-mail.org/clawsker
Source0:        http://www.claws-mail.org/tools/%{name}-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  /usr/bin/pod2man
# for automatic RPM package dependencies
BuildRequires:  perl-generators
BuildRequires: make

Requires:       claws-mail


%description
Clawsker is a Perl-GTK3 applet to edit hidden preferences for Claws Mail, and 
to do it in a safe and user friendly way, preventing users from raw editing of 
configuration files.

Claws Mail is a fast and lightweight Mail User Agent by the Claws Mail Team.


%prep
%autosetup -p1


%build
make %{?_smp_mflags}


%install
%make_install PREFIX=%{_prefix}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog.old NEWS README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep  8 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0.

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.8-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 25 2023 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.8-1
- Update to 1.3.8.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 30 2022 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.7-1
- Update to 1.3.7 / there was no 1.3.6.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 23 2022 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-1
- Update to 1.3.5.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 22 2021 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4.

* Mon Feb 15 2021 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.2-3
- Merge patch to sync with Claws Mail g_get_user_runtime_dir() change.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2.
- spec updates: drop removal of buildroot, use %%make_install macro

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1.

* Mon Dec 24 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.0-2
- Merge use_tls_sni patch from git.
- Switch to %%autosetup -p1.

* Mon Dec  3 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0 which has switched to using GTK+3 Perl bindings.

* Thu Aug 16 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.1-2
- Remove obsolete scriptlets

* Sun Dec 24 2017 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (bug-fix and preparation for Claws Mail 3.16.0).

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1.
- Validate the included desktop file.
- Build with perl-generators again.

* Sun Oct  2 2016 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0.

* Thu Aug 18 2016 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7.14-1
- Update to 0.7.14.
- Patch out the "uninitialized value" warning for line 470.
- Use the included/installed desktop file.
- Add icon cache scriptlets for the new icon.
- Remove the explicit "file" BR again, not needed anymore.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7.13-2
- drop superfluous %%defattr
- BR the "file" package update that fixes the Perl Prov/Req again

* Tue Dec 15 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7.13-1
- Update to 0.7.13 (also fixes hardcoded /tmp, #1161132).

* Tue Dec 15 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7.11-3
- Use %%license macro.
- Add a fix to readd the missing Perl dependencies (#1253920).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 13 2014 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.11-1
- Update to 0.7.11 (#1106424)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.7.2-7
- Perl 5.18 rebuild

* Mon Feb 18 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.2-6
- BR /usr/bin/pod2man for manpage generation
- Fix bogus dates in changelog
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 15 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 14 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.2-2
- No longer require perl(Gtk2) and perl(Locale::gettext)

* Sat Jun 26 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.2-1
- Initial package

