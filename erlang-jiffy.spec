%global realname jiffy

Name:           erlang-%{realname}
Version:        1.1.1
Release:        4%{?dist}
Summary:        Erlang JSON parser
License:        MIT and BSD
URL:            https://github.com/davisp/%{realname}
Source0:	https://github.com/davisp/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# Use double conversion from the system instead of the bundled one
Patch1:         erlang-jiffy-0001-Use-system-double-conversion.patch
BuildRequires:  erlang-rebar
BuildRequires:  gcc-c++
BuildRequires:  double-conversion-devel
Provides:       %{realname} = %{version}
Obsoletes:      %{realname} < %{version}


%description
A JSON parser for Erlang implemented as a NIF.


%prep
%autosetup -p 1 -n %{realname}-%{version}
# Use double conversion from the system instead of the bundled one
rm -r c_src/double-conversion


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%{erlang_appdir}/
%doc README.md
%license LICENSE

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct  4 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-1
- Ver. 1.1.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5 (#1798831).

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.1-2
- Bring jiffy back to s390x (#1772954).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1.
- Add an exclusion on the s390 architecture (see rhbz#1770256).

* Sun Sep 22 2019 Orion Poplawski <orion@nwra.com> - 0.15.2-3
- Rebuild for double-conversion 3.1.5

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.15.2-1
- Ver. 0.15.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.15.0-5
- Rebuild for Erlang 20 (with proper builddeps)

* Fri Feb 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.15.0-4
- Rebuild for Erlang 20

* Thu Feb 22 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.15.0-3
- Rebuild for Erlang 20.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.15.0-1
- Ver. 0.15.0

* Wed Nov 15 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.14.13-1
- Ver. 0.14.13

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.14.8-3
- Rebuild for newer erlang-nif

* Fri Apr 22 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.14.8-2
- Spec-file cleanup

* Wed Apr 6 2016 Filip Andres <filip@andresovi.net> - 0.14.8-1
- Update to version 0.14.8

* Wed Feb 10 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.14.5-4
- Add check stanza back

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Filip Andres <filip@andresovi.net> - 0.14.5-2
- Remove check stanza until #1240487 is resolved

* Sun Dec 27 2015 Filip Andres <filip@andresovi.net> - 0.14.5-1
- Update to version 0.14.5

* Mon Jun 29 2015 Filip Andres <filip@andresovi.net> - 0.13.1-1
- Update to version 0.13.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.5-8
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.8.5-6
- Use new erlang macros to build with $RPM_OPT/LD_FLAGS etc, verbosely
- Run unit tests during build

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.8.5-4
- Use system double-conversion instead of bundled one

* Wed Mar 12 2014 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.8.5-3
- Fix version number in version patch

* Wed Mar 12 2014 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.8.5-2
- Bring back Filip's version patch
- Rename to erlang-jiffy
- Adjust c++ requirement, as suggested by sir Andres

* Tue Mar 11 2014 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.8.5-1
- New version
- Remove the plt file
- Remove empty scriptlets
- Use correct compiler flags
- Remove artifacts not used by modern RPM
- Own the module directory
- Do not use bundled rebar
- No need for explicit GCC dependency
- Relax dependency on complete Erlang distribution
- Remove deproper patch
- Add documentation
- Fix library file mode

* Thu Jul 18 2013 Filip Andres <filip.andres@gooddata.com> - 0.8.3-1.gdc2
* Correcting the version inside jiffy.app and including jiffy_utf8

* Fri May 17 2013 Filip Andres <filip.andres@gooddata.com> - 0.8.3-1.gdc1
* Updating to 0.8.3

* Thu Jan 03 2013 Filip Andres <filip.andres@gooddata.com> - 0.6.1-1.gdc3
- Packaging the plt file with the rest of jiffy

* Wed Jan 02 2013 Filip Andres <filip.andres@gooddata.com> - 0.6.1-1.gdc2
- Building plt

* Mon Dec 10 2012 Filip Andres <filip.andres@gooddata.com> - 0.6.1-1.gdc1
- Imported version 0.6.1

* Mon Apr 16 2012 Filip Andres <filip.andres@gooddata.com> - 0.4.1
- Initial packaging
