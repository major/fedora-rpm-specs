Name:           sugar-fractionbounce
Version:        28.1
Release:        6%{?dist}
Summary:        A game which teaches fractions and estimations

License:        GPLv3+
URL:            http://wiki.sugarlabs.org/go/Activities/FractionBounce
Source0:        http://download.sugarlabs.org/sources/honey/FractionBounce/FractionBounce-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
BuildArch:      noarch
Requires:       sugar >= 0.116

%description
FractionBounce is a game that prompts the player to nudge a bouncing 
ball to land at a point on the bottom of the screen that is an estimate 
of a given fraction. e.g. if 1/3 is displayed, then the ball must land 
1/3 the distance along the bottom.

%prep
%autosetup -n FractionBounce-%{version}

sed -i 's/python/python3/' *.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/FractionBounce.activity/

%find_lang org.sugarlabs.FractionBounceActivity

%files -f org.sugarlabs.FractionBounceActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/FractionBounce.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 28.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 28.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 28.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 28.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 28.1-2
- Fix python3 typo

* Wed Aug 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 28.1-1
- Update to 28.1, move to python3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 25-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 25-1
- Version 25 release
- Remove the generated .desktop file (#1424493)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jul 19 2014 Kalpa Welivitigoda <callkalpa@gmail.com> - 22
- version 22 release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 09 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 21-1
- version 21 release

* Fri Aug 30 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 19-1
- version 19 release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 17-1
- version 17 release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Kalpa Welivitigoda <callkalpa@gmail.com< - 15-2
- replaced python-devel with python2-devel in BuildRequires

* Sun Jan 13 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 15-1
- version 15 release
- gtk 3 port

* Wed Mar 07 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 14-1
- initial packaging
