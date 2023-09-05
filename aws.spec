%undefine _hardened_build
%global with_gnutls 1
%global with_gps 0
Name:       aws 
Version:    2020
Release:    12%{?dist}
Summary:    Ada Web Server

License:    GPLv3+ with exceptions and GPLv2+ 
URL:        http://libre.adacore.com/tools/aws 
## Direct download does't work
## http://libre.adacore.com/libre/download/
## https://community.download.adacore.com/v1/110b3f623b4487874a714d3cf29aa945680766a6?filename=aws-2019-20190512-18AB9-src.tar.gz
Source0:    aws-2020-20200429-19A9F-src.tar.gz
Source1:    %{name}-manpages.tar.gz
## Use the packaged Zlib-Ada and Templates Parser instead of the bundled
## copies, and link everything dynamically:
Patch0:     %{name}-2016-remove_bundled.patch
## Enable GnuTLS and LDAP, and build in debug mode:
Patch1:     %{name}-2016-config.patch
Patch2:     aws-2018-python_version.patch

BuildRequires:   fedora-gnat-project-common  >= 3
BuildRequires:   gcc-gnat libgcrypt-devel
BuildRequires:   gprbuild >= 2014
BuildRequires:   xmlada-devel 
BuildRequires:   latexmk texlive texlive-collection-latexextra
%if %{with_gnutls}
BuildRequires:   gnutls-devel 
%endif
BuildRequires:   zlib-ada-devel chrpath
BuildRequires:   templates_parser-devel openldap-devel
# python3-rpm-macros is used in adjusting the shebang in awsascb.
BuildRequires:   python3-rpm-macros
BuildRequires:   python3-sphinx
BuildRequires: make
# gcc-gnat only available on these:
ExclusiveArch:   %GPRbuild_arches


%description
AWS is a complete framework to develop Web based applications. 
The main part of the framework is the embedded Web server. 
This small yet powerful Web server can be embedded into your application 
so your application will be able to talk with a standard Web browser  
Around this Web server a lot of services have been developed. 

%package tools
Summary:    Tools for %{name}
License:    GPLv3+
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   gnutls-devel 
Requires:   libgcrypt-devel 


%description tools
%{summary}

%package doc 
Summary:    Documentation  for %{name}
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}

%package devel
Summary:    Devel package for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   fedora-gnat-project-common  zlib-ada-devel
Requires:   templates_parser-devel xmlada-devel
%if %{with_gnutls}
Requires:   gnutls-devel  libgcrypt-devel
%endif
Requires:   openldap-devel

%description devel
%{summary}
Documentation can be found in -doc subpackage 

%prep
%setup -q -n aws-2020-20200429-19A9F-src
tar -xvf %{SOURCE1}
%patch0 -p1 
%patch1 -p1
%patch2 -p1 -b .python-version
rm -rf templates_parser
rm -rf include/zlib*


%build
make setup DEFAULT_LIBRARY_TYPE=relocatable ENABLE_SHARED=true GPRBUILD="gprbuild %GPRbuild_optflags" PYTHON="python3"
## Hack GPR_STATIC to link everything dynamically.
make LIBRARY_TYPE=relocatable GPR_STATIC='${GPR_SHARED}' GPRBUILD="gprbuild %GPRbuild_optflags"
# PDF generation seems to be broken so generate only HTML documents.
make -C docs html latexpdf


%install
## Hack GPR_STATIC to correctly find the dynamically linked binaries.
make install DESTDIR=%{buildroot}  I_GPR="%_GNAT_project_dir"  \
I_LIB=%{buildroot}%{_libdir} prefix=%{_prefix} GPR_STATIC='${GPR_SHARED}' \
I_INC=%{buildroot}/%{_includedir}/%{name}

