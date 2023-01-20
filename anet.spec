Name:           anet
Version:        0.4.1
Release:        14%{?dist}
Summary:        Ada Networking Library

License:        GPLv2+ with exceptions
URL:            https://www.codelabs.ch/anet/
Source:         https://www.codelabs.ch/download/libanet-%{version}.tar.bz2
Source2:        https://www.codelabs.ch/download/libanet-%{version}.tar.bz2.sig
Source3:        https://www.codelabs.ch/keys/0xBB793815pub.asc
# Fedora-specific patch to use the directories project:
Patch1:         anet-0.4.1-directories_gpr.patch
# Disable one test that doesn't work in Koji:
Patch2:         anet-0.3.3-no_IPv6_multicast_test.patch

BuildRequires:  gcc-gnat fedora-gnat-project-common make asciidoc ahven-devel
BuildRequires:  gprbuild
BuildRequires:  gnupg2
# gpgverify was introduced in redhat-rpm-config 129.
BuildRequires:  redhat-rpm-config >= 129
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
Anet is a networking library for the Ada programming language. It supports, \
among other things, IPv6, Unix domain sockets, multicast, raw sockets, link \
layer sockets and Netlink.

%global common_description_sv \
Anet är ett nätverksprogrammeringsbibliotek för programmeringsspråket ada. \
Det har bland annat stöd för IPv6, Unixsocketar, flersändning, råa socketar, \
länklagersocketar och Netlink.

%description %{common_description_en}

%description -l sv %{common_description_sv}


%package devel
Summary:        Development files for Anet
Summary(sv):    Filer för programmering med Anet
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use Anet.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder Anet.


%prep
%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE2}' --data='%{SOURCE0}'
%setup -q -n libanet-%{version}
%patch1 -p 1
%patch2


%define all_the_flags "GNAT_BUILDER_FLAGS=%{GNAT_builder_flags}" "ADAFLAGS=%{build_adaflags}" "LDFLAGS=%{build_ldflags}"
# define makes the macro lazily expanded, unlike global.


%build
make %{all_the_flags}
make doc


%install
# Pass all_the_flags here too to ensure that GPRbuild won't recompile anything.
%{make_install} %{all_the_flags} prefix=%{_prefix} libdir=%{_libdir} gprdir=%{_GNAT_project_dir}


%check
# Disable the hardening hack only for the testsuite.
# https://bugzilla.redhat.com/show_bug.cgi?id=1197501
# all_the_flags must be lazily expanded for this to work.
%undefine _hardened_build
make tests %{all_the_flags}


%files
%{_libdir}/*.so.*
%license COPYING
%doc AUTHORS

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/%{name}
%{_GNAT_project_dir}/*
%doc README TODO doc/html examples


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 0.4.1-13
- Rebuilt with GCC 13.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 0.4.1-9
- rebuilt with gcc-11.0.1-0.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Björn Persson <Bjorn@Rombobjörn.se> - 0.4.1-7
- Rebuilt with GCC 11.

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Björn Persson <Bjorn@Rombobjörn.se> - 0.4.1-1
- Upgraded to version 0.4.1.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Björn Persson <Bjorn@Rombobjörn.se> - 0.4.0-1
- Upgraded to version 0.4.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Björn Persson <Bjorn@Rombobjörn.se> - 0.3.4-4
- Switched to building with GPRbuild as project file support was removed from
  Gnatmake in GCC 8.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Björn Persson <Bjorn@Rombobjörn.se> - 0.3.4-1
- Upgraded to version 0.3.4.
- Excluded ppc64le because of a suspected endianness bug in Libgnat.

* Mon Jul 11 2016 Björn Persson <Bjorn@Rombobjörn.se> - 0.3.3-1
- Upgraded to version 0.3.3.

* Tue Feb 02 2016 Björn Persson <Bjorn@Rombobjörn.se> - 0.3.1-3
- Rebuilt with GCC 6 prerelease.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Björn Persson <bjorn@rombobjörn.se> - 0.3.1-1
- Upgraded to version 0.3.1.

* Sat Feb 07 2015 Björn Persson <bjorn@rombobjörn.se> - 0.2.3-5
- Rebuilt with GCC 5.0.0.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Björn Persson <bjorn@rombobjörn.se> - 0.2.3-2
- Rebuilt with GCC 4.9.0 prerelease.

* Wed Jan 29 2014 Björn Persson <bjorn@rombobjörn.se> - 0.2.3-1
- Upgraded to version 0.2.3.

* Sun Jul 28 2013 Björn Persson <bjorn@rombobjörn.se> - 0.2.2-2
- Use %%doc now that documentation directories are unversioned.

* Thu May 9 2013 Björn Persson <bjorn@rombobjörn.se> - 0.2.2-1
- ready to be submitted for review
