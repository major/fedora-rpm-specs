Name:           t-prot
Version:        3.4
Release:        21%{?dist}
Summary:        A filter which improves the readability of email messages and Usenet posts

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.escape.de/~tolot/mutt/
Source0:        http://www.escape.de/~tolot/mutt/t-prot/downloads/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Locale::gettext)
Requires:       perl(Locale::gettext)

%description
t-prot (TOFU Protection) is a filter which improves the readability of email
messages and Usenet posts by hiding some of their annoying parts. The
annoyances it handles include mailing list footers, signatures, TOFU,
sequences of blank lines, and repeated punctuation.

%prep
%setup -q

# Empty build
%build

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m755 t-prot $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 t-prot.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%doc ChangeLog TODO README contrib
%{_bindir}/t-prot
%{_mandir}/man1/t-prot.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4-20
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 3.4-1
- Update to 3.4

* Tue Sep 23 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 3.3-1
- Update to 3.3

* Sun Aug 24 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 3.2-1
- Update to 3.2
- Add perl(Locale::gettext) as a BR and a Requires

* Tue Aug 19 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 3.1-1
- Update to 3.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 3.0-2
- Fix packaging issues (#1080246)

* Tue Dec 31 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 3.0-1
- Update to 3.0

* Sun Nov 07 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.101-1
- Update to 2.101

* Mon Jul 19 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.100-1
- Update to 2.100

* Sun May 02 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.98-1
- Update to 2.98.

* Mon Dec 21 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 2.8.1-1
- Update to 2.8.1.

* Sun Nov 22 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 2.7.1-1
- Update to 2.7.1.

* Tue May 05 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 2.5-1
- Initial build
