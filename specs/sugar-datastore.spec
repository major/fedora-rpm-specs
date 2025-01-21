Name:    sugar-datastore
Version: 0.121
Release: 6%{?dist}
Summary: Sugar Datastore
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://sugarlabs.org/
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-xapian
# py-compile needs updating
BuildRequires: automake
Requires: python3-xapian

%description
sugar-datastore is a simple log like datastore able to connect with multiple
backends. The datastore supports connectionig and disconnecting from
backends on the fly to help the support the limit space/memory
characteristics of the OLPC system and the fact that network services
may become unavailable at times

%prep
%autosetup -p1

%build
ls -1 %{_datadir}/automake-*/py-compile | sort | \
	tail -n 1 | while read f
do
	cp -p $f .
done

%configure
%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%files
%license COPYING
%doc AUTHORS NEWS
%{python3_sitelib}/*
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.121-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.121-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.121-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.121-3
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.121-2
- Rebuilt for Python 3.13

* Wed Feb 07 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.121-1
- New Release 0.121

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.120-5
- Update py-compile for python 3.12, imp module removed

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.120-3
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 21 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.120-1
- New Release 0.120

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.119-1
- Update to 0.119 release

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.118-6
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.118-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.118-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Ibiam Chihurumnaya <ibiamchihurumnaya> - 0.118-3
- Temporary fix for issue with detecting python version, patch was sent by Alex Perez.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.118-2
- Rebuilt for Python 3.10

* Thu Jan 28 2021 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 0.118-1
- Update to 0.118 release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.116-3
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-1
- Update to 0.116 release

* Wed Aug 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.114-1
- Update to 0.114 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.113
- Update to sugar 0.113 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.112-6
- Minor build fixes and cleanups

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.112-5
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.112-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.112-1
- Upgrade to sugar 0.112 stable release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.110.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.110.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.110.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.110.0-1
- Upgrade to sugar 0.110.0 stable release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.108.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Mar  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.1-1
- Sugar 0.108.1 stable release

* Sat Feb 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.0-1
- Sugar 0.108.0 stable release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.2-1
- Sugar 0.107.2 devel release

* Mon Jan 4  2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.1-1
- Sugar 0.107.1 devel release

* Fri Nov 27 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.0-1
- Sugar 0.107.0 devel release

* Tue Jul  7 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.106.0-1
- Sugar 0.106.0 stable release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.105.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.105.2-1
- Sugar 0.105.2 development release

* Tue May 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.105.1-1
- Sugar 0.105.1 development release

* Tue Mar 10 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.1-1
- Sugar 0.104.1 stable release

* Sat Feb 14 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.0-1
- Sugar 0.104.0 stable release

* Sat Jan 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.2-1
- New upstream 0.103.2 development release

* Thu Dec 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.1-1
- New upstream 0.103.1 development release

* Thu Nov 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.0-1
- New upstream 0.103.0 development release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul  2 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.102.0-1
- Sugar 0.102.0 stable release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.0-1
- 0.101.0 devel release

* Fri Nov  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.0-1
- Sugar 0.100.0 stable release

* Tue Oct 8  2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.2-1
- 0.99.2 devel release

* Wed Jul 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-1
- 0.99.1 devel release

* Fri Jun 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.0-1
- 0.99.0 devel release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-1
- Sugar 0.98.1 stable release

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.0-1
- Sugar 0.98.1 stable release

* Sat Nov 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.4-1
- 0.97.4 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.3-1
- 0.97.3 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.2-1
- 0.97.2 devel release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.1-1
- 0.97.1 devel release

* Mon Sep 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.0-1
- 0.97.0 devel release
- Move from cjson to mainline python json

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-1
- devel release 0.95.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.1-1
- devel release 0.95.1
