Name:		owl-lisp
Version:	0.1.21
Release:	7%{?dist}
Summary:	Owl Lisp is a purely functional dialect of Scheme
License:	MIT 
URL:		https://gitlab.com/owl-lisp/owl/
source0:	https://gitlab.com/owl-lisp/owl/-/archive/v%{version}/owl-v%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	make

%description
Owl Lisp is a purely functional dialect of Scheme. 
It is based on the applicable subset of to-be R7RS Scheme standard, 
with some extensions useful for mutation free operation.

%prep
%autosetup -n owl-v%{version}

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}
chmod 644 c/ol.c

%install
%make_install


%files
%doc README.md LICENCE
%{_bindir}/ol
%{_bindir}/ovm
%{_mandir}/man1/ol.1.gz
%{_mandir}/man1/ovm.1.gz

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.21-2
- Explicitly list shipped files

* Tue May 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.21-1
- Update to 0.1.21
- Update URLs

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Niranjan MR <mrniranjan@fedoraproject.org> - 0.1.12-1
- Update owl-lisp to v0.1.12

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 16 2014 Niranjan MR <mrniranjan@fedoraproject.org> - 0.1.7-2
- Add man page for ovm

* Mon Dec 15 2014 Niranjan MR <mrniranjan@fedoraproject.org> - 0.1.7-1
- initial version 
