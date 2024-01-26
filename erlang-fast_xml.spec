%global srcname fast_xml

%global p1_utils_ver 1.0.20

Name: erlang-%{srcname}
Version: 1.1.49
Release: 5%{?dist}
License: ASL 2.0
Summary: Fast Expat based Erlang XML parsing and manipulation library
URL:     https://github.com/processone/fast_xml/
Source0: https://github.com/processone/fast_xml/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1:  erlang-fast_xml-0001-Disable-port-compiler-until-we-package-it.patch
Provides:  erlang-p1_xml = %{version}-%{release}
Obsoletes: erlang-p1_xml < 1.1.11
BuildRequires: gcc
BuildRequires: erlang-edoc
BuildRequires: erlang-rebar3
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: expat-devel


%description
Fast Expat based Erlang XML parsing and manipulation library, with a strong
focus on XML stream parsing from network. It supports full XML structure
parsing, suitable for small but complete XML chunks, and XML stream parsing
suitable for large XML document, or infinite network XML stream like XMPP.
This module can parse files much faster than built-in module xmerl. Depending
on file complexity and size xml_stream:parse_element/1 can be 8-18 times faster
than calling xmerl_scan:string/2.


%prep
%autosetup -n fast_xml-%{version}


%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/lib
gcc  c_src/fxml.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/fxml.o
gcc c_src/fxml_stream.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/fxml_stream.o
gcc c_src/fxml.o	$LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lexpat -lm -o priv/lib/fxml.so
gcc c_src/fxml_stream.o	$LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lexpat -lm -o priv/lib/fxml_stream.so


%install
%{erlang3_install}

install -p -D -m 755 priv/lib/* --target-directory=$RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/


%check
%{erlang3_test}


%files
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{erlang_appdir}


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.1.49-1
- Rebuild for Erlang 25
- Ver. 1.1.49

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.43-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 12 2021 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.43-2
- Rebuild for FTI (#1946471).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.43-1
- Update to 1.1.43 (#1807287).
- https://github.com/processone/fast_xml/blob/1.1.43/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.38-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.38-1
- Update to 1.1.38 (#1789168).
- https://github.com/processone/fast_xml/blob/1.1.38/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.37-2
- Bring fast_xml back to s390x (#1772968).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.37-1
- Update to 1.1.37 (#1742456).
- https://github.com/processone/fast_xml/blob/1.1.37/CHANGELOG.md
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.36-1
- Update to 1.1.36 (#1713300).
- https://github.com/processone/fast_xml/blob/1.1.36/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.35-1
- Update to 1.1.35 (#1683115).
- https://github.com/processone/fast_xml/blob/1.1.35/CHANGELOG.md

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.1.34-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
