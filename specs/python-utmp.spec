Name:		python-utmp
Version:	0.8.2
Release:	28%{?dist}
Summary:	Python modules for umtp records

License:	LicenseRef-Fedora-UltraPermissive
URL:		http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/
Source0:	http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/%{name}_%{version}.tar.gz

# Need to change the name of the shared library we create, so it is the same as the name
# of the module we import, or else Python will not be able to import it.
# And use the correct include paths.
Patch0:         patch-make.diff

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  pkgconf

%global _description %{expand:
python-utmp consists of three modules, providing access to utmp records.
It is quite difficult to access utmp record portably, because every UNIX
has different structure of utmp files. Currently, python-utmp works on
platforms which provide getutent, getutid, getutline, pututline,
setutent, endutent and utmpname functions (such as GNU systems
(Linux and hurd) and System V unices) and on BSD systems using
simple utmp structure.}

%description %_description

%package -n python3-utmp
Summary:        Python modules for umtp records
BuildRequires:	python3-devel
%{?python_provide:%python_provide python3-utmp}

%description -n python3-utmp %_description

%prep
%autosetup -n %{name} -p1


%build
%set_build_flags
make -f Makefile.glibc \
	DEFINES=" \
		-D_HAVE_UT_SESSION -D_HAVE_UT_ADDR_V6 -D_HAVE_UT_EXIT \
		-D_HAVE_UT_HOST -D_HAVE_UT_ID -D_HAVE_UT_TV -D_HAVE_UT_USER \
		-D_HAVE_UTMPNAME -D_HAVE_SETUTENT -D_HAVE_GETUTENT -D_HAVE_ENDUTENT \
		-D_HAVE_GETUTID -D_HAVE_GETUTLINE -D_HAVE_PUTUTLINE \
		%{optflags}" \
	PYTHONPKGVER=3 \
	PYTHONVER=%{python3_version} \
	PYTHONINCLUDE=/usr/include/python%{python3_version}/

%install
make \
	PYTHONDIR=%{buildroot}/%{python3_sitearch}/ \
	PYTHONVER=%{python3_version} \
	install
rm -f COPYING
install -D -p -m644 debian/copyright COPYING

%files -n python3-utmp
%license COPYING
%doc README TODO
%{python3_sitearch}/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.2-26
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.2-22
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.2-19
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.2-16
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-11
- Subpackage python2-utmp has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Oct 18 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.2-10
- Fix build (#1716538)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Charalampos Statakis <cstratak@redhat.com> - 0.8.2-1
- Update to 0.8.2
- Provide a Python 3 subpackage

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-15
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 28 2009 Juha Tuomala <tuju@iki.fi> - 0.7-5
- Minor spec imrovements.

* Tue Jul 21 2009 Juha Tuomala <tuju@iki.fi> - 0.7-4
- Minor spec imrovements.

* Sun Jul 05 2009 Juha Tuomala <tuju@iki.fi> - 0.7-3
- License string fix.

* Sun Jul 05 2009 Juha Tuomala <tuju@iki.fi> - 0.7-2
- Spec modifications, bug #505259.

* Thu Jun 11 2009 Juha Tuomala <tuju@iki.fi> - 0.7-1
- Initial package.
