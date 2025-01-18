%if 1
%global	mainver	11.0.0
%global	gitdate	20211017
%global	gitcommit	1e6a0256612c8f8b6b1d42bd75778b15c8c5ff67
%else
%endif
%global	shortcommit	%(c=%{gitcommit}; echo ${c:0:7})

%global	tarballdate	20221008
%global	tarballtime	2308

%global	toolchain	clang

Name:			clover2

# For Version, see README.md and so on
Version:		%{mainver}
Release:		10%{?dist}
Summary:		Yet another compiler language

# app-sample/	unused
# SPDX confirmed
License:		GPL-2.0-only
URL:			https://github.com/ab25cq/clover2/wiki
#Source0:		https://github.com/ab25cq/%{name}/archive/%{gitcommit}/%{name}-%{version}-git%{shortcommit}.tar.gz
Source0:		%{name}-%{tarballdate}T%{tarballtime}.tar.gz
Source1:		create-clover-git-bare-tarball.sh
# Port to pcre2 (bug 2128279)
Patch1:		clover2-11.0.0-0001-port-to-pcre2.patch

# Upstream suggests to use clang
BuildRequires:	clang
BuildRequires:	readline-devel
BuildRequires:	pcre2-devel
BuildRequires:	gc-devel

BuildRequires:	git
BuildRequires:	%{_bindir}/time
BuildRequires:	make
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}

# Currently test fails on s390x
# https://github.com/ab25cq/clover2/issues/19
#ExcludeArch:	s390x
# https://github.com/ab25cq/clover2/issues/22
#ExcludeArch:	ppc64
# Currently clang++-11 segfaults on armv7hl
ExcludeArch:	armv7hl

%description
clover2 is a Ruby-like compiler language with static type like Java.
This language consists of compilers and virtual machines like Java and C#.
In order to compile, type checking can be done at compile time. In addition,
it is designed to be able to use an easy-to-use library like Ruby.
Regular expressions, lambda, closure etc are first class objects.

%package	libs
Summary:	Library package needed for %{name}

%description	libs
This package contains libraries needed for clover2.

%package	devel
Summary:	Development files for %{name}
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -c -T -a 0
git clone ./clover2.git
cd clover2

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-owner@fedoraproject.org"

git checkout -b %{version}-fedora %{gitcommit}

cp -a [A-Z]* ..

# honor cflags, toolchain
git rm --cached configure~
git commit -m "untrack configure~" -a

sed -i.cflags configure.in configure \
	-e '\@CFLAGS=.*-DPREFIX=@s|-DPREFIX=|%build_cflags -DPREFIX=|' \
	-e 's|-O3|-O2|' \
	-e's|^CC=gcc|CC=%{toolchain}|' \
	%{nil}
# honor libdir
sed -i.lib configure.in configure -e 's|/lib |/%{_lib} |'
sed -i.lib Makefile.in -e 's|/lib$|/%{_lib}|'

git commit -m "Apply Fedora specific configuration" -a
cat %PATCH1 | git am

%build
cd clover2
# Not trying JIT yet
%configure \
	--with-interpreter \
	%{nil}
	# --with-jit

# parallel make fails
%make_build -j1

%install
cd clover2
# DESTDIR is unusual...
#%%make_install
make install \
	DESTDIR=%{buildroot}%{_prefix} \
	INSTALL="install -p" \
	%{nil}

chmod 0644 %{buildroot}%{_mandir}/man1/%{name}.1*

cd ..
# Once move documents back
rm -rf installed-doc
mv %{buildroot}%{_docdir}/%{name}/ installed-doc

%check
LANG=C.utf8 make -C clover2 test

