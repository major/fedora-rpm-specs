Name:           babeltrace
Version:        1.5.11
Release:        12%{?dist}
Summary:        Trace Viewer and Converter, mainly for the Common Trace Format
License:        MIT AND GPL-3.0-or-later WITH Bison-exception-2.2 AND LGPL-2.1-only AND BSD-4-Clause-UC
URL:            https://www.efficios.com/babeltrace
Source0:        https://www.efficios.com/files/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://www.efficios.com/files/%{name}/%{name}-%{version}.tar.bz2.asc
# gpg2 --export --export-options export-minimal 7F49314A26E0DE78427680E05F1B2A0789F12B11 > gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Source2:        gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Patch0:         babeltrace-getaddrinfo.patch

BuildRequires:  bison >= 2.4
BuildRequires:  flex >= 2.5.35
BuildRequires:  glib2-devel >= 2.22.0
BuildRequires:  libuuid-devel
BuildRequires:  popt-devel >= 1.13
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig >= 2.0
BuildRequires:  elfutils-devel >= 0.154
BuildRequires:  autoconf automake libtool
BuildRequires:  gnupg2
BuildRequires:  make

Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.

The main format expected to be converted to/from is the Common Trace
Format (CTF). See http://www.efficios.com/ctf.


%package -n lib%{name}
Summary:        Common Trace Format Babel Tower

%description -n lib%{name}
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.


%package -n lib%{name}-devel
Summary:        Common Trace Format Babel Tower
Requires:       lib%{name}%{?_isa} = %{version}-%{release} glib2-devel

%description -n lib%{name}-devel
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.


%package -n python3-%{name}
Summary:        Common Trace Format Babel Tower
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
# Reinitialize libtool with the fedora version to remove Rpath
autoreconf -vif

export PYTHON=%{__python3}
export PYTHON_CONFIG=%{__python3}-config
%configure --disable-static --enable-python-bindings

make %{?_smp_mflags} V=1

%check
make check

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete
# Clean installed doc
rm -f %{buildroot}/%{_pkgdocdir}/API.txt
rm -f %{buildroot}/%{_pkgdocdir}/LICENSE
rm -f %{buildroot}/%{_pkgdocdir}/gpl-2.0.txt
rm -f %{buildroot}/%{_pkgdocdir}/mit-license.txt
rm -f %{buildroot}/%{_pkgdocdir}/std-ext-lib.txt

%ldconfig_scriptlets  -n lib%{name}

%files
%doc ChangeLog
%doc doc/lttng-live.txt
%{_bindir}/%{name}*
%{_mandir}/man1/*.1*

%files -n lib%{name}
%doc doc/API.txt
%doc std-ext-lib.txt
%{!?_licensedir:%global license %%doc}
%license LICENSE gpl-2.0.txt mit-license.txt
%{_libdir}/*.so.*

%files -n lib%{name}-devel
%{_prefix}/include/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/babeltrace.pc
%{_libdir}/pkgconfig/babeltrace-ctf.pc

%files -n python3-%{name}
%{python3_sitearch}/babeltrace
%{python3_sitearch}/babeltrace*.egg-info


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 1.5.11-11
- Rebuilt for Python 3.14

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.11-8
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5.11-4
- Rebuilt for Python 3.12

* Mon May 30 2023 Keith Seitz <keiths@redhat.com>
- Update license expression.

* Mon May 08 2023 Michael Jeanson <mjeanson@efficios.com> - 1.5.11-3
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 02 2022 Michael Jeanson <mjeanson@efficios.com> - 1.5.11-1
- New upstream release
- Drop patches merged upstream
- Add builddep on python3-setuptools for Python 3.12+

* Fri Sep 16 2022 Keith Seitz - 1.5.8-13
- Add use-after-free patch for popt-1.19 update.
  (Keith Seitz, RHBZ 2126067)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.8-11
- Rebuilt for Python 3.11

* Wed Mar 16 2022 Keith Seitz <keiths@redhat.com> - 1.5.8-10
- Use getaddrinfo instead of gethostbyname.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.8-7
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Keith Seitz <keiths@redhat.com> - 1.5.8-5
- Remove workaround for 1890813 now that binutils is fixed.

* Mon Oct 26 2020 Keith Seitz <keiths@redhat.com> - 1.5.8-4
- Workaround __openat_missing_mode compiler error.
  (Keith Seitz, RH BZ 1890813)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.8-2
- Rebuilt for Python 3.9

* Wed Feb 12 2020 Michael Jeanson <mjeanson@efficios.com> - 1.5.8-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Michael Jeanson <mjeanson@efficios.com> - 1.5.7-5
- Add Python 3.9 patch

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.7-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Michael Jeanson <mjeanson@efficios.com> - 1.5.7-2
- Add GPG source file verification

* Wed Jul 24 2019 Michael Jeanson <mjeanson@efficios.com> - 1.5.7-1
- New upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Michael Jeanson <mjeanson@efficios.com> - 1.5.6-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.5-2
- Rebuilt for Python 3.7

* Tue Mar 27 2018 Michael Jeanson <mjeanson@efficios.com> - 1.5.5-1
- New upstream release

* Fri Feb 16 2018 2018 Lumír Balhar <lbalhar@redhat.com> - 1.5.4-2
- Fix directory ownership in python3 subpackage

* Tue Feb 13 2018 Michael Jeanson <mjeanson@efficios.com> - 1.5.4-1
- New upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Michael Jeanson <mjeanson@efficios.com> - 1.5.3-1
- New upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Michael Jeanson <mjeanson@efficios.com> - 1.5.2-2
- Revert python3 macro changes

* Wed Mar 01 2017 Michael Jeanson <mjeanson@efficios.com> - 1.5.2-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Michael Jeanson <mjeanson@efficios.com> - 1.5.1-1
- New upstream release

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuild for Python 3.6

* Wed Nov 30 2016 Michael Jeanson <mjeanson@efficios.com> - 1.5.0-1
- New upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 22 2016 Michael Jeanson <mjeanson@efficios.com> - 1.4.0-2
- Re-add rpath removing

* Tue Jun 21 2016 Michael Jeanson <mjeanson@efficios.com> - 1.4.0-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jul 28 2015 Michael Jeanson <mjeanson@gmail.com> - 1.2.4-2
- Added python3 bindings module

* Sun Jul 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.4.1
- Update to 1.2.4

* Sun Jul 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.1-5
- Fix FTBFS, use %%license

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.2.1-1
- New upstream release

* Sat Mar 01 2014 Suchakra Sharma <suchakra@fedoraproject.org> - 1.2.0-1
- New upstream release
- Popt patch for babeltrace.pc.in removed. Its fixed in Fedora now
- Add new file (babeltrace-ctf.pc)

* Mon Aug 05 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.1.1-3
- Remove reference to versionned docdir (#992011)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.1.1-1
- New upstream bugfix release

* Tue May 28 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.1.0-1
- New upstream release
- Patch babeltrace.pc to not depends on popt.pc, as it does not exist in Fedora

* Tue Feb 26 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.3-1
- New upstream release
- Add pkg-config file to devel package (#913895)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.2-1
- New upstream release

* Tue Jan 15 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.0-3
- Change documentation directory to proper versionned one. 

* Mon Jan 14 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.0-2
- Use autoreconf rpath fix because the sed one was breaking the make check
- Use correct tar file version
- Package documentations in the right packages

* Mon Oct 29 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.0-1
- New upstream release

* Tue Oct 02 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.0-0.1.rc5
- New upstream release candidate
* Thu Jul 05 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.0-0.1.rc4
- New package, inspired by the one from OpenSuse 

