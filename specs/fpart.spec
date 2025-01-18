Name:    fpart
Version: 1.5.1
Release: 9%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Summary: a tool that sorts files and packs them into bags
URL:     http://contribs.martymac.org

Source0:  https://github.com/martymac/%{name}/archive/%{name}-%{version}.tar.gz

%if 0%{?fedora}
Suggests: sudo rsync cpio
%endif
BuildRequires: gcc autoconf automake
BuildRequires: make

%description
Fpart is a tool that helps you sort file trees and pack them into bags (called
"partitions"). It is developed in C and available under the BSD license.

It splits a list of directories and file trees into a certain number of
partitions, trying to produce partitions with the same size and number of
files. It can also produce partitions with a given number of files or a limited
size.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
autoreconf --install
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc Changelog.md README.md TODO
%{_mandir}/man1/fpart.1*
%{_mandir}/man1/fpsync.1*
%{_bindir}/fpart
%{_bindir}/fpsync

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.1-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 survient@fedoraproject.org - 1.5.1-1
- Latest upstream release.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Sam P <survient@fedoraproject.org> - 1.4.0-1
- new version

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 survient@fedoraproject.org - 1.2.0-1
- Version 1.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Nov 19 2018 Sam P <survient@fedoraproject.org> - 1.1.0-2
- cleaned up prep and build sections
- trued up changelog entries
- corrected desciption
- added missing weak dependencies

* Fri Nov 16 2018 Sam P <survient@fedoraproject.org> - 1.1.0-1
- repackaged to stable release version 1.1.0

* Fri Nov 16 2018 Ganael Laplanche <ganael.laplanche@martymac.org> - 1.1.0
- Version 1.1.0

* Mon Nov 12 2018 Sam P <survient@fedoraproject.org> - 1.0.0-4.20181109git57f49f5
- pulled down latest snapshot which merged patch

* Wed Oct 31 2018 Sam P <survient@fedoraproject.org> - 1.0.0-3.20181022git130f8fd
- added patch for autoconf version for EL6 compatibility

* Wed Oct 31 2018 Sam P <survient@fedoraproject.org> - 1.0.0-3.20181022git130f8fd
- updated to snapshot 130f8fdadf2bbcc3cdaad479a356e8d0e3f6f041

* Thu Apr 19 2018 Sam P <survient@fedoraproject.org> - 1.0.0-2
- Used %%buildroot macro
- Correctly marked license
- Other small packaging corrections

* Fri Nov 10 2017 Ganael Laplanche <ganael.laplanche@martymac.org> - 1.0.0
- Version 1.0.0

* Thu Apr 27 2017 Ganael Laplanche <ganael.laplanche@martymac.org> - 0.9.3
- Version 0.9.3

* Tue Feb 17 2015 Ganael Laplanche <ganael.laplanche@martymac.org> - 0.9.2
- Version 0.9.2

* Mon Feb 16 2015 Tru Huynh <tru@pasteur.fr> - 0.9.1
- Initial build of the package.
