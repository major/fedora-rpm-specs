Name:           sugar-words
Version:        24
Release:        8%{?dist}
Summary:        A multi lingual dictionary with speech synthesis

License:        GPLv3+
URL:            https://github.com/sugarlabs/words-activity
Source0:        http://download.sugarlabs.org/sources/honey/Words/Words-%{version}.tar.bz2

BuildRequires:  python3 python3-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar

%description
Words is a multi lingual dictionary for sugar. It is enabled 
with speech synthesis.

%prep
%autosetup -n Words-%{version}
rm po/nah.po
rm po/son.po

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%/&{sugaractivitydir}/Words.activity/

%find_lang org.laptop.Words

%files -f org.laptop.Words.lang
%doc NEWS AUTHORS HACKING
%{sugaractivitydir}/Words.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 24-4
- add missing % in update for python bytecompile changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 24-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 24-1
- v24
- Update Python 3 depedency declarations

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 23-3
- Python 2 fixes

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 23-1
- New 23 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 22-1
- version 22 release

* Thu Feb 23 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 21-5
- Remove the generated .desktop file (#1424517)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jul 20 2014 Kalpa Welivitigoda <callkalpa@gmail.com> - 21-1
- version 21 release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 19-2
- replaced python-devel with python2-devel in BuildRequires
- removed obsolete stuff

* Sat Dec 15 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 19-1
- initial packaging
