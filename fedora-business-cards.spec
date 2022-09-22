%global forgeurl    https://pagure.io/fedora-business-cards/
Version:            2.3.0

%forgemeta

Name:               fedora-business-cards
Release:            4%{?dist}
Summary:            The Fedora business card generator

License:            GPLv2+
URL:                https://fedoraproject.org/wiki/Business_cards
Source:             %{forgesource}

BuildArch:          noarch
BuildRequires:      python3-setuptools
BuildRequires:      python3-devel
Requires:           python3-fedora fedora-logos
Requires:           inkscape ghostscript
Requires:           aajohan-comfortaa-fonts abattis-cantarell-fonts

%description
fedora-business-cards is a tool written in Python to generate business cards
for Fedora Project contributors.

%prep
%forgesetup

%build
%py3_build


%install
%py3_install

%files
%doc README
%license COPYING
%{python3_sitelib}/fedora_business_cards/
%{python3_sitelib}/fedora_business_cards-*.egg-info/
%{_bindir}/%{name}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 06 2021 Gerald Cox <gbcox@member.fsf.org> - 2.3.0-1
- Fedora Logo Update rhbz#1955327

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.1-5
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-2
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Brian Exelbierd <bexelbie@redhat.com> - 2.1.1-1
- Bugfix for Inkscape CLI usage

* Wed Apr 29 2020 Brian Exelbierd <bexelbie@redhat.com> - 2.2-1
- Works with inkscape 1.0's CLI

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Brian Exelbierd <bexelbie@redhat.com> - 2.1-1
- New Business Card Designs

* Mon Sep 02 2019 Brian Exelbierd <bexelbie@redhat.com> - 2-1
- Port to Python3

* Tue Apr 23 2019 Brian Exelbierd <bexelbie@redhat.com> - 1-0.15.beta1
- Removed unneeded python2-pygpgme dependency

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.14.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Brian Exelbierd <bexelbie@redhat.com> - 1-0.12.beta1
- Fix python2 usage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.12.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.11.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1-0.10.beta1
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.9.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.8.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-0.7.beta1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.6.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-0.5.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-0.4.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Ian Weller <iweller@redhat.com> - 1-0.1.beta1
- Lots of updates, including dynamic sizing and new fonts
- Fix CVE-2013-0159 (patch by Michael Scherer)
- Remove BuildRoot
- Get rid of "if Fedora 10 or earlier" because we are way past that

* Mon Jul 23 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2.4.3-5
- Remove PyXLM dep as it's not at all needed

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Ian Weller <ian@ianweller.org> - 0.2.4.3-1
- Add template for the Europe business card size

* Sun Jul 25 2010 Ian Weller <iweller@redhat.com> - 0.2.4.2-5
- Rebuilt again for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Ian Weller <ian@ianweller.org> - 0.2.4.2-2
- Add an appropriate conditional require for inkscape

* Wed Jun 17 2009 Ian Weller <ian@ianweller.org> - 0.2.4.2-1
- Fix pavement.py issues

* Wed Jun 17 2009 Ian Weller <ian@ianweller.org> - 0.2.4.1-1
- Fix bug #502338 (fedora-business-cards generate no PNG)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Ian Weller <ianweller@gmail.com> 0.2.4-3
- Fix F11 dependency on the MgOpen fonts (again)

* Wed Dec 31 2008 Ian Weller <ianweller@gmail.com> 0.2.4-2
- Fix F11 dependency on the MgOpen fonts

* Sun Dec 21 2008 Ian Weller <ianweller@gmail.com> 0.2.4-1
- Add CMYK PDF as an export option

* Sun Dec 14 2008 Ian Weller <ianweller@gmail.com> 0.2.3-1
- Add EPS as an export option

* Sun Dec 14 2008 Ian Weller <ianweller@gmail.com> 0.2.2-3
- Change summary to be more helpful

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.2-2
- Rebuild for Python 2.6

* Sun Nov 09 2008 Ian Weller <ianweller@gmail.com> 0.2.2-1
- Fix coloration in back templates

* Thu Oct 30 2008 Ian Weller <ianweller@gmail.com> 0.2.1-1
- Upstream update

* Mon Oct 06 2008 Ian Weller <ianweller@gmail.com> 0.2-3
- Fix BuildRequires

* Mon Oct 06 2008 Ian Weller <ianweller@gmail.com> 0.2-2
- Fix Source0 URL (fedorapeople.org doesn't do https)

* Mon Oct 06 2008 Ian Weller <ianweller@gmail.com> 0.2-1
- Initial package build.