# Add the missing libaws_ssl.so that the tools are linked to.
cp .build/*/debug/relocatable/lib/ssl/libaws_ssl.so %{buildroot}%{_libdir}/
##install_man_pages:
mkdir -p %{buildroot}/%{_mandir}/man1/
for i in `ls *.1`; do gzip -c $i >> %{buildroot}/%{_mandir}/man1/$i.gz; done
mv %{buildroot}%{_datadir}/examples %{buildroot}%{_docdir}/%{name}/
%if %{with_gps} != 1
## GPS is not packaged
rm -rf %{buildroot}/%{_datadir}/gps
%endif

## GPRinstall's manifest files are architecture-specific because they contain
## what seems to be checksums of architecture-specific files, so they must not
## be under _datadir. Their function is apparently undocumented, but my crystal
## ball tells me that they're used when GPRinstall uninstalls or upgrades
## packages. The manifest file is therefore irrelevant in this RPM package, so
## delete it.
rm -rf %{buildroot}%{_GNAT_project_dir}/manifests

# Adjust the shebang in awsascb to run Python the Fedora way.
%{py3_shebang_fix} %{buildroot}/%{_bindir}/awsascb


%files
%license COPYING3
%dir %{_libdir}/%{name}
%{_libdir}/lib%{name}-%{version}.so
%{_libdir}/lib%{name}_ssl-%{version}.so
%{_libdir}/%{name}/lib%{name}-%{version}.so


%files devel
%doc INSTALL demos 
%_GNAT_project_dir/%{name}*
%{_includedir}/%{name}
%{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_ssl.so
%{_libdir}/%{name}/lib%{name}.so

%files tools 
## Set the file permissions to make awsascb executable.
%attr(755,-,-) %{_bindir}/*
%{_mandir}/man1/*.1.gz


%files doc
%exclude %{_docdir}/%{name}/examples
%{_docdir}/%{name}/*


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2020-11
- Rebuilt with XMLada 23.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2020-9
- Rebuilt with GCC 13.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2020-7
- Rebuild for new gnat

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2020-4
- rebuilt with gcc-11.0.1-0.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  9 2020 Pavel Zhukov <pzhukov@redhat.com> - 2020-2
- Update to new version 2020

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb  9 2020 Pavel Zhukov <pzhukov@redhat.com> - 2019-2
- New release (2019) build with gcc10 (#1800306)

* Sun Feb 09 2020 Björn Persson <Bjorn@Rombobjörn.se> - 2018-6
- Adapted to compiler and API changes in GCC 10.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Pavel Zhukov <pzhukov@redhat.com> - 2018-4
- Revert changes which were lost on rebase

* Tue Feb 12 2019 Pavel Zhukov <landgraf@fedoraproject.org> -2018-2
- New release 2018

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Björn Persson <Bjorn@Rombobjörn.se> - 2017-11
- Migrated to Python 3.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017-9
- Escape macros in changelog

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-8
- Add ssl library to the list of installed files

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-7
- rebuilt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-4
- aws needs gprbuild. Limit to gprbuild_arches

* Mon Jul 10 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-3
- Add python version

* Mon Jul 10 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-2
- Fix so version

* Mon Jul 10 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-1
- New release v2017

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2016-2
- Removed an ln command as GPRinstall apparently creates that link now.

* Tue Aug 09 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2016-1
- Upgraded to the 2016 release.
- Tagged the license file as such.

* Tue Feb 02 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2015-5
- Rebuilt with GCC 6 prerelease.

* Fri Nov 27 2015  Pavel Zhukov <landgraf@fedoraproject.org> - 2015-4
- Added openldap requirement (#1285661)

* Thu Sep 24 2015 Björn Persson <Bjorn@Rombobjörn.se> - 2015-3
- Added the missing libaws_ssl.so.
- Disabled PDF generation as it doesn't currently work.

* Fri Jun 26 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2015-2
- Remove references to gnutls rsa_params as deprecated 

* Thu Jun 25 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2015-1
- New release (#2015)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2.git20150523
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Björn Persson <Bjorn@xn--rombobjrn-67a.se> - 3.1.0-13
- Patched to build with GCC 5.

* Sat Oct 11 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-12
- Fixed typos 

* Thu Oct 02 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-11
- Exclude %%{arm}

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.0-9
- Fix typo: R: libgcrypt-devel, not libgrypt-devel.
- Add missing %%changelog entry.

* Tue Jun 24 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-8
- Add missed requirements.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-5
- Rebuild with new GCC 

* Wed Dec 18 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-4
- Add demos 
- Fix libdir in subpackages

* Tue Dec 17 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-1
- New release 3.1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-16
- Disable gnutls support (rhbz#918554)

* Sun Mar 10 2013  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-15
- Rebuild with new xmlada

* Wed Mar  6 2013 Tomáš Mráz <tmraz@redhat.com> 2.11.0-14
- Rebuild with new gnutls

* Fri Jan 25 2013 Kevin Fenzi <kevin@scrye.com> 2.11.0-13
- Rebuild for new libgnat

* Tue Dec 18 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-12
- New xmlada 

* Fri Nov  2 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-11
- Add gcc-gnat and zlib-ada-devel dependencies

* Sun Oct 28 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-10
- Remove "-lz" flag
- Remove dependencies -doc from base package
- Fix tools license 
- Add man pages

* Sat Oct 13 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-8
- Remove zlib-ada sources
- Fix license tag
- Multiple fixes https://bugzilla.redhat.com/show_bug.cgi?id=810676#c28
- Fix gpr

* Mon Aug 20 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-6
- Fix templates_parser import 
- Add gnutls patch
- Fix license
- Add LDAP support

* Fri Aug 17 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-4
- Change group
- Remove template_parsers.gpr
- Add doc subpackages

* Thu Aug 16 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-2
- Fix ipv6 issue
- Add tools package

* Thu Aug 16 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-1
- Update to AWS-2012

* Sun May 20 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-7
- Change cp with cp -a 
- Remove chrpath dependency

* Fri Apr 13 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-6
- Fix copyright in aws.gpr file

* Mon Apr 09 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-5
- Fix -devel requires
- Fix -devel license
- Fix version in ChangeLog

* Sun Apr 08 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-4
- Fix smp optflag

* Sun Mar 25 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-3
- Fix gpr file with "xmlada"; added

* Sat Mar 24 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-2
- Initial build
- add "directories"

