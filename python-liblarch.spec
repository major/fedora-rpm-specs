Name:           python-liblarch
Version:        3.1.0
Release:        7%{?dist}
Summary:        Data structures helper library for python

License:        LGPLv3+
URL:            https://wiki.gnome.org/Projects/liblarch
Source0: https://github.com/getting-things-gnome/liblarch/archive/v%{version}/liblarch-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  gtk3
BuildRequires:  %{py3_dist pygobject}
BuildRequires:  python3-pytest
BuildRequires:  xorg-x11-server-Xvfb

%global _description %{expand:
Liblarch is a python library built to easily handle data structure such as\
lists, trees and directed acyclic graphs.}

%description %_description

%package -n python3-liblarch
Summary:        %{summary}
Requires:       python3-gobject-base

%description -n python3-liblarch %_description

%package -n python3-liblarch-gtk
Summary:        Liblarch gtk binding for use in Gtk.Treeview
Requires:       python3-liblarch = %{version}-%{release}
Requires:       gtk3

%description -n python3-liblarch-gtk
liblarch_gtk is a liblarch binding that will allow you to use your
data structure into a Gtk.Treeview.


%prep
%autosetup -n liblarch-%{version}
sed -i "1c#!%{_bindir}/python3" ./examples/contact_list/contact_list.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install


%check
xvfb-run -d %{_bindir}/pytest


%files -n python3-liblarch
%license LICENSE
%doc AUTHORS README.md examples
%{python3_sitelib}/liblarch/
%{python3_sitelib}/liblarch-%{version}.dist-info

%files -n python3-liblarch-gtk
%license LICENSE
%doc AUTHORS README.md
%{python3_sitelib}/liblarch_gtk/


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.1.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Miguel Reis de Araújo <miguel7r.araujo@gmail.com> - 3.1.0-1
- New upstream release 3.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Jan Beran <jberan@redhat.com> - 3.0 - 1
- New version in Python 3

* Tue Aug 29 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.0-12
- Fix python2 subpackage naming

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.0-11
- Python 2 binary package renamed to python2-liblarch
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan  9 2014 Yanko Kaneti <yaneti@declera.com> - 2.1.0-4
- Upstream moved to github and added examples and tests to the tarball

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov  9 2012 Yanko Kaneti <yaneti@declera.com> - 2.1.0-1
- New upstream release - 2.1.0. 
- Upstream merged python-liblarch_gtk - still package separately for now

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar  6 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.0-2
- Address review. BR python2-devel. No sitelib definition.
