Name:           deco
Version:        1.6.4
Release:        21%{?dist}
Summary:        Extractor for various archive file formats
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/peha/deco/
Source0:        https://github.com/peha/deco/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: make
Requires:       deco-archive >= 1.2

%description
deco is a Un*x program, written in SUSv3-compliant C99, 
that is able to extract various archive file formats
with features like consistent behavior, consistent 
interface and much more.

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX=%{_prefix} SHARE=%{_var}/lib/%{name} \
                     CFLAGS="%optflags" LDFLAGS=""

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
install -dm 755 %{buildroot}/%{_var}/lib/%{name}

%files
%doc LICENSE NEWS README.md
%{_bindir}/%{name}
%dir %{_var}/lib/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.4-20
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 11 2016 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.6.4-1
- Version update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.6.3-1
- Version update

* Sat Feb 23 2013 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.6.2-6
- Bugfix: occasional crash due to uninitialized pointer. RHBZ #914659

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 15 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.6.2-1
- Version update

* Fri Feb 05 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.6.1-1
- Version update.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.6-1
- Version update. Change in work flow for failed extractions.

* Thu Nov 20 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5.7-2
- License is GPLv3.
- The extraction scripts will be inside %%{_var}/lib/%%{name}.

* Wed Nov 19 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5.7-1
- Version update

* Wed Oct 29 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5.6-2
- Package deco-archive separately

* Tue Oct 28 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5.6-1
- Rebuild with version 1.5.6

* Mon Apr 28 2008 Steve 'Ashcrow' Milner <stevem@gnulinux.net> - 0.8.1-2
- Updates to file listings per review
- moved to macros instead of direct paths
- Source0 now in url form
- added dir for the deco data directory

* Fri Apr 25 2008 Steve 'Ashcrow' Milner <stevem@gnulinux.net> - 0.8.1-1
- Upstream updates.
- Updates to file listings.

* Mon Apr 14 2008 Steve 'Ashcrow' Milner <stevem@gnulinux.net> - 0.6-1
- Initial package.
