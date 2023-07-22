Summary: A library for accessing deltacloud
Name: libdeltacloud
Version: 0.9
Release: 29%{?dist}
License: LGPLv2+
URL: https://git.fedorahosted.org/git/deltacloud/libdeltacloud.git
Source0: https://git.fedorahosted.org/cgit/deltacloud.git/libdeltacloud.git/snapshot/%{name}-%{version}.tar.gz
Patch0: libdeltacloud-configure-ac-update.patch
Patch1: libdeltacloud-update-fsf-address.patch
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: libtool
BuildRequires: make

%description
Libdeltacloud is a library for accessing deltacloud via a
convenient C API.

%package devel
Summary: Header files for libdeltacloud library
License: LGPLv2+
Requires: %{name} = %{version}-%{release}

%description devel
The libdeltacloud-devel package contains the files needed for developing
applications that need to use the libdeltacloud library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# to support aarch64
libtoolize --force
aclocal
autoheader
autoconf
automake --add-missing
%configure --libdir=/%{_lib}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="${RPM_BUILD_ROOT}" install

# Move the symlink
rm -f $RPM_BUILD_ROOT/%{_lib}/%{name}.so
mkdir -p $RPM_BUILD_ROOT%{_libdir}
VLIBNAME=$(ls $RPM_BUILD_ROOT/%{_lib}/%{name}.so.*.*.*)
LIBNAME=$(basename $VLIBNAME)
ln -s ../../%{_lib}/$LIBNAME $RPM_BUILD_ROOT%{_libdir}/%{name}.so

# Move the pkgconfig file
mv $RPM_BUILD_ROOT/%{_lib}/pkgconfig $RPM_BUILD_ROOT%{_libdir}

# Remove a couple things so they don't get picked up
rm -f $RPM_BUILD_ROOT/%{_lib}/libdeltacloud.la
rm -f $RPM_BUILD_ROOT/%{_lib}/libdeltacloud.a

%ldconfig_scriptlets


%files
%doc COPYING
%attr(0755,root,root) /%{_lib}/libdeltacloud.so.*

%files devel
%attr(0644,root,root) %{_includedir}/libdeltacloud/action.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/address.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/bucket.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/driver.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/hardware_profile.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/image.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/instance.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/instance_state.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/key.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/libdeltacloud.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/link.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/loadbalancer.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/realm.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/storage_snapshot.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/storage_volume.h
%attr(0755,root,root) %{_libdir}/libdeltacloud.so
%{_libdir}/pkgconfig/libdeltacloud.pc

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Chris Lalancette <clalancette@gmail.com> - 0.9-14
- Do it for real this time

* Thu Feb 04 2016 Chris Lalancette <clalancette@gmail.com> - 0.9-13
- Update the FSF address in the COPYING file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Chris Lalancette <clalancette@gmail.com> - 0.9-7
- Update URL to get rid of now defunct people.redhat.com page

* Tue Jul 09 2013 Chris Lalancette <clalancette@gmail.com> - 0.9-6
- Update Source0 to get rid of now defunct people.redhat.com page

* Tue Apr 02 2013 Chris Lalancette <clalancette@gmail.com> - 0.9-5
- Run autoreconf in prep to handle aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 06 2011 Chris Lalancette <clalance@redhat.com> - 0.9-1
- Update to latest upstream (0.9)

* Mon Apr 18 2011 Chris Lalancette <clalance@redhat.com> - 0.8-1
- Update to latest upstream (0.8)

* Wed Mar 16 2011 Chris Lalancette <clalance@redhat.com> - 0.7-1
- Update to latest upstream (0.7)

* Thu Jul 08 2010 Chris Lalancette <clalance@redhat.com> - 0.3-1
- Bump version for API breakage (replace - with _, move id to parent XML)
- Rename the library from dcloudapi to libdeltacloud

* Fri Apr 23 2010 Chris Lalancette <clalance@redhat.com> - 0.2-1
- Bump version for new API (removed flavors, added hardware profiles)

* Mon Mar 08 2010 Chris Lalancette <clalance@redhat.com> - 0.1-1
- Initial build.

