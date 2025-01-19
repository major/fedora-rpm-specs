%global	repoid		60172
%global	xyzsh_min_ver	1.5.8
%undefine	_docdir_fmt

Name:			mfiler4
Version:		1.3.1
Release:		29%{?dist}
Summary:		2 pane file manager with a embedded shell

# SPDX confirmed
License:		MIT
URL:			http://sourceforge.jp/projects/mfiler4/
Source0:		http://dl.sourceforge.jp/mfiler4/%{repoid}/%{name}-%{version}.tgz
# -Werror=format-security
Patch0:		mfiler4-1.3.1-format.patch
# -Werror=implicit-function-declaration
Patch1:		mfiler4-1.3.1-implicit-function-declaration.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	cmigemo-devel
BuildRequires:	ncurses-devel
BuildRequires:	oniguruma-devel
BuildRequires:	readline-devel
BuildRequires:	xyzsh-devel >= %{xyzsh_min_ver}
# write xyzsh dependency explicitly
Requires:		xyzsh >= %{xyzsh_min_ver}

%description
mfiler4 is a 2pane file manager with a embedded shell.

%prep
%autosetup -p1

# Kill -O3
sed -i.optflags \
	-e 's|-O3|-O2|' \
	configure

# Kill -Werror
sed -i.werror \
	-e 's|-Werror||' \
	configure Makefile.in

# Change docdir
sed -i.docdir \
	-e '/^CFLAGS=.*DATAROOTDIR=/s|doc/mfiler4/|doc/mfiler4-%{version}/|' \
	configure

# Don't strip binary
# Keep timestamp
sed -i.bak \
	-e 's|install -m |install -p -m |' \
	-e 's|install -s |install |' \
	Makefile.in

# Umm...
sed -i.inst \
	 -e 's|USAGE.ja |USAGE.ja.txt |' \
	-e 's|USAGE |USAGE.txt |' \
	Makefile.in

%build
%configure \
	--bindir=%{_libexecdir}/%{name}/ \
	--with-migemo \
	--with-system-migemodir=%{_datadir}/cmigemo/

make %{?_smp_mflags} -k \
	CC="gcc %optflags -Werror=implicit-function-declaration" \
	docdir=%{_datadir}/doc/%{name}-%{version}

%install
make install \
	DESTDIR=%{buildroot} \
	docdir=%{_datadir}/doc/%{name}-%{version}

mkdir %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
export PATH=%{_libexecdir}/%{name}:\${PATH}
exec %{_libexecdir}/%{name}/%{name} "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

%files
%doc	AUTHORS
%lang(ja)	%doc	CHANGELOG
%license	LICENSE
%doc	README
%lang(ja)	%doc	README.ja
%lang(ja)	%doc	USAGE.ja.txt
%doc	USAGE.txt

%dir	%{_sysconfdir}/%{name}
%config(noreplace)	%{_sysconfdir}/%{name}/*.xyzsh

%{_bindir}/%{name}
%dir	%{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}
%{_libexecdir}/%{name}/mattr

%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-27
- SPDX confirmation

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-22
- Fix for gcc12 -Werror=format-security -Werror=implicit-function-declaration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr  1 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-12
- Rebuild against oniguruma 6.8.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-7
- Rebuild for oniguruma 6.1.1

* Mon Jul 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-6
- Rebuild for oniguruma 6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-1
- 1.3.1

* Thu Dec 19 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0-1
- 1.3.0

* Tue Nov 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.9-1
- 1.2.9

* Wed Oct  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.8-1
- 1.2.8

* Wed Oct  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.7-1
- 1.2.7

* Wed Sep 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-1
- 1.2.6

* Sun Aug 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-1
- 1.2.4

* Tue Aug  6 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-1
- 1.2.3

* Tue Aug  6 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.2-1
- 1.2.2

* Mon Jul  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-1
- 1.2.0

* Tue Apr  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.8-1
- 1.1.8

* Mon Mar 18 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.6-1
- 1.1.6

* Sun Mar 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.5-1
- 1.1.5

* Fri Mar  8 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.4-2
- 1.1.4

* Sun Feb 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.3-1
- 1.1.3

* Thu Jan 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Fri Jan 18 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-1
- 1.1.0
- Fix typo on summary (bug 896226)

* Tue Jan  8 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.8-1
- 1.0.8

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-1
- 1.0.6

* Wed Nov 14 2012 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-1
- 1.0.4

* Sun Nov 11 2012 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3-1
- Initial packaging

