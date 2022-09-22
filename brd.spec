%global	commit f984731d36aef24e630ead0e3818efd3b0b99f07
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		brd
Version:	1.0
Release:	23%{?dist}
Summary:	Scans directories and files for damage due to decay of storage medium

License:	GPLv2+
URL:		https://github.com/jsbackus/brd
Source0:	https://github.com/jsbackus/brd/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:	python3-devel
BuildArch:	noarch

Patch0: 000-fix-deprecation-warnings.patch
Patch1: 001-os-errno.patch

%description
bit_rot_detector, or brd, is a tool to scan a directory tree and check each file
for corruption caused by damage to the physical storage medium or by damage from
malicious programs. Files are fingerprinted using the SHA-1 algorithm. File
fingerprints, sizes, and modification times are stored in a SQLite database.

%prep
%setup -qn %{name}-%{commit}
%patch0 -p1
%patch1 -p1

%build
%{__python3} setup.py build

%check
cd unit_tests
%{__python3} -m unittest

%install
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT

# Move docs to appropriate place for versions prior to Fedora 20.
%if 0%{?fedora} < 20
mv %{buildroot}/%{_datadir}/doc/%{name} %{buildroot}/%{_pkgdocdir}
%endif

%files
%doc LICENSE README
%{_bindir}/brd
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{name}*.egg-info


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0-22
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0-19
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-16
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-14
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-10
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-6
- Rebuild for Python 3.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 01 2014 Jeff Backus <jeff.backus@gmail.com> - 1.0-2
- Modified to properly install docs on F19 and earlier.

* Sun Jun 15 2014 Jeff Backus <jeff.backus@gmail.com> - 1.0-1
- Initial package
