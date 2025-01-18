%global commit 11c08954f983345b8a4a49f330d21085d2a87603
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           clide
Version:        0.9
Release:        37.20160305git%{shortcommit}%{?dist}
Summary:        Color and style highlighting program for text

License:        GPL-3.0-or-later
URL:            http://suso.suso.org/xulu/Clide
Source0:        https://github.com/deltaray/clide/archive/%{commit}/clide-%{commit}.tar.gz

# Makefile changes (sent upstream):
#  1. Preserve timestamps of the clide script and man page.
#  2. Don't compress the man page (this is done automatically).
#  3. Don't install doc files (this is done automatically).
Patch0:         clide-Makefile.patch

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  make

%description
clide is a program that will colorize ASCII text on the command line using ANSI
escape sequences and user defined and predefined expressions. Searches can
include Perl Compatible Regular Expressions.

%prep
%setup -qn %{name}-%{commit}
%patch -P0 -p1

%build
make manpages

%install
make BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1 rpminstall

%files
%{_bindir}/clide
%doc CHANGELOG GOALS IDEAS README.md WARNING
%license COPYING LICENSE
%{_mandir}/man1/clide.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-37.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-36.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-35.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-34.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-33.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-32.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Richard Fearn <richardfearn@gmail.com> - 0.9-31.20160305git11c0895
- Use SPDX license identifier

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-30.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-29.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-28.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-27.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-26.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Richard Fearn <richardfearn@gmail.com> - 0.9-25.20160305git11c0895
- Use %%license

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-24.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-23.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-22.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-21.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-20.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 0.9-19.20160305git11c0895
- Remove unnecessary Group: tag

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-18.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17.20160305git11c0895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 05 2016 Richard Fearn <richardfearn@gmail.com> - 0.9-16.20160305git11c0895
- Update to git snapshot that includes new copying permission statements
- Drop clide-licence.patch

* Sat Mar 05 2016 Richard Fearn <richardfearn@gmail.com> - 0.9-15.20150109git4f1eca0
- Add BuildRequires: perl-podlators, for pod2man

* Sat Feb 06 2016 Richard Fearn <richardfearn@gmail.com> - 0.9-14.20150109git4f1eca0
- Update copying permission statements to remove invalid FSF addresses

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13.20150109git4f1eca0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12.20150109git4f1eca0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Richard Fearn <richardfearn@gmail.com> - 0.9-11.20150109git4f1eca0
- Update to git snapshot to add the highlight options

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.9-8
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun  8 2010 Richard Fearn <richardfearn@gmail.com> - 0.9-3
- Explicitly set BINDIR/MANDIR when installing

* Mon Jun  7 2010 Richard Fearn <richardfearn@gmail.com> - 0.9-2
- clide is GPLv3+; remove LICENSE file, which contradicts this
- Rename Makefile patch, and describe its purpose
- Don't compress the man page; this is done automatically
- Remove the doc file installation from the "rpminstall" target in the Makefile,
  not the "install" target

* Wed May 19 2010 Richard Fearn <richardfearn@gmail.com> - 0.9-1
- Initial package for Fedora
