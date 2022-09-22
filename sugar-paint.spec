Name:          sugar-paint
Version:       70
Release:       11%{?dist}
Summary:       Paint activity for Sugar
License:       GPLv2
URL:           http://wiki.sugarlabs.org/go/Activities/Paint

Source0:       http://download.sugarlabs.org/sources/honey/Paint/Paint-%{version}.tar.bz2
Patch0:        sugar-paint-Fedora.patch

BuildRequires: make
BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3-devel
Requires:      sugar

%description
Paint will provide a canvas for an individual or a group of children 
to express themselves creatively through drawing. 

%prep
%setup -q -n Paint-%{version}
%patch0 -p1 -b .fedora

# make sure to grab blob from the right location and remove prebuilt ones
rm -rf fill/linux* fill/arm*

%build
%{make_build} -C fill LD=%{__cc}
python3 ./setup.py build

%install
mkdir -p %{buildroot}%{python3_sitearch}/fill/
install -Dm 0755 fill/lib/_fill.so %{buildroot}%{python3_sitearch}/fill/
install -Dm 0644 fill/lib/__init__.py %{buildroot}%{python3_sitearch}/fill/

python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm -rf %{buildroot}%{sugaractivitydir}Paint.activity/fill
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Paint.activity/

%find_lang org.laptop.Oficina

%files -f org.laptop.Oficina.lang
%license COPYING
%doc NEWS
%{python3_sitearch}/fill/
%{sugaractivitydir}/Paint.activity/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 70-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 70-10
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 70-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 70-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 70-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 70-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 70-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 70-3
- Rebuilt for Python 3.9

* Mon Feb 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 70-2
- drop python3 sed workaround

* Mon Feb 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 70-1
- Update to 70

* Thu Jan 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> 69-1
- Release 69

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 68-1
- Release 68

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 66-3
- Add patch to fix upstream #27

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 66-1
- Release 66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 65-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 65-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 Peter Robinson <pbrobinson@fedoraproject.org> 65-5
- Fix crash on startup

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 65-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 65-1
- Release 65

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Peter Robinson <pbrobinson@fedoraproject.org> 64-1
- Release 64

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 63-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 63-3
- Fix linking of binary component (#1107402)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 63-1
- Release 63

* Thu Oct 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 62-1
- Release 62

* Mon Aug  5 2013 Peter Robinson <pbrobinson@fedoraproject.org> 61-1
- Release 61

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Peter Robinson <pbrobinson@fedoraproject.org> 60-1
- Release 60

* Tue May 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 59-1
- Release 59

* Sun May 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 58-1
- Release 58

* Thu Mar 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 57-1
- Release 57

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan  9 2013 Peter Robinson <pbrobinson@fedoraproject.org> 55-1
- Release 55

* Thu Dec 20 2012 Peter Robinson <pbrobinson@fedoraproject.org> 54-1
- Release 54

* Mon Dec 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 53-1
- Release 53

* Wed Nov 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> 52-1
- Release 52

* Sat Nov 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> 51-1
- Release 51

* Fri Nov 23 2012 Peter Robinson <pbrobinson@fedoraproject.org> 50-1
- Release 50

* Wed Nov 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 49-1
- Release 49

* Sun Nov  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 48-1
- Release 48

* Sat Oct 20 2012 Peter Robinson <pbrobinson@fedoraproject.org> 47-1
- Release 47

* Sat Oct  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> 46-1
- Release 46

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 43-1
- Release 43

* Thu Apr 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 42-1
- Release 42

* Thu Apr 12 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 41-1
- Release 41

* Fri Mar 16 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 40-1
- Release 40

* Sat Mar 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 39-1
- Release 39

* Thu Mar  8 2012 Tom Callaway <spot@fedoraproject.org> - 37-3
- fix build, do not strip .so file

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 13 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 37-1
- Release 37

* Thu Jun  9 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 34-1
- release 34

* Tue May 17 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 33-1
- release 33

* Mon Apr 11 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 32-1
- release 32

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 27-4
- Bump build

* Fri Jul 30 2010 Sebastian Dziallas <sebastian@when.com> - 27-3
- Rebuild for Python 2.7

* Mon May 24 2010 Sebastian Dziallas <sebastian@when.com> - 27-2
- Fix the buildroot

* Thu Mar 11 2010 Sebastian Dziallas <sebastian@when.com> - 27-1
- New upstream release
- Cleaned the spec file up

* Wed Nov 19 2008 Bryan Kearney <bkearney@redhat.com> - 23-2
- Deleted directory creation which is not required.

* Tue Nov 18 2008 Bryan Kearney <bkearney@redhat.com> - 23-1
- Initial packaging
