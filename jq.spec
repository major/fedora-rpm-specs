Name:           jq
Version:        1.6
Release:        14%{?dist}
Summary:        Command-line JSON processor

License:        MIT and ASL 2.0 and CC-BY and GPLv3
URL:            http://stedolan.github.io/jq/
Source0:        https://github.com/stedolan/jq/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# Backport of PR#1752 for RHBZ#2008979
Patch0:         jq-decimal-literal-number.patch
# Backport of PR#2400 for RHBZ#2017285
Patch1:         jq-fix-non-decimal-string.patch

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  oniguruma-devel

%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool


%description
lightweight and flexible command-line JSON processor

 jq is like sed for JSON data – you can use it to slice
 and filter and map and transform structured data with
 the same ease that sed, awk, grep and friends let you
 play with text.

 It is written in portable C, and it has zero runtime
 dependencies.

 jq can mangle the data format that you have into the
 one that you want with very little effort, and the
 program to do so is often shorter and simpler than
 you'd expect.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}


%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -if
%configure --disable-static
%make_build
# Docs already shipped in jq's tarball.
# In order to build the manual page, it
# is necessary to install rake, rubygem-ronn
# and do the following steps:
#
# # yum install rake rubygem-ronn
# $ cd docs/
# $ curl -L https://get.rvm.io | bash -s stable --ruby=1.9.3
# $ source $HOME/.rvm/scripts/rvm
# $ bundle install
# $ cd ..
# $ ./configure
# $ make real_docs

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Delete build-time RPATH that is unnecessary on an installed
# system - rhbz#1987608
chrpath -d %{buildroot}%{_bindir}/%{name}

%check
# Valgrind used, so restrict architectures for check
%ifarch %{ix86} x86_64
make check
%endif

%ldconfig_scriptlets

%files
%{_bindir}/%{name}
%{_libdir}/libjq.so.*
%{_datadir}/man/man1/jq.1.gz
%{_datadir}/doc/jq/AUTHORS
%{_datadir}/doc/jq/COPYING
%{_datadir}/doc/jq/README
%{_datadir}/doc/jq/README.md

%files devel
%{_includedir}/jq.h
%{_includedir}/jv.h
%{_libdir}/libjq.so


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 11 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.6-13
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Mar 08 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.6-12
- Backport PR#2400 to fix iteration for non-decimal strings (rhbz#2017285)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 29 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.6-10
- Backport PR#1752 to fix an integer logic issue (rhbz#2008979)

* Thu Aug 12 2021 Lon Hohberger <lon@redhat.com> - 1.6-9
- Drop build-time RPATH from jq binary (rhbz#1987608)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.6-6
- Use correct valgrind_arches macro to check for valgrind.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 David Fetter <david@fetter.org> - 1.6-1
- Upstream 1.6.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 01 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5-12
- Rebuild against oniguruma 6.8.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Lon Hohberger <lon@fedoraproject.org> - 1.5-10
- Fix CVE 2015-8863

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-9
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5-5
- Rebuild for oniguruma 6.1.1

* Mon Jul 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5-4
- Rebuild for oniguruma 6

* Sun Mar 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-3
- valgrind on all but s390

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 25 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 1.5-1
- Upstream 1.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Flavio Percoco <flavio@redhat.com> - 1.3-2
- Added check, manpage

* Fri Oct 18 2013 Flavio Percoco <flavio@redhat.com> - 1.3-1
- Initial package release.
