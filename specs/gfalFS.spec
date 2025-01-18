%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build


Name:			gfalFS
Version:		1.5.2
Release:		20%{?dist}
Summary:		Filesystem client based on GFAL 2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:		Apache-2.0
URL:			https://svnweb.cern.ch/trac/lcgutil/wiki/gfal2
# git clone https://gitlab.cern.ch/dmc/gfalFS.git gfalFS-1.5.2
# pushd gfalFS-1.5.2
# git checkout v1.5.2
# git submodule init
# popd
# tar czf gfalFS-1.5.2.tar.gz gfalFS-1.5.2 --exclude-vcs
Source0:		%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:		cmake3
BuildRequires:		gfal2-devel
BuildRequires:		fuse-devel

Requires:		fuse%{?_isa}
Provides:		gfal2-fuse = %{version}

%description
gfalFS is a filesystem based on FUSE capable of operating on remote storage
systems managed by GFAL 2.0. This include the common file access protocols 
in lcg ( SRM, GRIDFTP, DCAP, RFIO, LFN, ...). The practical effect is that
the user can seamlessly interact with grid and cloud storage systems just 
as if they were local files.

#%clean
#rm -rf %{buildroot};
#make clean

%prep
%setup -q

%build
%cmake3 \
-DDOC_INSTALL_DIR=%{_docdir}/%{name}-%{version}
%cmake3_build

%install
%cmake3_install

%files
%{_bindir}/gfalFS
%{_bindir}/gfalFS_umount
%{_mandir}/man1/*
%{_docdir}/%{name}-%{version}/DESCRIPTION
%{_docdir}/%{name}-%{version}/VERSION
%{_docdir}/%{name}-%{version}/LICENSE
%{_docdir}/%{name}-%{version}/README
%{_docdir}/%{name}-%{version}/RELEASE-NOTES
%{_docdir}/%{name}-%{version}/readme.html

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.2-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Alejandro Alvarez <aalvarez at cern.ch> - 1.5.2-1
- Update 1.5.2 of gfalFS

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Alejandro Alvarez <aalvarez at cern.ch> - 1.5.0-1
 - Update 1.5.0 of gfalFS

* Mon Oct 28 2013 Adrien Devresse <adevress at cern.ch> - 1.4.0-3
 - Update 1.4.0 of gfalFS

* Wed Mar 20 2013 Adrien Devresse <adevress at cern.ch> - 1.2.0-0
 - fix a EIO problem with the gfal 2.0 http plugin 

* Thu Nov 29 2012 Adrien Devresse <adevress at cern.ch> - 1.0.1-0
 - fix a 32 bits off_t size problem with gfal 2.1


* Fri Jul 20 2012 Adrien Devresse <adevress at cern.ch> - 1.0.0-1
 - initial 1.0 release
 - include bug fix for srm and gsiftp url for fgettr

* Thu May 03 2012 Adrien Devresse <adevress at cern.ch> - 1.0.0-0.3.20120503010snap
 - bug correction with fgetattr on gsiftp / srm file system
 - minor changes applied from the fedora review comments

* Thu May 03 2012 Adrien Devresse <adevress at cern.ch> - 1.0.0-0.2.2012050202snap
 - improve global EPEL compliance.

* Mon Nov 14 2011 Adrien Devresse <adevress at cern.ch> - 1.0.0-0.2.2012041515snap
 - Initial gfalFS 1.0 preview release
