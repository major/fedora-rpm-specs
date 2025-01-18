Name:           calcurse
Version:        4.8.1
Release:        7%{?dist}
Summary:        Text-based personal organizer

License:        BSD-2-Clause
URL:            https://calcurse.org
Source0:        https://calcurse.org/files/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext-devel ncurses-devel autoconf automake asciidoc
BuildRequires:  make
Requires:       python3-httplib2

%description
Calcurse is a text-based calendar and scheduling application. It helps 
keep track of events, appointments, and everyday tasks.

A configurable notification system reminds the user of upcoming 
deadlines, and the curses based interface can be customized to suit user 
needs.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
install -p -m 0644 doc/calcurse.1 $RPM_BUILD_ROOT%{_mandir}/man1/
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS doc/*.txt
%{_bindir}/calcurse*
%{_mandir}/man1/calcurse.1.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 10 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.8.1-6
- Require python3-httplib2 for calcav

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.8.1-1
- 4.8.1

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.8.0-4
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.8.0-1
- 4.8.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.7.1-1
- 4.7.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 4.7.0-1
- 4.7.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 4.6.0-1
- 4.6.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Gwyn Ciesla <gwync@protonmail.com> - 4.5.1-1
- 4.5.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 4.5.0-1
- 4.5.0

* Mon Feb 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 4.4.0-1
- 4.4.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Gwyn Ciesla <limburgher@gmail.com> - 4.3.0-1
- 4.3.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Jon Ciesla <limburgher@gmail.com> - 4.2.2-1
- New upstream.

* Thu Jan 19 2017 Jon Ciesla <limburgher@gmail.com> - 4.2.1-3
- Fix doc installation.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-2
- Rebuild for Python 3.6

* Mon Oct 31 2016 Jon Ciesla <limburgher@gmail.com> - 4.2.1-1
- New upstream.

* Wed Oct 12 2016 Jon Ciesla <limburgher@gmail.com> - 4.2.0-1
- New upstream.

* Thu Apr 14 2016 Jon Ciesla <limburgher@gmail.com> - 4.1.0-1
- New upstream.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 23 2015 Jon Ciesla <limburgher@gmail.com> - 4.0.0-1
- New upstream.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Jon Ciesla <limburgher@gmail.com> - 3.2.1-1
- New upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 3.1.4-1
- New upstream.

* Fri Feb 08 2013 Jon Ciesla <limburgher@gmail.com> - 3.1.3-1
- New upstream.

* Thu Jan 31 2013 Jon Ciesla <limburgher@gmail.com> - 3.1.2-1
- New upstream.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Jon Ciesla <limburgher@gmail.com> - 3.0.0-1
- New upstream.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Jon Ciesla <limb@jcomserv.net> 2.9.2-1
- New upstream.

* Tue Sep 06 2011 Jon Ciesla <limb@jcomserv.net> 2.9.1-1
- New upstream.

* Wed Jun 01 2011 Jon Ciesla <limb@jcomserv.net> 2.9.0-1
- New upstream.

* Wed Apr 06 2011 Jon Ciesla <limb@jcomserv.net> 2.8-3
- Updated URL and Source0 URL.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 07 2010 Jon Ciesla <limb@jcomserv.net> 2.8-1
- Update to 2.8.

* Tue Aug 25 2009 Jon Ciesla <limb@jcomserv.net> 2.7-1
- Update to 2.7.

* Tue Jul 28 2009 Jon Ciesla <limb@jcomserv.net> 2.6-1
- Update to 2.6.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Jon Ciesla <limb@jcomserv.net> 2.5-1
- Update to 2.5.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Jon Ciesla <limb@jcomserv.net> 2.4-1
- Update to 2.4.

* Wed Oct 22 2008 Jon Ciesla <limb@jcomserv.net> 2.3-1
- Update to 2.3.

* Thu Aug 28 2008 Jon Ciesla <limb@jcomserv.net> 2.2-1
- Update to 2.2.

* Tue Aug 12 2008 Jon Ciesla <limb@jcomserv.net> 2.1-1
- Update to 2.1.

* Tue Apr 01 2008 Jon Ciesla <limb@jcomserv.net> 2.0-1
- Update to 2.0.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> 1.9-2
- GCC 4.3 rebuild.

* Thu Oct 25 2007 Jon Ciesla <limb@jcomserv.net> 1.9-1
- Update to 1.9.
- License tag correction.

* Wed May 30 2007 Nigel Jones <dev@nigelj.com> 1.8-2
- Minor touchups to spec file

* Wed May 23 2007 Nigel Jones <dev@nigelj.com> 1.8-1
- Initial SPEC file

