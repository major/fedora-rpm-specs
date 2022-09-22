Name:           elementary
Version:        1.17.1
Release:        3%{?dist}
Summary:        Basic widget set that is easy to use based on EFL
License:        LGPLv2+
URL:            http://www.enlightenment.org
Source0:        http://download.enlightenment.org/rel/libs/elementary/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: efl-devel >= %{version}
BuildRequires: gettext
BuildRequires: make

%description
Elementary is a widget set. It is a new-style of widget set much more canvas
object based than anything else.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Development files for elementary

%description devel
Development files for elementary.

%prep
%setup -q

%build
%configure --disable-rpath --disable-doc --disable-static --disable-elementary-test
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
find %{buildroot} -name 'elementary_testql.so' -delete
find %{buildroot} -name 'elementary_test.desktop' -delete
find %{buildroot} -name 'elementary_testql' -delete

desktop-file-install                                                                    \
        --delete-original                                                               \
        --dir=%{buildroot}%{_datadir}/applications                                      \
%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}

%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons &>/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons &>/dev/null || :

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/elementary_codegen
%{_bindir}/elementary_config
%{_bindir}/elementary_quicklaunch
%{_bindir}/elementary_run
%{_bindir}/elm_prefs_cc
%{_libdir}/libelementary.so.1
%{_libdir}/libelementary.so.%{version}
%{_datadir}/applications/elementary_config.desktop
%{_datadir}/elementary
%{_datadir}/icons/elementary.png
%{_libdir}/edje/modules/elm
%{_libdir}/elementary
%{_datadir}/eolian/include/elementary-1/

%files devel
%{_includedir}/elementary-1
%{_includedir}/elementary-cxx-1/
%{_libdir}/libelementary.so
%{_libdir}/pkgconfig/elementary.pc
%{_libdir}/pkgconfig/elementary-cxx.pc
%{_libdir}/cmake/Elementary/

%changelog
* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 15 2016 Ding-Yi Chen <dchen@redhat.com> - 1.17.1-2
- Rebuild for efl-1.17.2

* Tue Jun 14 2016 Tom Callaway <spot@fedoraproject.org> - 1.17.1-1
- update to 1.17.1

* Mon May 23 2016 Ding-Yi Chen <dchen@redhat.com> - 1.17.0-2
- Rebuild for latest libinput

* Wed Feb  3 2016 Tom Callaway <spot@fedoraproject.org> - 1.17.0-1
- update to 1.17.0

* Mon Jan 11 2016 Ding-Yi Chen <dchen@redhat.com> - 1.16.1-1
- update to 1.16.1
- Remove rpath

* Tue Nov 10 2015 Tom Callaway <spot@fedoraproject.org> - 1.16.0-1
- update to 1.16.0

* Fri Aug 28 2015 Tom Callaway <spot@fedoraproject.org> - 1.15.1-1
- update to 1.15.1

* Mon Aug 10 2015 Tom Callaway <spot@fedoraproject.org> - 1.15.0-1
- update to 1.15.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun  3 2015 Tom Callaway <spot@fedoraproject.org> - 1.14.1-1
- update to 1.14.1

* Thu May 28 2015 Tom Callaway <spot@fedoraproject.org> - 1.14.0-1
- update to 1.14.0

* Mon Apr  6 2015 Tom Callaway <spot@fedoraproject.org> - 1.13.2-1
- update to 1.13.2

* Thu Apr  2 2015 Tom Callaway <spot@fedoraproject.org> - 1.13.1-1
- update to 1.13.1

* Thu Dec 18 2014 Tom Callaway <spot@fedoraproject.org> - 1.12.2-1
- update to 1.12.2

* Thu Oct 23 2014 Tom Callaway <spot@fedoraproject.org> - 1.7.10-1
- update to 1.7.10

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 07 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.7.9-1
- Update to 1.7.9

* Mon Oct 07 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.7.8-5
- Add ethumb support and others.

* Fri Sep 27 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.7.8-4
- Fix licensing
- Add icon scriptlets
- Remove elementary_test desktop and binary files
- Fix directory ownership
- Fix unused direct shlib dependency

* Thu Sep 26 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.7.8-3
- Fix build errors

* Tue Sep 24 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.7.8-2
- Remove useless shared object.

* Fri Sep 06 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.7.8-1
- Update to 1.7.8
- Pretty up spec file.

* Wed Jan 02 2013 Rahul Sundaram <sundaram@fedoraproject.org> 1.7.4-1
- Initial spec
