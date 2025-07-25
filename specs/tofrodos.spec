Name:           tofrodos
Version:        1.7.13
Release:        27%{?dist}
Summary:        Converts text files between MSDOS and Unix file formats
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.thefreecountry.com/tofrodos/
Source0:        http://tofrodos.sourceforge.net/download/tofrodos-%{version}.tar.gz

BuildRequires: make
BuildRequires:	gcc

%description
Tofrodos is a text file conversion utility that converts ASCII and Unicode 
UTF-8 files between the MSDOS (or Windows) format, which traditionally have 
CR/LF (carriage return/line feed) pairs as their new line delimiters, and 
the Unix format, which usually have LFs (line feeds) to terminate each line.

It is a useful utility to have around when you have to convert files between 
MSDOS (or Windows) and Unix/Linux/BSD (and her clones and variants). It comes 
standard with a number of systems and is often found on the system as "todos",
"fromdos", "dos2unix" and "unix2dos".

%prep
%setup -qn tofrodos

%build
make -C src/ TFLAG="%{optflags}" LDFLAGS="%{?__global_ldflags}" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
make -C src/ install INSTALL="install -p" BINDIR="%{buildroot}%{_bindir}" MANDIR="%{buildroot}%{_mandir}/man1/" DESTDIR=%{buildroot}

%files
%doc COPYING readme.txt tofrodos.html
%{_bindir}/fromdos
%{_bindir}/todos
%{_mandir}/man1/fromdos.1*
%{_mandir}/man1/todos.1*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.13-25
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Christian Dersch <lupinix.fedora@gmail.com> - 1.7.13-12
- BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Christopher Meng <rpm@cicku.me> - 1.7.13-2
- Correct the license.

* Mon Feb 10 2014 Christopher Meng <rpm@cicku.me> - 1.7.13-1
- Initial Package.
