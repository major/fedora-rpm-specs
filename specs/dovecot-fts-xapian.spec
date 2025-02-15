Name:           dovecot-fts-xapian
Version:        1.9
Release:        1%{?dist}
Summary:        Dovecot FTS plugin based on Xapian

# From the source code it isn't clear whether this is -only or -or-later, so
# I'm defaulting to the conservative choice here.
License:        LGPL-2.1-only
URL:            https://github.com/grosjo/fts-xapian
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  xapian-core-devel, libicu-devel, dovecot-devel, sqlite-devel, glibc-devel, libstdc++-devel
BuildRequires:  gcc, gcc-c++, make, automake, autoconf, libtool, libgcc
Requires:       dovecot

# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# dovecot does not ship i386
ExcludeArch:    %{ix86}

%description
This project intends to provide a straightforward, simple and
maintenance free, way to configure FTS plugin for Dovecot, 
leveraging the efforts by the Xapian.org team.

This effort came after Dovecot team decided to deprecate 
"fts_squat" included in the dovecot core, and due to the 
complexity of the Solr plugin capabilities, unneeded for most
users.

%prep
%autosetup -n fts-xapian-%{version}
autoreconf -vi

%build
%configure --enable-static=no --with-dovecot=%{_libdir}/dovecot
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/dovecot/lib21_fts_xapian_plugin.la

%files
%license COPYING
%doc AUTHORS README.md
%{_libdir}/dovecot/lib21_fts_xapian_plugin.so

%changelog
* Thu Feb 13 2025 Clemens Lang <cllang@redhat.com> - 1.9-1
- Rebase to 1.9

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Arjen Heidinga <dexter@beetjevreemd.nl> - 1.8.4
- Rebase to 1.8.4

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 1.7.17-2
- Rebuild for ICU 76

* Thu Nov 07 2024 Clemens Lang <cllang@redhat.com> - 1.7.17-1
- Rebase to 1.7.17
- Convert license to SPDX format
- Drop i686 package, since dovecot is no longer available in i686
- Do not depend on sqlite and xapian-core manually, rely on library dependency auto-detection instead

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1.5.4b-7
- Rebuilt for ICU 73.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.5.4b-5
- Rebuild for ICU 72

* Wed Aug  3 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5.4b-4
- Move %%configure to %%build for package_notes generation

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.5.4b-3
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 05 2022 Joan Moreau <jom@grosjo.net> - 1.5.4b
- Minor fixes
* Wed Mar 02 2022 Joan Moreau <jom@grosjo.net> - 1.5.4
- PR #119
- Issue #113, #117
* Sun Feb 20 2022 Joan Moreau <jom@grosjo.net> - 1.5.3
- Issues 112, 115, 116
* Tue Nov 23 2021 Joan Moreau <jom@grosjo.net> - 1.5.2
- Issues 103, 106, 109, 110
* Thu Nov 11 2021 Joan Moreau <jom@grosjo.net> - 1.5.1
- Fixed preprocessor issue 
* Wed Nov 10 2021 Joan Moreau <jom@grosjo.net> - 1.5.0
- FreeBSD compatibility
* Mon Nov 1 2021 Joan Moreau <jom@grosjo.net> - 1.4.14-1
- Alignment with Dovecot 2.3.17
- Better memory management for FreeBSD
* Sun Sep 12 2021 Joan Moreau <jom@grosjo.net> - 1.4.13-1
- Rebuild for dovecot 2.3.16
- Epel7 comptability
* Sat Aug 14 2021 Joan Moreau <jom@grosjo.net> - 1.4.12-1
- cf Github
* Sun Jul  4 2021 Joan Moreau <jom@grosjo.net> - 1.4.11-1
- cf Github
* Sat Jun 26 2021 Joan Moreau <jom@grosjo.net> - 1.4.10-1
- cf Github
* Tue Apr  6 2021 Joan Moreau <jom@grosjo.net> - 1.4.9b-1
- Initial RPM
