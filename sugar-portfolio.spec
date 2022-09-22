Name:           sugar-portfolio
Version:        52
Release:        7%{?dist}
Summary:        A simple tool for generating slide show from starred Journal entries

License:        GPLv3+
URL:            http://wiki.sugarlabs.org/go/Activities/Portfolio
Source0:        http://download.sugarlabs.org/sources/honey/Portfolio/Portfolio-%{version}.tar.bz2

BuildRequires:  python3-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.98.0

%description
Portfolio is a simple tool for generating a slide show from Journal 
entries that have been starred. The title, description, and preview 
image are used to auto-generate a slide. The slide show itself can be 
saved as an HTML document that can be shared.

%prep
%autosetup -n Portfolio-%{version}

sed -i 's/python/python3/' *.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Portfolio.activity/

%find_lang org.sugarlabs.PortfolioActivity

%files -f org.sugarlabs.PortfolioActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Portfolio.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 52-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 52-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 52-1
- v52
- Update Python 3 dependency declarations

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 01 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 51-1
- Release 51

* Thu Aug 09 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 50-1
- Release 50

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 49-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 49-1
- Release 49
- Remove the generated .desktop file (#1424509)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 13 2015 Kalpa Welivitigoda - 47-1
- release 47

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 07 2014 Kalpa Welivitigoda <callkalpa@gmail.com> 46-1
- release 46

* Sun Nov 23 2014 Peter Robinson <pbrobinson@fedoraproject.org> 45-1
- release 45

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 29 2013 Kalpa Welivitigoda <callkalpa@gmail.com> 44-1
- release 44

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 42-1
- release 42

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 37-1
- release v37

* Mon Nov 19 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 35-1
- release v35

* Fri Nov 02 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-2
- require sugar >= 0.97.6

* Thu Nov 01 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-1
- release v33

* Tue Oct 30 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 31-2
- gtk3 port

* Tue Oct 30 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 31-1
- release v31

* Fri Oct 26 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 28-1
- release v28

* Thu Oct 25 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 27-1
- release v27

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 24 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 26-1
- release v26

* Thu May 24 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 24-1
- release v24

* Fri Mar 16 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 23-1
- release v23

* Wed Feb 29 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 21-1
- release v21

* Thu Jan 19 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 20-1
- release v20

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 2 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 15-2
- release bump to fix the update issue of f-16 at bodhi

* Fri Oct 28 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 15-1
- initial packaging