%files
%doc	README.md
%doc	installed-doc/*

#%%{_bindir}/bclover2
%{_bindir}/cclover2
%{_bindir}/clover2
%{_bindir}/iclover2
%{_bindir}/tyclover2


%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%files	libs
%license	LICENSE
%{_libdir}/libclover2.so.1*

%files	devel
%{_libdir}/libclover2.so
%{_includedir}/clover2/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 16 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.0.0-9
- Port to pcre2 (bug 2128279)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 27 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.0.0-7
- Remove unneeded subpackge License tag

* Thu Feb 29 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.0.0-6
- SPDX migration

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct  8 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.0.0-1
- Update to 11.0.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.6-10.D20190613git6f483b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.6-9.D20190613git6f483b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.6-8.D20190613git6f483b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.6-7.D20190613git6f483b4
- Exclude armv7hl for now (for clang++-11)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.6-7.D20190613git6f483b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Jeff Law <law@redhat.com> - 10.4.6-6.D20190613git6f483b4
- Enable LTO, but not -ffat-lto-objects.  This package really should set
  %toolchain to clang, but that doesn't work yet.

* Fri Aug  7 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.4.6-5.D20190613git6f483b4
- Disable lto, clang does not support these options
- parser.c: fix memset size

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.6-4.D20190613git6f483b4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.6-3.D20190613git6f483b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.6-2.D20190613git6f483b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.4.6-1.D20190613git6f483b4
- 10.4.6

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.1-2.D20190428gitae89cda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.4.1-1.D20190428gitae89cda
- 10.4.1

* Thu Mar 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.2.3-1.D20190319git7cb24af
- 10.2.3

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 10.0.6-3.D20190122gitc392f9c
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.6-2.D20190122gitc392f9c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.0.6-0.100.D20190122gitc392f9c
- 10.0.6

* Sun Dec 30 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.9-1.D20181230gitdc70e91
- 8.2.9

* Sat Dec  8 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.1-1.D20181208gitd8b1b9a
- 8.1.1

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.5.0-2.D2018112gitb3d1611
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Mon Nov 12 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.5.0-1.D2018112gitb3d1611
- 7.5.0

* Wed Sep  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.7-1.D20180902git35da6ac
- 5.0.7

* Fri Aug 24 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.3-1.D20180822gitcfa5389
- 5.0.3

* Sun Aug 12 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.9.5-1.D20180812gitd10f7c1
- 4.9.5

* Wed Aug  1 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.7.8-1.D20180801git66fdbac
- 4.7.8

* Mon Jul 23 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.7.2-1.D20180723gita3db523
- 4.7,2

* Mon Jul 23 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.6.8-1.D20180721git97b74cd
- 4.6.8
- Once enable all architecture

* Fri Jul 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.6.6-1.D20180713gitdad0996
- 4.6.6
- Once exclude ppc64

* Tue Jun 26 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.5-1.D20180626gitbb2fd0a
- 4.2.5

* Sun Apr  1 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.6-1.D20180323git2b30ac5
- 3.7.6

* Sun Mar 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.4-1.D20180310git9f2ef3a
- 3.7.4

* Thu Mar  8 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.2-1.D20180307git35659ca
- 3.7.2

* Mon Mar  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.1-1.D20180305gitc92a713
- 3.7.1

* Sat Mar  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.0-1.D20180301git28cd615
- 3.7.0

* Tue Feb 27 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.9-1.D20180227git8f79f5e
- 3.6.9

* Sat Feb 24 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.5-1.D20180223gite605de4
- 3.6.2

* Mon Feb 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.2-1.D20180218gitc6d6092
- 3.6.2

* Sat Feb 17 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.1-1.D20180216gitb392824
- 3.6.1

* Mon Feb 12 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.8-1.20180207git0300a9e
- 3.5.8
  (Actually the previous rpm was already 3.5.8...)

* Wed Feb  7 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.7-1.20180207git0300a9e
- 3.5.7
- Enable big endians, fixed upstream

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.6-3.20180202git93d24a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.6-2.20180202git93d24a6
- Modify license tag

* Sun Feb  4 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.6-1.20180202git93d24a6
- Initial packaging

