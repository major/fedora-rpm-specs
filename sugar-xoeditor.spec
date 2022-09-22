Name:		sugar-xoeditor
Version:	14
Release:	5%{?dist}
Summary:	Editor for XO icon colors

License:	GPLv3+ and MIT
URL:		http://wiki.sugarlabs.org/go/Activities/XoEditor
Source0:	http://download.sugarlabs.org/sources/honey/xoEditor/xoEditor-%{version}.tar.bz2

BuildRequires:	python3-devel
BuildRequires:	sugar-toolkit-gtk3
BuildRequires:	gettext
BuildArch:	noarch
Requires:	sugar


%description
Editor for XO icon colors; Lets you explore different color patterns.

%prep
%setup -q -n xoEditor-%{version}
sed -i "s|python|python3|g" setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/xoEditor.activity/

%find_lang org.laptop.xoEditorActivity


%files -f org.laptop.xoEditorActivity.lang
%license COPYING
%doc NEWS 
%{sugaractivitydir}/xoEditor.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 14-1
- Update to xoEditor 14, migrate to python3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Kalpa Welivitigoda <callkalpa@gmail.com> - 13-10
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 13-1
- Release 13

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Danishka Navin <danishka@gmail.com> - 11-2
- fixed the licence and droped defattr

* Tue Jun 04 2013 Danishka Navin <danishka@gmail.com> - 11-1
- updated to version 11

* Mon Jul 16 2012 Danishka Navin <danishka@gmail.com> - 6-1
- initial packaging

