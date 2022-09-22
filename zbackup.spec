%undefine __cmake_in_source_build

Name:		zbackup
Version:	1.4.4
Release:	29%{?dist}
Summary:	A versatile deduplicating backup tool

License:	GPLv2+ with exceptions
URL:		http://zbackup.org/
Source0:	https://github.com/zbackup/zbackup/archive/%{version}.tar.gz
Patch0:		https://patch-diff.githubusercontent.com/raw/zbackup/zbackup/pull/159.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake >= 2.8.2
BuildRequires:	xz-devel
BuildRequires:	openssl-devel
BuildRequires:	protobuf-devel
BuildRequires:	zlib-devel
BuildRequires:	lzo-devel
BuildRequires:	pandoc

%description
zbackup is a globally-deduplicating backup tool, based on the ideas
found in rsync. Feed a large .tar into it, and it will store duplicate
regions of it only once, then compress and optionally encrypt the
result. Feed another .tar file, and it will also re-use any data found
in any previous backups. This way only new changes are stored, and as
long as the files are not very different, the amount of storage
required is very low.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%cmake
%cmake_build
cd tartool
%cmake
%cmake_build
cd -

%install
%cmake_install
install -Dpm0755 tartool/%{_vpath_builddir}/tartool %{buildroot}%{_bindir}/
grep -v travis README.md | pandoc -s -f markdown_github -t man -o %{name}.1 \
-V title=%{name} -V section=1 -V date="$(LANG=C date -d @$(stat -c'%Z' README.md) +'%B %d, %Y')"
install -D -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
ln -s %{name}.1 %{buildroot}%{_mandir}/man1/tartool.1

%files
%license LICENSE LICENSE-GPL*
%doc CONTRIBUTORS
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 1.4.4-27
- Rebuilt for protobuf 3.19.0

* Sat Oct 23 2021 Adrian Reber <adrian@lisas.de> - 1.4.4-26
- Rebuilt for protobuf 3.18.1

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.4.4-25
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 14:44:23 CET 2021 Adrian Reber <adrian@lisas.de> - 1.4.4-22
- Rebuilt for protobuf 3.14

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.4.4-21
- Rebuilt for protobuf 3.13

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-20
- Force C++14 as this code is not yet C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.4.4-18
- Rebuilt for protobuf 3.12

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.4.4-16
- Rebuild for protobuf 3.11

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.4-13
- Rebuild for protobuf 3.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4.4-10
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.4-9
- Rebuild for protobuf 3.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.4.4-6
- Rebuild for protobuf 3.3.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 1.4.4-4
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.4.4-3
- Rebuild for protobuf 3.1.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Vladimir Stackov <amigo.elite at gmail dot com> - 1.4.4-1
- Version bumped to 1.4.4

* Wed Aug 19 2015 Vladimir Stackov <amigo.elite at gmail dot com> - 1.4.3-1
- Version bumped to 1.4.3

* Fri Jul 31 2015 Vladimir Stackov <amigo.elite at gmail dot com> - 1.4.2-1
- Version bumped to 1.4.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-2
- Rebuild for protobuf soname bump

* Wed Jan 07 2015 Vladimir Stackov <amigo.elite at gmail dot com> - 1.4.1-1
- Version bumped to 1.4.1
- Added macroses for EL6

* Fri Dec 19 2014 Vladimir Stackov <amigo.elite at gmail dot com> - 1.3-4
- Modified in appliance with rhbz#1172525

* Fri Dec 12 2014 Vladimir Stackov <amigo.elite at gmail dot com> - 1.3-3
- Produce hardened binaries

* Thu Dec 11 2014 Vladimir Stackov <amigo.elite at gmail dot com> - 1.3-2
- Modified in appliance with rhbz#1172525
- Added tartool

* Wed Dec 10 2014 Vladimir Stackov <amigo.elite at gmail dot com> - 1.3-1
- Initial version of the package
