Name:		sugar-colordeducto
Version:	8
Release:	7%{?dist}
Summary:	To improve students skills to deducing logic and learning colors & schemes

License:	GPLv3 and MIT
URL:		https://github.com/sugarlabs/colordeducto
Source0:	http://download.sugarlabs.org/sources/honey/ColorDeducto/ColorDeducto-%{version}.tar.bz2

BuildRequires:	sugar-toolkit-gtk3 gettext python3-devel
BuildArch:	noarch
Requires:	sugar

%description
To improve students skills to deducing logic and learning colors & schemes.

%prep
%setup -q -n ColorDeducto-%{version}
chmod +x  mun.py
sed -i 's/\r//' README.txt
sed -i "s|python|python3|g" setup.py
sed -i "s|python|python3|g" mun.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Colordeducto.activity/

%find_lang in.seeta.ColorDeducto


%files -f in.seeta.ColorDeducto.lang
%license COPYING
%doc NEWS README.txt
%{sugaractivitydir}/ColorDeducto.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 8-1
- v8

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Kalpa Welivitigoda <callkalpa@gmail.com> - 7-13
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7-10
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Danishka Navin <danishka@gmail.com> - 7-3
- removed python from  BuildRequires and removed newline after %%changelog

* Tue Jun 04 2013 Danishka Navin <danishka@gmail.com> - 7-2
- fixed new BuildRequires for python2-devel and sugar-toolkit-gtk3 added

* Tue Jun 04 2013 Danishka Navin <danishka@gmail.com> - 7-1
- updated to the version 7

* Tue Jul 17 2012 Danishka Navin <danishka@gmail.com> - 5-4
- droped %%defattr(-,root,root,-)

* Tue Jul 17 2012 Danishka Navin <danishka@gmail.com> - 5-3
- fixed both executable bit and wrong-file-end-of-line-encoding of README.txt

* Tue Jul 17 2012 Danishka Navin <danishka@gmail.com> - 5-2
- removed %%defattr(-,root,root,-) and fixed the versining issue in the changelog

* Mon Jul 16 2012 Danishka Navin <danishka@gmail.com> - 5-1
- initial packaging

