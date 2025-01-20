%global upstream_name easygui

Name:           python-easygui
Version:        0.96
Release:        46%{?dist}
Summary:        Very simple, very easy GUI programming in Python

#License file, says CC 2.0 upstream website says with this version they moved to BSD.
License:        BSD-3-Clause
URL:            http://easygui.sourceforge.net/
# Source doesn't follow the normal SF convention since upstream isn't using the SF Files system.
Source0:        http://easygui.sourceforge.net/download/version%{version}/easygui_v%{version}_docs.tar.gz
Source1:        easygui-LICENSE.txt

BuildArch:      noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools

%global _description\
Experienced Pythonistas need support for quick and dirty GUI features. New\
Python programmers need GUI capabilities that don't require any knowledge\
of Tkinter, frames, widgets, callbacks or lambda. This is what EasyGUI\
provides. Using EasyGUI, all GUI interactions are invoked by simple\
function calls.\
\
EasyGUI is different from other GUIs in that EasyGUI is NOT event-driven.\
It allows you to program in a traditional linear fashion, and to put up\
dialogs for simple input and output when you need to. If you have not yet\
learned the event-driven paradigm for GUI programming, EasyGUI will allow\
you to be productive with very basic tasks immediately. Later, if you\
wish to make the transition to an event-driven GUI paradigm, you can do\
so with a more powerful GUI package such as anygui, PythonCard, Tkinter,\
wxPython, etc.

%description %_description

%package -n python%{python3_pkgversion}-%{upstream_name}
Summary:        Very simple, very easy GUI programming in Python3
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-tkinter

%description -n python%{python3_pkgversion}-%{upstream_name}
Experienced Pythonistas need support for quick and dirty GUI features. New 
Python programmers need GUI capabilities that don't require any knowledge 
of Tkinter, frames, widgets, callbacks or lambda. This is what EasyGUI 
provides. Using EasyGUI, all GUI interactions are invoked by simple 
function calls.

EasyGUI is different from other GUIs in that EasyGUI is NOT event-driven. 
It allows you to program in a traditional linear fashion, and to put up 
dialogs for simple input and output when you need to. If you have not yet 
learned the event-driven paradigm for GUI programming, EasyGUI will allow 
you to be productive with very basic tasks immediately. Later, if you 
wish to make the transition to an event-driven GUI paradigm, you can do 
so with a more powerful GUI package such as anygui, PythonCard, Tkinter, 
wxPython, etc. 
This package allows for use of easygui with Python 3.

%prep
%setup -qc %{upstream_name}-%{version}

rm -rf %{py3dir}
cp -a . %{py3dir}

%build
pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd

%install
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

install -m 644 %{SOURCE1} .


%files -n python%{python3_pkgversion}-%{upstream_name}
%doc easygui_license_info.txt cookbook/ easygui_pydoc.html easygui_version_info.html epydoc/ faq/ pydoc/ tutorial/
%doc easygui-LICENSE.txt
%{python3_sitelib}/easygui*
%{python3_sitelib}/__pycache__/easygui.cpython-3*.py*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.96-44
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.96-40
- Rebuilt for Python 3.12

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.96-39
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.96-36
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-34
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.96-33
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.96-30
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.96-28
- Drop python 2.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.96-27
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.96-26
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.96-22
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.96-21
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Robert Scheck <robert@fedoraproject.org> - 0.96-19
- Minor spec file changes to build also for EPEL 7 (#1498637)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.96-18
- Python 2 binary package renamed to python2-easygui
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.96-15
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-14
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Jon Ciesla <limburgher@gmail.com> - 0.96-12
- Fix Python 3 build.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.96-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.96-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Thu Jul 26 2012 David Malcolm <dmalcolm@redhat.com> - 0.96-4
- generalize fileglob to ease transition to Python 3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 25 2011 Jon Ciesla <limb@jcomserv.net> - 0.96-1
- Corrected pycache file inclusion.

* Wed May 04 2011 Jon Ciesla <limb@jcomserv.net> - 0.96-0
- Initial RPM release
