Name: cockpit-ostree
Epoch: 1
Version: 207
Release: 1%{?dist}
BuildArch: noarch
Summary: Cockpit user interface for rpm-ostree
License: LGPL-2.1-or-later
BuildRequires: make
Requires: cockpit-bridge >= 125
Requires: cockpit-system >= 125
Requires: rpm-ostree

Source: https://github.com/cockpit-project/%{name}/releases/download/%{version}/cockpit-ostree-%{version}.tar.xz

%if 0%{?fedora} >= 41 || 0%{?rhel}
ExcludeArch: %{ix86}
%endif

%define debug_package %{nil}

%description
Cockpit component for managing software updates for ostree based systems.

%prep
%setup -n cockpit-ostree

%install
%make_install PREFIX=/usr

%files
%doc README.md
%license LICENSE dist/ostree.js.LEGAL.txt dist/ostree.css.LEGAL.txt
%{_datadir}/cockpit/*

%changelog
* Thu Jan 30 2025 Packit <hello@packit.dev> - 1:207-1
- Bug fixes and translation updates

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:206-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 20 2024 Packit <hello@packit.dev> - 1:206-1
- Updates to translations

* Wed Oct 23 2024 Packit <hello@packit.dev> - 1:205-1
- Bug fixes and translation updates

* Thu Aug 08 2024 Packit <hello@packit.dev> - 1:204-1
- Bug fixes

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:203-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Packit <hello@packit.dev> - 1:203-1
- Bug fixes and performance improvements

* Thu Apr 25 2024 Packit <hello@packit.dev> - 1:202-1
- Bug fixes and stability improvements

* Wed Mar 27 2024 Packit <hello@packit.dev> - 1:201-1
- Show OCI container origin

* Wed Feb 14 2024 Packit <hello@packit.dev> - 1:200-1
- Bug fixes and stability improvements

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:199-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:199-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Packit <hello@packit.dev> - 1:199-1
- library and translation updates

* Wed Nov 29 2023 Packit <hello@packit.dev> - 1:198.1-1
- Fix card and dialog titles

* Wed Nov 29 2023 Packit <hello@packit.dev> - 1:198-1
- Redesign cards, add reset, cleanup, and pinning

* Wed Sep 06 2023 Packit <hello@packit.dev> - 1:197-1
- Bug fixes and stability improvements

* Wed Aug 09 2023 Packit <hello@packit.dev> - 1:196-1
- Update to PatternFly 5

* Wed Jul 26 2023 Packit <hello@packit.dev> - 1:195-1
- Performance and stability improvements

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:194-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Packit <hello@packit.dev> - 1:194-1
- Bug fixes and translation updates

* Tue May 16 2023 Packit <hello@packit.dev> - 1:193-1
- Fix crash on OCI repository deployments
- Move to esbuild bundler
- Translation updates

* Wed Feb 08 2023 Packit <hello@packit.dev> - 1:192-1
- Stability and performance improvements

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:191-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Packit <hello@packit.dev> - 1:191-1
- Dark theme support


* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:190.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 11 2022 Allison Karlitskaya <allison.karlitskaya@redhat.com> - 190.1-1
- Update to upstream 190.1 release

* Wed May 11 2022 Allison Karlitskaya <allison.karlitskaya@redhat.com> - 190-1
- Translation improvements

* Wed Feb 02 2022 Martin Pitt <martin@piware.de> - 189-1
- Fix page status icons with current cockpit versions
- Translation updates

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:188-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 19 2021 Martin Pitt <martin@piware.de> - 188-1
- React to superuser changes
- Fix building with npm 7
- Switch release tarballs to tar.xz
- Many translation updates (they did not happen since Feb 2020)

* Wed Aug 04 2021 Martin Pitt <martin@piware.de> - 187-1
- Port from moment to date-fns
- Translation updates

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:186-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Allison Karlitskaya <allison.karlitskaya@redhat.com> - 186-1
- ockpit-ostree 186
 - move to webpack 5 and Dart Sass
 - various node modules updates
 - set an RPM version epoch (to 1)


* Wed Apr 14 2021 Matej Marusak <mmarusak@redhat.com> - 185-1
- PatternFly 4 updates


* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 184-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Martin Pitt <martin@piware.de> - 184-1
- NPM updates
- Release to Fedora 33


* Mon Oct 05 2020 Martin Pitt <martin@piware.de> - 183-3
- Rebuilt after accidental test release 999

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 183-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Martin Pitt <martin@piware.de> - 183-1
- Rewrite with PatternFly 4
- Send update availability to Overview Health notifications


* Sun Jun 14 2020 Martin Pitt <martin@piware.de> - 182-1
- Stop importing cockpit's deprecated base1/patternfly.css
- Use Red Hat font
- npm module updates


* Wed Mar 04 2020 Martin Pitt <martin@piware.de> - 181-1
- Fix building under NODE_ENV=production
- NPM updates
- Move translations to weblate
- Translation updates


* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 180-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Martin Pitt <martin@piware.de> - 180-1
- timeline: Use PF4 inspired background color
- NPM dependency updates


* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 179-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Martin Pitt <martin@piware.de> - 179-1
- Update to upstream 179 release

* Fri Jul 12 2019 Martin Pitt <martin@piware.de> - 178-1
- new upstream release: 178

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 176-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Martin Pitt <martin@piware.de> - 176-1
- RPM spec fixes
- Drop python3 build requirement


* Thu Aug 02 2018 Martin Pitt <martin@piware.de> - 175-1
- Simplify spec file
- Adjust tests for new rpm-ostree on RHEL Atomic


* Thu Jul 19 2018 Martin Pitt <martin@piware.de> - 173-1
- Split out into a separate upstream project:
  https://github.com/cockpit-project/cockpit-ostree
  (rhbz#1603146)
- No behaviour changes

