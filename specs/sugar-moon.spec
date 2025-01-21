Version:   19
Release:   18%{?dist}
Name:      sugar-moon
Summary:   Moon phases activity for sugar
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:   Apache-2.0
BuildArch: noarch
URL:       http://wiki.laptop.org/go/Moon
Source0:   http://download.sugarlabs.org/sources/honey/Moon/Moon-%{version}.tar.bz2

BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
Requires: sugar 
Requires: sugar-toolkit-gtk3

%description
Moon is a simple Lunar phase activity for Sugar.

%prep
%setup -q -n Moon-%{version}
sed -i 's/env python/env python3/' setup.py

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Moon.activity/

%find_lang com.garycmartin.Moon

%files -f com.garycmartin.Moon.lang
%license COPYING
%doc AUTHORS
%{sugaractivitydir}/Moon.activity/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 19-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 19-6
- Fix python3 env

* Mon Feb 10 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 19-5
- Update Python 3 dependency declarations

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Peter Robinson <pbrobinson@fedoraproject.org> 19-1
- Release 19

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 18-1
- Release 18

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 17-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 17-1
- Release 17

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 16-5
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 16-1
- Release 16

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 14-1
- Release 14

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 12-1
- Release 12

* Mon Jun 20 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 12-1
- v12

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 11-3
- Bump build

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 11-2
- recompiling .py files against Python 2.7 (rhbz#623381)

* Thu Jun 10 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 11-1
- Update to 11

* Mon Dec 14 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 10-3
- Add buildreq gettext to fix build issues on F-12/rawhide - fixes # 539034

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 3 2009 Bryan Kearney <bkearney@redhat.com> - 10-1
- Resolve BZ#503892 by upgrading to latest upstream
- Merged alsroot's solution to future proof json module
- Picked-up latest localizations 

* Fri Feb 27 2009 Bryan Kearney <bkearney@redhat.com> - 9-1
- Code cleanup (make pylint happier)
- Merged alsroot's excellent independence resolution code addition   
  (resizes moon image to fit available display, much better for misc   
  SoaS hardware screen resolutions)
- Updated localizations (latest from Pootle, thanks all!)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 8-3
- Rebuild for Python 2.6

* Mon Oct 14 2008 Bryan Kearney <bkearney@redhat.com>- 8-2
- Review comments from simon@schampijer.de

* Mon Oct 13 2008 Bryan Kearney <bkearney@redhat.com>- 8-1
- New release of the moon activity

* Thu Oct 2 2008 Bryan Kearney <bkearney@redhat.com> - 7-1
- Initial packaging
