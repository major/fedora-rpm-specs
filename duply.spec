Name:           duply
Version:        2.4.1
Release:        1%{?dist}
Summary:        Wrapper for duplicity
License:        GPLv2
URL:            http://duply.net/
Source0:        http://downloads.sourceforge.net/ftplicity/%{name}_%{version}.tgz
BuildArch:      noarch
BuildRequires:  txt2man >= 1.5.6
Requires:       duplicity


%description
duply is a frontend for the mighty duplicity magic. It simplifies
running duplicity with cron or on command line by:

- keeping recurring settings in profiles per backup job
- automated import/export of keys between profile and keyring
- enabling batch operations e.g. backup_verify_purge
- executing pre/post scripts
- precondition checking for flawless duplicity operation

Since version 1.5.0 all duplicity backends are supported. Hence the
name changed from ftplicity to duply.


%prep
%setup -q -n %{name}_%{version}


%build
# generate the man page
chmod +x %{name}
./%{name} txt2man > %{name}.1


%install
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
# root's profiles will be stored there
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
# fix shebang line
sed -i "1c#!/bin/bash" %{buildroot}%{_bindir}/%{name}
mv gpl-2.0.txt LICENSE


%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_sysconfdir}/%{name}


%changelog
* Thu Sep 15 2022 Thomas Moschny <thomas.moschny@gmx.de> - 2.4.1-1
- Update to 2.4.1.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr  9 2022 Thomas Moschny <thomas.moschny@gmx.de> - 2.4-1
- Update to 2.4.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 27 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.1-1
- Update to 2.3.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2.3-1
- Update to 2.3.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.2-1
- Update to 2.2.2.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.1-1
- Update to 2.2.1.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar  2 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2.2-1
- Update to 2.2.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2.1-1
- Update to 2.1.
- Spec file updates.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar  4 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.4-1
- Update to 2.0.4.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.3-2
- Add missing %%changelog.

* Wed Aug 30 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.3-1
- Update to 2.0.3.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun  3 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.2-1
- Update to 2.0.2.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.1-1
- Update to 2.0.1.

* Tue Nov  8 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.0-1
- Update to 2.0.

* Fri Jun  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.11.3-1
- Update to 1.11.3.

* Sat Feb 13 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.11.2-1
- Update to 1.11.2.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan  5 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.11.1-1
- Update to 1.11.1
- Mark license with %%license.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.9.1-1
- Update to 1.9.1.

* Wed Aug 27 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.9.0-1
- Update to 1.9.0.
- Modernize spec file.

* Fri Jul 18 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.0-1
- Update to 1.8.0.

* Fri Jul 18 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.7.4-1
- Update to 1.7.4.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.7.3-1
- Update to 1.7.3.

* Tue Apr  1 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.7.1-1
- Update to 1.7.1
- Update %%description.

* Fri Mar 21 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.7.0-1
- Update to 1.7.0.

* Tue Jan 28 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.6.0-1
- Update to 1.6.0.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.11-1
- Update to 1.5.11.

* Thu Apr  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.10-1
- Update to 1.5.10.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.9-1
- Update to 1.5.9.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.7-1
- Update to 1.5.7.

* Tue Jun  5 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.6-1
- Updte to 1.5.6.

* Wed Feb  8 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.5.5-1
- Update to 1.5.5.5.

* Fri Nov 11 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.5.4-1
- Update to 1.5.5.4.
- Rename license file to LICENSE.
- Remove %%defattr directive in %%files.

* Tue Jul  5 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.5.1-1
- Update to 1.5.5.1.

* Tue May 10 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.5-1
- Update to 1.5.5.
- Generate and pack a man page.

* Wed Feb 23 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.4.2-2
- Convert duply script to UTF-8.

* Thu Feb  3 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.4.2-1
- New package.
