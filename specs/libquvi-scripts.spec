%global debug_package %{nil}

Name:           libquvi-scripts
Version:        0.9.20131130
Release:        25%{?dist}
Summary:        Embedded lua scripts for parsing the media details
License:        AGPL-3.0-or-later
URL:            http://quvi.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/quvi/0.9/%{name}/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       lua-expat
Requires:       lua-socket
Requires:       lua-json

# https://bugzilla.redhat.com/show_bug.cgi?id=1134853
Patch0: 0001-guardian.lua-Update-for-website-changes.patch

BuildRequires:  gcc
BuildRequires: make
%description
libquvi-scripts contains the embedded lua scripts that libquvi
uses for parsing the media details. Some additional utility
scripts are also included.

%prep
%setup -q
%patch -P0 -p1

%build
%configure --with-nsfw

%install
# Noarch fix.
make install DESTDIR=%{buildroot} pkgconfigdir=%{_datadir}/pkgconfig/

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_datadir}/%{name}
%{_datadir}/pkgconfig/%{name}*.pc
%{_mandir}/man7/%{name}.7*
%{_mandir}/man7/quvi-modules*.7*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 21 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.20131130-23
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20131130-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20131130-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Bastien Nocera <bnocera@redhat.com> 0.9.20131130-4
- Another update for guardian.lua

* Mon Sep 01 2014 Bastien Nocera <bnocera@redhat.com> 0.9.20131130-3
- Fix guardian.lua for website changes (#1134853)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20131130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Christopher Meng <rpm@cicku.me> - 0.9.20131130-1
- Update to 0.9.20131130

* Sat Nov 09 2013 Christopher Meng <rpm@cicku.me> - 0.9.20131104-1
- Update to 0.9.20131104

* Sun Oct 20 2013 Christopher Meng <rpm@cicku.me> - 0.9.20131012-1
- Update to 0.9.20131012
- Add missing lua dep again(BZ#1021156).

* Thu Sep 26 2013 Christopher Meng <rpm@cicku.me> - 0.9.20130903-1
- Update to 0.9.20130903
- Add missing lua dep(BZ#1012165).

* Tue Aug 27 2013 Christopher Meng <rpm@cicku.me> - 0.9.20130805-3
- Add missing lua dep.

* Mon Aug 26 2013 Christopher Meng <rpm@cicku.me> - 0.9.20130805-2
- License changed to AGPL.
- Correct filenames.

* Sun Aug 25 2013 Christopher Meng <rpm@cicku.me> - 0.9.20130805-1
- Update to 0.9.20130805

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.10-1
- Update to 0.4.10

* Sun Oct 28 2012 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.9-1
- Update to 0.4.9

* Fri Aug 10 2012 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.7-1
- Update to 0.4.7

* Sun Jul 15 2012 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.6-1
- Update to 0.4.6

* Thu Mar 29 2012 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.4-1
- Update to 0.4.4

* Sun Mar 11 2012 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.3-1
- Update to 0.4.3

* Fri Dec  2 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.2-1
- Update to 0.4.2

* Thu Nov 10 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.1-1
- Update to 0.4.1

* Tue Oct 11 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.0-3
- Remove the devel subpackage
- The package is now noarch

* Sun Oct  9 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.0-2
- Create the devel subpackage

* Sat Oct  8 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.0-1
- Initial build
