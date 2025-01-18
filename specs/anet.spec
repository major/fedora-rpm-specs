Name:           anet
Version:        0.5.1
Release:        3%{?dist}
Summary:        Ada Networking Library

License:        GPL-2.0-or-later WITH GNAT-exception
URL:            https://www.codelabs.ch/anet/
Source:         https://www.codelabs.ch/download/libanet-%{version}.tar.bz2
Source2:        https://www.codelabs.ch/download/libanet-%{version}.tar.bz2.sig
Source5:        https://www.codelabs.ch/keys/0xDBF6D7E1095FD0D9.asc
# Disable one test that doesn't work in Koji:
Patch:          anet-0.3.3-no_IPv6_multicast_test.patch

BuildRequires:  gcc-gnat fedora-gnat-project-common make ahven-devel
BuildRequires:  gprbuild
BuildRequires:  gnupg2
# gpgverify was introduced in redhat-rpm-config 129.
BuildRequires:  redhat-rpm-config >= 129
BuildRequires:  asciidoctor
BuildRequires:  sed
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
License:        GPL-2.0-or-later WITH GNAT-exception AND MIT
# Asciidoctor inserts an MIT-licensed stylesheet in the manual.
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use Anet.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder Anet.


%prep
%{gpgverify} --keyring='%{SOURCE5}' --signature='%{SOURCE2}' --data='%{SOURCE0}'
%autosetup -n libanet-%{version} -p0


# Override the upstream usage of control-flow checking with Fedora's arch-
# dependent choice because GCC doesn't offer control-flow checking for all
# arches.
%global fix_cf_protection %([[ '%{build_adaflags}' = *-fcf-protection* ]] || echo -fcf-protection=none)
# This expands to an empty string if "-fcf-protection" is found among Fedora's
# compiler flags, and to "-fcf-protection=none" if it's not found.

%define all_the_flags "GNAT_BUILDER_FLAGS=%{GNAT_builder_flags}" "ADAFLAGS=%{build_adaflags} %{fix_cf_protection}" "LDFLAGS=%{build_ldflags}"
# define makes the macro lazily expanded, unlike global.


%build
make %{all_the_flags}
make build-doc


%install
# Pass all_the_flags here too to ensure that GPRbuild won't recompile anything.
%{make_install} %{all_the_flags} GPRINSTALLFLAGS='%{GPRinstall_flags}'

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/%{name}");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/%{name}";|i' \
    %{buildroot}%{_GNAT_project_dir}/*.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 4: Replace the value of Library_Dir with Directories.Libdir.
# 5: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.


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
%doc README TODO obj/html examples


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Björn Persson <Bjorn@Rombobjörn.se> - 0.5.1-2
- Rebuilt with GCC 15 prerelease.

* Mon Nov 04 2024 Björn Persson <Bjorn@Rombobjörn.se> - 0.5.1-1
- Upgraded to version 0.5.1.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 25 2024 Björn Persson <Bjorn@Rombobjörn.se> - 0.5.0-1
- Upgraded to version 0.5.0.

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 0.4.1-16
- Rebuilt with GCC 14 prerelease.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
