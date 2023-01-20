%undefine _hardened_build

Name:       aunit
Version:    2020
Release:    7%{?dist}
Summary:    Unit test framework for Ada
License:    GPLv2+
URL:        http://libre.adacore.com/libre/tools/aunit
## No direct download link
Source0:    aunit-2020-20200429-19B6C-src.tar.gz
Patch0:     %{name}-2020-gprdir.patch
Patch1:     %{name}-2020-disable_static.patch


BuildRequires: fedora-gnat-project-common >= 2     
BuildRequires:  chrpath gprbuild gcc-gnat
BuildRequires: make

Requires:    fedora-gnat-project-common >= 2

# gprbuild only available on these:
ExclusiveArch:  %GPRbuild_arches

%description
%{summary}

%package devel
Summary:    Devel package for aunit
License:    GPLv2+
Requires: fedora-gnat-project-common >= 2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel 
%{summary}

%prep
%setup -q -n aunit-2020-20200429-19B6C-src
%patch0 -p1
%patch1 -p1

%build
## Doen't compile without this options
make %{?_smp_mflags} GPROPTS="%GPRbuild_optflags"


%install
rm -rf %{buildroot}
export GPRINSTALL_OPTS="--build-name=relocatable --lib-subdir=%{buildroot}/%{_libdir}/%{name} --link-lib-subdir=%{buildroot}/%{_libdir} --prefix=%{buildroot} \
--sources-subdir=%{buildroot}/%{_includedir}/%{name} --project-subdir=%{buildroot}%{_GNAT_project_dir}"
make install DESTDIR="%{buildroot}" GPROPTS="${GPRINSTALL_OPTS}" INSTALL="%{buildroot}" 
## There is no gps in fedora
rm -rf %{buildroot}/%{_datadir}/gps/
##chrpath --delete %{buildroot}/%{_libdir}/%{name}/libaunit.so.%{version}

%ldconfig_scriptlets

%files
%doc COPYING* README
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_docdir}/%{name}
%{_libdir}/%{name}/lib%{name}.so
%{_libdir}/lib%{name}.so
%{_libdir}/%{name}/%{name}*
%{_libdir}/%{name}/ada_containers*
%{_includedir}/%{name}
%{_GNAT_project_dir}/*.gpr
%{_GNAT_project_dir}/manifests/%{name}



%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Pavel Zhukov <pzhukov@redhat.com> - 2020-2
- Rebuild with new gnat

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org - 2017-5
- rebuilt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 16 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-2
- Limit to grpbuild arches

* Fri Jul  7 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-1
- New release v2017

* Mon Feb 13 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2015-5
- Remove unused link

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015  Pavel Zhukov <landgraf@fedoraproject.org> - 2015-2
- Build on arm

* Thu Jun 25 2015  Pavel Zhukov <landgraf@fedoraproject.org> - 2015-1
- New release (#2015)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-8
- Rebuild with new gnat 

* Sat Oct 11 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-7
- Exclude arm

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2013-4
- Use GNAT_arches rather than an explicit list

* Wed May  7 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-3
- Rebuild with new libgnat

* Sun Feb 16 2014  Pavel Zhukov <landgraf@fedoraproject.org> - 2013-2
- New release (2014)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Kevin Fenzi <kevin@scrye.com> 2012-3
- Rebuild for new libgnat

* Tue Dec 18 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2012-1
- New release 2012
- Add gcc-gnat to BR

* Sun Mar 04 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-1
- Update to 2011

* Fri Jun 03 2011 Dan Horák <dan[at]danny.cz> - 2010-3
- updated the supported arch list

* Sat Apr 30 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2010-2
- Remove vendor optflags

* Mon Mar 28 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2010-1
%{GNAT_arches}- Initial build
