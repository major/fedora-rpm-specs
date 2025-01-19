Name:           jdupes
Version:        1.28.0
Release:        2%{?dist}
Summary:        Duplicate file finder and an enhanced fork of 'fdupes'

License:        MIT
URL:            https://codeberg.org/jbruchon/jdupes
Source0:        https://codeberg.org/jbruchon/jdupes/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libjodycode-devel

%description
jdupes is a program for identifying and taking actions upon duplicate
files.

A WORD OF WARNING: jdupes IS NOT a drop-in compatible replacement for
fdupes! Do not blindly replace fdupes with jdupes in scripts and
expect everything to work the same way. Option availability and
meanings differ between the two programs. For example, the -I switch
in jdupes means "isolate" and blocks intra-argument matching, while in
fdupes it means "immediately delete files during scanning without
prompting the user."


%prep
%autosetup -n %{name} -p1


%build
%make_build CFLAGS="%{optflags} -DENABLE_DEDUPE -DHARDEN" PREFIX="%{_prefix}" MAN_BASE_DIR="%{_mandir}"


%install
%make_install PREFIX="%{_prefix}" MAN_BASE_DIR="%{_mandir}"


%files
%license LICENSE.txt
%doc CHANGES.txt INSTALL.txt README.md README.stupid_dupes
%{_bindir}/jdupes
%{_mandir}/man1/jdupes.1.gz


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Jonathan Wright <jonathan@almalinux.org> - 1.28.0-1
- update to 1.28.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 13 2023 David Cantrell <dcantrell@redhat.com> - 1.27.3-1
- Upgrade to jdupes-1.27.3
- Upstream project moved to codeberg.org; update spec accordingly
- Add patch from author to fix a hash database error that could lead
  to data loss

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 20 2023 David Cantrell <dcantrell@redhat.com> - 1.25.1-1
- Upgrade to jdupes-1.25.1

* Thu Jan 26 2023 David Cantrell <dcantrell@redhat.com> - 1.20.2-6
- Pass -DENABLE_DEDUPE and -DHARDEN to CFLAGS (#2156509)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 David Cantrell <dcantrell@redhat.com> - 1.20.2-2
- Drop Makefile patch, pass ENABLE_DEDPUE=1 HARDEN=1 to build

* Mon Dec 20 2021 David Cantrell <dcantrell@redhat.com> - 1.20.2-1
- Upgrade to jdupes-1.20.2

* Tue Aug 10 2021 David Cantrell <dcantrell@redhat.com> - 1.20.1-3
- Enable DEDUPE support at build time (#1988738)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 David Cantrell <dcantrell@redhat.com> - 1.20.0-1
- Initial package
