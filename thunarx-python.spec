%global  minorversion 0.5

Name:    thunarx-python
Version: 0.5.2
Release: 6%{?dist}
Summary: Python bindings for the Thunar Extension Framework	

License: LGPLv2+
URL:     http://goodies.xfce.org/projects/bindings/%{name}
Source0: http://archive.xfce.org/src/bindings/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: Thunar-devel >= 1.8.0
BuildRequires: pygobject3-devel >= 2.6.0
BuildRequires: gtk-doc
BuildRequires: python3
BuildRequires: python3-devel

# Renamed / Obsoleted in F32
Provides:       python2-thunarx = %{version}-%{release}
Provides:       python2-thunarx%{?_isa} = %{version}-%{release}
Obsoletes:      python2-thunarx < %{version}-%{release}
# Renamed / Obsoleted in F32
Provides:       python3-thunarx = %{version}-%{release}
Provides:       python3-thunarx%{?_isa} = %{version}-%{release}
Obsoletes:      python3-thunarx < %{version}-%{release} 

%global _description\
These bindings allow one to create python plugins for Thunar.

%description %_description

Summary: %summary

%prep
%autosetup

%build
export PYTHON=%{python3}
export PYTHON_LIBS=-lpython%{python3_version}
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig
%configure --enable-gtk-doc
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name *.la -print -delete
find %{buildroot} -name style.css -print -exec mv '{}' docs/html \;
mkdir -p %{buildroot}/%{_datadir}/thunarx-python/extensions

%global _docdir_fmt %{name}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/thunarx-3/
%{_datadir}/thunarx-python/extensions
%{_datadir}/gtk-doc/html/%{name}/
%doc %{_pkgdocdir}/examples/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.2-5
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.10

* Sat Jan 30 2021 Filipe Rosset <rosset.filipe@gmail.com> - 0.5.2-1
- Update to 0.5.2, remove upstreamed patch, fixes rhbz#1800296

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.1-27
- Add patch to fix building with gcc-10

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-26
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 23 2019 Kevin Fenzi <kevin@scrye.com> - 0.5.1-24
- Rename binary package thunarx-python and obsolete/provide the old python2/python3 versions.

* Thu Aug 22 2019 Kevin Fenzi <kevin@scrye.com> - 0.5.1-23
- Rebuild with python3.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.1-20
- Update to 0.5.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 10 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.0-6
- Python 2 binary package renamed to python2-thunarx
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Raphael Groner <projects.rg@smart.ms> - 0.3.0-1
- new version
- modernize
- fix license and documentation

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Kevin Fenzi <kevin@scrye.com> 0.2.3-8
- Reconf to add aarch64 support. Fixes bug #926633

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.3-4
- Rebuild for new libpng

* Mon Mar 21 2011 G.Balaji <balajig81@gmail.com> 0.2.3-3
- Addressed Second level of Review Comments.

* Mon Mar 21 2011 G.Balaji <balajig81@gmail.com> 0.2.3-2
- Addressed Review Comments.

* Tue Mar 15 2011 G.Balaji <balajig81@gmail.com> 0.2.3-1
- Initial Version.
