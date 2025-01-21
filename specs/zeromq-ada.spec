%define debug_package %{nil}
%global git_commit fca30bb86f41e24d878c32ce399500f195513400
%global git_date 20200330

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:       zeromq-ada
Version:    4.1.5
Release:    15.git%{?dist}
Summary:    Ada binding for zeromq
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        http://zeromq.org
Source0:    https://github.com/persan/zeromq-Ada/archive/%{git_commit}/%{name}-%{version}.tar.gz
## Use shared libs instead static
Patch0:     %{name}-libdir.patch
## Use directories.gpr
Patch1:     %{name}-fedora.patch
BuildRequires: make
BuildRequires: fedora-gnat-project-common >= 2 zeromq-devel >= 2.1
BuildRequires: chrpath gcc-gnat gprbuild
Requires:    zeromq >= 2.1
# gcc-gnat only available on these:
ExclusiveArch: %{GPRbuild_arches}

%description
Ada bindings for zeromq

%package devel
Summary:        Devel package for Ada binding for zeromq
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Requires:       fedora-gnat-project-common  >= 2
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zeromq-devel >= 2.1

%description devel
%{summary}
%prep
%setup -q -n zeromq-Ada-%{git_commit}
%patch -P0 -p1
%patch -P1 -p1
touch Makefile.config
cp -v libsodium.gpr.in libsodium.gpr
cp -v libzmq.gpr.in libzmq.gpr

%build
make %{?_smp_mflags}  GNATFLAGS="%{GNAT_optflags}"  GNATMAKE="gprbuild -p -R %{GNAT_optflags}" PREFIX=/usr
## for tests aunit needed


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} ADA_PROJECT_DIR=%{_GNAT_project_dir}  GNATFLAGS="%{GNAT_optflags}" PREFIX=/usr
rm -f %{buildroot}/%{_libdir}/zmq/static/libzmqAda.a
rm -rf %{buildroot}/%{_libdir}/zmq/static
chrpath --delete %{buildroot}%{_libdir}/zmq/relocatable/libzmqAda.so.%{version}

%ldconfig_scriptlets

%files
%doc README.md COPYING
%dir %{_libdir}/zmq
%dir %{_libdir}/zmq/relocatable
%{_libdir}/zmq/relocatable/libzmqAda.so.%{version}
%{_libdir}/libzmqAda.so.*


%files devel
%{_libdir}/zmq/relocatable/libzmqAda.so
%{_libdir}/libzmqAda.so
%dir %{_includedir}/zmq/
%{_includedir}/zmq/*.adb
%{_includedir}/zmq/*.ads
%{_GNAT_project_dir}/zmq.gpr
%{_libdir}/zmq/relocatable/*.ali
%{_datadir}/zmq/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-15.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.5-14.git
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-13.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-12.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 4.1.5-11.git
- rebuild for new libsodium

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-10.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-9.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-8.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-7.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-6.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Max Reznik <reznikmm@gmail.com> - 4.1.5-5.git
- rebuilt with gcc-11.1.1-1

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-4.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  9 2020 Pavel Zhukov <pzhukov@redhat.com> - 4.1.5-3.git
- Rebuild with new libgnat

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Max Reznik <reznikmm@gmail.com> - 4.1.5-1.git
- Update to 4.1.5

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-30.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-29.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-28.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-27.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Pavel Zhukov <landgraf@fedoraproject.org - 2.1.0-26.24032011git
- rebuilt with new gnat
- Use gprbuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-23.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-22.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 2.1.0-21.24032011git
- Rebuilt for libgnat soname bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-20.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.1.0-19.24032011git
- rebuilt for new zeromq 4.1.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-18.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.0-17.24032011git
- Rebuilt for new libgnat

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-16.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-15.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-14.24032011git
- Use GNAT_arches rather than an explicit list

* Sun Apr 20 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-13.24032011git
- Rebuild with new GCC 

* Sun Mar 02 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-12.24032011git
- Fix library finalization. https://github.com/persan/zeromq-Ada/issues/10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-11.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Kevin Fenzi <kevin@scrye.com> 2.1.0-10.24032011git
- Rebuild for new libgnat
- Add buildrequires on gcc-gnat. It's no longer pulled in by fedora-gnat-project-common

* Sun Sep 23 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-9.24032011git
- Fix gpr path

* Sun Sep 23 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-8.24032011git
- Fix libraries symlinks
- Add usrmove patch

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-7.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 05 2011 Dan Horák <dan[at]danny.cz> - 2.1.0-6.24032011git
- updated the supported arch list

* Fri Apr 29 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-4.24032011git
- Create shared libraries path
- Fix license tag
- Fix spec errors

* Thu Mar 24 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-1.24032011git
- update to new commit

* Wed Feb 2 2011 Pavel Zhukov <pavel@zhukoff.net> - 2.0.10-02022011git
- Initial package
