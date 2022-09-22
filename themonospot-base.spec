Summary   : Base component for themonospot system, parser/editor and content descriptor
Name      : themonospot-base
Version   : 0.8.2
Release   : 31%{?dist}
License   : GPLv2
Group     : Applications/Multimedia
URL       : http://www.integrazioneweb.com/themonospot
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-base-%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: make
BuildRequires: mono-devel

Obsoletes: themonospot < 0.8.0

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
themonospot-base is core package for themonospot system. It install:
    - themonospot-base mono assembly (use from other gui applications)
    - themonospot-plugin-interface (use to write plugins)
    - themonospot-plugin-manager (use to load plugins at runtime)
    - xml language files


%package devel
Summary: Development files for themonospot-base
Requires: %{name} = %{version}-%{release}



%description devel
Development files for themonospot-base 


%prep
%setup -q

sed -i "s#gmcs#mcs#g" configure*
sed -i "s#gmcs#mcs#g" */Makefile*

%build
%configure
make

%install
make DESTDIR=%{buildroot} install
chmod 0755 %{buildroot}%{_libdir}/themonospot/*.dll


%files
%doc themonospot-base/readme themonospot-base/copying.gpl
%{_libdir}/themonospot/
%{_datadir}/themonospot/


%files devel
%{_libdir}/pkgconfig/* 


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.2-22
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-18
- mono rebuild for aarch64 support

* Thu Oct 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 0.8.2-17
- aarch64 bootstrap

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.2-14
- Rebuild (mono4)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 29 2011 Dan Horák <dan[at]danny.cz> - 0.8.2-7
- updated the supported arch list

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 14 2010 Armando Basile <hmandevteam@gmail.com> 0.8.2-5
- removed %%{?_smp_mflags} from make command, parallel make sometimes fails

* Fri Jan 01 2010 Armando Basile <hmandevteam@gmail.com> 0.8.2-4
- changed file permissions for dll assembly after buildroot install

* Fri Jan 01 2010 Armando Basile <hmandevteam@gmail.com> 0.8.2-3
- added versioning to Obsoletes
- fixed description

* Thu Dec 31 2009 Armando Basile <hmandevteam@gmail.com> 0.8.2-2
- added mono-devel as BuildRequires (to detect mono dependency automatically)
- removed mono-core from BuildRequires and Requires
- removed pkgconfig from BuildRequires
- added themonospot to Obsoletes

* Wed Dec 30 2009 Armando Basile <hmandevteam@gmail.com> 0.8.2-1
- removed GAC use

* Mon Dec 14 2009 Armando Basile <hmandevteam@gmail.com> 0.8.1-3
- first release of new base component
