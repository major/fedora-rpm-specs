%global fosrev fosf51aa371d9
%global isdev 1

Name:           tkabber-plugins
Version:        1.1.2
Release:        23%{?fosrev:.%{fosrev}}%{?dist}
Summary:        Additional plugins for tkabber

# most have BSD, some GPL and tkabber-khim is under TCL
# Automatically converted from old format: GPLv2 and BSD and TCL - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-BSD AND TCL
URL:            http://tkabber.jabber.ru/
Source:         %{name}-%{version}%{?isdev:-dev}.tar.gz
# for relase version:
#Source0:        http://files.jabber.ru/tkabber/%{name}-%{version}.tar.gz
# script to get tkabber from svn
Source1:        tkabber-plugins-snapshot.sh
# modify installation system for Fedora
Patch1:         tkabber-plugins-1.1.2-install.patch

BuildArch:      noarch

BuildRequires:  make
Requires:       tkabber = %{version}


%description
%{summary}.

%prep
%setup -qn %{name}-%{version}%{?isdev:-dev}
%patch 1 -p1 -b .install

%build

# empty here

%install
make install-bin DESTDIR=%{buildroot}

cp attline/license.terms license.BSD
cp tkabber-khim/tklib_licence.terms license.TCL


%files
%doc COPYING ChangeLog README license.*
%{_datadir}/tkabber-plugins

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-23.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.2-22.fosf51aa371d9
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-21.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 1.1.2-20.fosf51aa371d9
- F41 rebuild.
- Patch numerated.

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-19.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-18.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-17.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-14.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5.fosf51aa371d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 1.1.2-4.fosf51aa371d9
- Update to latest dev version.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 01 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.1.2-1
- Update to 1.1.2.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2.svn2173
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 01 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.1.1-1.svn2173
- Update to 1.1.1+ svn.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.svn2150
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 02 2014 Dmitrij S. Kryzhevich <krege@land.ru> 1.1-1.svn2150
- Fix patch for Makefile.

* Wed Apr 02 2014 Dmitrij S. Kryzhevich <krege@land.ru> 1.1-1.svn2150
- Update to 1.1+ svn, revision 2150.
- Clean spec.

* Tue Jan 28 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 1.0-1.svn2114
- Update to 1.0+ svn, revision 2114.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-8.svn1948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-7.svn1948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-6.svn1948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-5.svn1948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-4.svn1948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.11.1-3.svn1948
- Add license files to %%doc.

* Mon Dec 13 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.11.1-2.svn1948
- License: GPLv2 and BSD and TCL.

* Fri Nov 05 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.11.1-1.svn1948
- First build.