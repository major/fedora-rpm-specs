Name:		sugar-story
Version:	20
Release:	8%{?dist}
Summary:	An activity that uses images to prompt the learner to tell stories

# grecord.py and sprites.py is in MIT and all other files in GPLv3+
License:	GPLv3+ and MIT
URL:		http://wiki.sugarlabs.org/go/Activities/Story
Source0:	http://download.sugarlabs.org/sources/honey/Story/Story-%{version}.tar.bz2

BuildRequires:	gettext
BuildRequires:	python3-devel
BuildRequires:	sugar-toolkit-gtk3
BuildArch:	noarch
Requires:	sugar
Requires:	sugar-toolkit-gtk3


%description
An activity that uses images to prompt the learner to tell stories.

%prep
%setup -q -n Story-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Story.activity/

%find_lang org.sugarlabs.StoryActivity


%files -f org.sugarlabs.StoryActivity.lang
%license COPYING
%doc CREDITS NEWS
%{sugaractivitydir}/Story.activity/


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20-1
- Release 20

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 19-1
- Release 19

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 18-1
- Release 18

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 15-1
- Release 15

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul  1 2014 Peter Robinson <pbrobinson@fedoraproject.org> 12-1
- Release 12

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 11-1
- Release 11

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 9-6
- Updated the license tag with GPLv3+ and MIT

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 9-5
- removed the rm po/nah.po entry, removed backslash between %%{buildroot} and %%{_prefix}

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 9-4
- correct the license

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 9-3
- correct the license

* Tue Jun 04 2013 Danishka Navin <danishka@gmail.com> - 9-2
- added COPYING
- removed duplicate CREDITS
- added entry to remove po/nah.po
- changed python2-devel to python under BuildRequires
- added sugar-toolkit-gtk3

* Tue Jun 04 2013 Danishka Navin <danishka@gmail.com> - 9-1
- updated to the version 9

* Wed Jul 18 2012 Danishka Navin <danishka@gmail.com> - 5-1
- initial packaging
